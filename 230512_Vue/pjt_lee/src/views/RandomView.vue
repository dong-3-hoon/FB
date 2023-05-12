<template>
  <div
    class="container d-flex flex-column justify-content-center align-items-center"
  >
  <h1 v-if="movie">{{ weather }}에 어울리는 영화입니다.</h1>
    <div class="row justify-content-center">
      <div class="w-100 text-center">

        <a v-if="movie" class="pickBtn w-50 m-5 btn btn-outline-success" @click="changeMovie">Pick</a>
      </div>
      <MovieListItem :movie="movie" :list="false" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from "@/components/MovieListItem.vue";
import _ from "lodash";
export default {
    data(){
        return {
            movie : null,
            weather : null,
        }
    },
    methods : {
    changeMovie(){
        const movies = this.$store.state.movieList.filter(movie =>{
            return this.$store.state.Genres.match[this.weather].includes(movie.genre_ids[0])
        });
      this.movie = _.sample(movies);
    },
    getWeather(){
      axios({
        url : `https://api.openweathermap.org/data/2.5/onecall?lat=35.15&lon=126.85&exclude=hourly,daily&appid=9cbe77b703b0c172de8e80ade55ae511`,
        method : 'get',
      })
      .then((res)=>{
        console.log(res.data.current.weather[0].main)
        this.weather = res.data.current.weather[0].main
        this.changeMovie();
      })
      .catch((err)=>{
        console.log(err)
      })
    },
  },
  created(){
    this.getWeather();

  },
  

  components: {
    MovieListItem,
  },
};
</script>

<style>
.fade-enter{
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active{
  transition : opacity 1s ease-out;
}
.fade-leave-to{
  opacity: 0;
}
</style>
