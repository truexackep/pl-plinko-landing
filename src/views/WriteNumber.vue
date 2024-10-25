<script setup>
import { ref, computed, onMounted } from 'vue';
import {RouterLink, useRouter} from 'vue-router';
import SelectCountryCode from '../components/SelectCountryCode.vue';
import ContactSupport from '../components/ContactSupport.vue';
import Country from '../components/Country.json';
import Menu from "@/components/Menu.vue";

const flag = ref(false);
const dataCountry = ref({
	code: Country[0].dial_code,
	codeCountry: Country[0].code,
	flag: Country[0].emoji
});
const availableCountries = ref([]);
const tel = ref();
const agree = ref(false);
const disabled = ref(true);
const router = useRouter();

const globalError = ref(false);
const globalErrorText = ref('Error!!!');

const errorPhone = ref(false);
const errorAgree = ref(false);

function onInput() {
	errorPhone.value = false;
	disabled.value = false;
}

function onFocus() {
	setTimeout(() => {
        window.scrollTo({
            top: 80,
            behavior: 'smooth'
        });
    }, 300);
}

function onAgree() {
	if (agree.value) {
		errorAgree.value = false;
	} else {
		errorAgree.value = true;
	}
}

async function onSubmit() {
	if (tel.value == undefined || tel.value == '') {
		errorPhone.value = true;
		return false;
	}

	if (!agree.value) {
		errorAgree.value = true;

		gtag('event', 'button_click', {
	    	'event_category': 'Button',
	    	'event_label': 'The check box is not selected'
	    });

	    fbq('trackCustom', 'The check box is not selected');

		return false;
	}

	const cleanedNumber = tel.value.replace(/[()\-]/g, '');
	const phone = dataCountry.value.code + cleanedNumber;
	const queryString = window.location.search;
	const urlParams = new URLSearchParams(queryString);
	console.log(queryString)
	const result = await fetch('https://endpoint-send.com/api/v1/clients', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			"name": "new client",
			"utm_campaign": urlParams.get('utm_campaign'),
			"fbPixel": urlParams.get('pixel'),
			"fbToken": urlParams.get('token'),
			"fbclid": urlParams.get('fbclid'),
			"phone": phone,
			"countryCode": dataCountry.value.codeCountry,
			"bundle": "plinko.company"
		})
	});

	const data = await result.json();

	if (data.success) {
		localStorage.setItem('token', data.token);
		localStorage.setItem('code', dataCountry.code);
		localStorage.setItem('phone', tel.value.toString());

		gtag('event', 'button_click', {
	    	'event_category': 'Button',
	    	'event_label': 'New clients'
	    });

	    fbq('trackCustom', 'New clients');

		if (data.needVerif) {
			router.push('/verification');
		} else {
			router.push('/timer-verifi');
		}
	} else if(data.needVerif == false || data.success == false) {
		console.log(data)
		localStorage.setItem('token', data.token);
		localStorage.setItem('phone', tel.value.toString());

		const response = await fetch('https://endpoint-send.com/api/v1/clients/play-game', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'x-token': data.token
			},

		});
		const res = await response.json()
		if(res.policyUrl != null) {

			localStorage.setItem('url', res.policyUrl)
			router.push('/play');
		}else {
			router.push('/timer-verifi');
		}
	}else {
		globalError.value = true;
		globalErrorText.value = data;
	}
}

const filteredCountries = computed(() => {
	return Country.filter(country => availableCountries.value.includes(country.iso));
});

onMounted(async () => {
	window.scrollTo(0, 0);

	const result = await fetch('https://endpoint-send.com/api/v1/countries', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({
			"bundle": "string"
		})
	});

	const data = await result.json();

	availableCountries.value = data.availableCountries;

	dataCountry.value = {
		code: filteredCountries.value[0].code,
		codeCountry: filteredCountries.value[0].iso,
		flag: filteredCountries.value[0].flag,
		mask: filteredCountries.value[0].mask,
	};
});
</script>

<template>
	<div style="padding: 20px;" class="logo-mob">
		<img src="/timer/logo2.svg">

	</div>
	<div class="page-write">
		<div class="frame-1f" style="width: 78%;">
			<div class="lll">
				<div class="logo"></div>

				<div class="frame-22"><router-link class="no-underline" to="#bn"><span class="home">Dom</span></router-link><router-link class="no-underline" to="#about"><span class="about-us">O nas</span></router-link><router-link class="no-underline" :to="{ path: '/', hash: '#rezen' }"   ><span class="reviews">Recenzje</span></router-link><router-link class="no-underline" to="#cele"><span  class="goals">Cele</span></router-link></div>
				<button class="frame-20">
					<router-link class="no-underline" :to="{ path: '/write-number', query: $route.query }"><span class="discover-21">Odkryj</span></router-link>
				</button>
			</div>
		</div>
		<Menu/>

		<div class="center">
			<img src="/timer/logo-verif.png" class="ver-logo">
			<p class="inf">
				ZAREJESTRUJ SIĘ, PODAJĄC SWÓJ NUMER
			</p>
			<p style="color: #FFF;
