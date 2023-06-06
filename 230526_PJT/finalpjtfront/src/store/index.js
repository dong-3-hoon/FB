import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import app from '../App.vue'
Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
plugins:[
  createPersistedState({})
],
  state: {
    token : '',
    profileImage : '',
    comments : [],
    nickname : '',
    userInfo : {},
    username : '',
    user_id : '',
    followings:[],
    followers:[],
    recommendList:[],
    weather : '',


  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
    },

    LOG_OUT(state){
      state.profileImage = ''
      state.token = ''
      sessionStorage.setItem('token', '')
    },
    GET_ARTICLES(state, articles) {
      const reversedArticles = articles.reverse()
      state.articles = reversedArticles

    },
    GET_USERINFO(state, userInfo){
      state.nickname = userInfo.nickname
      state.username = userInfo.username
      state.followings = userInfo.followings
      state.followers = userInfo.followers
      state.profileImage = userInfo.profile_image ? `http://localhost:8000${userInfo.profile_image}` : '' 
      
      
      state.user_id = userInfo.id
      console.log(state.user_id)
      console.log(state.userInfo, '유저 정보 받아오기')
    },
    UPDATE_NICKNAME(state, nickname){
      state.nickname = nickname
    },
    SAVE_RECOMMEND_LIST(state, recommendList){
      state.recommendList = recommendList
    },
    SAVE_WEATHER(state, weather){
      state.weather = weather
    }
  },
  actions: {
    //로그인 할 경우 로그인 유지를 위해 state에 저장
    saveToken(context, payload){
      const token = payload.access
      sessionStorage.setItem("token", token)
      context.commit('SAVE_TOKEN', token)
      context.dispatch("getProfile")
    },
    //다른 곳 갔다 올 경우 sessionStorage에 있는 거 빼와서 state에 저장
    getToken(context){
      const token = sessionStorage.getItem('token')
      // const parsedToken = JSON.parse(token)
      context.commit('SAVE_TOKEN', token)
    },
    getUserinfo(context){
      axios({
        url: "http://localhost:8000/accounts/update/",
        method: "get",
        headers: {
          Authorization: `Bearer ${context.state.token}`,
        },
      })
        .then((res) => {

          //프로필 이미지에 가져온 이미지 저장하기
          const userInfo = res.data
          console.log(userInfo)

          context.commit('GET_USERINFO', userInfo)
          
        })
        .catch((err) => {
          console.log(err);
        });
    },
    logout(context){
      context.commit('LOG_OUT')
    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers:{
          Authorization: `Bearer ${ context.state.token }`
        }
      })
        .then((res) => {
        // console.log(res, context)
        console.log(res.data)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    updateNickname(context, nickname){
      axios({
        url : `http://localhost:8000/accounts/update/nickname/`,
        method : 'put',
        data : {
          nickname
        },
        headers :{
          Authorization: `Bearer ${context.state.token}`,

        }
      })
      .then(res =>{
        console.log(res)
      })
      .catch(err =>{
        console.log(err)
      })
      context.commit('UPDATE_NICKNAME', nickname)
    },
    updateUserInfo(context, userInfo){
      axios({
        url : 'http://localhost:8000/accounts/password/change/',
        method : 'post',
        data : {
          ...userInfo
        },
        headers : {
          Authorization : `Bearer ${context.state.token}`,
        }
      })
      .then(res =>{
        console.log(res)
      })
      .catch(err =>{
        console.log(err)
      })
    },
  saveRecommendList(context, recommendList){
    context.commit('SAVE_RECOMMEND_LIST', recommendList)
    console.log(recommendList)
  },
  saveWeather(context, weather){
    context.commit('SAVE_WEATHER', weather)
  }
    
  },
  getters : {
    getProfile(state){
      return state.profileImage
    },
    stateUserInfo(state){
      return state.userInfo
    }
  },
  modules: {
  }
})

