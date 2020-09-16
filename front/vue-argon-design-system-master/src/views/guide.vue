<template>
    <div>
        <hero></hero>
        <h1>argon 컴포넌트 페이지입니다.</h1>
        여기인가요1
        <basic-elements></basic-elements>
        여기인가요2
        <inputs></inputs>
        여기인가요3
        <custom-controls></custom-controls>
        여기인가요4
        <navigation></navigation>
        여기인가요5
        <javascript-components></javascript-components>
        여기인가요6
        <icons></icons>
        여기인가요7
        <examples></examples>
        여기인가요8
        <download-section></download-section>
        여기인가요9
        <carousel></carousel>
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
    DownloadSection
  }
};
</script>
