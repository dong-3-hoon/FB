<template>
    <div
      class="stage position-relative"
      @mousedown="handleImageMouseDown"
      @mousemove="handleImageMouseMove"
      @mouseup="handleImageMouseUp"
    >
      <h1
        class="position-absolute display-6 fw-bolder text-black pt-5 ps-5 text-center"
      >
        추천 영화
      </h1>
      <div class="container">
        <div class="ring">
          <div
            class="img hvr-grow-shadow rounded"
            v-for="(movie, index) in movieList"
            :key="index"
            :class="{
              active: activeIndex === index,
              deactive: (activeIndex != index && hovered),
            }"
            :style="`background-image: url(${movie.url})`"
            @mouseenter="handleImageHover(index)"
            @mouseleave="handleImageHover(-1)"
            @click="goDetail(movie.id)"
          >
                      </div>

            <!-- <div class="h-100 d-flex flex-column justify-content-between">
              <div class="ms-2 movie-title-container">
                <div>
                  <span class="movie-title text-white fw-bolder">{{
                    movie.title
                  }}</span>
                </div>
              </div> -->
              <!-- <div class="hover-detail" v-if="activeIndex===index && hovered">
                <div>
                  <span>
                    <i
                      v-for="(star, idx) in stars"
                      :key="idx"
                      class="fa-solid fa-star"
                      :class="{
                        'text-black': (idx + 1) * 2 <= movie.vote_average,
                      }"
                    ></i>
                  </span>
                </div>
                <div class="ms-2 me-2 detail-overview-container">
                  <span class="text-white detail-overview">{{
                    movie.overview.slice(0, 100) + "..."
                  }}</span>
                </div>
                <div class="d-flex justify-content-end">
                  <button class="detail-btn rounded fw-bold text-white me-3">
                    영화 보기
                  </button>
                </div>
                <span class="movie-title text-white fw-bolder">{{
                  movie.vote_average
                }}</span>
              </div> -->
          </div>
        </div>
      </div>
  
</template>

