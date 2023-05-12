<template>
  <div>
    <img v-if="movie" :src="imgURL" alt="">
    <p>{{movie.title}}</p>
    <p>{{movie.overview}}</p>
  </div>
</template>

<script>
export default {
    name: "MovieCard",
    props:{
        movie: Object,
    },
    computed:{
        imgURL(){
            return `https://image.tmdb.org/t/p/w400/${this.movie.poster_path}`
        }
    }
}
</script>

<style>

</style>