<template>
  <div>
    <h1>메인페이지입니다.</h1>
    <router-link to="/guide">컴포넌트 가이드</router-link><br>
    <router-link to="/nmdetail">논문상세페이지 임시 이동 링크</router-link><br>
    <router-link to="/search">검색페이지 임시 이동 링크</router-link>

    <div style="text-align : center;">
      <h1><strong>PDF 논문 요약 서비스</strong></h1>
    </div>
    <div>
      <file />
    </div>
    <div>
      <introduce />
    </div>
  

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
};
</script>
