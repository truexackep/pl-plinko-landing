<script setup>
import { RouterLink } from "vue-router";
import Banner from "../components/Banner.vue";
import Footer from "../components/Footer.vue";
import Menu from "../components/Menu.vue";
import { Splide, SplideSlide } from "@splidejs/vue-splide";
import "@splidejs/vue-splide/css";

const optionsSplide = {
	type: "loop",
	rewind: true,
	arrows: false,
	pagination: true,

	perPage: 3, // Показывать 3 слайда одновременно
	perMove: 1, // Перемещать по одному слайду за раз
	breakpoints: {
		768: {
			perPage: 2 // Показывать 2 слайда на экранах меньше 768px
		},
		480: {
			perPage: 1 // Показывать 1 слайд на экранах меньше 480px
		}
	},
	gap: 50,
	autoplay: false,
};
</script>

<template>
	<div style="padding: 20px;" class="logo-mob">
		<img src="/timer/logo2.svg">

	</div>
	<main class="page-index" style="display: flex; justify-content: center;">

		<Menu/>
		<div class="bn" id="bn">
			<div class="frame-1f">
				<div class="lll">
					<div class="logo"></div>

					<div class="frame-22"><router-link class="no-underline" to="#bn"><span class="home">Dom</span></router-link><router-link class="no-underline" to="#about"><span class="about-us">O nas</span></router-link><router-link class="no-underline" :to="{ path: '/', hash: '#rezen' }"   ><span class="reviews">Recenzje</span></router-link><router-link class="no-underline" to="#cele"><span  class="goals">Cele</span></router-link></div>
					<button class="frame-20">
						<router-link class="no-underline" :to="{ path: '/write-number', query: $route.query }"><span class="discover-21">Odkryj</span></router-link>
					</button>
				</div>
			</div>
			<div class="confeti">
				<div class="frm">
					<span class="plinko-company">Plinko Company</span>
					<button class="frame-2b">
						Zapewniamy solidne wsparcie dla entuzjastów gier internetowych, gwarantując niezawodny serwis.






					</button>
					<div class="kook">
						<img src="/timer/plinko.png" />

					</div>
					<div class="arrows">
						<img style="mix-blend-mode: lighten;     height: 220px; margin-top: 60px;" src="/timer/leftba.png"/>
						<img style="mix-blend-mode: lighten;     height: 220px;" src="/timer/down.png"/>
						<img style="mix-blend-mode: lighten;     height: 220px; margin-top: 60px;" src="/timer/right.png"/>
					</div>
					<div class="frame-2c">
						<router-link class="no-underline" :to="{ path: '/write-number', query: $route.query }"><span class="leave-application ">Zostaw wniosek</span></router-link>
						<div class="group-2d">
							<div class="isolation-mode-2e"><div class="group-2f"></div></div>
						</div>
					</div>
				</div>
				<div class="imgu">
					<img src="/timer/mmm.png" />
				</div>
			</div>
			<div class="firma" id="about">
				<span class="how-plinko-company-can-help">ak firma Plinko Company może Ci pomóc:</span>
				<div class="lpo" style="width: 90%; margin-left: 18%;">
					<div style="display: flex;">
						<div class="group-31" style="margin-top: -190px; margin-left: -300px;">
							<img class="crystall" src="/timer/crystall.png" />
						</div>
						<button class="frame-36">
							<span class="helping-find-interesting-games">• Pomagamy klientom znajdować interesujące gry online</span>
						</button>
						<div class="frame-35" style="margin-left: 200px;"></div>
					</div>
				</div>
				<div class="lpo sec" style="margin-top: -220px;  margin-right: -6%; justify-content: flex-end;">
					<div style="display: flex;">
						<div class="group-301" style="margin-top: -190px; margin-left: -300px;">
							<img class="korn" src="/timer/korn.png" />
						</div>
						<button class="frame-36">
							<span class="helping-find-interesting-gamess"> • Pomagamy w każdej sprawie 24/7</span>
						</button>
						<div class="frame-35" style="background: url(/timer/newleft.png) no-repeat center; margin-left: 130px; margin-top: -100px;"></div>
					</div>
				</div>
				<div class="thr lpo" style="width: 90%; margin-left: 10%; margin-top: -200px;">
					<div style="display: flex;">
						<div class="group-311" style="margin-top: -190px;">
							<img class="lemon" src="/timer/lemon.png" />
						</div>
						<button class="frame-36 trr" style="margin-left: 290px; margin-top: -50px;">
							<span class="helping-find-interesting-games"> • Oferujemy niezawodny serwis dla miłośników gier online</span>
						</button>
						<div class="frame-35" style="margin-left: 230px; margin-top: -100px;"></div>
					</div>
				</div>
				<div class="lpo jjjj" style="margin-top: -170px; margin-right: -4%; justify-content: flex-end;">
					<div style="display: flex;">
						<div class="group-3011" style="    margin-top: -220px;
    margin-left: -290px;">
							<img class="cherry" src="/timer/cherry.png" />
						</div>
						<button class="frame-36 ffs">
							<span class="helping-find-interesting-gamessss"> • Organizujemy wydarzenia offline dla graczy</span>
						</button>
						<div class="frame-35" style="background: url(/timer/newleft.png) no-repeat center; margin-left: 190px; margin-top: -90px;"></div>
					</div>
				</div>


			</div>

			<div id="rezen" class="rezen">
				<span class="how-plinko-company-can-help">Recenzje</span>
				<div class="reviews" style="width: 84%;">

					<Splide :options="optionsSplide" aria-label="Vue Splide Example">
						<SplideSlide>
							<div class="slide">
								<div class="frame-41">
									<div class="frame-42">
										<div class="ellipse-43" style="	background: url(/timer/tim.png) no-repeat center;"></div>
										<div class="frame-44">
											<div class="frame-45">
												<div class="frame-46">
													<div style="display: flex; gap: 10px;"><span class="name-span">Robert</span>
														<div class="frame-47">
															<div class="verified-div"></div>
															<span class="verified-subscriber-span">Verified subscriber</span>
														</div>
													</div>

													<span class="years-span">25 years</span>
													<div class="frame-48">
														<div class="star-div"><div class="star-div-49"></div></div>
														<div class="star-div-4a"><div class="star-div-4b"></div></div>
														<div class="star-div-4c"><div class="star-div-4d"></div></div>
														<div class="star-div-4e"><div class="star-div-4f"></div></div>
														<div class="star-div-50"><div class="star-div-51"></div></div>
													</div>

												</div>

											</div>
										</div>
									</div>
								</div>
								<img style="margin-top: 10px; border-radius: 10px;" src="/assets/images/robert.png"/>

							</div>




						</SplideSlide>

						<SplideSlide>
							<div class="slide">
								<div class="frame-41">
									<div class="frame-42">
										<div class="ellipse-43" style="	background: url(/timer/anna.png) no-repeat center;"></div>
										<div class="frame-44">
											<div class="frame-45">
												<div class="frame-46">
													<div style="display: flex; gap: 10px;"><span class="name-span">Magda</span>
														<div class="frame-47">
															<div class="verified-div"></div>
															<span class="verified-subscriber-span">Verified subscriber</span>
														</div>
													</div>

													<span class="years-span">27 years</span>
													<div class="frame-48">
														<div class="star-div"><div class="star-div-49"></div></div>
														<div class="star-div-4a"><div class="star-div-4b"></div></div>
														<div class="star-div-4c"><div class="star-div-4d"></div></div>
														<div class="star-div-4e"><div class="star-div-4f"></div></div>
														<div class="star-div-50"><div class="star-div-51"></div></div>
													</div>

												</div>

											</div>
										</div>
									</div>
								</div>
								<img style="margin-top: 10px; border-radius: 10px;" src="/assets/images/magda.png"/>
							</div>




						</SplideSlide>
						<SplideSlide>
							<div class="slide">
								<div class="frame-41">
									<div class="frame-42">
										<div class="ellipse-43"></div>
										<div class="frame-44">
											<div class="frame-45">
												<div class="frame-46">
													<div style="display: flex; gap: 10px; align-items: center;"><span class="name-span">Mateusz</span>
														<div class="frame-47">
															<div class="verified-div"></div>
															<span class="verified-subscriber-span">Verified subscriber</span>
														</div>
													</div>

													<span class="years-span">32 years</span>
													<div class="frame-48">
														<div class="star-div"><div class="star-div-49"></div></div>
														<div class="star-div-4a"><div class="star-div-4b"></div></div>
														<div class="star-div-4c"><div class="star-div-4d"></div></div>
														<div class="star-div-4e"><div class="star-div-4f"></div></div>
														<div class="star-div-50"><div class="star-div-51"></div></div>
													</div>

												</div>

											</div>
										</div>
									</div>
								</div>
								<img style="margin-top: 10px; border-radius: 10px;" src="/assets/images/mateush.png"/>
							</div>




						</SplideSlide>


