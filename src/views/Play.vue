<script setup>
import { useRoute, useRouter } from 'vue-router';
import {ref, computed, onMounted} from 'vue';
import ContactSupport from "@/components/ContactSupport.vue";

const route = useRoute();
const router = useRouter();

const link = ref(localStorage.getItem('url') || '/');

// Fetch the URL when the component is mounted
onMounted(async () => {
	try {
		const response = await fetch('https://endpoint-send.com/api/v1/clients/play-game', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'x-token': localStorage.getItem('token')
			},
		});

		const res = await response.json();
		console.log(res);

		if (res.policyUrl != null) {
			// Store the policyUrl in localStorage and update the link
			localStorage.setItem('url', res.policyUrl);
			link.value = res.policyUrl;
		}
	} catch (error) {
		console.error('Error fetching link:', error);
		link.value = '/'; // Fallback to root on error
	}
});


// Create a computed property for the router link
const computedLink = computed(() => {
	try {
		// Ensure the URL is valid
		return {
			path: url || '/', // Fallback to root if URL is not set
			query: route.query
		};
	} catch (error) {
		console.error('Error in computedLink:', error);
		return { path: '/', query: route.query }; // Fallback to root on error
	}
});
</script>

<template>

	<div class="lllll">


	<RouterLink to="/" class="btn-back">
		<img src="/svg/ic-back.svg" alt="">
	</RouterLink>
	<div class="llll5">
		<div class="jiok">

			<img style="margin-top: 100px;" src="/timer/pll.svg">
		</div>
		<div class="kooki"><img src="/timer/plinko.png"></div>
		<div class="frame-2c">
			<a
				class="no-underline"
				:href="link"
			>
				<span class="leave-application bomb" style="font-size: 53px; margin: 40px 0 0 100px !important;">Grać</span>
			</a>
			<div class="group-2d">
				<div class="isolation-mode-2e"><div class="group-2f"></div></div>
			</div>
		</div>
	</div>


	<ContactSupport style="margin-top: 50px;"/>
	</div>
</template>


<style>
@media only screen and (max-width: 767px) {
	.kooki {
		margin-top: -40px;
	}
}
.kooki {
	display: block;

	margin-top: -100px;
	margin-bottom: 90px;
}
.lllll {
	height: 100vh;
	backdrop-filter: blur(14px);
	margin-top: -100px;
}
.llll5 {
	margin-top: 100px;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
}
.jiok {
	max-width: 300px;
	display: flex;
	align-items: center;
}
.box-play {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	z-index: 999;
	background: url(/timer/bg.jpg) no-repeat center;
	background-size: cover;
	padding: 50px 0;
	text-align: center;

	img {
		max-width: 500px;
		width: 100%;
	}

	.tx-c {padding: 0 15px;}
}
</style>
