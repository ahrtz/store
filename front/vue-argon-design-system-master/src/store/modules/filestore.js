import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
Vue.use(Vuex);

const filestore = {
    state: {
        boards: [],
        board: {}
    },

    actions: {


        //파일 전송
        [Constant.SEND_FILE]: (store, payload) => {

            http.post('/reports/addreport/', {
                    file: payload.file

                })
                .then(() => {
                    // store.dispatch(Constant.GET_BOARDLIST, {
                    //     bstate: payload.bstate
                    // });
                    // store.dispatch('upFileForBoard', {
                    //     bno: res.data
                    // })
                })
                .catch(exp => {
                    alert('파일 전송에 실패하였습니다.' + exp);
                })
        },


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

    modules: {}
};

export default filestore;