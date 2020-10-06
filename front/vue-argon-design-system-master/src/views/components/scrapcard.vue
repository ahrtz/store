<template>
  <div class="card">
    <!-- 카드 헤더 -->

    <div
      class="card-header"
      v-bind:style="{
        backgroundImage:
          'url(' + require('@/assets/images/category/'+addr+'.jpg') + ')',
      }"
    >
      <button class="card-header-is_closed" @click="deleteScrap">
        <div class="card-header-text">스크랩 삭제</div>
      </button>
      <div class="card-header-is_closed2">
        <div class="card-header-text">{{ sid.subject }}</div>
      </div>
    </div>

    <!--  카드 바디 -->

    <div class="card-body">
      <!--  카드 바디 헤더 -->

      <div class="card-body-header">
        <h1>{{ sid.title_kor.substring(0, 20) }}...</h1>

        <badge
          class="text-uppercase"
          v-for="(keyword, index) in keywords"
          :key="index"
          :type="colors[index % 5]"
        >
          <b v-if="keyword.length > 9">{{ keyword.substring(0, 9) }}..</b>
          <b v-else>{{ keyword }}</b>
        </badge>

        <p class="card-body-nickname">
          작성자: {{ sid.main_author.substring(0, 20) }}...
        </p>
      </div>

      <p class="card-body-description">
        {{ sid.title_kor }}
        <br />
        <router-link
          :to="'/showdetail/' + sid.id"
          tag="button"
          class="btn btn-primary"
          >상세보기</router-link
        >
      </p>

      <!--  카드 바디 본문 -->

      <!--  카드 바디 푸터 -->

      <div class="card-body-footer">
        <hr style="margin-bottom: 8px; opacity: 0.5; border-color: #ef5a31" />

        <i class="icon icon-view_count"></i>인용횟수 {{ sid.quote }}회

        <i class="icon icon-comments_count"></i>

        <i class="reg_date"> 발행연월 {{ sid.issue_year }} </i>
      </div>
    </div>
  </div>
</template>

<script>
import Constant from "../../Constant.js";
import http from "@/http-common.js";
export default {
  data() {
    return {
      selectedCard: -1,
      addr: this.sid.subject,
      keywords: this.sid.keyword_kor.replace(" · ",", ").split(", ").slice(0,3),
      colors: ["primary", "success", "danger", "warning", "info"],
    };
  },
  props: {
    sid: {
      type: Object,
      required: true,
    },
    id: {
      type: Number,
      required: true,
    },
  },
  created() {
    // console.log("개별 디스패치");
    // this.$store.dispatch(Constant.GET_NM, { sid: this.sid });
    
  },
  computed: {
    // scp() {
    //       console.log('개별 컴퓨티드');
    //   return this.$store.state.nmstore.nm;
    // },
  },
  methods: {
    deleteScrap() {
      var bool = confirm('정말 삭제하시겠습니까?');
      if(bool){
        // alert('yes');
        this.$store.dispatch(Constant.DELETE_SCRAP, { id: this.id });

      }
    },
  },
};
</script>

<style scoped lang="scss">
html,
body,
div,
span,
applet,
object,
iframes,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
quotes,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
sub,
sup,
tt,
var,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;

  padding: 0;

  border: 0;

  font-size: 100%;

  do: inherit;

  vertical-align: baseline;
}

article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}

blockquote,
q {
  quotes: none;
}

// blockquote : before, blockquote : after, q : before, q : after {

// 	content: '';

// 	content: none;

// }

table {
  border-collapse: collapse;

  border-spacing: 0;
}

/*css 초기화*/

.card {
  height: 400px;

  width: 350px;

  border-radius: 15px;

  display: inline-block;

  margin-top: 30px;

  margin-left: 30px;

  margin-bottom: 30px;

  position: relative;

  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);

  overflow: hidden;
}

.card-header {
  -webkit-transition: 0.5s; /*사파리 & 크롬*/

  -moz-transition: 0.5s; /*파이어폭스*/

  -ms-transition: 0.5s; /*인터넷 익스플로러*/

  -o-transition: 0.5s; /*오페라*/

  transition: 0.5s;

  width: 100%;

  height: 270px;

  border-radius: 15px 15px 0 0;

  // background-image: url("images/korea.jpeg");

  background-size: 100% 280px;

  background-repeat: no-repeat;
}

.card:hover .card-header {
  opacity: 0.8;

  height: 100px;
}

.card-header-is_closed {
  background-color: #ef5a31;

  color: #fff;

  font-weight: bold;

  text-align: center;

  float: right;

  margin: 15px 15px 0 0;

  border-radius: 50%;

  font-weight: bold;

  padding: 10px 10px;

  line-height: 20px;
}
.card-header-is_closed2 {
  background-color: rgba(58, 160, 201, 0.836);

  color: #fff;

  font-weight: bold;

  text-align: center;

  float: right;

  margin: 15px 15px 0 0;

  // border-radius: 50%;

  font-weight: bold;

  padding: 10px 10px;

  line-height: 20px;
}

h1 {
  font-size: 22px;

  font-weight: bold;
}

.card-body {
}

.card-body-header {
  line-height: 25px;

  margin: 10px 20px 0px 20px;
}

.card-body-description {
  opacity: 0;

  color: black;

  line-height: 25px;

  -webkit-transition: 0.2s ease-in-out; /*사파리&크롬*/

  -moz-transition: 0.2s ease-in-out; /*파이어폭스*/

  -ms-transition: 0.2s ease-in-out; /*익스플로러*/

  -o-transition: 0.2s ease-in-out; /*오페라*/

  transition: 0.2s ease-in-out;

  overflow: hidden;

  height: 180px;

  margin: 5px 20px;
}

.card:hover .card-body-description {
  opacity: 1;

  -webkit-transition: 0.5s ease-in-out;

  -moz-transition: 0.5s ease-in-out;

  -ms-transition: 0.5s ease-in-out;

  -o-transition: 0.5s ease-in-out;

  transition: 0.5s ease-in-out;

  overflow: scroll;
}

.card-body-hashtag {
  color: #2478ff;

  font-style: italic;
}

.card-body-footer {
  position: absolute;

  margin-top: 15px;

  margin-bottom: 6px;

  bottom: 0;

  width: 314px;

  font-size: 14px;

  color:black;

  padding: 0 15px;
}

.icon {
  display: inline-block;

  vertical-align: middle;

  margin-right: 2px;
}

.icon-view_count {
  width: 25px;

  height: 17px;

  // background: url("images/eye.jpg") no-repeat;
}

.icon-comments_count {
  margin-left: 5px;

  width: 25px;

  height: 17px;

  // background: url("images/comment.jpg") no-repeat;
}

.reg_date {
  float: right;
}
</style>