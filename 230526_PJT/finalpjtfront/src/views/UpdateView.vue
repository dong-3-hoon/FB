<template>
  <section class="bg-c9dbe9 gradient-form">
    <div class="container py-5 h-100">
      <h1 class="fw-bold mt-1 mb-5 pb-1" style="color: white">게시글 수정</h1>
      <div class="row d-flex justify-content-center align-items-center">
        <div class="col-xl-10">
          <div class="card rounded-3 text-black">
            <div class="row g-0">
              <div class="col-lg-12">
                <div class="card-body p-md-5 mx-md-4">
                  <form @submit.prevent="updateArticle">
                    <div class="form-outline mb-4">
                      <label class="form-label" for="formTitle">Title</label>
                      <input
                        v-model="title"
                        type="text"
                        id="formTitle"
                        class="form-control"
                        placeholder="제목"
                      />
                    </div>

                    <div class="form-outline mb-4">
                      <label class="form-label" for="formContent">Content</label>
                      <textarea
                        v-model="content"
                        id="formContent"
                        class="form-control"
                        placeholder="내용"
                      ></textarea>
                    </div>

                    <div class="text-center pt-1 mb-5 pb-1">
                      <button
                        class="btn btn-dark btn-block fa-lg gradient-custom-2 mb-3"
                      >
                        게시글 수정
                      </button>
                    </div>
                  </form>
                  
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
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'
export default {
  name: 'CreateView',
  data() {
    return {
        title: null,
        content: null,
        username : null,
    };
  },
  methods: {
    
    updateArticle(){
      const title = this.title
      const content = this.content
    
      axios({
        url:`http://localhost:8000/articles/${this.$route.params.id}/`,
        data:{
          content, title
        },
        method : 'put',
        headers : {
          Authorization : `Bearer ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log(res, 'put매핑 성공!')
        this.$router.push({name: 'articles'})
      
      })
      .catch(err=>{
        console.log(err)
      })
    }
    
  },
  
  created(){
    this.title = this.$route.params.article.title
    this.content = this.$route.params.article.content
    this.username = this.$route.params.article.username

  }
  
};
</script>

<style scoped>
/* Add your custom styles here */
</style>