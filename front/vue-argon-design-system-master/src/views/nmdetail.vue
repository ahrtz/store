<template>
    <div>
        <base-nav v-for="menu in menus"
                  :key="menu.type"
                  :type="menu.type"
                  effect="dark"
                  expand
                  title="논문 요약 시스템"
                  :content-id="`navbar-${menu.type}`">
            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="./index.html">
                        <img src="img/brand/blue.png">
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu" :target="`navbar-${menu.type}`">

                    </close-button>
                </div>
            </div>
            <component :is="menu.menuComponent"></component>
        </base-nav>
        <div class="container ct-example-row">
            <div class="row">
                <div class="col">
                    <tabs fill class="flex-column flex-md-row">
                        <card shadow slot-scope="{activeTabIndex}">
                            <tab-pane key="tab1">
                                <template slot="title">
                                    <i class="ni ni-folder-17"></i>요약 전체
                                </template>

                                <p class="description">Raw denim you probably haven't heard of them jean shorts
                                    Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache
                                    cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro
                                    keffiyeh dreamcatcher synth.</p>
                                <p class="description">Raw denim you probably haven't heard of them jean shorts
                                    Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse.</p>
                            </tab-pane>

                            <tab-pane key="tab2">
                                <template slot="title">
                                    <i class="ni ni-bulb-61"></i>연구 주제
                                </template>

                                <p class="description">Cosby sweater eu banh mi, qui irure terry richardson ex
                                    squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan
                                    american apparel, butcher voluptate nisi qui.</p>
                            </tab-pane>

                            <tab-pane key="tab3">
                                <template slot="title">
                                    <i class="ni ni-atom"></i>연구 방법
                                </template>

                                <p class="description">Raw denim you probably haven't heard of them jean shorts
                                    Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache
                                    cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro
                                    keffiyeh dreamcatcher synth.</p>
                            </tab-pane>

                            <tab-pane key="tab4">
                                <template slot="title">
                                    <i class="ni ni-chart-bar-32"></i>연구 결과
                                </template>

                                <p class="description">Raw denim you probably haven't heard of them jean shorts
                                    Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache
                                    cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro
                                    keffiyeh dreamcatcher synth.</p>
                            </tab-pane>
                        </card>
                    </tabs>
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
import CloseButton from "@/components/CloseButton";
import Menu1 from "./components/Navigation/Menu1";
import { BCarousel } from "bootstrap-vue/esm/components/carousel/carousel";
import { BCarouselSlide } from "bootstrap-vue/esm/components/carousel/carousel-slide";
import wordcloud from 'vue-wordcloud'

export default {
  name: "nmdetail",
  components: {
        Tabs,
        TabPane,
        TabsSection,
        Navigation,
        BaseNav,
        CloseButton,
        Menu1,
        wordcloud,
        BCarousel,
        BCarouselSlide
  },
    methods: {
      wordClickHandler(keyword, frequency, vm) {
        console.log('wordClickHandler', keyword, frequency, vm)
      }
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
      defaultWords: [{
          "keyword": "Lux",
          "frequency": 26
        },
        {
          "keyword": "Syndra",
          "frequency": 17
        },
        {
          "keyword": "Orianna",
          "frequency": 14
        },
        {
          "keyword": "Lulu",
          "frequency": 8
        },
        {
          "keyword": "Xerath",
          "frequency": 8
        },
        {
          "keyword": "Viktor",
          "frequency": 7
        },
        {
          "keyword": "Ezreal",
          "frequency": 7
        },
        {
          "keyword": "Poppi",
          "frequency": 4
        },
        {
          "keyword": "Ryze",
          "frequency": 4
        },
        {
          "keyword": "Jayce",
          "frequency": 3
        },
      ],
      menus: [
        { type: "default", menuComponent: Menu1 }
      ]
    }),
};
</script>

<style>
    .row {
        margin-bottom: 40px;
    }
</style>