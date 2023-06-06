<template>
  <section class="bg-c9dbe9 gradient-form">
    <div class="container py-5 h-100">
      <h1 class="fw-bold mt-1 mb-5 pb-1" style="color: black">게시판</h1>
      <div class="row w-100 bg-white rounded" >
          <div class="text-end col-12 w-100 rounded-3 text-black create-button ">
            <router-link
                    to="/create"
                    class="btn btn-dark fa-lg mt-3 mb-4 me-5"
                  >
                    Create Post
                  </router-link>
          </div>
             
                <div class="row">
            
                    <ArticleList />
                  
                </div>
            </div>
      </div>
  </section>
</template>

<script>
import axios from "axios";
import ArticleList from "@/components/ArticleList.vue";

export default {
  name: "ArticleView",
  components: {
    ArticleList,
  },
  mounted() {
    this.$store.dispatch("getArticles");
  },
  
  methods: {
    getArticles() {
      // if(this.isLogin){
      //   this.$store.dispatch('getArticles')
      // }
      // else{
      //   this.$router.push('/login');
      // }
      // 로그인이 되어 있으면 getArticles actio 실행
      // 로그인 x라면 login 페이지로 이동
    },
  },

};
</script>

<style scoped>
section {
  height: 100%;
  min-height: 100vh;
  overflow-y: scroll;
}

.gradient-custom-2 {
  /* fallback for old browsers */
  background: #3b3b3b;
}

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh;
  }
}

@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}

.gradient-form input.form-control {
  border-radius: 50px;
  padding: 10px 20px;
  margin-top: 10px;
  background-color: #f5f5f5;
  border: none;
}

.gradient-form button.btn-primary {
  border-radius: 50px;
  padding: 10px 20px;
  margin-top: 10px;
  background-color: #e62b1e;
  color: #fff;
  font-weight: bold;
  border: none;
}

.gradient-form button.btn-primary:hover {
  background-color: #dd1813;
  cursor: pointer;
}

.card.text-black {
  background-color: #f5f5f5;
}

.card.text-black,
.card.text-black .card-header {
  background-color: #ffffff;
}

.card-header {
  background-color: #e8e8e8;
  border-bottom: none;
  font-weight: bold;
}
.create-button{
  width:10%;
  z-index:9999;
}
.card-body {
  padding: 1.5rem 2rem;
}

@media (max-width: 768px) {
  .gradient-form {
    height: auto;
  }
}
</style>
