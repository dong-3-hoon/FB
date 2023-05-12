<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="getMovies">hkkhk</button>
    <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"></MovieCard>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard.vue"

export default {
  name: "MovieView",
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  components: {
    MovieCard,
  }
  
}
</script>

<style>

</style>