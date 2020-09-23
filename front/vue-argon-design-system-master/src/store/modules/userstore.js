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
            console.log(response)
            if (response.data.status) {
                this.showAlert = true;
                this.errMsg = response.data.data.email + "로그인 되었습니다"
                store.commit('TOKEN', response.headers["jwt-auth-token"])
                store.commit('IS_AUTH', true)
            }
            else {
                store.commit('TOKEN', '')
                store.commit('IS_AUTH', false)
            }
        }).catch(e => {
            store.commit('TOKEN', '')
            store.commit('IS_AUTH', false)
            alert('로그인 정보가 올바르지 않습니다')
        })
        return store.getters.getIsAuth
    },

    async signUp (store, {username, password1, password2}) {
        await axios.post(`/api/rest-auth/signup/`,
        {
            username: username,
            password1: password1,
            password2: password2,
        }, {headers: {'Content-Type': 'application/json'}}
        ).then((response) => {
            console.log(response)
            if (response.data.status) {
                sessionStorage.setItem('jwt-auth-token', response.data.key)
                store.commit('TOKEN', response.data.key)
                store.commit('IS_AUTH', true)
                return true
            }
            else {
                store.commit('TOKEN', '')
                store.commit('IS_AUTH', false)
                return false
            }
        }).catch(e => {
          store.commit('TOKEN', '')
          store.commit('IS_AUTH', false)
          return false
          console.log(e.message)
        })
    },

    async checkLogin (store) {
        var result;
        if (sessionStorage.getItem('jwt-auth-token')) {
            store.commit('TOKEN', sessionStorage.getItem('jwt-auth-token'))
            store.commit('IS_AUTH', true)
            await axios.get(`/api/user/${store.getters.getToken}`, {
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(res => {
                result = res.data
            }).catch(e => {
                store.commit('logout')
                alert('토큰이 만료되었습니다. 다시 로그인해주세요')
                router.push('/');
            })
            return result;
        }
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
