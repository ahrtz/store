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
          placeholder="검색어를 입력하세요"
          class="form-control"
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
    <div style="display : flex;">
    <scrapcard
      v-for="(scrap, index) in scraps"
      :key="index"
      :sid="scrap.summary"
    />
    </div>
    <!-- end cardvue -->
    <hr />

    <div
      class="row row-grid justify-content-between align-items-center mt-lg pg"
    >
      <div></div>
      <base-pagination
        :page-count="10"
        v-model="pagination.default"
      ></base-pagination>
      <div></div>
    </div>
  </div>
</template>

<script>
import Constant from "../Constant.js";
import http from "@/http-common.js";
import scrapcard from "./components/scrapcard";
export default {
  components: {
    scrapcard,
  },
  data() {
    return {
      pagination: {
        default: 1,
      },
      selectval: "",
    };
  },
  created() {
    // console.log('스크랩디스패치');
    this.$store.dispatch("getScraplist");
  },
  computed: {
    scraps() {
      // console.log('스크랩 컴퓨티드');
      // console.dir(this.$store.state.scrapstore.scraps);

      return this.$store.state.scrapstore.scraps;
    },
  },
  methods: {
    searchscrap() {
      //타이틀 검색
      if (this.selectval == "title") {
        // this.$store.dispatch(Constant.GET_SCRAPLIST);
      }
      //키워드 검색
      else {
        // this.$store.dispatch(Constant.GET_SCRAPLIST);
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