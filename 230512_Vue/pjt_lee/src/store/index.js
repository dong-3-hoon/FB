import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Genres from './modules/genres.js'

Vue.use(Vuex)
const API_KEY = 'd838f386c11255ef5f578f676243694f'
const API_URL = 'https://api.themoviedb.org/3/movie/top_rated'
export default new Vuex.Store({
  state: {
    articleList : [],
    movieList : [],
    watchMovieList:[],
    
  },
  getters: {
  },
  mutations: {
    ADD_WATCH_MOVIE(state, watchMovie){
      state.watchMovieList.push(watchMovie)

    },
    GET_ARTICLES(state, articleList){
      state.articleList = articleList
    },
    GET_MOVIE_LIST(state, data){
      state.movieList = data.results
    }
  },
  actions: {
    
    getMovieList(context){
      axios.get(API_URL, {
        params : {
          api_key : API_KEY,
          language : 'ko-KR'
        }
      
      })
      .then((res)=>{
        console.log(res.data)
        context.commit('GET_MOVIE_LIST', res.data)
      })
    },
    addWatchMovie(context, getMovie){
      const watchMovie = {title : getMovie, is_completed:false}
      context.commit('ADD_WATCH_MOVIE', watchMovie)
    },
    watched(context, movie){
      const newMovie = movie
      newMovie.is_completed = !newMovie.is_completed
      const newIdx  = context.state.watchMovieList.indexOf(newMovie)
      context.state.watchMovieList[newIdx] = newMovie
      console.log(context.state.watchMovieList[newIdx].is_completed)
    }
  },
  modules: {
    Genres
  }
})