font-family: Jomhuria;
font-size: 48px;
font-style: normal;
text-align: center;
font-weight: 400;
line-height: 70%; /* 33.6px */">
				Rozmawiamy o Tobie 5 minut wcześniej
			</p>
			<p style="color: #FFF;
text-align: center;
font-family: Jomhuria;
font-size: 32px;
font-style: normal;
font-weight: 400;
line-height: 70%; ">
				Wpisz swój numer telefonu
			</p>
<!--			<div class="tx-c">-->
<!--				<h3 class="title">Zarejestruj się, podając swój numer</h3>-->
<!--			</div>-->

			<SelectCountryCode v-if="flag" @onFlag="flag = $event" @onCode="dataCountry = $event"/>

			<form action="/verification" class="form" @submit.prevent>
				<div class="label-text">Wpisz swój numer telefonu</div>

				<div class="input-tel field" :class="{'input-error': error}">
					<div class="code" @click="flag = true">
						<img class="flag" :src="dataCountry.flag" alt="">
						{{ dataCountry.code }}
					</div>

					<MaskInput
						type="tel"
						:mask="dataCountry.mask"
						placeholder="telefon komórkowy"
						v-model="tel"
						inputmode="numeric"
						@input="onInput"
						@focus="onFocus"
					/>

					<div class="error" v-if="errorPhone">Wprowadź numer telefonu</div>
				</div>

				<div class="tx-c">
					<button type="submit" class="frame-20" :class="{disabled: disabled || tel == ''}" @click="onSubmit">
						<span class="inner"><span>Kontynuować</span></span>
					</button>
				</div>

				<label class="input-checkout field">
					<input type="checkbox" v-model="agree" @change="onAgree">
					<div class="input"></div>
					<div class="text" style="color: white!important; font-size: 22px;">Mam ukonczone 18 lat i akceptuje warunki korzystania z witryny</div>
					<div class="error" v-if="errorAgree">Wybierz znacznik wyboru</div>
				</label>
			</form>
		</div>

		<div class="global-error" v-if="false">
			<span>{{ globalErrorText }}</span><br>
			<button @click="globalError = false">zamknąć</button>
		</div>
	</div>
</template>

<style>
.page-write {
	position: relative;
	height: 100vh;
	width: 100%;
	display: flex;
	align-items: center;
	flex-direction: column;
	.form {
		max-width: 700px;
		width: 100%;
		padding: 25px 0 50px 0;
	}
}
.ver-logo {
	width: 500px;
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
.label-text {
	font-size: 18px;
	color: #fff;
	font-weight: 600;
	margin-bottom: 8px;
}

.input-tel {
	width: 100%;
	height: 52px;
	border-radius: 60px;
	border: 1px solid white;
	display: flex;
	align-items: center;
	font-size: 14px;
	font-weight: 500;
	color: #fff;
	padding: 0 12px;
	margin-bottom: 30px;

	.code {
		min-width: 97px;
		position: relative;
		border-right: 1px solid white;
		cursor: pointer;
		display: flex;
		align-items: center;
		gap: 5px;
		font-size: 23px;

		span {font-size: 25px;}

		&:after {
			content: '';
			display: block;
			width: 10px;
			height: 6px;
			background: url(/svg/ic-arr.svg) no-repeat;
			position: absolute;
			right: 12px;
			top: 50%;
			transform: translateY(-50%);
		}
	}

	input {
		background: none;
		border: none;
		padding-left: 12px;
		color: #fff;
		display: block;
		width: 100%;
		height: 100%;
		font-size: 22px;
		&::placeholder {
			color: #A4ACB5;
			font-size: 14px;
			font-weight: 500;
		}
	}
}

.input-checkout {
	display: flex;
	align-items: center;
	gap: 10px;
	font-size: 14px;
	color: #848484;
	line-height: 1.2;
	margin-top: 25px;
	user-select: none;

	input {display: none;}

	.input {
		width: 28px;
		min-width: 28px;
		height: 28px;
		border-radius: 8px;
		border: 2px solid #4D5761;
		position: relative;

		&:after {
			content: '';
			display: block;
			width: 16px;
			height: 10px;
			background: url(/svg/ic-check.svg) no-repeat;
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			opacity: 0;
			transition: all 0.3s;
		}
	}

	input:checked + .input:after {opacity: 1;}
}
</style>
