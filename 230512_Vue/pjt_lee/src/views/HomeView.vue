<template>
  <div class="home">
   <div class="hero">
  <div class="hero-content">
    <h1 class="fw-bold">9차 관통 프로젝트</h1>
    <p>영화 추천</p>
    <router-link :to="{name : 'movieList'}">Go to Board</router-link>
  </div>
</div>

  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src

export default {
  name: 'HomeView',
  data(){
    return {
      imageUrl : null,
    }
  },
  components: {
  },
  methods : {
    getCats(){
      axios({
        url : `https://api.thecatapi.com/v1/images/search`,
        method : 'get'
      }).then((res) =>{
        this.imageUrl = res.data[0].url
      })
    }
  },
  created(){
    this.getCats()
  }

}
</script>

<style>
 .hero {
  position: relative;
  height: 500px;
  background-color: #ffffff;
}

.hero img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #000;
  transition: opacity 1s ease-in-out;
}


.hero-content h1, .hero-content p, .hero-content a {
  opacity: 0;
  animation-name: fade-in;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-fill-mode: forwards;
}

.hero-content h1 {
  animation-delay: 1s;
}

.hero-content p {
  animation-delay: 2s;
}

.hero-content a {
  animation-delay: 3s;
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}


.hero h1 {
  font-size: 4rem;
  margin-bottom: 20px;
}

.hero p {
  font-size: 1.5rem;
  margin-bottom: 30px;
}

.hero a {
  display: inline-block;
  background-color: #000;
  color: #ffffff;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
}

.hero a:hover {
  background-color: #fff;
  color: #000;
}

</style>
