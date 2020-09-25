<template>
  <card>
    <!-- Card body -->
    <div class="row align-items-center col-12">
      <div class="col-4">
        <h4 class="mb-0">
          {{ nm.title_kor }}({{ String(nm.issue_year).slice(0, 4) }})
        </h4>
        <badge
          class="text-uppercase"
          v-for="(keyword, index) in keywords"
          :key="index"
          :type="colors[index % 5]"
          >{{ keyword }}</badge
        >
      </div>
      <div class="col-2">{{ nm.subject }}</div>
      <div class="col-2">{{ nm.main_author }} 외 {{ subcnt }}명</div>
      <div class="col-1">{{ nm.issuer_kor }}</div>

      <div class="col-1">
        <base-button @click="modals.modal1 = true">초록 보기</base-button>
        <modal :show.sync="modals.modal1">
          <h6 slot="header" class="modal-title" id="modal-title-default">
            논문 초록 미리보기
          </h6>

          <p>{{ nm.abstract }}</p>

          <!-- <template slot="footer">
            <base-button type="link" class="ml-auto" @click="modals.modal1 = false">Close</base-button>
          </template>-->
        </modal>
      </div>
      <div class="col-1">
        <button type="button" class="btn" @click="onClickRedirect()">
          참고사이트
        </button>
      </div>
      <div class="col-1">
        <button type="button" class="btn btn-primary" @click="movedetail()">
          상세보기
        </button>
      </div>
    </div>
  </card>
</template>

<script>
import Modal from "@/components/Modal.vue";

export default {
  components: {
    Modal,
  },
  created() {
    this.keywords = this.nm.keyword_kor.split(", ");
    this.subcnt = this.nm.sub_author.split(",").length;
  },
  data() {
    return {
      modals: {
        modal1: false,
      },
      keywords: [],
      subcnt: 0,
      colors: ["primary", "success", "danger", "warning", "info"],
    };
  },
  props: {
    nm: {
      type: Object,
      required: true,
    },
  },
  methods: {
    onClickRedirect() {
      window.open(this.nm.direct_urls);
    },
    movedetail(){
      var url = '/showdetail/' + this.nm.id;
      this.$router.push(url);
    }
  },
};
</script>

<style>
</style>