<template>
    <div>
      <div class="container">
        <div class="row justify-content-center">

            <MovieListItem v-for="(movie, index) in movieList" :key=index :movie="movie" :list="true"/>
        </div>
      </div>
        
    
    </div>
</template>

<script>
import MovieListItem from '../components/MovieListItem.vue';

export default {
    name: 'MovieListView',

    data() {
        return {
            
        };
    },

    mounted() {
        
    },
    computed : {
        movieList(){
            return this.$store.state.movieList
        }
    },

    methods: {
        
    },
    components :{
        MovieListItem
    }
};
</script>

<style lang="scss" scoped>

</style>