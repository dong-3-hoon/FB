import Vue from 'vue'
import Vuex from 'vuex'
import todo from '@/store/modules/todo.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {

  },
  getters: {

  },
  mutations: {
    SET_IMPORTANT: (state, id) => {
      state.todo.list.forEach(todo => {
        if (todo.id === id) {
          todo.isImportant = !todo.isImportant
        }
      })
    },
    SET_COMPLETED: (state, id) => {
      state.todo.list.forEach(todo => {
        if (todo.id === id) {
          todo.isCompleted = !todo.isCompleted
        }
      })
    },
  },
  actions: {
    important({ commit }, id) {
      commit('SET_IMPORTANT', id)
    },
    check({ commit }, id) {
      commit('SET_COMPLETED', id)
    }
  },
  modules: {
    todo
  }
})