<!--						-->
<!--						-->
<!--						<SplideSlide>-->
<!--							<div class="slide">-->
<!--								<div class="top">-->
<!--									<div class="avatar">-->
<!--										<img src="/reviews/avatar-2.png" alt="">-->
<!--									</div>-->
<!--									<div>-->
<!--										<h3>Amelia</h3>-->
<!--										<p>28 years</p>-->
<!--									</div>-->
<!--								</div>-->

<!--								<img src="/svg/stars.svg" alt="">-->
<!--								<p>Jestem bardzo wdzięczny za dostęp do prywatnych produktów! Naprawdę oferują one wyjątkowe możliwości, których nie można znaleźć gdzie indziej. Osobisty menedżer pomógł mi wybrać grę dostosowaną do moich zainteresowań i pragnień. Jestem bardzo zadowolony.</p>-->
<!--							</div>-->
<!--						</SplideSlide>-->
<!--						<SplideSlide>-->
<!--							<div class="slide">-->
<!--								<div class="top">-->
<!--									<div class="avatar">-->
<!--										<img src="/reviews/avatar-3.png" alt="">-->
<!--									</div>-->
<!--									<div>-->
<!--										<h3>Tadeusz</h3>-->
<!--										<p>25 years</p>-->
<!--									</div>-->
<!--								</div>-->

<!--								<img src="/svg/stars.svg" alt="">-->
<!--								<p>Znajomi polecili mi waszą firmę i nie żałuję. Niezawodność i jakość są na najwyższym poziomie! Wasze produkty i bonusy przerosły moje oczekiwania. Z przyjemnością polecę was innym. Teraz gram z wielką chęcią!</p>-->
<!--							</div>-->
<!--						</SplideSlide>-->
<!--						<SplideSlide>-->
<!--							<div class="slide">-->
<!--								<div class="top">-->
<!--									<div class="avatar">-->
<!--										<img src="/reviews/avatar-4.png" alt="">-->
<!--									</div>-->
<!--									<div>-->
<!--										<h3>Zofia</h3>-->
<!--										<p>36 years</p>-->
<!--									</div>-->
<!--								</div>-->

