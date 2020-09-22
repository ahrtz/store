<template>
  <div>
    <h1>메인페이지입니다.</h1>
    <router-link to="/guide">컴포넌트 가이드</router-link>
    <br />
    <router-link to="/nmdetail">논문상세페이지 임시 이동 링크</router-link>
    <br />
    <router-link to="/search">검색페이지 임시 이동 링크</router-link>
    <br />
    <router-link to="/scrap">스크랩 페이지 임시 이동 링크</router-link>

    <div style="text-align : center;">
      <h1>
        <strong>PDF 논문 요약 서비스</strong>
      </h1>
    </div>
    <div>
      <file v-on:update="showloading" />
    </div>
    <div>
      <introduce />
    </div>
    <!-- The Modal -->
    <div class="modal" id="momo" style="z-index : 100;">
      <img src="@/assets/images/loading.gif" alt />
      <h1 class="whitetext">
        <b>PDF 요약 중입니다.</b>
      </h1>
      <h1 class="whitetext">
        <b>잠시만 기다려주세요!</b>
      </h1>
    </div>
    <!-- Modal end  -->
    <!-- <button @click="showloading()">임시</button> -->
  </div>
</template>
<script>
// import Hero from "./components/Hero";
import BasicElements from "./components/BasicElements";
import Inputs from "./components/Inputs";
import CustomControls from "./components/CustomControls";
import Navigation from "./components/Navigation";
import JavascriptComponents from "./components/JavascriptComponents";
import Carousel from "./components/Carousel";
import Icons from "./components/Icons";
import Examples from "./components/Examples";
import DownloadSection from "./components/DownloadSection";

// import nmdetail from "./nmdetail";
import file from "./components/file";
import introduce from "./components/introduce";
import search from "./search";

export default {
  name: "components",
  components: {
    // Hero,
    BasicElements,
    Inputs,
    CustomControls,
    Navigation,
    JavascriptComponents,
    Carousel,
    Icons,
    Examples,
    DownloadSection,
    // nmdetail,
    file,
    introduce,
    search,
  },

  methods: {
    showloading() {
      console.log("한단계");
      this.openModal();
    },

    openModal() {
      // Get the modal
      var modal = document.getElementById("momo");

      // Get the <span> element that closes the modal
      var span = document.getElementsByClassName("close")[0];

      // When the user clicks on the button, open the modal
      modal.style.display = "block";
      // window.scrollY = 0;
      // document.querySelector("html").scrollTop = 0;
      // document.querySelector(".main-panel").scrollTop = 0;
      // When the user clicks on <span> (x), close the modal
      // span.onclick = function () {
      //   modal.style.display = "none";
      // };
      // When the user clicks anywhere outside of the modal, close it
      window.onclick = function (event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      };
    },
  },
};
</script>

<style scoped>
/* .active {

  background-color: rgba(0, 0, 0, 0.4); 
} */
@import url("https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap");

.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
  text-align: center;
  padding-top: 10%;
}

.whitetext {
  font-family: "Gamja Flower", cursive;
  color: white;
}
</style>
