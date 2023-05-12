<template>
    <div class="mb-5" :class="{'col-4': list, 'd-flex' : !list, 'justify-content-center' : !list}">
        <div v-if="movie" class="card h-100 rounded" style="width: 18rem;">
            <img  class="h-100 rounded-top " :src="imageURL" alt="">
            <div class="border border-white"></div>
  <div class="card-body rounded-bottom text-title h-100">
    <h5 class="card-title">{{ movie.title }}</h5>
    <p class="card-text fw-normal">{{ movie.overview.slice(0, 100) + '...' }}</p>
  </div>
</div>
    
    </div>
</template>

<script>
export default {
    name: 'FrontVueArticlePreview',

    data() {
        return {
        };
    },
    props : {
        movie:Object,
        list:Boolean
    },
    computed:{
        imageURL(){
            return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
        }
    },

    mounted() {
        
    },

    methods: {
        
    },
};
</script>

<style scoped>
.card-body{
    background-color:black;
    color:white;
    height:100%;
}
</style>