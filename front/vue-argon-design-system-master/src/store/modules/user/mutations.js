import * as types from './mutation_type'
import { _ } from 'core-js'

export default {
    [types.TOKEN] (state, token) {
        state.token = token
    },
    [types.ERROR_STATE] (state, errorState) {
        state.errorState = errorState
    },
    [types.IS_AUTH] (state, isAuth) {
        state.isAuth = isAuth
    },
    [types.JOIN_SUCCESS] (state, joinSuccess) {
        state.joinSuccess = joinSuccess
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
}