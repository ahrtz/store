<template>
  <card>
    <!-- Card body -->
    <div class="row align-items-center col-12">
      <div class="col-4">
        <h4 class="mb-0">논문제목(발행연도)</h4>
        <badge type="primary" class="text-uppercase">키워드</badge>
        <badge type="success" class="text-uppercase">키워드</badge>
        <badge type="danger" class="text-uppercase">키워드</badge>
        <badge type="warning" class="text-uppercase">키워드</badge>
        <badge type="info" class="text-uppercase">키워드</badge>
      </div>
      <div class="col-2">대분류 - 소분류</div>
      <div class="col-1">저자</div>
      <div class="col-1">발행기관</div>
      
      <div class="col-2">
        <base-button  @click="modals.modal1 = true">초록 보기</base-button>
        <modal :show.sync="modals.modal1">
          <h6 slot="header" class="modal-title" id="modal-title-default">논문 초록 미리보기</h6>

          <p>
            abstract 잘라 넣기
          </p>
          

          <!-- <template slot="footer">
            <base-button type="link" class="ml-auto" @click="modals.modal1 = false">Close</base-button>
          </template> -->
        </modal>
      </div>
      <div class="col-2">
        <button type="button" class="btn">상세보기</button>
      </div>
    </div>
  </card>
</template>

<script>
import Modal from "@/components/Modal.vue";

export default {
  components: {
    Modal
  },
  data() {
    return {
      modals: {
        modal1: false,
       
      }
    };
  }
};
</script>

<style>
</style>