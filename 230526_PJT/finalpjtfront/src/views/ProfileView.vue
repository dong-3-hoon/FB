<template>
  <div class="container bg-white">
    <div>

        <span>{{ username }}</span>
    </div>
    <div>
        <button class="btn btn-secondary" v-if="followState" @click="follow">언팔로우</button>
        <button class="btn btn-primary" v-else @click="follow">팔로우</button>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            followState : false,
     
        }
    },
    props : {
        user_id :String,
        username:String,
    },
    methods:{
        follow(){
            axios({
                url : `http://localhost:8000/accounts/follow/${this.user_id}/`,
                method:'post',
                headers:{
                    Authorization : `Bearer ${this.$store.state.token}`
                }
            })
            .then(res =>{
                console.log(res.data, this.user_id)
                const user_id = parseInt(this.user_id)
                console.log(user_id)
                if(res.data.followings.includes(user_id)){
                    this.followState = true

                }else{
                    this.followState =false
                }
            })
        }
    },
 

  
    created(){
        axios({
                url : `http://localhost:8000/accounts/follow/${this.user_id}/`,
                method:'get',
                headers:{
                    Authorization : `Bearer ${this.$store.state.token}`
                }
            })
            .then(res =>{
                const user_id = parseInt(this.user_id)
                if(res.data.followings.includes(user_id)){
                    this.followState = true

                }else{
                    this.followState =false
                }
            })
    },
    updated(){
    }
  
    
}
</script>

<style>

</style>