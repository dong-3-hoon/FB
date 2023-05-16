<template>
  <div>
    <b-container role="grup" class="p-5 login-form">
        <h1>회원가입</h1>
        <b-row>
            <label for="input-username">아이디</label>
            <b-form-input id="input-username" placeholder="ID" v-model="username"
            :state="nameState"
            aria-describedby="input-live-feedback" trim></b-form-input>

            <b-form-invalid-feedback id="input-username-feedback" class="text-right">
                알파벳/숫자 3글자 이상</b-form-invalid-feedback>
        </b-row>
        <b-row>
            <label for="input-password1">비밀번호</label>
            <b-form-input id="input-password1" placeholder="password1" v-model="password1"
            :state="password1State"
            aria-describedby="input-live-feedback"
            trim type="password"></b-form-input>
        <b-form-invalid-feedback id="input-password1-feedback" class="text-right">
            알파벳/숫자 5글자 이상</b-form-invalid-feedback>
        </b-row>
        <b-row>
            <label for="input-password2">비밀번호</label>
            <b-form-input id="input-password2" placeholder="password2" v-model="password2"
            :state="password2State"
            aria-describedby="input-live-feedback"
            trim type="password"></b-form-input>
        <b-form-invalid-feedback id="input-password2-feedback" class="text-right">
            비밀번호가 일치하지 않습니다.</b-form-invalid-feedback>
        </b-row>
        <b-row>
            <label for="input-lastname">성</label>
            <b-form-input id="input-lastname" placeholder="lastname" v-model="lastname"
            aria-describedby="input-live-feedback"
            trim></b-form-input>
        </b-row>
        <b-row>
            <label for="input-firstname">이름</label>
            <b-form-input id="input-firstname" placeholder="firstname" v-model="firstname"
            aria-describedby="input-live-feedback"
            trim></b-form-input>
        </b-row>
        <b-button variant="success" @click="signup">회원 가입</b-button>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            username: "",
            password1: "",
            password2: "",
            lastname: "",
            firstname: "",
        }
    },
    computed: {
        nameState(){    
            return this.username.length >= 3 ? true : false
        },
        password1State() {
            return this.password1.length >= 5 ? true : false
        },
        password2State() {
            return this.password1== this.password2 ? true : false
        },
    },
    methods:{
        signup(){
            axios({
                method: "post",
                url: 'http://127.0.0.1:8000/auth/signup/',
                data: {
                    username: this.username,
                    password1: this.password1,
                    password2: this.password2,
                    lastname: this.lastname,
                    firstname: this.firstname,
                },
            })
            .then((res)=>{
            console.log(res.data)})
            .catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>