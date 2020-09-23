<template>
    <div>
        <div class="container ct-example-row">
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-header">
                            <h5 class="h3 mb-0">논문 정보</h5>
                        </div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item px-0">
                                    <div class="row align-items-center">
                                        <div class="col">
                                            제목
                                        </div>
                                        <div class="col-10">
                                            <span>{{essay.title}}</span>
                                        </div>
                                    </div>
                                </li>
                                <li class="list-group-item px-0">
                                    <div class="row align-items-center">
                                        <div class="col">
                                            분야
                                        </div>
                                        <div class="col-10">
                                            <span>{{essay.topic}}</span>
                                        </div>
                                    </div>
                                </li>
                                <li class="list-group-item px-0">
                                    <div class="row align-items-center">
                                        <div class="col">
                                            키워드 
                                        </div>
                                        <div class="col-10">
                                            <span v-for="keyword in essay.keywords" :key="keyword" style="display: inline-block; width: 160px; text-align: center">{{keyword}}</span>
                                        </div>
                                    </div>
                                </li>
                                <base-button type="success" @click="essay.whichDescription = !essay.whichDescription">
                                    <span v-if="!essay.whichDescription">요약</span>
                                    <span v-else>본문</span>
                                </base-button>
                                <li class="list-group-item px-0">
                                    <div class="row align-items-center">
                                        <div class="col">
                                            요약
                                        </div>
                                        <div class="col-10">
                                            <span v-if="!essay.whichDescription">{{essay.shortDescription}}</span>
                                            <span v-else>{{essay.longDescription}}</span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <b-carousel id="carousel1"
                                controls
                                indicators>
                        <!-- Text slides with image -->
                        <b-carousel-slide img-src="/img/theme/img-1-1200x1000.jpg"></b-carousel-slide>
                        <b-carousel-slide img-src="/img/theme/img-2-1200x1000.jpg"></b-carousel-slide>
                    </b-carousel>
                </div>
                <div class="col">
                    <wordcloud
                        :data="defaultWords"
                        nameKey="keyword"
                        valueKey="frequency"
                        :showTooltip="false"
                        :color="Accent"
                        :wordClick="wordClickHandler">
                    </wordcloud>
                </div>  
            </div>
            <div class="row">
                <div class="col">
                    <div class="list-group">
                        <a href="#" class="list-group-item list-group-item-action active">
                            추천 논문 1
                        </a>
                        <a href="#" class="list-group-item list-group-item-action">추천 논문 2</a>
                        <a href="#" class="list-group-item list-group-item-action">추천 논문 3</a>
                        <a href="#" class="list-group-item list-group-item-action">추천 논문 4</a>
                        <a href="#" class="list-group-item list-group-item-action disabled">추천 논문 5</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Tabs from "@/components/Tabs/Tabs.vue";
import TabPane from "@/components/Tabs/TabPane.vue";
import TabsSection from "./components/JavascriptComponents/TabsSection";
import Navigation from "./components/Navigation.vue";
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";
import { BCarousel } from "bootstrap-vue/esm/components/carousel/carousel";
import { BCarouselSlide } from "bootstrap-vue/esm/components/carousel/carousel-slide";
import Card from "@/components/Card";
import wordcloud from 'vue-wordcloud';

export default {
  name: "nmdetail",
  components: {
        Tabs,
        TabPane,
        TabsSection,
        Navigation,
        BaseNav,
        BaseDropdown,
        CloseButton,
        wordcloud,
        BCarousel,
        BCarouselSlide
  },
    methods: {
      wordClickHandler(keyword, frequency, vm) {
        console.log('wordClickHandler', keyword, frequency, vm)
      }
    },
    created: function() {
        let result = this.$store.getters.getResult
        let splitResult = result.key.split(/[, ()]+/)
        var a = new Object()
        for (var s in splitResult) {
            if (splitResult[s] != "[" && splitResult[s] != "]") {
                if (isNaN(parseInt(splitResult[s]))) {
                    this.essay.keywords.push(splitResult[s].slice(1, -1))
                    a.keyword = splitResult[s].slice(1, -1)
                }
                else {
                    a.frequency = parseInt(splitResult[s])
                    this.defaultWords.push(a)
                    a = new Object()
                }
            }
        }
        splitResult = result.abstract_short.split(";^")
        this.essay.title = splitResult[0]
        this.essay.shortDescription = splitResult[1]
        this.essay.longDescription = result.abstract_long
    },
    data: () => ({
      drawer: null,
      colors: [
        'primary',
        'secondary',
        'yellow darken-2',
        'red',
        'orange',
      ],
      model: 0,
      defaultWords: [],
      essay: {
          title: 'Application of Digital Forensics for Epidemiological Contact Tracing',
          author: 'In Ha, Yoon',
          keywords: [],
          topic: 'Computer Science',
          shortDescription: '',
          longDescription: '',
          whichDescription: false
      }
    }),
};
</script>

<style>
    .row {
        margin-bottom: 30px;
    }
</style>