<template>
  <div id="app">
    <button @click="getUsers">유저 정보 가져오기</button>
    <ul>
      <UserComponent v-for="user in users" :key="user.id" :user="user">{{user.username}}</UserComponent>
    </ul>
  </div>
</template>

<script>
import UserComponent from "@/components/UserComponent"
export default {
  name: 'App',
  components: {
    UserComponent,
  },
  created(){
    this.$store.dispatch("getUsers", 10)
  },
  methods:{
    getUsers(){
      this.$store.dispatch("getUsers", 5)
    },
  },
  computed:{
    users(){
      return this.$store.state.users
    }
  },
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
