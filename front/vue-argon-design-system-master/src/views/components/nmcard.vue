<template>
  <card>
    <!-- Card body -->
    <div class="row align-items-center">
      <div class="col-auto">
        <h4 class="mb-0">논문제목</h4>
        <p class="text-sm text-muted mb-0">Working remoteley</p>
      </div>
      <div class="col-auto">발행연도</div>
      <div class="col-auto">
        <button type="button" class="btn btn-sm btn-primary">상세보기</button>
      </div>
      <div class="col-auto">
        <badge type="primary" class="text-uppercase">Primary</badge>
        <badge type="success" class="text-uppercase">Success</badge>
        <badge type="danger" class="text-uppercase">Danger</badge>
        <badge type="warning" class="text-uppercase">Warning</badge>
        <badge type="info" class="text-uppercase">Info</badge>
      </div>
      <div class="col-auto">
        <base-button block type="primary" class="mb-3" @click="modals.modal1 = true">Default</base-button>
        <modal :show.sync="modals.modal1">
          <h6 slot="header" class="modal-title" id="modal-title-default">논문 초록 미리보기</h6>

          <p>
            abstract 잘라 넣기
          </p>
          

          <template slot="footer">
            <base-button type="link" class="ml-auto" @click="modals.modal1 = false">Close</base-button>
          </template>
        </modal>
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