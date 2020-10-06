<template>
  <div class="container2">
    <div class="col-12" style="display: flex">
      <div class="col-2">
        <!-- <select
          class="form-control"
          data-toggle="select"
          data-minimum-results-for-search="Infinity"
        >
          <option>5개씩 보기</option>
          <option>10개씩 보기</option>
          <option>20개씩 보기</option>
        </select> -->
      </div>

      <div class="col-3"></div>

      <div class="col-2">
        <select
          class="form-control"
          data-toggle="select"
          data-minimum-results-for-search="Infinity"
          v-model="selectval"
        >
          <option value="title">제목으로 검색</option>
          <option value="keyword">키워드로 검색</option>
        </select>
      </div>
      <div class="col-4">
        <input
          type="text"
          placeholder="대소문자를 구분하여 검색어를 입력해주세요"
          class="form-control"
          v-model="sv"
        />
      </div>

      <div class="col-1">
        <button class="btn btn-primary col-12" @click="searchscrap">
          검색
        </button>
      </div>
    </div>
    <hr />

    <!-- cardvue list -->
    <div v-if="scraps.length > 0">
      <scrapcard
        v-for="(scrap, index) in scraps"
        :key="index"
        :sid="scrap.summary"
        :id="scrap.id"
      />
    </div>
    <div v-else>
      <nothing />
    </div>
    <!-- end cardvue -->
    <hr />

    <div
      class="row row-grid justify-content-between align-items-center mt-lg pg"
    >
      <div></div>
      <base-pagination :page-count="pagecnt" v-model="page"></base-pagination>
      <div></div>
    </div>
  </div>
</template>

<script>
import Constant from "../Constant.js";
import http from "@/http-common.js";
import scrapcard from "./components/scrapcard";
import nothing from "./components/nothing";
export default {
  components: {
    scrapcard,
    nothing,
  },
  data() {
    return {
      page: 1,
      // pagecnt: this.$store.state.scrapstore.pagecnt,
      selectval: "",
      sv: "", //서치 밸류
    };
  },
  // watch: {
  //   page() {
  //     this.$store.state.scrapstore.scraps = this.$store.state.scrapstore.scraps.slice(
  //       10 * (this.page - 1),
  //       10 * (this.page - 1) + 9
  //     );
  //   },
  // },
  created() {
    // console.log('스크랩디스패치');
    this.$store.dispatch("getScraplist");
  },
  computed: {
    pagecnt(){
      return this.$store.state.scrapstore.pagecnt;
    },
    scraps() {
      // console.log('스크랩 컴퓨티드');
      // console.dir(this.$store.state.scrapstore.scraps);

      return this.$store.state.scrapstore.scraps.slice(
        10 * (this.page - 1),
        10 * (this.page - 1) + 9
      );;
    },
  },
  methods: {
    async searchscrap() {
      await this.$store.dispatch("getScraplist");

      //타이틀 검색
      if (this.selectval == "title") {
        // console.log(this.sv)
        if (this.sv == "") {
          this.$store.dispatch("getScraplist");
        } else {
          var temp = [];
          for (let i = 0; i < this.scraps.length; i++) {
            if (this.scraps[i].summary.title_kor.includes(this.sv))
              temp.push(this.scraps[i]);
          }
          this.$store.state.scrapstore.scraps = temp;
        }
      }
      //키워드 검색
      else {
        if (this.sv == "") {
          this.$store.dispatch("getScraplist");
        } else {
          var temp = [];
          for (let i = 0; i < this.scraps.length; i++) {
            var kws = this.scraps[i].summary.keyword_kor
              .replace(" · ", ", ")
              .split(", ");
            console.dir(kws.length);
            for (let j = 0; j < kws.length; j++) {
              if (kws[j].includes(this.sv)) {
                temp.push(this.scraps[i]);
                break;
              }
            }
          }
          this.$store.state.scrapstore.scraps = temp;
        }
      }
    },
  },
};
</script>

<style scoped>
.container2 {
  text-align: center;
  margin-top: 5%;
  margin-bottom: 5%;
  margin-left: 10%;
  margin-right: 10%;
}
</style>