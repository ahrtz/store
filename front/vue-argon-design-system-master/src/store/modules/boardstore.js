import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
Vue.use(Vuex);

const boardstore = {
  state: {
      boards: [],
      board: {}
  },
 
  actions: {
    //게시판

    //bstate에 맞는 리스트 가져오기
    [Constant.GET_BOARDLIST]: (store,payload) => {
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
      http.get('/api/board/statesearching/'+ payload.bstate,config)
          .then(response => {
              store.commit(Constant.GET_BOARDLIST, { boards: response.data })
        })
        //   .catch(exp => alert('getBoardList처리에 실패하였습니다!!' + exp));
    },
    //bno으로 게시글 하나 가져오기
    [Constant.GET_BOARD]: (store, payload) => {
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.get('/api/board/no/' + payload.bno,config)
            .then(response => {
                // console.log(response.data);
                store.commit(Constant.GET_BOARD, { board: response.data })})
            // .catch(exp => alert('getTodo처리에 실패하였습니다.' + exp));

    },
    //게시글 추가
    [Constant.ADD_BOARD]: (store, payload) => {
        // console.log(payload.bstate);
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.post('/api/board/', {
                // bno : payload.bno,
                bwriter : payload.bwriter,
                btitle : payload.btitle,
                bcontent : payload.bcontent,
                bview : payload.bview,
                bfile : payload.bfile,
                bstate : payload.bstate,
                makeDay : payload.makeDay,
                // changeDay : payload.changeDay,
                makeId : payload.makeId,
                // changeId : payload.changeId
            },config)
            .then((res) => {
                store.dispatch(Constant.GET_BOARDLIST, {bstate : payload.bstate});
                store.dispatch('upFileForBoard',{bno:res.data})
            })
            // .catch(exp => {
            //     alert('추가 처리에 실패하였습니다.' + exp);
            // })
    },
    //게시글 수정
    [Constant.MODIFY_BOARD]: (store, payload) => {
        // console.log(payload);
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.put('/api/board/change/' + payload.board.bno, {
                bno:payload.board.bno,
                bwriter: payload.board.bwriter,
                btitle: payload.board.btitle,
                bcontent: payload.board.bcontent,
                bview : payload.board.bview,
                bfile : payload.board.bfile,
                bstate : payload.board.bstate,
                makeDay : payload.board.makeDay,
                changeDay : new Date(),
                makeId : payload.board.makeId,
                changeId : payload.board.changeId //세션 id
            },config)
            .then(() => {
                // console.log('수정하였습니다.'+ response.data);
                store.dispatch(Constant.GET_BOARD, {bno : payload.board.bno});
            })
            // .catch(exp => alert('수정 처리에 실패하였습니다.' + exp));
    },

    
    [Constant.READ_BOARD]: (store, payload) => {
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.put('/api/board/read/' + payload.bno, config)
            .then(() => {
                //store.dispatch(Constant.READ_BOARD, {bno : payload.bno});
            })
            // .catch(exp => alert('읽음 처리에 실패하였습니다.' + exp));
    },

    //게시글 삭제
    [Constant.REMOVE_BOARD]: (store, payload) => {
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.delete('/api/board/delete/' + payload.bno,config)
            .then(() => {
                alert('삭제하였습니다.');
                store.dispatch(Constant.GET_BOARDLIST, {bstate : payload.bstate});

            })
            // .catch(exp => alert('삭제 처리에 실패하였습니다.' + exp));

    },
    //제목으로 찾기
    [Constant.SEARCH_BOARD_TITLE]: (store,payload) => {
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.get('/api/board/typesearch/btitle='+ payload.btitle + '&bstate=' + payload.bstate,config)
            .then(response => {
                store.commit(Constant.GET_BOARDLIST, { boards: response.data })
          })
            // .catch(exp => alert('search by title 처리에 실패하였습니다.' + exp));
      },
    //작성자로 찾기
    [Constant.SEARCH_BOARD_WRITER]: (store,payload) => {
        const config = {
            headers: {"jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")}
        }
        http.get('/api/board/typesearch/writer='+ payload.bwriter + '&bstate=' + payload.bstate,config)
            .then(response => {
                store.commit(Constant.GET_BOARDLIST, { boards: response.data })
          })
            // .catch(exp => alert('search by title 처리에 실패하였습니다.' + exp));
      },





    // [Constant.COMPLETE_TODO]: (store, payload) => {
    //     http.put('/api/qna/' + payload.qna_no)
    //         .then(() => {
    //             console.log('완료 처리하였습니다.');
    //             store.dispatch(Constant.GET_TODOLIST);
    //         })
    //         .catch(exp => alert('완료 처리에 실패하였습니다.' + exp));
    // },
    
  },

  mutations: {
    [Constant.GET_BOARDLIST]: (state, payload) => {
        // console.log('mutation' + payload.boards);
        state.boards = payload.boards;
    },
    [Constant.GET_BOARD]: (state, payload) => {
        state.board = payload.board;
    },
    // [Constant.CLEAR_TODO]: (state, payload) => {
    //     state.board = payload.todo;
    //     state.boards = payload.todoItems;
    // }
  },

  modules: {
  }
};

export default boardstore;
