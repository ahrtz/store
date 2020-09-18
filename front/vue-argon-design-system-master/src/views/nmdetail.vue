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

            <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
              <li class="nav-item">
                  <a class="nav-link nav-link-icon" href="#">
                      논문 요약
                  </a>
              </li>
              <li class="nav-item">
                  <a class="nav-link nav-link-icon" href="#">
                      논문 검색
                  </a>
              </li>
            </ul>
            <ul class="navbar-nav align-items-lg-center ml-lg-auto">
                <base-dropdown tag="li" class="nav-item">
                    <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
                        <i class="ni ni-circle-08"></i>
                    </a>
                    <a class="dropdown-item" @click="modals.modal0 = true">로그인</a>
                    <a class="dropdown-item" @click="modals.modal1 = true">회원가입</a>
                </base-dropdown>
            </ul>
        </base-nav>
        <modal :show.sync="modals.modal0">
            <my-login>
            </my-login>
        </modal>
        <modal :show.sync="modals.modal1">
            <my-sign-in>
            </my-sign-in>
        </modal>
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
                                            <span v-for="keyword in essay.keywords" :key="keyword" style="display: inline-block; margin-right: 20px">{{keyword}}</span>
                                        </div>
                                    </div>
                                </li>
                                <base-button type="success" @click="essay.whichDescription = !essay.whichDescription">
                                    <span v-if="!essay.whichDescription">긴 요약</span>
                                    <span v-else>짧은 요약</span>
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
import Menu1 from "./components/Navigation/Menu1";
import { BCarousel } from "bootstrap-vue/esm/components/carousel/carousel";
import { BCarouselSlide } from "bootstrap-vue/esm/components/carousel/carousel-slide";
import Modal from "@/components/Modal";
import Card from "@/components/Card";
import wordcloud from 'vue-wordcloud';
import Login from './Login';
import MyLogin from './MyLogin';
import MySignIn from './MySignIn';

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
        Menu1,
        wordcloud,
        BCarousel,
        BCarouselSlide,
        Modal,
        Login,
        MyLogin,
        MySignIn
  },
    methods: {
      wordClickHandler(keyword, frequency, vm) {
        console.log('wordClickHandler', keyword, frequency, vm)
      }
    },
    created: function() {
        let result = this.$store.getters.getResult
        let splitResult = result.key.split(/[, ()]+/)
        for (var s in splitResult) {
            if (splitResult[s] != "[" && splitResult[s] != "]" && isNaN(parseInt(splitResult[s]))) {
                this.essay.keywords.push(splitResult[s])
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
      keywords: [],
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
      ],
      modals: {
          modal0: false,
          modal1: false
      },
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