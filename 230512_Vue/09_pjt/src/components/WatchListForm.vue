<template>
  <div>
    <input type="text" v-model="watchMovie" />
    <button @click="addWatchList">Add</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      watchMovie: null,
    };
  },
  methods: {
    addWatchList() {
        //state안에 있는 wishMovieList에 push
        this.$store.dispatch('addWatchMovie', this.watchMovie)

    },
  },
};
</script>

<style>
</style>