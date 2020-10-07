<template>
    <div>
        <div class="container ct-example-row">
            <div class="row">
                <div class="col">
                    <card>
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
                                            
                                            <badge
                                            class="text-uppercase"
                                            v-for="(keyword, index) in essay.keywords"
                                            :key="index"
                                            :type="colors[index % 5]"
                                            >
                                            <b v-if="keyword.length > 30">{{ keyword.substring(0,30) }}...</b>
                                            <b v-else>{{ keyword }}</b>
                                            </badge>
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
                                            <div v-if="!essay.whichDescription">
                                                <span v-for="sentence in essay.shortDescription" :key="sentence">
                                                    {{sentence}}
                                                    <br><br>
                                                </span>
                                            </div>
                                            <span v-else>{{essay.longDescription}}</span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </card>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <b-carousel id="carousel1"
                                controls
                                indicators>
                        <!-- Text slides with image -->
                        <b-carousel-slide v-for="imgName in image.img_list" :key="imgName" :img-src="'http://localhost:8000/' + image.path + '/' + imgName"></b-carousel-slide>
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
                        <div
                            v-for="recom in recommend"
                            :key="recom[0]"
                            @click="goDetail(recom[0])"
                            class="list-group-item list-group-item-action"
                            >{{recom[1]}}
                        </div>
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
import Constant from "@/Constant";

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
      },
      goDetail(nid) {
          this.$router.push({name: 'showdetail', params: {id: nid}})
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
        splitResult = splitResult[1].split("\n")
        for (var s in splitResult) {
            if (splitResult[s] != "") {
                this.essay.shortDescription.push(splitResult[s])
            }
        }
        this.essay.longDescription = result.abstract_long
    },
    async mounted() {
        await this.$store.dispatch(Constant.GET_RECOMMEND, {title: this.essay.title}).then(() => {
            this.recommend = this.$store.state.filestore.recommend.result
        })
        await this.$store.dispatch(Constant.GET_IMAGE).then(() => {
            this.image = this.$store.state.filestore.image
        })
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
          shortDescription: [],
          longDescription: '',
          whichDescription: false,
          filename: ''
      },
      colors: ["primary", "success", "danger", "warning", "info"],
      recommend: [],
      image: {},
    }),
};
</script>

<style>
    .row {
        margin-bottom: 30px;
    }
</style>