import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
import axios from 'axios'
Vue.use(Vuex);

const scrapstore = {
  state: {
      scraps: [],
      scrap: {}
  },
 
  actions: {
    //스크랩

    //아이디로 스크랩 리스트 가져오기
    [Constant.GET_SCRAPLIST]: (store,payload) => {
      
      http.get('/reports/scrap/list')
          .then(response => {
            console.log('덴');
            console.dir(response.data);
              store.commit(Constant.GET_SCRAPLIST, { scraps: response.data })
        })
          .catch(exp => alert('getScrapList처리에 실패하였습니다!!' + exp));
    },

    async [Constant.ADD_SCRAP] (store, payload) {
        await axios.post(`/api/reports/scrap/make/${payload.essayId}`, {
            headers: {'Content-Type': 'application/json'}
        }).then(response => {
            alert('스크랩 목록에 추가되었습니다')
        }).catch(e => {
            console.log(e.message)
            alert('스크랩 중 문제가 발생했습니다')
        })
    }


    

    
,

    // //게시글 삭제
    // [Constant.REMOVE_BOARD]: (store, payload) => {
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.delete('/api/board/delete/' + payload.bno,config)
    //         .then(() => {
    //             alert('삭제하였습니다.');
    //             store.dispatch(Constant.GET_BOARDLIST, {bstate : payload.bstate});

    //         })
    //         // .catch(exp => alert('삭제 처리에 실패하였습니다.' + exp));



    
  },

  mutations: {
    [Constant.GET_SCRAPLIST]: (state, payload) => {
        console.log('mutation' + payload.scraps);
        state.scraps = payload.scraps;
    },
    // [Constant.GET_BOARD]: (state, payload) => {
    //     state.board = payload.board;
    // },

  },

  modules: {
  }
};

export default scrapstore;
