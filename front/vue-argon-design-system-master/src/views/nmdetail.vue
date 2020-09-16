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
                    <router-link to="/register" class="dropdown-item">회원가입</router-link>
                </base-dropdown>
            </ul>
        </base-nav>
        <modal :show.sync="modals.modal0">
            <template slot="header">
                <h5 class="modal-title" id="exampleModalLabel">로그인</h5>
            </template>
            <div>
                <base-input type="text" name="uid" v-model="formData.uid" v-validate="'required'" label="아이디"/>
                <base-input type="password" name="password" v-model="formData.password" v-validate="'required'" label="패스워드"/>
            </div>
            <template slot="footer">
                <base-button type="primary">로그인</base-button>
            </template>
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
                                            저자
                                        </div>
                                        <div class="col-10">
                                            <span>{{essay.author}}</span>
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
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <tabs fill class="flex-column flex-md-row">
                        <card shadow>
                            <tab-pane key="tab1">
                                <template slot="title">
                                    <i class="ni ni-folder-17"></i>요약 전체
                                </template>

                                <div class="list-group">
                                    <a href="#" class="list-group-item list-group-item-action active">
                                        연구 주제 1
                                    </a>
                                    <a href="#" class="list-group-item list-group-item-action">연구 방법 1</a>
                                    <a href="#" class="list-group-item list-group-item-action">연구 방법 2</a>
                                    <a href="#" class="list-group-item list-group-item-action">연구 결과 1</a>
                                    <a href="#" class="list-group-item list-group-item-action">연구 결과 2</a>
                                </div>
                            </tab-pane>

                            <tab-pane key="tab2">
                                <template slot="title">
                                    <i class="ni ni-bulb-61"></i>연구 주제
                                </template>

                                <div class="list-group">
                                    <a href="#" class="list-group-item list-group-item-action active">연구 주제 1</a>
                                </div>
                            </tab-pane>

                            <tab-pane key="tab3">
                                <template slot="title">
                                    <i class="ni ni-atom"></i>연구 방법
                                </template>

                                <div class="list-group">
                                    <a href="#" class="list-group-item list-group-item-action active">연구 방법 1</a>
                                    <a href="#" class="list-group-item list-group-item-action">연구 방법 2</a>
                                </div>
                            </tab-pane>

                            <tab-pane key="tab4">
                                <template slot="title">
                                    <i class="ni ni-chart-bar-32"></i>연구 결과
                                </template>

                                <div class="list-group">
                                    <a href="#" class="list-group-item list-group-item-action active">연구 결과 1</a>
                                    <a href="#" class="list-group-item list-group-item-action">연구 결과 2</a>
                                </div>
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
        Modal
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
      formData: {
          uid: '',
          password: ''
      },
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
          modal0: false
      },
      essay: {
          title: 'Application of Digital Forensics for Epidemiological Contact Tracing',
          author: 'In Ha, Yoon',
          keywords: [
              'Digital Forensics',
              'Contact Tracing',
          ],
          topic: 'Computer Science'
      }
    }),
};
</script>

<style>
    .row {
        margin-bottom: 30px;
    }
</style>