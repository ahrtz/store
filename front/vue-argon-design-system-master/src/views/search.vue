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

      <!-- <div class="col-2">
      </div>-->
      <div class="col-3">
        <!-- <select
          class="form-control"
          data-toggle="select"
          data-minimum-results-for-search="Infinity"
        >
          <option>발행연도</option>
          <option>2020</option>
          <option>2019</option>
          <option>2018</option>
          <option>2017</option>
          <option>2016</option>
          <option>2015</option>
          <option>2014</option>
          <option>2013</option>
          <option>2012</option>
          <option>2011</option>
          <option>2010</option>
        </select>-->
      </div>

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
        <input type="text" placeholder="검색어를 입력하세요" class="form-control" v-model="inputval"/>
      </div>

      <div class="col-1">
        <button class="btn btn-primary col-12" @click="searchnms">검색</button>
      </div>
    </div>

    <!--  -->
    <div class="table tb">
      <div>
        <table class="table align-items-center" style="margin : 10px;">
          <thead class="thead-light">
            <tr>
              <th>논문명</th>
              <th>분류</th>
              <th>저자 발행기관</th>
              <th>초록</th>
              <th>상세보기</th>
            </tr>
          </thead>
          <tbody class="list">
            <tr>
              <td colspan="6">
                                  <!-- v-for="(nm,index) in nms.slice(this.perPage*(currentPage-1),perPage*(currentPage))" -->

                <nmcard
                  v-for="(nm,index) in nms.results"
                  :key="index"
                  :nm="nm"
                />
              </td>
              <!-- <th scope="row">
                <div class="media align-items-center">
                  <div class="media-body">
                    <span class="name mb-0 text-sm">Argon Design System</span>
                  </div>
                </div>
              </th>
              <td class="budget">$2500 USD</td>
              <td>
                <span class="status">pending</span>
              </td>
              <td>
                <div class="avatar-group">ddd</div>
              </td>
              <td>
                <span class="completion mr-2">60%</span>
              </td>
              <td class="text-right"></td>-->
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="row row-grid justify-content-between align-items-center mt-lg pg">
      <div></div>
      <base-pagination :page-count="10" v-model="pagination.default"></base-pagination>
      <div></div>
    </div>
  </div>
</template>

<script>
import nmcard from "@/views/components/nmcard";
import Constant from "@/Constant";
import http from "@/http-common.js";

export default {
  components: {
    nmcard,
  },
  data() {
    return {
      pagination: {
        default: 1,
      },
      selectval: "",
      inputval: "",
    };
  },
  created() {
    this.$store.dispatch(Constant.GET_NMLIST);
  },
  computed: {
    nms() {
      console.log('확인'+this.$store.state.nmstore.nms.next);
      return this.$store.state.nmstore.nms;
    },
  },
  methods: {
    searchnms() {
      //타이틀 검색
      if (this.selectval == "title") {
        this.$store.dispatch(Constant.SEARCH_TITLE_NMLIST,{title : this.inputval});
      }
      //키워드 검색
      else {
        this.$store.dispatch(Constant.SEARCH_KEYWORD_NMLIST,{keyword : this.inputval});
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

.tb {
  margin-top: 5%;
  margin-bottom: 5%;
}

.pg {
  text-align: center;
}

nmcard {
  width: 100%;
}
</style>