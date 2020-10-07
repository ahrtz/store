<template>
  <div class="section-hero section-shaped my-0">
    <appHeader />
    <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
    <div class="shape shape-style-1 shape-primary"></div>
    <div class="container py-0 pb-lg">
      <div class="row justify-content-between align-items-center">
        <div class="col-lg-5 mb-5 mb-lg-0">
          <h1 class="text-white font-weight-light">STORE Service</h1>
          <p class="lead text-white mt-4">
            Summary Thesis Online <br />and Recommend for Everyone
          </p>
          <p class="lead text-white mt-4">
            더 이상 힘들이지 말고<br />스토어를 이용해보세요!!
          </p>
          <!-- <router-link to="/stepper" class="btn btn-white mt-4">STORE 이용 가이드</router-link> -->
        </div>
        <div class="col-lg-6 mb-lg-auto">
          <div
            class="rounded shadow-lg overflow-hidden transform-perspective-right"
          >
            <b-carousel id="carousel1" controls indicators>
              <!-- Text slides with image -->
              <b-carousel-slide
                img-src="img/theme/논문요약.PNG"
              ></b-carousel-slide>
              <b-carousel-slide
                img-src="img/theme/논문검색.PNG"
              ></b-carousel-slide>
              <b-carousel-slide
                img-src="img/theme/마이스크랩.PNG"
              ></b-carousel-slide>
            </b-carousel>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { BCarousel } from "bootstrap-vue/esm/components/carousel/carousel";
import { BCarouselSlide } from "bootstrap-vue/esm/components/carousel/carousel-slide";
import AppHeader from "@/layout/AppHeader";

export default {
  components: {
    BCarousel,
    BCarouselSlide,
    AppHeader,
  },
};
</script>
<style scoped>
.section-hero {
  width: 100%;
  height: 80%;
}

#logo {
  width: 100%;
  height: 100%;
}
</style>
