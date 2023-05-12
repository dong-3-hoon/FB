<template>
    <div class="container">
        <div class="row justify-content-center text-center">
            <div class="col">
                <h1 class="fw-bold">보고싶은 영화</h1>
                <WatchListForm />
            
        
                    <div class="list-container border border-dark rounded h-100 text-start ms-3 mt-5">
                        <WatchListItem  v-for="(watchMovie, idx) in watchMovieList" :watchMovie=watchMovie :key=idx />
                    </div>
                
            </div>
        </div>
      
    </div>
  </template>
  
  <script>
  import WatchListItem from '@/components/WatchListItem.vue'
  import WatchListForm from '@/components/WatchListForm.vue'
  export default {
      computed :{
          watchMovieList(){
              return this.$store.state.watchMovieList
          }
      },
      components :{
          WatchListForm,
          WatchListItem
      }
  }
  </script>
  
  <style scoped>

  .list-container{
    height:600px !important;
    background-color:white;
    font-size:x-large
  }
  </style>