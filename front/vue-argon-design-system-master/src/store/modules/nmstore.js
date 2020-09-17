import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
Vue.use(Vuex);

const nmstore = {
  state: {
      nms: [],
      nm: {}
  },
 
  actions: {
    //게시판

    //논문 리스트 가져오기 (전체 혹은 필터링 된 논문리스트가 거쳐가는 액션)
    [Constant.GET_NMLIST]: (store,payload) => {
      
      http.get('/api/board/statesearching/')
          .then(response => {
              store.commit(Constant.GET_NMLIST, { nms: response.data })
        })
          .catch(exp => alert('getNmList처리에 실패하였습니다!!' + exp));
    },
    //???으로 논문 하나 가져오기
    [Constant.GET_NM]: (store, payload) => {
        
        http.get('/api/board/no/' + payload.bno)
            .then(response => {
                // console.log(response.data);
                store.commit(Constant.GET_NM, { nm: response.data })})
            .catch(exp => alert('getNm처리에 실패하였습니다.' + exp));

    },
    
    //필터링 조건으로 논문리스트 가져오기
    [Constant.SEARCH_NMLIST]: (store,payload) => {
        
        http.get('/api/board/typesearch/btitle='+ payload.btitle + '&bstate=' + payload.bstate)
            .then(response => {
                store.commit(Constant.GET_NMLIST, { nms: response.data })
          })
            .catch(exp => alert('searchNmList 처리에 실패하였습니다.' + exp));
      },
    
    
  },

  mutations: {
    [Constant.GET_NMLIST]: (state, payload) => {
        // console.log('mutation' + payload.boards);
        state.nms = payload.nms;
    },
    [Constant.GET_NM]: (state, payload) => {
        state.nm = payload.nm;
    },
  
  },

  modules: {
  }
};

export default nmstore;
