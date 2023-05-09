import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  // computed같은 애
  getters: {
    messageLength(state){
      return state.message.length
    },
    doubleLength(state, getters){
      return getters.messageLength*2
    }
  },
  // station 변경
  mutations: {
    CHANGE_MESSAGE(state, payload){
      // console.log(state)
      // console.log(message)
      state.message = payload
    }
  },
  // action 실행
  actions: {
    changeMessage(context, message){
      console.log(context)
      console.log(message)
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
