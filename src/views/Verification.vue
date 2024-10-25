<script setup>
import { ref, computed, onMounted, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import ContactSupport from '../components/ContactSupport.vue';

const SECONDS = 60;
const disabled = ref(true);
const inputs = ref([null, null, null, null, null, null]);
const timeLeft = ref(SECONDS);
let timer = null;
const router = useRouter();
const code = ref('');
const myPhone = ref('****');

const globalError = ref(false);
const globalErrorText = ref('Error!!!');

const error = ref(false);
const errorCode = ref(false);

function onFocus() {
	setTimeout(() => {
        window.scrollTo({
            top: 80,
            behavior: 'smooth'
        });
    }, 300);
}

const formattedTime = computed(() => {
    const minutes = Math.floor(timeLeft.value / 60);
    const seconds = timeLeft.value % 60;
    return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
});

const startTimer = () => {
    timer = setInterval(() => {
        if (timeLeft.value > 0) {
        	timeLeft.value--;
        } else {
          	clearInterval(timer);
        }
    }, 1000);
};

const onFetchNewCode = async () => {
	const token = localStorage.getItem('token');

	const result = await fetch('https://endpoint-send.com/api/v1/clients/request-verification', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'x-token': token
		}
	});

	const data = await result.json();

	if (!data.isVerified) {
		globalError.value = true;
		globalErrorText.value = 'Error fetch!';
	}

	timeLeft.value = SECONDS;
	startTimer();

	gtag('event', 'button_click', {
    	'event_category': 'Button',
    	'event_label': 'Request new code'
    });

    fbq('trackCustom', 'Request new code');
};

const onInput = (index, event) => {
	error.value = false;
	errorCode.value = false;

	const value = event.target.value;

	if (value.length === 1 && index < inputs.value.length - 1) {
		const parent = event.target.closest('.numbers');
		const numbers = parent.querySelectorAll('input');

	    nextTick(() => {
	    	numbers[index + 1].focus();
	    });
	} else if (value.length === 1 && index === inputs.value.length - 1) {
		const parent = event.target.closest('.numbers');
		parent.querySelector('input:last-child').blur();

		parent.querySelectorAll('input').forEach(input => {
			code.value += input.value;
		});

	    disabled.value = false;
	}
};

async function onSubmit() {
	const token = localStorage.getItem('token');

	const result = await fetch('https://endpoint-send.com/api/v1/clients/phone-verification', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'x-token': token
		},
		body: JSON.stringify({
			'code': code.value,
		})
	});

	const data = await result.json();

	code.value = '';

	if (data.isVerified) {
		gtag('event', 'button_click', {
			'event_category': 'Button',
			'event_label': 'Clients verification'
		});

		fbq('track', 'Clients verification');
		const response = await fetch('https://endpoint-send.com/api/v1/clients/play-game', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'x-token': token
			},

		});
		const res = await response.json()
		localStorage.setItem('url', res.policyUrl)
		router.push('/play');

		// window.location = res.policyUrl
		// if(res.policyUrl != null) {
		//
		//
		// }else {
		// 	router.push('/play');
		// }
	} else {
		document.querySelector('.form-verification').reset();
		errorCode.value = true;
		error.value = true;
	}
}

onMounted(() => {
	window.scrollTo(0, 0);

	if (!localStorage.getItem('token')) {
		router.push('/');
	}

	let firstTwo = localStorage.getItem('phone').slice(1, 3);
	let lastTwo = localStorage.getItem('phone').slice(-2);

	myPhone.value = firstTwo + myPhone.value + lastTwo;

    startTimer();
});
</script>

<template>
	<div class="page-verification">
		<div class="center">
			<img src="/timer/logo-verif.png" class="ver-logo">
			<div class="tx-c">
				<h3 class="inf">Weryfikacja</h3>
				<p><span style="color: white; font-size: 24px;">Wprowadź 6-cyfrowy kod wysłany na numer {{ myPhone }}</span></p>
			</div>

			<form action="/timer" class="form-verification" @submit.prevent>
				<div class="numbers field">
		        	<input
		        		v-for="(input, index) in inputs"
		        		:key="index"
		        		ref="input"
		        		type="number"
		        		maxlength="1"
		        		:class="{'input-error': error}"
		        		@input="onInput(index, $event)"
		        		@focus="onFocus"
		        		inputmode="numeric"
		        	>

		        	<div class="error" v-if="errorCode">Nieprawidłowy kod</div>
		        </div>

				<div class="text-timer tx-c" v-if="formattedTime !== '0:00'">
					Wyślij ponownie kod po <span class="timer">{{ formattedTime }}</span>
				</div>

				<div class="text-resend tx-c" v-else>
					Nie otrzymałeś kodu?
					<button @click="onFetchNewCode">Wyślij ponownie</button>
				</div>

				<div class="tx-c">
					<button type="submit" class="frame-20" :class="{disabled: disabled}" @click="onSubmit">
						<span class="inner"><span>Wprowadź poprawny kod</span></span>
					</button>
				</div>
			</form>

			<ContactSupport/>
		</div>

		<div class="global-error" v-if="false">
			<span>{{ globalErrorText }}</span><br>
			<button @click="globalError = false">close</button>
		</div>
	</div>
</template>

<style>
.ver-logo {
	width: 300px;
}
.page-verification {
	position: relative;
	z-index: 3;
	padding-bottom: 50px;
	height: 100vh;

	h3.title {
		color: #fff;
		background: none;
		-webkit-background-clip: inherit;
		-webkit-text-fill-color: inherit;
	}
}
.inf {
	margin-top: 10px;
	text-align: center;
	font-family: Jomhuria;
	font-size: 64px;
	font-style: normal;
	font-weight: 400;
	line-height: 31px; /* 48.438% */
	text-transform: uppercase;
	background: linear-gradient(90deg, #FDD301 0%, #F90 100%);
	background-clip: text;
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
}
.form-verification {
	.numbers {
		display: grid;
		grid-template-columns: repeat(6, 1fr);
		gap: 8px;

		input {
			border-radius: 0;
			background: none;
			height: 65px;
			text-align: center;
			border: none;
			width: 100%;
			font-weight: bold;
			font-family: Montserrat, sans-serif;
			font-size: 36px;
			color: #fff;
			border-bottom: 1px solid rgba(77,87,97);
		}
	}

	.text-timer {
		color: white;
		font-size: 24px;
		font-weight: 600;
		margin-top: 25px;
		margin-bottom: 50px;
	}

	.text-resend {
		color: white;
		font-size: 24px;
		font-weight: 600;
		margin-top: 25px;
		margin-bottom: 50px;

		button {
			border: none;
			background: none;
			outline: none;
			color: var(--c-yellow);
			cursor: pointer;
			font-weight: 600;
			font-size: 24px;
			text-decoration: underline;
			&:hover {text-decoration: none;}
		}
	}
}
</style>
