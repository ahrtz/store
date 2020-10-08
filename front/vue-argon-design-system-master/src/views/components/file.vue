<template>
  <div class="example-drag bg">
    <div class="text-center p-5 upload">
      <ul v-if="files.length" style="list-style: none">
        <i class="fa fa-file-pdf-o fa-5x" aria-hidden="true"></i>
        <br />
        <br />
        <h4>pdf 파일을 올려주세요</h4>
        <!-- <li v-for="(file) in files" :key="file.id" style="font-size : 150%;"> -->
        <div style="font-size: 150%">
          <span>{{ files[files.length - 1].name }}</span>
          <!-- <span>{{files[files.length-1].size | formatSize}}</span> B -->
          <span v-if="files[files.length - 1].error">{{
            files[files.length - 1].error
          }}</span>
          <span v-else-if="files[files.length - 1].success">success</span>
          <span v-else-if="files[files.length - 1].active">active</span>
          <span v-else></span>
        </div>
        <!-- </li> -->
        <br />
        <br />
        <file-upload
          class="btn btn-primary"
          post-action="/upload/post"
          :multiple="true"
          :drop="true"
          :drop-directory="true"
          v-model="files"
          ref="upload"
        >
          <i class="fa fa-plus"></i>
          Change file
        </file-upload>
        <button
          class="btn btn-md btn-danger"
          @click="sendfile(files[files.length - 1])"
        >
          요약 실행
        </button>
      </ul>
      <ul v-else>
        <!-- <td colspan="7"> -->

        <i class="fa fa-file-pdf-o fa-5x" aria-hidden="true"></i>
        <br />
        <br />
        <h4>pdf 파일을 올려주세요</h4>

        <div class="text-center p-5">
          <file-upload
            class="btn btn-primary"
            post-action="/upload/post"
            :multiple="true"
            :drop="true"
            :drop-directory="true"
            v-model="files"
            ref="upload"
          >
            <i class="fa fa-plus"></i>
            Select file
          </file-upload>

          <!-- <label for="file" class="btn btn-lg btn-primary">
            <i class="fa fa-plus" aria-hidden="true"></i>
            Select File
          </label>-->
          <br />
          <br />
          <span>
            <h4>또는 파일을 여기로 끌어 놓으세요</h4>
          </span>
        </div>
        <!-- </td> -->
      </ul>

      <div v-show="$refs.upload && $refs.upload.dropActive" class="drop-active">
        <h3>Drop file to upload</h3>
      </div>

      <!-- <div class="example-btn">
        <file-upload
          class="btn btn-primary"
          post-action="/upload/post"
          :multiple="true"
          :drop="true"
          :drop-directory="true"
          v-model="files"
          ref="upload"
        >
          <i class="fa fa-plus"></i>
          Select files
      </file-upload>-->
      <!-- <button type="button" class="btn btn-success" v-if="!$refs.upload || !$refs.upload.active" @click.prevent="$refs.upload.active = true">
          <i class="fa fa-arrow-up" aria-hidden="true"></i>
          Start Upload
      </button>-->
      <!-- <button type="button" class="btn btn-danger"  v-else @click.prevent="$refs.upload.active = false">
          <i class="fa fa-stop" aria-hidden="true"></i>
          Stop Upload
      </button>-->
      <!-- </div> -->
    </div>

    <!-- <div class="pt-5">
      Source code: <a href="https://github.com/lian-yue/vue-upload-component/blob/master/docs/views/examples/Drag.vue">/docs/views/examples/Drag.vue</a>
    </div>-->
  </div>
</template>


<script>
import FileUpload from "vue-upload-component";
import Constant from "../../Constant";
import http from "../../http-common.js";

export default {
  components: {
    FileUpload,
  },

  data() {
    return {
      files: [],
      check: false,
    };
  },

  methods: {
    async sendfile(file) {
      //확장자 pdf 외 거르기
      var len = file.name.length;
      var type = file.name.substring(len - 3, len);
      // console.log(type)

      if (type != "pdf") {
        alert("pdf 형식의 논문만 요약 가능합니다.");
      } else {
        if (file.name.indexOf(" ") == -1) {
          this.$emit("update");
          await this.$store
            .dispatch(Constant.SEND_FILE, { file: file.file })
            .then(() => {
              this.$router.push("/nmdetail");
            });
        } else {
          alert("파일명에 공백을 제거해주세요!");
        }
      }
    },
  },
};
</script>

<style>
.bg {
  width: 60%;
  height: 30%;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 5%;
  margin-bottom: 5%;
  padding-top: 2%;
  background-color: white;
  border-style: dashed;
  border-width: 10px;
}
.example-drag label.btn {
  margin-bottom: 0;
  margin-right: 1rem;
}
.example-drag .drop-active {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
  z-index: 9999;
  opacity: 0.6;
  text-align: center;
  background: #000;
}
.example-drag .drop-active h3 {
  margin: -0.5em 0 0;
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  font-size: 40px;
  color: #fff;
  padding: 0;
}
</style>