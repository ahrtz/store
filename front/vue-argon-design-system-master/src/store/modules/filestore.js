import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
import axios from "axios";

Vue.use(Vuex);

const filestore = {
    state: {
        file: {},
        result: {}
    },

    actions: {


        //파일 전송
        [Constant.SEND_FILE]: (store, payload) => {
            let formData = new FormData()
            formData.append('datafile', payload.file)

            // console.dir(payload.file.data + ' 왔습니다 여기까지')
            axios.post('http://127.0.0.1:8080/reports/addreport/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(() => {
                    store.commit(Constant.GET_RESULT, { result: response.data })

                    alert('파일 전송 성공!!');
                })
                .catch(exp => {
                    console.log(exp.data)
                    alert('파일 전송에 실패하였습니다.' + exp);
                })
        },


    },

    mutations: {
        [Constant.GET_RESULT]: (state, payload) => {
            state.result = payload.result;
        },
        // [Constant.GET_BOARD]: (state, payload) => {
        //     state.board = payload.board;
        // },
        // [Constant.CLEAR_TODO]: (state, payload) => {
        //     state.board = payload.todo;
        //     state.boards = payload.todoItems;
        // }
    },

    modules: {}
};

export default filestore;