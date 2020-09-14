<template>
    <div>
        <hero></hero>
        여기인가요
        <basic-elements></basic-elements>
        여기인가요
        <inputs></inputs>
        여기인가요
        <custom-controls></custom-controls>
        여기인가요
        <navigation></navigation>
        여기인가요
        <javascript-components></javascript-components>
        여기인가요
        <icons></icons>
        여기인가요
        <examples></examples>
        여기인가요
        <download-section></download-section>
        여기인가요
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