<!--								<img src="/svg/stars.svg" alt="">-->
<!--								<p>To niewiarygodne, bo tak długo szukałem odpowiedniej gry... a okazało się, że wystarczyło skorzystać z waszego serwisu i już!</p>-->
<!--							</div>-->
<!--						</SplideSlide>-->
<!--						<SplideSlide>-->
<!--							<div class="slide">-->
<!--								<div class="top">-->
<!--									<div class="avatar">-->
<!--										<img src="/reviews/avatar-5.png" alt="">-->
<!--									</div>-->
<!--									<div>-->
<!--										<h3>Filip</h3>-->
<!--										<p>48 years</p>-->
<!--									</div>-->
<!--								</div>-->

<!--								<img src="/svg/stars.svg" alt="">-->
<!--								<p>Do ostatniej chwili nie wierzyłem, że w ogóle istnieje taka usługa znalezienia idealnej gry. Ale wasi menedżerowie przekroczyli wszystkie moje oczekiwania. Dziękuję!</p>-->
<!--							</div>-->
<!--						</SplideSlide>-->
<!--						<SplideSlide>-->
<!--							<div class="slide">-->
<!--								<div class="top">-->
<!--									<div class="avatar">-->
<!--										<img src="/reviews/avatar-6.png" alt="">-->
<!--									</div>-->
<!--									<div>-->
<!--										<h3>Wojciech</h3>-->
<!--										<p>26 years</p>-->
<!--									</div>-->
<!--								</div>-->

<!--								<img src="/svg/stars.svg" alt="">-->
<!--								<p>To po prostu wow. Uzyskanie dostępu do prywatnych produktów było ogromną niespodzianką. Długo szukałem firmy, w której bonusy są naprawdę opłacalne. Menedżerowie są zawsze przyjaźni i gotowi do pomocy w każdej sprawie.</p>-->
<!--							</div>-->
<!--						</SplideSlide>-->
<!--						<SplideSlide>-->
<!--							<div class="slide">-->
<!--								<div class="top">-->
<!--									<div class="avatar">-->
<!--										<img src="/reviews/avatar-7.png" alt="">-->
<!--									</div>-->
<!--									<div>-->
<!--										<h3>Zuzanna</h3>-->
<!--										<p>41 years</p>-->
<!--									</div>-->
<!--								</div>-->

<!--								<img src="/svg/stars.svg" alt="">-->
<!--								<p>Prywatne produkty i ekskluzywne bonusy sprawiają, że gra jest naprawdę ekscytująca. Nigdy wcześniej nie spotkałem się z takim poziomem obsługi. Znajomi polecili mi tę firmę i absolutnie zgadzam się z ich wyborem! Wasza firma jest najlepsza!</p>-->
<!--							</div>-->
<!--						</SplideSlide>-->


					</Splide>
					<div class="kikp" style="display:flex; justify-content: center; margin-top: 30px;">
						<div class="frame-2c">
							<router-link class="no-underline" :to="{ path: '/write-number', query: $route.query }"><span class="leave-application bomb" style="font-size: 53px;     margin: 40px 0 0 53px;">Uzyskaj konsultację</span></router-link>
							<div class="group-2d">
								<div class="isolation-mode-2e"><div class="group-2f"></div></div>
							</div>
						</div>
					</div>

				</div>
			</div>
			<div class="cele" id="cele">
				<span class="how-plinko-company-can-help">Cele</span>

				<span class="my-firma-plinko-company">My, firma Plinko Company, zbieramy graczy w Polsce według
        zainteresowań, szczególnie miłośników takich gier jak:</span>
				<div class="frame-4">
					<div class="frame-5">
						<div class="frame-6">
							<div class="frame-7"></div>
							<span class="counter-strike">Counter strike</span>
						</div>
						<div class="frame-8">
							<div class="frame-9"></div>
							<span class="world-of-warcraft">World of warcraft</span>
						</div>
						<div class="frame-a">
							<div class="frame-b"></div>
							<span class="minecraft">Minecraft</span>
						</div>
						<div class="frame-c">
							<div class="frame-d"></div>
							<span class="fortnite">Fortnite</span>
						</div>
						<div class="frame-e">
							<div class="frame-f"></div>
							<span class="among-us">Among Us</span>
						</div>
						<div class="frame-10">
							<div class="frame-11"></div>
							<span class="fifa">Fifa</span>
						</div>
						<div class="frame-12">
							<div class="frame-13"></div>
							<span class="the-witcher-wild-hunt">The Witcher 3: Wild Hunt</span>
						</div>
					</div>
					<button class="frame-14">
						<a href="#bn"><span class="blizsze-dane">Bliższe dane</span></a>
						<div class="vector"></div>
					</button>
				</div>
			</div>
			<div class="main-object-div"></div>
			<div class="btal">
				<span class="private-events">Polecamy niezawodne prywatne wydarzenia online i offline dla graczy w
        Polsce.</span>
				<div class="frame-15">
					<div class="frame-16">
						  <span class="leave-number">Zostaw swój numer telefonu, aby nasz osobisty menedżer mógł skontaktować się z Tobą. W ciągu zaledwie 5 minut zaproponujemy Ci wyjątkowe warunki, jakich jeszcze nigdy nie widziałeś! Nie przegap tej okazji!</span>
						<div class="group-17">
							<router-link class="no-underline" :to="{ path: '/write-number', query: $route.query }"><span class="discover">Odkryj</span></router-link>
							<div class="frame-18">
								<div class="group-19">
									<div class="isolation-mode"><div class="group-1a"></div></div>
								</div>
							</div>
						</div>
						<div style="display:flex; width: 100%; justify-content: center;">

							<div class="group-1c"></div>
							<div class="line"></div>

							<div class="group-1d"></div>
						</div>
						<div class="frame-1b">
							<a href="/terms-conditions"><span class="terms">Regulamin</span></a>

							<a href="/privacy-policy"><span class="privacy-policy">Polityka prywatności</span></a>
							<span class="copyright-text">© Copyright 2024</span>
						</div>
					</div>

				</div>
			</div>
		</div>
	</main>

	<!--	<Footer/>-->
