<template>

	<div class="hhh">
		<!-- Кнопка бургера -->

		<button class="burger-button" @click="toggleMenu">
			<svg v-if="!menuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
				<line x1="1.5" y1="2.5" x2="22.5" y2="2.5" stroke="url(#paint0_linear_52_2922)" stroke-width="3" stroke-linecap="round"/>
				<line x1="4.5" y1="10.5" x2="22.5" y2="10.5" stroke="url(#paint1_linear_52_2922)" stroke-width="3" stroke-linecap="round"/>
				<line x1="18.5" y1="18.5" x2="22.5" y2="18.5" stroke="url(#paint2_linear_52_2922)" stroke-width="3" stroke-linecap="round"/>
				<defs>
					<linearGradient id="paint0_linear_52_2922" x1="0" y1="4.5" x2="24" y2="4.5" gradientUnits="userSpaceOnUse">
						<stop stop-color="#FDD301"/>
						<stop offset="1" stop-color="#FF9900"/>
					</linearGradient>
					<linearGradient id="paint1_linear_52_2922" x1="3" y1="12.5" x2="24" y2="12.5" gradientUnits="userSpaceOnUse">
						<stop stop-color="#FDD301"/>
						<stop offset="1" stop-color="#FF9900"/>
					</linearGradient>
					<linearGradient id="paint2_linear_52_2922" x1="17" y1="20.5" x2="24" y2="20.5" gradientUnits="userSpaceOnUse">
						<stop stop-color="#FDD301"/>
						<stop offset="1" stop-color="#FF9900"/>
					</linearGradient>
				</defs>
			</svg>
		</button>

		<!-- Мобильное меню -->
		<div :class="{'mobile-menu': true, 'menu-open': menuOpen}">
			<div style="margin-top: 20px; padding-left: 20px; padding-bottom: 15px; align-items: center; border-bottom: 1px solid rgba(255, 255, 255, 0.10); display: flex;
    justify-content: space-between;">
				<img src="/timer/logo2.svg">
				<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" style="margin-right: 15px;" @click="toggleMenu" fill="none">
					<rect width="32" height="32" rx="3.024" fill="url(#paint0_linear_52_4182)"/>
					<path d="M17.1728 16.0002L22.1568 11.0159C22.4812 10.6917 22.4812 10.1675 22.1568 9.84325C21.8326 9.51905 21.3084 9.51905 20.9842 9.84325L16 14.8276L11.016 9.84325C10.6916 9.51905 10.1676 9.51905 9.84336 9.84325C9.51901 10.1675 9.51901 10.6917 9.84336 11.0159L14.8274 16.0002L9.84336 20.9845C9.51901 21.3087 9.51901 21.8329 9.84336 22.1571C10.0049 22.3189 10.2174 22.4001 10.4297 22.4001C10.6419 22.4001 10.8542 22.3189 11.016 22.1571L16 17.1728L20.9842 22.1571C21.146 22.3189 21.3582 22.4001 21.5705 22.4001C21.7828 22.4001 21.9951 22.3189 22.1568 22.1571C22.4812 21.8329 22.4812 21.3087 22.1568 20.9845L17.1728 16.0002Z" fill="white"/>
					<defs>
						<linearGradient id="paint0_linear_52_4182" x1="0" y1="16" x2="32" y2="16" gradientUnits="userSpaceOnUse">
							<stop stop-color="#FDD301"/>
							<stop offset="1" stop-color="#FF9900"/>
						</linearGradient>
					</defs>
				</svg>
			</div>
			<button class="frame-20">
				<router-link class="no-underline" :to="{ path: '/write-number', query: $route.query }"><span class="discover-21">Odkryj</span></router-link>
			</button>
			<ul>
				<li @click="toggleMenu" ><router-link to="/">Dom</router-link></li>
				<li @click="toggleMenu" ><router-link :to="{ path: '/', hash: '#about' }"  >O nas</router-link></li>
				<li @click="toggleMenu" ><router-link :to="{ path: '/', hash: '#rezen' }"  >Recenzje</router-link></li>
				<li @click="toggleMenu" ><router-link :to="{ path: '/', hash: '#cele' }"  >Cele</router-link></li>
			</ul>
		</div>
	</div>
</template>

<script>
import {RouterLink} from "vue-router";

export default {
	components: {RouterLink},
	data() {
		return {
			menuOpen: false,
		};
	},
	methods: {
		toggleMenu() {
			this.menuOpen = !this.menuOpen;
		},
	},
};
</script>

<style scoped>
.hhh {
	display: none;
}
@media only screen and (max-width: 767px) {
	.hhh {
		display: block!important;
	}
}
/* Стили для кнопки бургера */
.burger-button {
	position: fixed;
	top: 20px;
	right: 20px; /* Кнопка остается справа */
	width: 40px;
	height: 40px;
	background-color: transparent;
	border: none;
	cursor: pointer;
	z-index: 1001;
	display: flex;
	justify-content: center;
	align-items: center;
}
li {
	font-size: 34px;
}
.burger-icon {
	display: block;
	width: 25px;
	height: 3px;
	background-color: black;
	position: relative;
	transition: transform 0.3s ease-in-out;
}

.burger-icon::before,
.burger-icon::after {
	content: '';
	display: block;
	width: 25px;
	height: 3px;
	background-color: black;
	position: absolute;
	transition: 0.3s ease-in-out;
}

.burger-icon::before {
	top: -8px;
}

.burger-icon::after {
	bottom: -8px;
}

.burger-icon.open {
	transform: rotate(45deg);
}

.burger-icon.open::before {
	transform: rotate(90deg);
	top: 0;
}

.burger-icon.open::after {
	transform: rotate(90deg);
	bottom: 0;
}

/* Стили для мобильного меню */
.mobile-menu {
	position: fixed;
	top: 0;
	left: 0; /* Меню фиксируется слева */
	width: 330px;
	height: 100%;
	background: rgba(0, 0, 0, 0.50);

	backdrop-filter: blur(14px);
	color: white;
	transform: translateX(-100%); /* Начальная позиция за пределами экрана */
	transition: transform 0.3s ease-in-out;
	z-index: 1000;
}

.mobile-menu.menu-open {
	transform: translateX(0); /* Меню выезжает на экран */
}

.mobile-menu ul {
	list-style: none;
	padding: 20px;
	padding-top: 0px;
}
.frame-20 {
	margin-left: 20px;
	margin-top: 20px;
	width: 198px;
	height: 45px;
	font-size: 24px;
	font-weight: 600;
	cursor: pointer;
	background: linear-gradient(90deg, #ffe555, #ff7b5d);
	border: none;
	z-index: 35;
	overflow: hidden;
	border-radius: 32px;
}
.discover-21 {
	font-size: 46px;
	color: #210349;


	font-family: Jomhuria, var(--default-font-family);
	font-weight: 400;
}
.mobile-menu li {
	margin: 15px 0;
}

.mobile-menu a {
	color: white;
	text-decoration: none;
}

.mobile-menu a:hover {
	color: #ff4081;
}
</style>
