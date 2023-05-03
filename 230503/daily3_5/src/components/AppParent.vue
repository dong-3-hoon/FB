<template>
  <div>
    <h2>앱 부모</h2>
    <AppChild />
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  components: {
    AppChild
  }
}
</script>

<style>

</style>