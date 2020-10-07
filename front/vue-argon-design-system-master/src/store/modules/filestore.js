import Vuex from 'vuex';
import Vue from 'vue';

import Constant from '../../Constant.js';
import http from '../../http-common.js';
import axios from "axios";

Vue.use(Vuex);

const filestore = {
    state: {
        file: {},
        result: [],
        filename: '',
        recommend: [],
        recommend_search: [],
        image: []
    },

    getters: {
        getResult: state => state.result
    },

    actions: {


        //파일 전송
        [Constant.SEND_FILE]: async (store, payload) => {
            let formData = new FormData()
            store.commit(Constant.GET_FILENAME, {filename: payload.file.name})
            formData.append('datafile', payload.file)

            // console.dir(payload.file.data + ' 왔습니다 여기까지')
            await axios.post('/api/reports/addreport/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then((response) => {
                    store.commit(Constant.GET_RESULT, { result: response.data })

                    alert('파일 전송 성공!!');
                })
                .catch(exp => {
                    console.log(exp.data)
                    alert('파일 전송에 실패하였습니다.' + exp);
                })
        },

        [Constant.GET_RECOMMEND]: async (store, payload) => {
            await axios.get(`/api/reports/recommend/${payload.title}/${store.state.filename}/`, 
            {
                headers: {'Content-Type': 'javascript/json'}
            }).then(response => {
                store.commit(Constant.GET_RECOMMEND, {recommend: response.data})
            })
        },

        [Constant.GET_RECOMMEND_SEARCH]: async (store, payload) => {
            await axios.get(`/api/reports/recommend_search/${payload.title}/`, 
            {
                headers: {'Content-Type': 'javascript/json'}
            }).then(response => {
                store.commit(Constant.GET_RECOMMEND_SEARCH, {recommend_search: response.data})
            })
        },

        [Constant.GET_IMAGE]: async (store, payload) => {
            await axios.get(`/api/reports/images/${store.state.filename}/`, {
                headers: {'Content-Type': 'javascript/json'}
            }).then(response => {
                store.commit(Constant.GET_IMAGE, {image: response.data})
            })
        }
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
        [Constant.GET_FILENAME]: (state, payload) => {
            state.filename = payload.filename
        },
        [Constant.GET_RECOMMEND]: (state, payload) => {
            state.recommend = payload.recommend
        },
        [Constant.GET_RECOMMEND_SEARCH]: (state, payload) => {
            state.recommend_search = payload.recommend_search
        },
        [Constant.GET_IMAGE]: (state, payload) => {
            state.image = payload.image
        }
    },

    modules: {}
};

export default filestore;