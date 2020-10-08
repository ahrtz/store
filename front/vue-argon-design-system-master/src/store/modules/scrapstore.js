import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
import axios from 'axios'
Vue.use(Vuex);

const scrapstore = {
  state: {
    scraps: [],
    scrap: {},
    pagecnt:0,
  },

  actions: {
    //스크랩

    //아이디로 스크랩 리스트 가져오기
    /* 
    [Constant.GET_SCRAPLIST]: async (store,payload) => {
      
      await http.get('/reports/scrap/list/')
          .then(response => {
            console.log('덴');
            console.dir(response.data);
              store.commit(Constant.GET_SCRAPLIST, { scraps: response.data })
        })
          .catch(exp => alert('getScrapList처리에 실패하였습니다!!' + exp));
    },
    */
    async [Constant.GET_SCRAPLIST](store, payload) {

      await axios.get('/api/reports/scrap/list/')
        .then(response => {
          // console.log('덴');
          // console.dir(response.data);
          store.commit(Constant.GET_SCRAPLIST, {
            scraps: response.data
          })
        })
        .catch(exp => alert('getScrapList처리에 실패하였습니다!!' + exp));
    },

    async [Constant.ADD_SCRAP](store, payload) {
      await axios.post(`/api/reports/scrap/make/${payload.essayId}/`, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => {
        alert('스크랩 목록에 추가되었습니다')
      }).catch(e => {
        console.log(e.message)
        alert('스크랩 중 문제가 발생했습니다')
      })
    },

    //스크랩삭제
    async [Constant.DELETE_SCRAP](store, payload) {
      console.log('여기');
      console.log(payload.id);
      await axios.post(`/api/reports/scrap/delete/${payload.id}/`,{
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        alert('해당 스크랩이 삭제되었습니다')
        store.dispatch(Constant.GET_SCRAPLIST);

      }).catch(e => {
        console.log(e.message)
        alert('스크랩 삭제 중 문제가 발생했습니다')
      })
    },






  },

  mutations: {
    [Constant.GET_SCRAPLIST]: (state, payload) => {
      // console.log('mutation' + payload.scraps);
      state.scraps = payload.scraps;
      state.pagecnt = payload.scraps.length/9+1;
    },

  },

  modules: {}
};

export default scrapstore;