<script>
import axios from "axios";
import "hover.css/css/hover-min.css";
import _ from "lodash";
let direction = 0; // 1 for clockwise, -1 for counterclockwise
let rotation = 0;
export default {
  data() {
    return {
      dragging : '',
      stars: _.range(5),
      activeIndex: -1,
      hovered: false,
      movieList: [],
      startX: 0,
      currentX: 0,
      prevX: 0,
      recommendList:[],
    };
  },
  methods: {
    handleImageMouseDown(event) {
      this.dragging = true;
      this.hovered = false;
      this.startX = event.clientX || event.touches[0].clientX;
    },
    handleImageMouseMove(event) {
      if (!this.dragging) return;
      this.hovered = false;
      this.currentX = event.clientX || event.touches[0].clientX;
      const deltaX = this.currentX - this.startX;
      // 조절 가능한 회전 속도
      if (this.currentX - this.prevX > 0) {
        rotation += Math.abs((deltaX + 1) / 360);
      } else {
        rotation -= Math.abs((deltaX + 1) / 360);
      }
      this.prevX = this.currentX;
      
    },
    handleImageMouseUp() {
      this.dragging = false;
    },
    handleImageClick(index) {
      this.activeIndex = index;
      this.hovered = true;
      this.centerImage(index);
    },
    centerImage(index) {
      const ring = document.querySelector(".ring");
      const images = document.querySelectorAll(".img");
      const rotationAngle = 360 / images.length;
      const targetRotation = -index * rotationAngle;

      images.forEach((image, idx) => {
        rotation = targetRotation + idx * rotationAngle;
        image.style.transform = `rotateY(${rotation}deg) translateZ(500px)`;
      });
    },

    startStyle() {
      if (true) {
        this.start = true;
        const ring = document.querySelector(".ring");
        const images = document.querySelectorAll(".img");
        const leftBtn = document.querySelector(".left-rotate");
        const rightBtn = document.querySelector(".right-rotate");
        let rotationSpeed = 0.1; // Adjust the rotation speed as desired

        images.forEach((image, index) => {
          const initialRotation = rotation + index * 36;
          image.style.transform = `rotateY(${initialRotation}deg) translateZ(500px)`;
          image.style.opacity = 1;
        });

        function rotateCarousel() {
          rotation += rotationSpeed * direction;
          images.forEach((image, index) => {
            const newRotation = rotation + index * 36;
            image.style.transform = `rotateY(${newRotation}deg) translateZ(500px)`;
          });
        }

       
        const stage = document.querySelector('.stage')
        stage.addEventListener("mouseleave", () => {
          this.dragging =false
        });

        setInterval(() => {
          requestAnimationFrame(rotateCarousel);
        });
      }
    },
    handleImageHover(index) {
      this.activeIndex = index;

      this.hovered = true;
      if (index == -1) {
        this.hovered = false;
      }
      console.log(index);
    },
    goDetail(id){
      this.$router.push({name:'MovieDetailView', params:{id}})
    }
  },

  mounted() {
    this.recommendList = this.$store.state.recommendList
    const rankCount = [0, 0, 0, -1]
    axios
      .get("http://localhost:8000/movies")
      .then((res) => {
        const data = _.shuffle(res.data)
        const selectedData = data.filter((movie)=>{
          // recommendList에서 이름 받아오기
          if(movie.genre_ids[0] && this.recommendList.includes(movie.genre_ids[0]?.name)){
            let idx = -1
            movie.genre_ids.forEach((genre)=>{
              idx = this.recommendList.indexOf(genre.name)
              return
            })
            if (idx != -1){
              if (rankCount[idx] < idx+1){
              rankCount[idx]+=1
              return movie
            }
            }
          }
        })
        console.log(selectedData)
        selectedData.forEach((data) => {
          this.movieList.push({
            ...data,
            url: `https://image.tmdb.org/t/p/w500/${data.poster_path}`,
          });
        });
      })
      .then(() => {
        this.startStyle();
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
* {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.left-rotate {
  position: absolute;
  z-index: 9999;
  left: 0;
  height: 100%;
  width: 15%;
}
.right-rotate {
  position: absolute;
  right: 0;
  z-index: 9999;
  width: 15%;
  height: 100%;
}
h1.position-absolute {
  top: 0px;
  right: 50%;
}
.stage {
  margin-left: 5rem;
  width: 100%;
  height: 100vh;
  display: flex;

  justify-content: center;
  align-items: center;
}

.container {
  position: relative;
  width: 400px;
  height: 300px;
  perspective: 1000px;
}

.ring {
  position: absolute;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  /* animation: spin 24s linear infinite; */
}

.img {
  position: absolute;
  width: 250px;

  height: 350px;
  background-size: cover;
  background-position: center;
  transform-style: preserve-3d;
  opacity: 1;
  transition: opacity 0.5s ease-in-out;
}

@media (max-width: 1000px) {
  .img {
    width: 200px;
  }
}

.box.left {
  position: absolute;
  left: 30px;
  z-index: 999;
  height: 50px;
  width: 50px;
  top: 50%;
  transform: translateY(-50%);
}
.box.right {
  position: absolute;
  right: 30px;
  z-index: 999;
  height: 50px;
  width: 50px;
  top: 50%;
  transform: translateY(-50%);
}
.active {
  opacity: 1 !important;

  /* 원하는 스타일을 추가로 적용하세요 */
}
.deactive {
  opacity: 0.1 !important;
}

/* .movie-title-container {
  background: rgba(79, 79, 79, 0.071);
  z-index:9999;
} */



.hover-detail {
  background-color: rgba(70, 70, 70, 0.438);
}

.detail-btn {
  border: solid 1px black;
  background:none;

}

.detail-overview {
  font-size: 0.3rem;
  -webkit-text-stroke: 0.2px black;
}

@keyframes spin {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(360deg);
  }
}
@keyframes unspin {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(-360deg);
  }
}
</style>
