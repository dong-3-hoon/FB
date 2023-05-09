<template>
  <div>
    <nav>
      <router-link to="/">모든</router-link> |
      <router-link to="/todaytodopage">오늘</router-link> |
      <router-link to="/importanttodopage">중요</router-link>
    </nav>
    <hr>
    <router-view/>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>