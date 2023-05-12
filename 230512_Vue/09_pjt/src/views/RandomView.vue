<template>
  <div class="home">
    <button @click="randomMovie">Pick</button>
    <movie-card :movie="movie"></movie-card>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from "@/components/MovieCard.vue";
import _ from "lodash";
// @ is an alias to /src
export default {
  name: "RandomView",
  data() {
    return {
      movie: null,
      weather: null,
      weatherMovie: [],
    };
  },
  methods: {
    getWeather(){
      axios({
        url : `https://api.openweathermap.org/data/2.5/onecall?lat=35.15&lon=126.85&exclude=hourly,daily&appid=9cbe77b703b0c172de8e80ade55ae511`,
        method : 'get',
      })
      .then((res)=>{
        console.log(res.data.current.weather[0].main)
        this.weather = res.data.current.weather[0].main
        this.randomMovie();
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    randomMovie() {
      this.weatherMovie = []
      const movies = this.$store.state.movies
      console.log(this.weather)
      console.log(this.$store.state.Genres.match[this.weather], '날씨체크')
      movies.forEach(movie => {
        // console.log(this.$store.state.Genres.match)
        if (this.$store.state.Genres.match[this.weather].includes(movie.genre_ids[0])) {
          this.weatherMovie.push(movie)
        }
      });
      console.log(this.weatherMovie)
      
      this.movie = _.sample(this.weatherMovie);
    },

  },
  computed: {},
  created() {
    this.getWeather();
  },
  components: {
    MovieCard,
  },
};
</script>
