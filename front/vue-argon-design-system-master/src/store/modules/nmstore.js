import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
Vue.use(Vuex);

const nmstore = {
  state: {
    nms: [],
    nm: {},
    count : 0
  },

  actions: {
    //게시판

    //논문 리스트 가져오기 (전체 혹은 필터링 된 논문리스트가 거쳐가는 액션)
    [Constant.GET_NMLIST]: (store, payload) => {
      // console.log('전체리스트 가져오기 도착');
      http.get('/reports/list/?page='+payload.pg)
        .then(response => {
          // console.log('전체리스트 가져오기 스토어 성공');

          // console.log('타입 '+ typeof(response.data));
          // console.dir(response.data);
          // console.dir(response.data.results);
          store.commit(Constant.GET_NMLIST, {
            
            nms: response.data
          })
        })
        .catch(exp => alert('getNmList처리에 실패하였습니다!!' + exp));
    },
    //???으로 논문 하나 가져오기
    [Constant.GET_NM]: (store, payload) => {

      http.get('/reports/detail/' + payload.bno + '/')
        .then(response => {
          // console.log(response.data);
          store.commit(Constant.GET_NM, {
            nm: response.data
          })
        })
        .catch(exp => alert('getNm처리에 실패하였습니다.' + exp));

    },

    //제목으로 논문리스트 가져오기
    [Constant.SEARCH_TITLE_NMLIST]: (store, payload) => {

      http.get('/reports/searcht/' + payload.title + '/')
        .then(response => {
          // console.dir(response);
          store.commit(Constant.GET_NMLIST, {
            nms: response.data
          })
        })
        .catch(exp => alert('searchNmList 처리에 실패하였습니다.' + exp));
    },

    //키워드로 논문리스트 가져오기
    [Constant.SEARCH_KEYWORD_NMLIST]: (store, payload) => {

      http.get('/reports/searchk/' + payload.keyword + '/')
        .then(response => {
          store.commit(Constant.GET_NMLIST, {
            nms: response.data
          })
        })
        .catch(exp => alert('searchNmList 처리에 실패하였습니다.' + exp));
    },


  },

  mutations: {
    [Constant.GET_NMLIST]: (state, payload) => {
      console.log('mutation' + payload.nms);
      // console.log('뮤테');
      state.nms = payload.nms.results;
      state.count = payload.nms.count;
    },
    [Constant.GET_NM]: (state, payload) => {
      state.nm = payload.nm;
    },

  },

  modules: {}
};

export default nmstore;