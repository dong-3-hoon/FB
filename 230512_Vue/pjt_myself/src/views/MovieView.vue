<template>
  <div class="about">
    <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieView',
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  },
  computed:{
    movies(){
      return this.$store.state.movies
    }
  },
  components: {
    MovieCard
  }
}
</script>
