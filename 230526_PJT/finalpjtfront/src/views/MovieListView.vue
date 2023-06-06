<template>
  <div class="background container">
    <div class="bg-light pb-3 rounded">

      <h4 class="mt-5 fw-bold text-black">{{ weather }} 한 현재 날씨에 추천하는 영화 <i class="fa-solid fa-chevron-right text-secondary"></i></h4>
      <div class="d-flex justify-content-center">
        <div class="multi-item-carousel">
          <div class="swiper-container">
            <div class="swiper-wrapper">
              <div class="swiper-slide" v-for="(movie, index) in movies" :key="index">
                <router-link :to="`/moviedetail/${movie.id}`">
                  <div class="item rounded">
                    <img :src="`https://image.tmdb.org/t/p/w500/`+movie.poster_path" class="item-image" alt="Movie Poster">
              
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        
        </div>
      </div>

    </div>
    <div class="bg-light pb-3 rounded">
      <h3 class="fw-bold text-black mt-5">현재 상영중인 영화<i class="fa-solid fa-chevron-right text-secondary"></i></h3>
      <div class="d-flex justify-content-center">
        <div class="multi-item-carousel">
          <div class="swiper-container">
            <div class="swiper-wrapper">
              <div class="swiper-slide" v-for="(movie, index) in nowPlayingMovies" :key="index">
                <router-link :to="`/moviedetail/${movie.id}`">
                  <div class="item rounded">
                    <img :src="`https://image.tmdb.org/t/p/w500/`+movie.poster_path" class="item-image" alt="Movie Poster">
              
                  </div>
                </router-link>
               
              </div>
            </div>
          </div>
   
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swiper from "swiper";
import axios from 'axios'
import _ from 'lodash'
export default {
  data() {
    return {
      movies : [],
      nowPlayingMovies : [],
      swiperOptions: {
        slidesPerView: 4,
        spaceBetween: 20,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
      swiper: null,
    };
  },
  methods:{
    getMovies(){
      console.log(this.$store.state.weather)
      axios({
          method: 'get',
          url : `http://localhost:8000/movies/${this.$store.state.weather}/`
        })
        .then((res) => {
          console.log(res.data, '영화 가져오기 완료')
          this.movies = res.data

        })
        .catch((err) => {
          console.log(err)
        })

        axios({
          method: 'get',
          url : `http://localhost:8000/movies/now/`
        })
        .then((res) => {
          console.log(res.data, '영화 가져오기 완료')

         
          this.nowPlayingMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
   
  },
  computed : {
    weather(){
      return this.$store.state.weather
    }
  },
  mounted() {
    this.swiper = new Swiper('.multi-item-carousel .swiper-container', this.swiperOptions);
    this.getMovies();
    this.getWeather();
  },
};
</script>

<style scoped>
.background {
  height: 100vh;
  z-index: 2;
}

.multi-item-carousel {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 80%;
  height: 300px;
  margin: 0 auto;
  overflow: hidden;
}

.swiper-container {
  width: 100%;
  overflow: hidden;
}

.swiper-wrapper {
  display: flex;
}

.swiper-slide {
  width: calc(100% / 4);
  flex-shrink: 0;
}

.item {
  position: relative;
  width: 220px;
  height: 300px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  cursor: pointer;
}

.item:hover {
  transform: scale(1.05);
}

.item-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.7);
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.item-title {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 5px;
}

.item-rating {
  font-size: 12px;
  font-weight: 400;
}

.swiper-button-prev,
.swiper-button-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #ccc;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
  z-index: 1;
}

.swiper-button-prev {
  left: 10px;
}

.swiper-button-next {
  right: 10px;
}

.swiper-button-prev:hover,
.swiper-button-next:hover {
  background-color: #999;
}

.text-black {
  color: #000;
}

.text-secondary {
  color: #888;
}

.mt-5 {
  margin-top: 2rem;
}

.fw-bold {
  font-weight: bold;
}

.d-flex {
  display: flex;
}

.justify-content-center {
  justify-content: center;
}
</style>
