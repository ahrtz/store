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
        <button
          type="button"
          class="btn btn-default"
          data-container="body"
          data-toggle="popover"
          data-placement="top"
          data-content="abstract 내용이 들어갈 자리입니다."
        >abstract 보기</button>
      </div>
    </div>
  </card>
</template>

<script>
export default {};
</script>

<style>
</style>