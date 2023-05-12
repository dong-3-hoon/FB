<template>
  <div id="app">
    <nav class="d-flex align-items-center">
    <div class="logo">게시판</div>
    <ul class="nav-links d-flex align-items-center mt-2">
      <li><router-link to="/">홈</router-link></li>
      <li><router-link :to="{name : 'movieList'}">게시판</router-link></li>
      <li><router-link :to="{name : 'random'}">Random</router-link></li>
      <li><router-link :to="{name : 'watchList'}">WatchList</router-link></li>
    </ul>
  </nav>
    <transition name="fade" mode="out-in">
    
    <router-view/>
    </transition>
  </div>
</template>
<script>

export default ({
  name : 'app',
  created(){
    this.getMovieList()
  },
  methods:{
   
    getMovieList(){
      this.$store.dispatch('getMovieList')
    }
  },
 
})
</script>

<style>
body{
  background-color:#ffffffb6 !important;
}
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
}

nav {
  background-color: #0a0a0ab6;
  color: #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
}

.nav-links li:not(:last-child) {
  margin-right: 20px;
}

.nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
}

.nav-links a:hover {
  color: #fff;
  background-color: #000;
  padding: 5px 10px;
  border-radius: 5px;
}

.hero {
  background-color: #000;
  color: #f0db4f;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-content {
  text-align: center;
}

.hero h1 {
  font-size: 4rem;
  margin-bottom: 20px;
}

.hero p {
  font-size: 1.5rem;
  font-weight: bold;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.board-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.board-item {
  border: 1px solid #000;
  padding: 10px;
  border-radius: 5px;
}

.board-item h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.board-item p {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

footer {
  background-color: #f0db4f;
  color: #000;
  text-align: center;
  padding: 10px;
}

.fade-enter{
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active{
  transition : opacity 0.5s ease-out;
}
.fade-leave-to{
  opacity: 0;
}
html * {
  font-weight:bolder;
}
</style>
