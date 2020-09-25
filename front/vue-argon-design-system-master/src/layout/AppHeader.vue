<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent type="" effect="light" expand>
            <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                <img src="@/assets/images/logo.png" alt="logo" style="width : 100px; height : 100px;">
            </router-link>

            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/">
                        <img src="img/brand/blue.png">
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>

            <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
                <router-link  class="nav-link" to="/search">논문 검색</router-link>
            </ul>
            <ul class="navbar-nav align-items-lg-center ml-lg-auto">
                <base-dropdown tag="li" class="nav-item" menu-classes="dropdown-menu-xl"  v-if="this.$store.getters.getIsAuth == false"> 
                    <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
                        <i class="ni ni-circle-08"></i>
                    </a>
                    <a class="dropdown-item" @click="modals.modal0 = true">로그인</a>
                    <a class="dropdown-item" @click="modals.modal1 = true">회원가입</a>
                </base-dropdown>
                <base-dropdown tag="li" class="nav-item" menu-classes="dropdown-menu-xl"  v-else> 
                    <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
                        <i class="ni ni-circle-08"></i>
                    </a>
                    <a class="dropdown-item" @click="userLogout()">로그아웃</a>
                    <a class="dropdown-item" @click="modals.modal2 = true">선호주제</a>
                </base-dropdown>

                <div tag="li" class="nav-item">
                    <router-link slot="title" to="/scrap" class="nav-link" role="button">마이스크랩</router-link>
                </div>
            </ul>
        </base-nav>
        <modal :show.sync="modals.modal0">
            <my-login v-on:closemodal="modals.modal0 = false">
            </my-login>
        </modal>
        <modal :show.sync="modals.modal1">
            <my-sign-up v-on:closemodal="modals.modal1 = false; modals.modal2 = true">
            </my-sign-up>
        </modal>
        <modal :show.sync="modals.modal2">
            <my-priority v-on:closemodal="modals.modal2 = false">
            </my-priority>
        </modal>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";
import Modal from "@/components/Modal";
import MyLogin from '@/views/MyLogin';
import MySignUp from '@/views/MySignUp';
import MyPriority from '@/views/MyPriority'

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown,
    Modal,
    MyLogin,
    MySignUp,
    MyPriority
  },
  data: () => ({
      modals: {
          modal0: false,
          modal1: false,
          modal2: false
      },
  }),
  methods: {
      userLogout() {
          this.$axios.post('/api/rest-auth/logout/').then(response => {
              this.$store.commit('IS_AUTH', false)
              this.$router.push('/').catch(()=>{})
          }).catch(e => {
              console.log(e.message)
          })
      }
  }
};
</script>
<style>
</style>
