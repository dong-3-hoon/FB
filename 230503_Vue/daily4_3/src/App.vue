<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class="container">
      <timetable></timetable>
      <mylist></mylist>
    </div>
  </div>
</template>

<script>
import Mylist from './components/Mylist.vue'
import Timetable from './components/Timetable.vue'
export default {
  name: 'App',
  components:{
    Mylist,
    Timetable,
  },
  methods : {
    reservation(){

    }
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
.container {
  border: 1px solid gray;
  border-radius: 10px 10px 10px 10px;
  width: 70%;
  height: 600px;
  margin: 0 auto;
  display : flex;
  box-shadow: -10px 10px 5px gray;
  overflow: hidden;
}
</style>
