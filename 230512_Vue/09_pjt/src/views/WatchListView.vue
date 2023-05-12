<template>
  <div>
    <h1>보고싶은 영화</h1>
    <WatchListForm />

    <ul>
    <WatchListItem  v-for="(watchMovie, idx) in watchMovieList" :watchMovie=watchMovie :key=idx />
    </ul>
    
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

<style>
</style>