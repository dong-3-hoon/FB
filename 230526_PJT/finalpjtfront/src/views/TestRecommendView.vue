<template>
  <div id="app">
    <div class="container">
      <div class="circle-container">
        <img
          v-for="(circle, index) in circles"
          :key="index"
          src="../assets/testcloud.png"
          :class="{ circle: true, clicked: circle.clicked, show: circle.show }"
          @click="handleClick(index)"
        ></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.circle {
  width: 200px;
  height: 200px;
  background-color: #000000;
  position: relative;
  cursor: pointer;
  opacity: 1;
  transition: opacity 0.5s;
}

.clicked {
  animation: explode 0.5s ease;
  opacity: 0;
}

@keyframes explode {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(1.5);
  }
}
/* .circle{
    transition: opacity 2s 1s ease;
    opacity:0;
} */

.show {
  opacity: 1;
}

.circle-container {
  display: grid;
  width: 100%;
  grid-template-columns: repeat(3, 250px);
  grid-template-rows: repeat(3, 1fr);
  row-gap: 40px;
}
</style>

<script>
import _ from 'lodash';
import gsap from 'gsap';

export default {
  data() {
    return {
      colorList : [
      '#ffcccc',

      '#ffccff', // 빨간색
      '#eeccff', // 초록색
      '#ccddff', // 파란색
      '#ccccff', // 노란색
      '#b3ffe6', // 보라색
      '#ffe6cc', // 청록색
      '#99ffcc', // 주황색
      '#b3ffb3'  // 자주색
      // 원하는 색상을 추가할 수 있습니다.
    ],
      circles: [
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },
        { clicked: false, color: '' },


        // 원하는 개수의 동그라미를 추가할 수 있습니다.
      ]
    };
  },
  methods: {
    handleClick(index) {
      const circle = this.circles[index];
      if (!circle.clicked) {
        circle.clicked = true;

        gsap.to(`#circle-${index}`, { opacity: 0, duration: 0.5, onComplete: () => {
          // 터진 동그라미를 삭제하거나 상태를 변경할 수 있습니다.
        }});

      }
      
      setTimeout((index)=>{
        circle.color = _.sample(this.colorList)
            circle.clicked=false;
            
        },2000)
    }
  },
  mounted() {
    this.circles.forEach((circle)=>{
        const newColor = _.sample(this.colorList)
        circle.color = newColor
    })
    gsap.registerPlugin();


  },

};
</script>
