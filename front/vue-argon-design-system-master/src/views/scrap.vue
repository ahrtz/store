<template>
  <div class="container2">
    <div class="col-12" style="display : flex;">
      <div class="col-2">
        <select
          class="form-control"
          data-toggle="select"
          data-minimum-results-for-search="Infinity"
        >
          <option>5개씩 보기</option>
          <option>10개씩 보기</option>
          <option>20개씩 보기</option>
        </select>
      </div>

      <div class="col-3"></div>

      <div class="col-2">
        <select
          class="form-control"
          data-toggle="select"
          data-minimum-results-for-search="Infinity"
        >
          <option>제목으로 검색</option>
          <option>키워드로 검색</option>
        </select>
      </div>
      <div class="col-4">
        <input type="text" placeholder="검색어를 입력하세요" class="form-control" />
      </div>

      <div class="col-1">
        <button class="btn btn-primary col-12">검색</button>
      </div>
    </div>
    <hr />

    <!-- cardvue list -->
        <scrapcard />
    <!-- end cardvue -->
    <hr />

    <div class="row row-grid justify-content-between align-items-center mt-lg pg">
      <div></div>
      <base-pagination :page-count="10" v-model="pagination.default"></base-pagination>
      <div></div>
    </div>
  </div>
</template>

<script>
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
    };
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