<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link :to="{name: 'happeed'}">Start</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 700px;
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
