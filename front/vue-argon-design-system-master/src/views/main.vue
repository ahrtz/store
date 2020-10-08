<template>
  <div>
    <!-- <carousel /> -->
    <div style="text-align : center;">
      <br><br><br>
      <div style="font-size: 4rem; font-family: 'Black Han Sans', sans-serif; text-align:center;">PDF KCI 논문 요약 서비스</div>

    </div>
    <div>
      <file v-on:update="showloading" />
    </div>
      <div style="font-size: 2rem; font-family: 'Black Han Sans', sans-serif; text-align:center;">※ KCI 논문에 최적화되어 있으며 영어 논문 요약의 경우 한글보다 더 오래 걸릴 수도 있습니다.</div>
      <br><br><br>
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
