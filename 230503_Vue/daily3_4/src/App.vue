<template>
  <div id="app">
    <h1>소득세계산기</h1>
    <hr>
    <Income/>
  </div>
</template>

<script>
import Income from './components/Income.vue'

export default {
  name: 'App',
  components: {
    Income,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
