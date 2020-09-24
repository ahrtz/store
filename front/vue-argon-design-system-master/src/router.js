import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Components from "./views/Components.vue";
import Landing from "./views/Landing.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Profile from "./views/Profile.vue";
import main from "./views/main.vue";


//커스터마이징

//논문요약결과페이지
import nmdetail from "./views/nmdetail.vue";
//논문검색상세페이지
import showdetail from "./views/showdetail.vue";
//검색페이지
import search from "./views/search.vue";

//argon 컴포넌트페이지
import guide from "./views/guide.vue";

// 스크랩 페이지
import scrap from "./views/scrap.vue";


Vue.use(Router);

export default new Router({
  linkExactActiveClass: "active",
  routes: [{
      path: "/",
      name: "main",
      components: {
        header: AppHeader,
        default: main,
        footer: AppFooter
      }
    },
    {
      path: "/landing",
      name: "landing",
      components: {
        header: AppHeader,
        default: Landing,
        footer: AppFooter
      }
    },
    {
      path: "/login",
      name: "login",
      components: {
        header: AppHeader,
        default: Login,
        footer: AppFooter
      }
    },
    {
      path: "/register",
      name: "register",
      components: {
        header: AppHeader,
        default: Register,
        footer: AppFooter
      }
    },
    {
      path: "/profile",
      name: "profile",
      components: {
        header: AppHeader,
        default: Profile,
        footer: AppFooter
      }
    },

    ///////////////////// 여기서부터 커스터마이징

    //논문상세페이지
    {
      path: "/showdetail/:id",
      name: "showdetail",
      components: {
        header: AppHeader,
        default: showdetail,
        footer: AppFooter
      }
    },
    //논문요약결과
    {
      path: "/nmdetail",
      name: "nmdetail",
      components: {
        header: AppHeader,
        default: nmdetail,
        footer: AppFooter
      }
    },
    //가이드 페이지
    {
      path: "/guide",
      name: "guide",
      components: {
        header: AppHeader,
        default: guide,
        footer: AppFooter
      }
    },
    //검색 페이지
    {
      path: "/search",
      name: "search",
      components: {
        header: AppHeader,
        default: search,
        footer: AppFooter
      }
    },
    //스크랩
    {
      path: "/scrap",
      name: "scrap",
      components: {
        header: AppHeader,
        default: scrap,
        footer: AppFooter
      }
    },



  ],
  scrollBehavior: to => {
    if (to.hash) {
      return {
        selector: to.hash
      };
    } else {
      return {
        x: 0,
        y: 0
      };
    }
  }
});