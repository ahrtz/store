<template>
  <div>
    <hero></hero>
    <h1>메인페이지입니다.</h1>
    <router-link to="/guide">컴포넌트 가이드</router-link><br>
    <router-link to="/nmdetail">논문상세페이지 임시 이동 링크</router-link>
  </div>
</template>
<script>
import Hero from "./components/Hero";
import BasicElements from "./components/BasicElements";
import Inputs from "./components/Inputs";
import CustomControls from "./components/CustomControls";
import Navigation from "./components/Navigation";
import JavascriptComponents from "./components/JavascriptComponents";
import Carousel from "./components/Carousel";
import Icons from "./components/Icons";
import Examples from "./components/Examples";
import DownloadSection from "./components/DownloadSection";

import nmdetail from "./nmdetail";

export default {
  name: "components",
  components: {
    Hero,
    BasicElements,
    Inputs,
    CustomControls,
    Navigation,
    JavascriptComponents,
    Carousel,
    Icons,
    Examples,
    DownloadSection,
    nmdetail,
  },
};
</script>
