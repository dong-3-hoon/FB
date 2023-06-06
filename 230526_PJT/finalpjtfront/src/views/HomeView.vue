<template>
  <div class="homeview d-flex justify-content-center text-center">
    <div class="grid-container text-center">
      <div class="grid-item item2 poster-box w-100 h-100  animate__animated animate__fadeIn animate__delay-0.5s"  @click="flip(2)">
        <img class="w-100 h-100 position-absolute card-back" src="../assets/johnwick.jpg" alt="">
        <img class="w-100 h-100 position-absolute card-front" src="../assets/mario.jpg" alt="">
      </div >
      <div class="grid-item item3 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-1s">
        <img class="w-100 h-100" src="../assets/johnwick.jpg" alt="">
      </div>
      <div class="grid-item item4 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-0.5s">
        <img class="w-100 h-100" src="../assets/doorlock.jpg" alt="">
      </div>
    
      <div class="grid-item item5 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-1s">
        <img class="w-100 h-100" src="../assets/galaxy.png" alt="">
      </div>


        <div class="d-flex justify-content-center align-items-center grid-item item2 text-box w-100 h-100 animate__animated animate__backInDown animate__delay-2s" style="background-color:rgba(255, 255, 255, 0);" @click="changePage">
  <h1 class="fw-bold display-1 text-center my-auto" style="color: #000000; font-size: 60px;">COFLIX</h1>
</div>
      <div class="grid-item item6 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-1s">
        <img class="w-100 h-100" src="../assets/deadbody.jpg" alt="">
      </div>
      <div class="grid-item item7 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-0.5s">
        <img class="w-100 h-100" src="../assets/windchild.jpg" alt="">
      </div>
      <div class="grid-item item8 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-1s">
        <img class="w-100 h-100" src="../assets/rage.jpg" alt="">
      </div>
      <div class="grid-item item8 w-100 h-100 poster-box image-right animate__animated animate__fadeIn animate__delay-0.5s">
        <img class="w-100 h-100" src="../assets/crimecity.jpg" alt="">
      </div>
      
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { gsap } from "gsap";
import { MotionPathPlugin } from "gsap/MotionPathPlugin.js"
import anime from 'animejs/lib/anime.es.js';

gsap.registerPlugin(MotionPathPlugin);

export default {
  setup() {
    
  },
  methods: {
    getMovies() { 
      axios({
        url: 'http://localhost:8000/movies/',
        methods: 'get',
      })
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
     flip(target){
      const card = document.querySelector(`.item${target}`)
      const front = card.querySelector('.card-front')
      const back = card.querySelector('.card-back')
    
      anime({
      targets: card,
      rotateY: {
        value: '+=180',
        easing: 'easeInOutSine'
      },
    });

    },
    changePage(){
      const homeview = document.querySelector('.homeview');

      // Create the black hole effect animation
      gsap.to(homeview, {
        opacity: 0,
        scale: 0,
        duration: 1,
        onComplete: () => {
          // Navigate to the destination page after the animation is complete
          this.$router.push('/movielist');
        }
      });
    }

  },
  mounted() {

  }
}
</script>

<style scoped>

.text-box{
  cursor:pointer;
}

 .card-front,
  .card-back {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    backface-visibility: hidden;
  }

   .card-front {
    background-color: #7B9EA8;
    transform: rotateY(0deg);
    transition: transform 500ms ease-out;
  }

  .card-back {
    background-color: #FF7F50;
    transform: rotateY(180deg);
    transition: transform 500ms ease-out;
  }
.grid-container {
  display: grid;
  margin-top:30px;
  grid-template-columns: repeat(3, 220px);
  grid-template-rows: repeat(3, 280px);
  grid-column-gap: 10px;
  grid-row-gap: 10px;
}

.grid-item {
  display: flex;
  justify-content: center;
  align-items: center;
  position:relative;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 5px;
  font-size: 30px;
  text-align: center;
}



.animate__animated.animate__lightSpeedInLeft {
  --animate-duration: 1s;
}


.homeview {
 margin-top:-100px;
}

.text-box * {
  margin-top: 5rem;
  color: rgb(250, 250, 250);
 
}




#svg {
  position: absolute;
  overflow: visible;
  top: 0;
  left: 0;
}

#content {
  text-align: center;
  font-family: sans-serif;
  user-select: none;
}

.balloon {
  cursor: pointer;
}

#behind_svg {
  z-index: 1;
}

#content {
  z-index: 2;
}

#svg {
  z-index: 3;
}
</style> 
