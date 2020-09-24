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

    // //bno으로 게시글 하나 가져오기
    // [Constant.GET_BOARD]: (store, payload) => {
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.get('/api/board/no/' + payload.bno,config)
    //         .then(response => {
    //             // console.log(response.data);
    //             store.commit(Constant.GET_BOARD, { board: response.data })})
    //         // .catch(exp => alert('getTodo처리에 실패하였습니다.' + exp));

    // },
    //게시글 추가
    // [Constant.ADD_BOARD]: (store, payload) => {
    //     // console.log(payload.bstate);
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.post('/api/board/', {
    //             // bno : payload.bno,
    //             bwriter : payload.bwriter,
    //             btitle : payload.btitle,
    //             bcontent : payload.bcontent,
    //             bview : payload.bview,
    //             bfile : payload.bfile,
    //             bstate : payload.bstate,
    //             makeDay : payload.makeDay,
    //             // changeDay : payload.changeDay,
    //             makeId : payload.makeId,
    //             // changeId : payload.changeId
    //         },config)
    //         .then((res) => {
    //             store.dispatch(Constant.GET_BOARDLIST, {bstate : payload.bstate});
    //             store.dispatch('upFileForBoard',{bno:res.data})
    //         })
    //         // .catch(exp => {
    //         //     alert('추가 처리에 실패하였습니다.' + exp);
    //         // })
    // },
    //게시글 수정
    // [Constant.MODIFY_BOARD]: (store, payload) => {
    //     // console.log(payload);
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.put('/api/board/change/' + payload.board.bno, {
    //             bno:payload.board.bno,
    //             bwriter: payload.board.bwriter,
    //             btitle: payload.board.btitle,
    //             bcontent: payload.board.bcontent,
    //             bview : payload.board.bview,
    //             bfile : payload.board.bfile,
    //             bstate : payload.board.bstate,
    //             makeDay : payload.board.makeDay,
    //             changeDay : new Date(),
    //             makeId : payload.board.makeId,
    //             changeId : payload.board.changeId //세션 id
    //         },config)
    //         .then(() => {
    //             // console.log('수정하였습니다.'+ response.data);
    //             store.dispatch(Constant.GET_BOARD, {bno : payload.board.bno});
    //         })
    //         // .catch(exp => alert('수정 처리에 실패하였습니다.' + exp));
    // },

    
    // [Constant.READ_BOARD]: (store, payload) => {
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.put('/api/board/read/' + payload.bno, config)
    //         .then(() => {
    //             //store.dispatch(Constant.READ_BOARD, {bno : payload.bno});
    //         })
    //         // .catch(exp => alert('읽음 처리에 실패하였습니다.' + exp));
    // },

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

    // },
    // //제목으로 찾기
    // [Constant.SEARCH_BOARD_TITLE]: (store,payload) => {
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.get('/api/board/typesearch/btitle='+ payload.btitle + '&bstate=' + payload.bstate,config)
    //         .then(response => {
    //             store.commit(Constant.GET_BOARDLIST, { boards: response.data })
    //       })
    //         // .catch(exp => alert('search by title 처리에 실패하였습니다.' + exp));
    //   },
    // //작성자로 찾기
    // [Constant.SEARCH_BOARD_WRITER]: (store,payload) => {
    //     const config = {
    //         headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
    //     }
    //     http.get('/api/board/typesearch/writer='+ payload.bwriter + '&bstate=' + payload.bstate,config)
    //         .then(response => {
    //             store.commit(Constant.GET_BOARDLIST, { boards: response.data })
    //       })
    //         // .catch(exp => alert('search by title 처리에 실패하였습니다.' + exp));
    //   },


    
  },

  mutations: {
    [Constant.GET_SCRAPLIST]: (state, payload) => {
        // console.log('mutation' + payload.boards);
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
