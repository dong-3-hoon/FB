<template>
  <section class="bg-c9dbe9 gradient-form">
    <div class="container py-5 h-100">
      <h1 class="fw-bold mt-1 mb-5 pb-1" style="color: white">게시글 상세보기</h1>
      <div class="row d-flex justify-content-center align-items-center">
        <div class="col-xl-10">
          <div class="card rounded-3 text-black">
            <div class="row g-0">
              <div class="col-lg-12">
                <div class="card-body p-md-5 mx-md-4">
                  <div v-if="article">
                    <div>
                      <h1 id="formTitle" class="mb-0 mb-4"><b>{{ article?.title }}</b></h1>
                      <h5 style="font-size: 16px">작성자:{{ article?.username }}</h5>
                      <i
    class="fa-regular fa-heart comment me-2 like-icon"
    :style="{ color: isUserLiked ? 'red' : '#000000' }"
    @click="like_toggle"
  >
    {{ article.like_users.length }}
  </i>
                    </div>
                    <br>
                    <hr>
                    <div class="mb-4">
                      <ul><h3 id="formContent" class="mb-0">{{ article?.content }}</h3></ul>
                      
                    </div>
                    <hr>
                    <div class="mb-4">
                      <p style="font-size: 12px">
                        작성시간: {{ formatDate(article.created_at) }}
                        <span style="float: right">수정시간: {{ formatDate(article?.updated_at) }}</span>
                      </p>
                    </div>
                  </div>
                  <div v-else>
                    <p>Loading...</p>
                  </div>
                  <div class="mb-4">
                    <h4>댓글</h4>
                    <textarea v-model="newComment" class="form-control" rows="4" placeholder="댓글 작성"></textarea>
                    <button class="btn btn-dark mt-3 me-3" type="button" @click="createComment">댓글 작성</button>
                    <router-link to="/articles" class="btn btn-dark mt-3 me-3">글 목록</router-link>
                    <button v-if="loginUser===article?.username" class="btn btn-dark mt-3 me-3" type="button" @click="deleteArticle">글 삭제</button>
                    <button class="btn btn-dark mt-3 me-3" type="button" @click="updateArticle" v-if="article?.username === loginUser">글 수정</button>
                    
                  </div>
                  <div>
                    <h4>댓글 목록</h4>
                    <ul>
                      <div v-for="(comment, index) in comments" :key="index">
                        <div class="comment-container">
                          <p><img v-if="comment.user.profile_image" :src="'http://localhost:8000'+comment.user.profile_image" alt="엑박" style="width:25px;height:25px;border-radius:50%;"><img v-else :src="require('@/assets/baseuser.png')" style="width:25px;height:25px;border-radius:50%;" alt=""> {{comment.user.nickname}} : {{comment.content}}</p>
                        </div>
                          <button class="btn btn-dark" v-if="comment.user.username === loginUser" @click="deleteComment(index)">삭제</button>

                        <hr>
                      </div>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      comments: null,
      newComment: null,
      isUserLiked : false,
      
    }
  },
  
  computed : {
    loginUser(){
      console.log(this.$store.state.username, 'state의 username입니다.')
      return this.$store.state.username
    },
 
  },

  methods: {
    like_toggle(e) {
      this.isUserLiked = !this.isUserLiked
      if(this.isUserLiked == true){
       e.target.innerText = ' '+(parseInt(e.target.innerText) + 1 )       
      }else{
        e.target.innerText = ' '+(parseInt(e.target.innerText) - 1)
      }
  // 좋아요 상태를 서버에 업데이트
  axios({
    method: 'put',
    url: `${API_URL}/articles/${this.article.id}/likes/`,
    headers: {
      Authorization: `Bearer ${this.$store.state.token}`,
    },
  })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
},
    formatDate(dateString) {
      const date = new Date(dateString);
      const hours = String(date.getHours()).padStart(2, "0");
      const minutes = String(date.getMinutes()).padStart(2, "0");
      return `${hours}:${minutes}`;
    },
    getArticleDetail() {
      axios.get(`${API_URL}/articles/${this.$route.params.id}/`)
        .then((response) => {
          this.article = response.data
          this.comments = response.data.comment_set
          const like_users = response.data.like_users
          const user_id = this.$store.state.user_id
          if (response.data.like_users.includes(this.$store.state.user_id)){
            this.isUserLiked = true
            console.log('ee')
          }else {
            this.isUserLiked = false
          }
        })
        .catch((error) => {
        })
    },
    updateArticle() {
      const articleId = this.$route.params.id;
      this.$router.push({name: 'update', params:{article : this.article}})

      
    },
    deleteArticle(){
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${this.$route.params.id}`,
      })
      .then((response) => {
        this.$router.push({name: 'articles'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createComment() {
      axios({
       url :  `${API_URL}/articles/${this.$route.params.id}/comments/`,
       method : 'post',
       data : {
        content : this.newComment
       },
       headers :{
        Authorization : `Bearer ${this.$store.state.token}`
       }
      })
        
        .then((response) => {
          const createdComment = response.data;
          
          this.comments.push(createdComment)
          this.newComment = '';
        })
        .catch((error) => {
          console.log(this.newComment)
          console.log(error)
        });
    },
    deleteComment(index) {
      const commentId = this.comments[index].id;
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}`,
      })
        .then(response => {
          this.comments.splice(index, 1);
          this.Delete(response.data, commentId);
        })
        .catch(error => {
          console.log(error);
        });
    },
    Delete(article, commentId) {
      const commentIndex = article.comment_set.findIndex(comment => comment.id === commentId);
      if (commentIndex !== -1) {
        article.comment_set.splice(commentIndex, 1);
        axios({
          method: 'delete',
          url: `${API_URL}/articles/comments/${commentId}`,
        })
          .then(() => {
            console.log(`댓글 ${commentId} 삭제됨`);
          })
          .catch(error => {
            console.log(error);
          });
        }
    },
    
  },
  created() {
    this.getArticleDetail()
  },

}

</script>

<style scoped>
.comment-container {
  display: flex;
  align-items: center;
}

.comment-container p.comment-content {
  display: flex;
  align-items: center;
  margin-bottom: 0;
}

.comment-container button {
  margin-left: auto;
}
.like-icon{
  cursor:pointer;
}

</style>