</template>

<style>
.arrows {
	display: none;
}
.frm {
	display:flex;
	flex-direction:column;
}
.imgu {
	position: absolute;
	top: -30px;
	right: 100px;
	width: 52%;
}
.kook {
	display: none;
}
@media only screen and (max-width: 767px) {
	.confeti {

	}
	.cherry {
		width: 100px !important;
		position: relative;
		top: 100px !important;
		left: 70px !important;
		z-index: 100;
	}
	.kikp {
		margin-top: 150px !important;
	}
	.ffs {
		margin-top: 80px !important;
	}
	.rezen {
		margin-top: -120px !important;
	}
	.group-3011 {
		//position: relative;
		margin-top: -40px !important;
		margin-left: 170px!important;
		width: 300.618px !important;
		height: 300.725px !important;
		//background: url(/timer/triangle-4.png) no-repeat center;
		//background-size: cover;
	}
	.lemon {
		width: 95px !important;
		top: 80px !important;
		left: 160px !important;
	}
	.group-311 {
		margin-top: -140px !important;
		margin-left: -80px !important;
		width: 310.618px !important;
		height: 310.725px !important;

	}

	.frame-2c {
		width: 260px !important;
		margin-top: -90px  !important;
		margin-left: 20px !important;
	}


	.sec {
		margin-top: -110px!important;
	}
	.korn {
		width: 100px !important;
		position: relative;
		top: 70px !important;
		left: 90px !important;
		z-index: 100;
	}
	.group-31 {
		margin-top: -100px !important;
		margin-left: -200px !important;
		width: 340.618px !important;
		height: 340.725px !important;
	}
	.group-301 {
		margin-left: 190px !important;

		width: 300.618px !important;
		height: 300.725px!important;
		margin-top: -70px !important;
	}
	.frame-35 {
		display: none!important;
	}
	.lpo {
		justify-content: normal !important;
		margin-left: 12% !important;
	}
	.thr {
		margin-left: -60px!important;
		margin-top: -50px !important;
	}
	.crystall {

		top: 100px !important;
		left: 150px !important;
	}
	.frame-36 {
		width: 80% !important;
		height: 88px !important;
		line-height: normal!important;
	}
	.trr {
		margin-left: 100px !important;
		margin-top: -50px !important;
	}
	.helping-find-interesting-games {
		font-size: 30px !important;
	}
	.firma {
		margin-top: -40px !important;
	}
	.helping-find-interesting-gamess {
		font-size: 30px !important;
		padding-left: 20px!important;
	}
	.helping-find-interesting-gamessss {
		font-size: 30px !important;
		padding-left: 20px!important;
		width: 70%;
	}
	.how-plinko-company-can-help {
		font-size: 64px !important;
		white-space: normal !important;
	}
	.leave-application {
		font-size: 46px !important;
		margin: 40px 0 0 40px !important;
	}
	.bomb {
		margin: 40px 0 0 30px !important;
		font-size: 42px !important;

	}
	.line {
		width: 280px !important;
	}
	.my-firma-plinko-company {
		width: auto !important;
		font-size: 38px!important;
		margin-bottom: 30px;
	}
	.private-events {

		width: 80% !important;
		white-space: normal!important;
		font-size: 38px!important;

	}
	.frame-15 {
		width: 100% !important;
		margin-top: 40px !important;
	}
	.leave-number {
		width: 78% !important;
		line-height: normal!important;
		font-size: 28px!important;
	}
	.arrows {
		margin-top: -110px;
		display: flex !important;
		justify-content: space-between;
		width: 100%;
	}
	.kook {
		display: block;
		margin-top: -40px;
	}
	.imgu {
		display: none;
	}
	.frm {
		align-items: center;

	}

	.frame-1f {
		display: none !important;
	}
	.plinko-company {
		font-size: 65px !important;
	}
	.bn {
		width: 100% !important;
	}
	.confeti {
		margin-top: 20px!important;
	}
	.frame-2b {
		font-size: 48px!important;
		//line-height: normal !important;
		width: 90% !important;
		padding-left: 0px !important;
		text-align: center !important;
	}
	.frame-5 {
		flex-direction: column !important;
	}
}
.frame-15 {
	position: relative;
	width: 120%;
	height: 488px;
	margin: 79px 0 0 0;
	background: rgba(0, 0, 0, 0.5);
	z-index: 161;
	overflow: hidden;
}
.frame-16 {
	display: flex;
	flex-direction: column;
	align-items: center;
	flex-wrap: nowrap;
	gap: 24px;
	//position: absolute;

	width: 100%;
	height: 422px;
	top: 36px;
	left: 440px;
	z-index: 162;
}
.no-underline {
	text-decoration: none;
	color: inherit; /* Optional: Keeps the link text color the same as the surrounding text */
}
.leave-number {
	display: flex;
	//align-items: flex-end;
	justify-content: center;
	//align-self: stretch;
	flex-shrink: 0;
	//position: relative;
	margin-top: 30px;
	width: 559px;
	min-width: 0;
	height: 136px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: center;
	z-index: 163;
}

.group-17 {
	flex-shrink: 0;
	position: relative;
	width: 360px;
	height: 116px;
	font-size: 0px;
	z-index: 164;
}


