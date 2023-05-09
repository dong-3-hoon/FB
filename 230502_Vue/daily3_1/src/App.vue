<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Home</h1>
    <h3><b>첫번째 박스</b></h3>
    <div class='global'>
      <HomeBox/>
    </div>
    <h3><b>두번째 박스</b></h3>
    <div class='global'>
      <HomeBox/>
    </div>
    <h1>About</h1>
    <h3><b>첫번째 박스</b></h3>
    <div class='global'>
      <AboutBox/>
    </div>
    
    <h3><b>두번째 박스</b></h3>
    <div class='global'>
      <AboutBox/>
    </div>
    
  </div>
</template>

<script>
import AboutBox from './components/AboutBox.vue'
import HomeBox from './components/HomeBox.vue'

export default {
  name: 'App',
  components: {
    AboutBox,
    HomeBox,
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
