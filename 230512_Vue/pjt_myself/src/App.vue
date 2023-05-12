<template>
  <div id="app">
    <nav>
      <nav id="navbar-example2" class="navbar bg-light px-3 mb-3">
        <a class="navbar-brand" href="#">Navbar</a>
        <ul class="nav nav-pills">
          <li class="nav-item">
            <router-link to="/movies">Movie</router-link> | 
          </li>
          <li class="nav-item">
            <router-link to="/random">Random</router-link> | 
          </li>
          <li class="nav-item">
            <router-link to="/watch-list">Watchlist</router-link>
          </li>
        </ul>
      </nav>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  created(){
    this.$store.dispatch('getMovies')
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
