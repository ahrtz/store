<template>
    <div>
        <div class="container ct-example-row">
            <div class="row">
                <div class="col">
                    <card>
                        <div class="card-header">
                            <h5 class="h3 mb-0">
                                논문 정보
                                <div v-if="this.$store.getters.getIsAuth == true">
                                    <button class="btn btn-1 btn-primary pull-right" @click="scrapEssay()" v-if="!scrapped">스크랩 추가</button>
                                    <button class="btn btn-1 btn-primary pull-right" @click="deleteScrap()" v-else>스크랩 삭제</button>
                                </div>
                            </h5>
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
                                <li class="list-group-item px-0">
                                    <div class="row align-items-center">
                                        <div class="col">
                                            요약
                                        </div>
                                        <div class="col-10">
                                            <span>{{essay.shortDescription}}</span>
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
                    <h5 class="h3 mb-0">추천 논문</h5>
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
  name: "showdetail",
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
      },
      scrapEssay() {
          this.$store.dispatch('addScrap', {essayId: this.$route.params.id}).then(() => {
              this.scrapped = true
          }).catch(e => {
              console.log(e.message)
          })
      },
        async getNMDetail() {
            await this.$store.dispatch(Constant.GET_NM, {sid: this.$route.params.id}).then(() => {
                let nm = this.$store.state.nmstore.nm
                this.essay.title = nm.title_kor != "" ? nm.title_kor : nm.title_eng
                this.essay.author = nm.main_author + " / " + nm.sub_author
                if (nm.keyword_kor != "") {
                    let splitResult = nm.keyword_kor.split(", ")
                    for (var s in splitResult) {
                        this.essay.keywords.push(splitResult[s])
                    }
                }
                if (nm.keyword_eng != "") {
                    let splitResult = nm.keyword_eng.split(", ")
                    for (var s in splitResult) {
                        this.essay.keywords.push(splitResult[s])
                    }
                }
                this.essay.topic = nm.subject
                this.essay.shortDescription = nm.abstract
            }).then(() => {
                this.getRecommend()
            })
        },
        async isScrapped() {
            await this.$store.dispatch(Constant.GET_SCRAPLIST).then(() => {
                let scraps = this.$store.state.scrapstore.scraps
                for (var sc in scraps) {
                    if (scraps[sc].summary.id == this.$route.params.id) {
                        this.scrapped = true
                        break;
                    }
                }
            })
        },
        async getRecommend() {
            await this.$store.dispatch(Constant.GET_RECOMMEND_SEARCH, {title: this.essay.title}).then(() => {
                this.recommend = this.$store.state.filestore.recommend_search.result
            })
        },
        deleteScrap() {
            this.$store.dispatch(Constant.DELETE_SCRAP, {id: this.$route.params.id}).then(() => {
                this.scrapped = false
            }).catch(e => {
              console.log(e.message)
          })
        }
    },
    created: function() {
        this.getNMDetail()
        this.isScrapped()
    },
    watch: {
        '$route.params.id': function() {
            this.getNMDetail()
            this.isScrapped()
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
      keywords: [],
      model: 0,
      scrapped: false,
      defaultWords: [
      ],
      essay: {
          title: 'Application of Digital Forensics for Epidemiological Contact Tracing',
          author: 'In Ha, Yoon',
          keywords: [],
          topic: 'Computer Science',
          shortDescription: '',
          longDescription: ''
      },
        recommend: [],
      colors: ["primary", "success", "danger", "warning", "info"],
    }),
};
</script>

<style>
    .row {
        margin-bottom: 30px;
    }
</style>