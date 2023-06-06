<template>
  <div class="col-6 position-relative">
    <div v-if="clicked" class="position-absolute balloon-container">
          <div class="balloon text-center" @click="follow">
            <i v-if="followCheck" class="fa-sharp fa-solid fa-person mt-1"></i>            
            <i class="fa-solid fa-person mt-1"></i>
          </div>
        </div>
    <router-link :to="'/detail/' + article.id" class="article-link">
      <h3 class="article-title">
        <span class="fw-bold article-title">{{ article.title.slice(0, 30) }}</span>
      </h3>
    </router-link>
    <br>
    <p class="article-info">
      <img v-if="article.user.profile_image" :src="`http://localhost:8000${article.user.profile_image}`" alt="" class="d-inline" style="width:50px;height:50px;border-radius:50%;">
      
      <div v-if="!article.user.profile_image" class="bg-secondary rounded-circle me-2 mb-2" style="width:50px;height:50px;">
                    <i class="fa-solid fa-user user-icon"></i>
                  </div>
        <span @click="showFollow" class="author text-black fw-bold profile-name">작성자:{{ article.user.nickname }}</span>
        
      <i class="fa-regular fa-comment comment me-2" style="color: #000000;"> {{ comments }}</i>
      <i
        class="fa-regular fa-heart comment me-3"
        style="color: #000000;" :style="{color : isLiked ? 'red' : 'black'}"> {{ article.like_users.length }}
      </i>
    </p>
    <br>
    <hr>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // Replace with your actual API URL

export default {
  name: 'ArticleListItem',
  data() {
    return {
      comments: [],
      isLiked : false,
      clicked : false,
      followState : false,
    }
  },
  props: {
    article: Object,
  },
  mounted() {
    this.fetchComments();
    console.log(this.article.user.id,'이 게시물의 article')
  },
  methods: {
    follow(){
      
            axios({
                url : `http://localhost:8000/accounts/follow/${this.article.user.id}/`,
                method:'post',
                headers:{
                    Authorization : `Bearer ${this.$store.state.token}`
                }
            })
            .then(res =>{
                console.log(res.data, this.article.user.id)
                const user_id = parseInt(this.article.user.id)
                console.log(user_id)
                if(res.data.followings.includes(user_id)){
                    this.followState = true

                }else{
                    this.followState =false
                }
            })
            this.$store.dispatch('getUserinfo')
        },
    fetchComments() {
      const articleId = this.article.id; // Get the article ID from the props
      axios.get(`${API_URL}/articles/${articleId}/`)
        .then(response => {
          this.comments = response.data.comment_count;
          if(response.data.like_users.includes(this.$store.state.user_id)){
            this.isLiked = true
          }
          
        })
        .catch(error => {
          console.log(error);
        });
    },
    showFollow(){
      this.clicked = !this.clicked
    }
  },
  created(){
    console.log(this.article.user)
  },
  computed : {
    followCheck(){
      return this.$store.state.followings.includes(this.article.user.id)
    }
  }
}
</script>

<style>
.article-title{
  font-size:1.5rem;
}
.article-link {
  text-decoration: none;
}
.article-title {
  color: black;
  text-decoration: none;
}
.article-info {
  margin-top: 0.5rem;
}

.fa-person{
  font-size:3rem;
  color:rgb(80, 80, 80);
}

.author {
  float: left;
}
.user-icon {
  font-size: 30px; /* 아이콘의 크기 조절 */
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px; /* 원하는 너비로 조절 */
  height: 50px; /* 원하는 높이로 조절 */
}
.comment {
  float: right;
}
.profile-name{
  cursor:pointer;
}
.balloon {  
 position:relative; 
 left:-30%;
 width:120px; 
 height:60px;
  background:rgb(192, 232, 255); 
  border-radius: 10px;
  z-index:999;
}
.balloon:after { 
 border-top:0px solid transparent; 
 border-left: 10px solid transparent; 
 border-right: 10px solid transparent; 
 border-bottom: 10px solid rgb(192, 232, 255);
 content:""; 
 position:absolute;
 top:-10px;
 left:45%;  
}
.balloon-container{
  bottom:-15%;
  left:5%;
}
</style>
