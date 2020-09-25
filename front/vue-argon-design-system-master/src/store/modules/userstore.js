import Vuex from 'vuex';
import Vue from 'vue';
import router from '../../router';
import Constant from '../../Constant.js';
import http from '../../http-common.js';
import axios from 'axios'
Vue.use(Vuex);

const storage = window.sessionStorage;
const userstore = {
  state: {
    token: '',
    errorState: '',
    isAuth: false,
  },

  actions: {
    async login (store, {username, password}) {
        sessionStorage.setItem("jwt-auth-token", "")
        await axios.post(`/api/rest-auth/login/`,
        {
            username: username,
            password: password
        }, {headers: {'Content-Type': 'application/json'}}
        ).then((response) => {
            sessionStorage.setItem('jwt-auth-token', response.data.key)
            store.commit('IS_AUTH', true)
            return true
        }).catch(e => {
            sessionStorage.setItem('jwt-auth-token', '')
            store.commit('IS_AUTH', false)
            alert('로그인에 실패하였습니다')
            return false
        })
    },

    async signUp (store, {username, password1, password2}) {
        await axios.post(`/api/rest-auth/signup/`,
        {
            username: username,
            password1: password1,
            password2: password2,
        }, {headers: {'Content-Type': 'application/json'}}
        ).then((response) => {
            sessionStorage.setItem('jwt-auth-token', response.data.key)
            store.commit('IS_AUTH', true)
            return true
        }).catch(e => {
            sessionStorage.setItem('jwt-auth-token', '')
          store.commit('IS_AUTH', false)
          alert('회원가입에 실패하였습니다')
          return false
        })
    },

    async checkLogin (store) {
        if (sessionStorage.getItem('jwt-auth-token')) {
            store.commit('IS_AUTH', true)
        }
    },

    async setFavorites (store, {favorites, insmod}) {
        var res = false;
        if (insmod) {
            await axios.patch('/api/favorites/users/update/', {
                favorites: favorites
            }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                alert('선호 주제가 변경되었습니다')
                res = true
            }).catch(e => {
                console.log(e.message)
                alert('변경 중 문제가 발생했습니다')
                res = false
            })
        }
        else {
            await axios.post('/api/favorites/users/insert/', {
                favorites: favorites
            }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                alert('선호 주제가 등록되었습니다')
                res = true
            }).catch(e => {
                console.log(e.message)
                alert('등록 중 문제가 발생했습니다')
                res = false
            })
        }
        return res
    }
  },

  mutations: {
    [Constant.TOKEN] (state, token) {
        state.token = token
    },
    [Constant.ERROR_STATE] (state, errorState) {
        state.errorState = errorState
    },
    [Constant.IS_AUTH] (state, isAuth) {
        state.isAuth = isAuth
    },
    logout (state) {
        if (sessionStorage.getItem('jwt-auth-token')) {
            sessionStorage.removeItem('jwt-auth-token')
            this.commit('TOKEN', '')
            this.commit('IS_AUTH', false)
        }
    },
    isLogin (state) {
        return state.isAuth
    }
  },

  getters: {
    getToken: state => state.token,
    getErrorState: state => state.errorState,
    getIsAuth: state => state.isAuth,
  },

  modules: {}
};

export default userstore;
