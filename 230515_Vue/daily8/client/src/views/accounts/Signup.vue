<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="SignUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'SignUp',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    SignUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      if(!username){
        alert('아이디를 입력하시오')
        return
      }
      else if(!password1 || !password2){
        alert('비밀번호를 모두 입력하시오')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {username, password1, password2}
      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name: 'TodoList'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
}
</script>
