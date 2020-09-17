import Vue from 'vue';
import Vuex from 'vuex';
// import Constant from '../Constant.js';
// import http from '../http-common.js';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

// 작성한 모듈을 가져옵니다.
import boardstore from '@/store/modules/boardstore.js';
import userstore from '@/store/modules/userstore.js';
import filestore from '@/store/modules/filestore.js';
import nmstore from '@/store/modules/nmstore.js';

const store = new Vuex.Store({
  modules: {
    // 키: 값 형태로 저장됩니다.
    // 이런형태로 저장!
    boardstore,
    userstore,
    filestore,
    nmstore
  },
  // plugins: [
  //   createPersistedState({
  //     paths: ['mapstore', 'issuestore'],
  //   })
  // ]
});

export default store;
