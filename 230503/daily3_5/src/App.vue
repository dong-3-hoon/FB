<template>
  <div>
    <h1>앱</h1>
    <AppParent />
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  components: {
    AppParent
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