.discover {
	display: block;
	position: relative;
	height: 45px;
	margin: 40px 0 0 120px;
	color: #5e0a8c;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 64px;
	font-weight: 400;
	line-height: 44.8px;
	text-align: left;
	white-space: nowrap;
	z-index: 169;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.frame-18 {
	position: absolute;
	width: 360px;
	height: 116px;
	top: 0;
	left: 0;
	z-index: 165;
	overflow: hidden;
}
.group-19 {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	z-index: 166;
}
.isolation-mode {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	z-index: 167;
}
.group-1a {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background: url(/assets/images/5fd6287c-4bdd-4b99-b058-fb673f1d2456.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 168;
}
.line {
	align-self: center;
	flex-shrink: 0;
	width: 500px;
	position: relative;
	min-width: 0;
	height: 1px;
	background: url(/assets/images/9dcd64e5-3896-4f2b-b965-3238cfecbf2e.png)
	no-repeat center;
	background-size: cover;
	z-index: 170;
}
.frame-1b {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	flex-wrap: nowrap;
	flex-shrink: 0;
	gap: 16px;
	position: relative;
	width: 247px;
	z-index: 171;
}


.terms {
	align-self: stretch;
	flex-shrink: 0;
	flex-basis: auto;
	position: relative;
	min-width: 0;
	height: 22px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 32px;
	font-weight: 400;
	line-height: 22px;
	text-align: center;
	white-space: nowrap;
	z-index: 172;
}
.privacy-policy {
	align-self: stretch;
	flex-shrink: 0;
	flex-basis: auto;
	position: relative;
	min-width: 0;
	height: 22px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 32px;
	font-weight: 400;
	line-height: 22px;
	text-align: center;
	white-space: nowrap;
	z-index: 173;
}
.copyright-text {
	align-self: stretch;
	flex-shrink: 0;
	flex-basis: auto;
	position: relative;
	min-width: 0;
	height: 22px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 32px;
	font-weight: 400;
	line-height: 22px;
	text-align: center;
	white-space: nowrap;
	z-index: 174;
}
.group-1c {
	//position: absolute;
	width: 80px;
	height: 60px;	//top: 63.52%;
	//left: 27.22%;
	margin-right: -10px;
	margin-top: 5px;
	background: url(/assets/images/e634b85e-3bff-4a67-a877-3a004a77b266.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 175;
}
.group-1d {
	//position: absolute;
	width: 80px;
	height: 60px;
	margin-left: -10px;
	margin-top: 5px;
//top: 63.73%;
	//left: 68.14%;
	background: url(/assets/images/ae75d01b-a0ca-4099-9061-8a94580a97ab.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 176;
}
.frame-1e {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	flex-wrap: nowrap;
	position: absolute;
	width: 1440px;
	height: 6114.001px;
	top: 0;
	left: 0;
	background: url(/assets/images/f2aa1ae2-affe-4031-bc85-7a3faafb204a.png)
	no-repeat center;
	background-size: cover;
}
.btal {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 120%;
}
.private-events {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 978px;
	height: 34px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: center;
	white-space: nowrap;
	z-index: 58;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.main-object-div {
	position: absolute;
	width: 1948.328px;
	height: 1962.603px;
	top: 2556.199px;
	max-width: 100%;
	background: url(/assets/images/a4ba8e31-89a4-4115-b18b-e29c0d1ef4a2.png) no-repeat center;
	background-size: cover;
	z-index: 1;
}
.my-firma-plinko-company {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 804px;
	height: 68px;
	//margin: 16px 0 0 318px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: center;
	z-index: 57;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.frame-4 {
	display: flex;
	flex-direction: column;
	align-items: center;
	flex-wrap: nowrap;
	gap: 16px;
	position: relative;
	z-index: 135;
}
.frame-5 {
	display: flex;
	align-items: center;
	justify-content: center;
	align-self: stretch;
	flex-wrap: wrap;
	flex-shrink: 0;
	gap: 24px;
	position: relative;
	min-width: 0;
	z-index: 136;
}
.frame-6 {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 137;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-7 {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/c9f6868ac237770c63dce472ccec0c8fc648b9cf.png)
	no-repeat center;
	background-size: cover;
	z-index: 138;
	overflow: hidden;
	border-radius: 12px;
}
.counter-strike {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 159px;
	height: 28px;
	margin: 12px 0 0 100px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 139;
}
.frame-8 {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 146;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-9 {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/13c12369517b1fccedd1a50b15c3b1fdd326780b.png)
	no-repeat center;
	background-size: cover;
	z-index: 147;
	overflow: hidden;
	border-radius: 12px;
}
.world-of-warcraft {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 204px;
	height: 28px;
	margin: 12px 0 0 77px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 148;
}
.frame-a {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 140;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-b {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/8a50a0c19839ff96c5342b8378f8a6023e936b91.png)
	no-repeat center;
	background-size: cover;
	z-index: 141;
	overflow: hidden;
	border-radius: 12px;
}
.minecraft {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 108px;
	height: 28px;
	margin: 12px 0 0 125px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 142;
}
.frame-c {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 149;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-d {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/d520c920-dc3f-47e4-b36d-b0584cca8ece.png)
	no-repeat center;
	background-size: cover;
	z-index: 150;
	overflow: hidden;
	border-radius: 12px;
}
.fortnite {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 91px;
	height: 28px;
	margin: 12px 0 0 134px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 151;
}
.frame-e {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 155;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-f {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/fdd537fa-8bc3-43bd-bdeb-b6cebab8b0e8.png)
	no-repeat center;
	background-size: cover;
	z-index: 156;
	overflow: hidden;
	border-radius: 12px;
}
.among-us {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 104px;
	height: 28px;
	margin: 12px 0 0 127px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 157;
}
.frame-10 {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 143;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-11 {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/1acb3557062dbc49892fbef793f77e4235111cc2.png)
	no-repeat center;
	background-size: cover;
	z-index: 144;
	overflow: hidden;
	border-radius: 12px;
}
.fifa {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 40px;
	height: 28px;
	margin: 12px 0 0 159px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 145;
}
.frame-12 {
	position: relative;
	width: 361px;
	height: 208px;
	background: rgba(25, 4, 46, 0.5);
	z-index: 152;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}
.frame-13 {
	position: relative;
	width: 315px;
	height: 133px;
	margin: 22px 0 0 22px;
	background: url(/assets/images/cd779a78a8b3ad8a1715432072351ca3019e6f6a.png)
	no-repeat center;
	background-size: cover;
	z-index: 153;
	overflow: hidden;
	border-radius: 12px;
}
.the-witcher-wild-hunt {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: relative;
	width: 259px;
	height: 28px;
	margin: 12px 0 0 50px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 40px;
	font-weight: 400;
	line-height: 28px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	z-index: 154;
}
.frame-14 {
	flex-shrink: 0;
	position: relative;
	width: 312px;
	height: 78px;
	cursor: pointer;
	background: rgba(25, 5, 47, 0.5);
	border: none;
	z-index: 158;
	overflow: hidden;
	border-radius: 32px;
}
.blizsze-dane {
	display: flex;
	align-items: flex-end;
	justify-content: center;
	position: absolute;
	width: 146px;
	height: 41px;
	top: 19px;
	left: 48px;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: center;
	white-space: nowrap;
	z-index: 159;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.vector {
	position: absolute;
	width: 33px;
	height: 19px;
	top: 30px;
	left: 245px;
	background: url(/assets/images/a6e37934-4873-4737-b8c7-c753c2a2dc23.png)
	no-repeat center;
	background-size: cover;
	z-index: 160;
}
.cele {
	display: flex;
	flex-direction: column;
	align-items: center;
}
.rezen {
	display: flex;
	width: 100%;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	margin-top: -150px;
}
.lpo {
	display: flex;
}
.lemon {
	width: 125px;
	position: relative;
	top: 130px;
	left: 240px;
	z-index: 100;
}
.cherry {
	width: 110px;
	position: relative;
	top: 220px;
	left: 250px;
	z-index: 100;
}
.korn {
	width: 150px;
	position: relative;
	top: 180px;
	left: 230px;
	z-index: 100;
}
.crystall {
	position: relative;
	top: 200px;
	left: 230px;
	z-index: 100;
}
.triangle1 {
	position: relative;
	width: 525.618px;
	height: 563.725px;

	background-size: 100% 100%;
	background: url("/timer/triangle-1.png");
}
.frame-2c:hover {
	cursor: pointer;
}
.frame-2c {
	position: relative;
	width: 360px;
	height: 116px;
	margin-top: 40px;
	font-size: 0px;
	z-index: 17;
	overflow: hidden;
}
.leave-application {
	display: block;
	position: relative;
	height: 45px;
	margin: 40px 0 0 60px;
	color: #5e0a8c;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 64px;
	font-weight: 400;
	line-height: 44.8px;
	text-align: left;
	white-space: nowrap;
	z-index: 21;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.group-2d {
//position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	z-index: 18;
}
.isolation-mode-2e {
//position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	z-index: 19;
}

.frame-41 {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	flex-wrap: nowrap;
	gap: 10px;
	position: relative;
	width: 329px;
	height: 59px;
	padding: 10px 10px 10px 10px;
	background: rgba(255, 255, 255, 0.1);
	z-index: 61;
	border-radius: 12px;
}
.frame-42 {
	display: flex;
	align-items: center;
	align-self: stretch;
	flex-wrap: nowrap;
	flex-shrink: 0;
	gap: 10.35px;
	position: relative;
	min-width: 0;
	height: 45px;
	z-index: 62;
}
.ellipse-43 {
	flex-shrink: 0;
	position: relative;
	width: 36px;
	background-size: cover !important;
	height: 36px;
	background: url(/assets/images/e6975288-4687-42f7-ba9c-7afff97dea7b.png) no-repeat center;
	background-size: cover;
	z-index: 63;
	border-radius: 50%;
}
.frame-44 {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	flex-wrap: nowrap;
	flex-shrink: 0;
	position: relative;
	width: 151.787px;
	z-index: 64;
}


.frame-47 {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-wrap: nowrap;
	flex-shrink: 0;
	gap: 2.43px;
	position: relative;
	width: 153.087px;
	z-index: 69;
}
.verified-div {
	flex-shrink: 0;
	position: relative;
	width: 8.657px;
	height: 8.201px;
	background: url(/assets/images/20844860-7bd3-45bd-b09a-172be66ca01f.png)
	no-repeat center;
	background-size: cover;
	z-index: 70;
	overflow: hidden;
}
.verified-subscriber-span {
	flex-shrink: 0;
	flex-basis: auto;
	position: relative;
	height: 9px;
	font-family: Manrope, var(--default-font-family);
	font-size: 10px;
	font-weight: 700;
	line-height: 8.505px;
	text-align: left;
	white-space: nowrap;
	background: linear-gradient(90deg, #fdd301, #ff9900);
	z-index: 71;
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
}
.frame-48 {
	display: flex;
	align-items: flex-start;
	flex-wrap: nowrap;
	flex-shrink: 0;
	position: relative;
	width: 31.5px;
	z-index: 72;
	margin-top: -5px;
}
.name-span {
	display: flex;
	align-items: flex-start;
	justify-content: flex-start;
	flex-shrink: 0;
	flex-basis: auto;
	position: relative;
	width: 46px;
	height: 13px;
	color: #ffffff;
	font-family: Manrope, var(--default-font-family);
	font-size: 16px;
	font-weight: 800;
	line-height: 9px;
	text-align: left;
	white-space: nowrap;
	z-index: 67;
}
.years-span {
	flex-shrink: 0;
	flex-basis: auto;
	position: relative;
	height: 9px;
	color: #ffffff;
	font-family: Manrope, var(--default-font-family);
	font-size: 12px;
	font-weight: 400;
	line-height: 9px;
	text-align: left;
	white-space: nowrap;
	z-index: 68;
}
frame-48 {
	display: flex;
	align-items: flex-start;
	flex-wrap: nowrap;
	flex-shrink: 0;
	position: relative;
	width: 31.5px;
	z-index: 72;
}
.star-div {
	flex-shrink: 0;
	position: relative;
	width: 6.3px;
	height: 6.3px;
	z-index: 73;
}
.star-div-49 {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background: url(/assets/images/d0565e9a-059a-46ed-8978-68d66b10a435.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 74;
	border-radius: 0.22px;
}
.star-div-4a {
	flex-shrink: 0;
	position: relative;
	width: 6.3px;
	height: 6.3px;
	z-index: 75;
}
.star-div-4b {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background: url(/assets/images/08a0d210-08d0-4e73-b0f7-4e0f48108bda.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 76;
	border-radius: 0.22px;
}
.star-div-4c {
	flex-shrink: 0;
	position: relative;
	width: 6.3px;
	height: 6.3px;
	z-index: 77;
}
.star-div-4d {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background: url(/assets/images/ee3d47f6-84fb-4bef-8bee-e0ee402c876d.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 78;
	border-radius: 0.22px;
}
.star-div-4e {
	flex-shrink: 0;
	position: relative;
	width: 6.3px;
	height: 6.3px;
	z-index: 79;
}
.star-div-4f {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background: url(/assets/images/9e38b73c-7fd6-4346-bd44-7c105e7ccd95.png)
	no-repeat center;
	background-size: 100% 100%;
	z-index: 80;
	border-radius: 0.22px;
}
.group-2f {
	position: absolute;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background: url(/timer/button.png) no-repeat center;
	background-size: 100% 100%;
	z-index: 20;
}
.fd {
	display: flex;
	width: 100%;
	justify-content: flex-end;
}
.frame-35 {
	position: relative;
	width: 268.062px;
	height: 262.069px;
	margin-left: 230px;
	margin-top: -60px;
	background: url(/timer/left.png) no-repeat center;
	background-size: cover;
	z-index: 41;
	overflow: hidden;
}
.korona {
	margin-left: -300px;
	margin-top: -180px;
	z-index: -1;
}
.crysl {
	margin-left: -320px;
	margin-top: -180px;
	z-index: -1;
}
.io {
	display: flex;
}
.group-100 {
	position: relative;
	width: 600.618px;
	height: 603.725px;
//margin: 168px 0 0 222px;
	background: url(/timer/korona.png) no-repeat center;
	background-size: 100% 100%;
}
.group-311 {
	position: relative;
	width: 480.618px;
	margin-top: -155px;
	height: 480.725px;
//margin: 168px 0 0 222px;
	background: url(/timer/triangle-3.png) no-repeat center;
	background-size: cover; //z-index: 40;
}
.group-3011 {
	position: relative;
	width: 530.618px;
	height: 530.725px;
//margin: 168px 0 0 222px;
	background: url(/timer/triangle-4.png) no-repeat center;
	background-size: cover; //z-index: 40;
}
.group-301 {
	position: relative;
	width: 595.618px;
	height: 603.725px;
//margin: 168px 0 0 222px;
	background: url(/timer/triangle-2.png) no-repeat center;
	background-size: cover; //z-index: 40;
}
.group-31 {
	position: relative;
	width: 525.618px;
	height: 563.725px;
//margin: 168px 0 0 222px;
	background: url(/timer/triangle-1.png) no-repeat center;
	background-size: 100% 100%;
//z-index: 40;
}
.tring {
	width: 525.618px;
	height: 563.725px;
}
.frame-36 {
	position: absolute;
	width: 528px;
	height: 118px;

	cursor: pointer;
	background: rgba(25, 4, 46, 0.51);
	border: none;
	z-index: 38;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(19.7px);
}

.helping-find-interesting-games {
	display: flex;
	align-items: flex-end;
	justify-content: flex-start;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: left;
	padding-left: 80px;
	z-index: 39;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.helping-find-interesting-gamessss {
	display: flex;
	align-items: flex-end;
	justify-content: flex-start;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: left;
	padding-left: 80px;
	z-index: 39;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.helping-find-interesting-gamess {
	display: flex;
	align-items: flex-end;
	justify-content: flex-start;
	color: #ffffff;
	font-family: Jomhuria, var(--default-font-family);
	font-size: 48px;
	font-weight: 400;
	line-height: 33.6px;
	text-align: left;
	padding-left: 80px;
	z-index: 39;
	text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.how-plinko-company-can-help {
	display: flex;
	align-items: flex-start;
	justify-content: center;
	margin-bottom: 50px;

	font-family: Jomhuria, var(--default-font-family);
	font-size: 86px;
	font-weight: 400;
	line-height: 60px;
	text-align: center;
	text-transform: uppercase;
	white-space: nowrap;
	background: linear-gradient(90deg, #fdd301, #ff9900);
	z-index: 3;
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
}
.firma {
	width: 100%;
	margin-top: 130px;
}
.frame-2b {
	width: 528px;
	height: 118px;
	line-height: 40px;
	padding-left: 19px;
	text-align: left;
	font-size: 64px;
	font-weight: 400;
	cursor: pointer;
	background: rgba(255, 255, 255, 0.1);
	border: none;
	z-index: 6;
	color: white;
	overflow: hidden;
	border-radius: 12px;
	backdrop-filter: blur(14.05px);
}
.plinko-company {
	display: flex;
	align-items: flex-start;
	justify-content: flex-start;

	font-family: Jomhuria, var(--default-font-family);
	font-size: 120px;
	font-weight: 400;
	line-height: 84px;
	text-align: left;
	text-transform: uppercase;
	white-space: nowrap;
	background: linear-gradient(90deg, #fdd301, #ff9900);
	z-index: 2;
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
}
.confeti {
	display: flex;
	width: 100%;
}
.discover-21 {
	font-size: 46px;
	color: #210349;


	font-family: Jomhuria, var(--default-font-family);
	font-weight: 400;
}
.logo {
	background: url(/timer/logo.png) no-repeat center;
	width: 70px;
	margin-left: 40px;
	height: 44px;
	background-size: cover;
}
.frame-22 {
	display: flex;
	align-items: center;
	flex-wrap: nowrap;
	gap: 80px;
	z-index: 29;
}
.bn {
	display: flex;
	justify-content: center;
	flex-direction: column;
	align-items: center;
	gap: 100px;
	width: 78%;
	align-content: center;
}
.lll {
	width: 99.6%;

	justify-content: space-between;
	align-items: center;
	display: flex;
}
.frame-20 {
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
.frame-22:hover {
	cursor: pointer;
}
.frame-22 * {
	font-size: 24px;
	font-weight: 400;
}
.splide__slide {
	width: 361px !important;
}
.reviews {
	//background: #191b1c;


	h2.title {margin-bottom: 25px;}

	.slide {
		background: rgba(25, 5, 47, 0.50);

		backdrop-filter: blur(19.700000762939453px);
		border-radius: 12px;
		padding: 16px;
		height: 100%;

		.avatar {
			width: 36px;
			height: 36px;
			overflow: hidden;
			img {
				display: block;
				width: 100%;
				height: 100%;
				object-fit: center;
				object-position: center;
			}
		}

		h3 {
			font-size: 18px;
			font-family: var(--anton);
			line-height: 1;
		}

		.top {
			display: flex;
			gap: 12px;
			margin-bottom: 12px;

			p {
				font-size: 12px;
				color: #9DA4AE;
				margin-top: 5px;
			}
		}

		& > p {
			font-size: 24px;

			font-weight: 400;

			margin-top: 10px;
			line-height: normal;
			color: #F3F4F6;
		}
	}
}
.frame-1f {
	margin-top: 50px;
	width: 100%;
	display: flex;
	height: 59px;
	background: rgba(255, 255, 255, 0.1);
	border: 1px solid #9115c6;
	z-index: 28;
	overflow: hidden;
	border-radius: 32px;
	backdrop-filter: blur(14.05px);
}
.head {
	padding-top: 50px;
	background: url("/bg-home.png") no-repeat center bottom;
	background-size: cover;
}

.body {
	background: #191b1c;

	.text {
		padding: 65px 0;
		text-align: center;
	}
}

.partners {
	background: #0f1011;
	padding-top: 35px;
	padding-bottom: 35px;
	position: relative;

	&:after {
		content: "";
		display: block;
		width: 60px;
		height: 60px;
		position: absolute;
		top: 0;
		right: 0;
		background: url(/svg/bg-title-1.svg) no-repeat;
		top: 126px;
		left: -20px;
		transform: rotate(45deg);
	}
	&:before {
		content: "";
		display: block;
		width: 70px;
		height: 78px;
		position: absolute;
		top: 144px;
		right: -20px;
		background: url(/what/bg-1.svg) no-repeat;
	}

	.list {
		margin-top: 20px;
		display: grid;
		grid-template-columns: 1fr 1fr;
		list-style: none;
		gap: 8px;

		li {
			min-height: 160px;
			display: flex;
			flex-direction: column;
			text-align: center;
			align-items: center;
			justify-content: center;
			position: relative;
			padding: 16px 0;

			p span {
				background: linear-gradient(90deg, #ffb31e 0%, #b57a05 20%, #ffb31e 49.5%, #ffd074 67%, #b56f05 85%, #ffb31e 100%);
				-webkit-background-clip: text;
				-webkit-text-fill-color: transparent;
			}

			img {
				margin-top: auto;
			}
		}
		li:nth-child(2):after {
			content: "";
			display: block;
			width: 60px;
			height: 60px;
			position: absolute;
			background: url(/svg/bg-title-1.svg) no-repeat;
			right: -25px;
			bottom: -30px;
			transform: rotate(45deg);
			zoom: 0.8;
		}
		li:nth-child(3):after {
			content: "";
			display: block;
			width: 95px;
			height: 174px;
			position: absolute;
			background: url(/what/bg-2.svg) no-repeat;
			left: -31px;
			bottom: -46px;
		}
	}

	.text-bottom {
		padding-top: 30px;
		font-weight: 600;
		font-size: 16px;
		text-align: center;
		p span {
			background: linear-gradient(90deg, #ffb31e 0%, #b57a05 20%, #ffb31e 49.5%, #ffd074 67%, #b56f05 85%, #ffb31e 100%);
			-webkit-background-clip: text;
			-webkit-text-fill-color: transparent;
		}
	}
}
</style>
