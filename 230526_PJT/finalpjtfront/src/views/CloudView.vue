<template>
  <div id="app">
    <div class="container">
      <div class="circle-container">
        <div
          v-for="(circle, index) in circles"
          :key="index"
          class="position-relative"
        >
          <img
            :src="circle.imageUrl"
            :class="{
              circle: true,
              clicked: circle.clicked,
              show: circle.show,
            }"
            @click="handleClick(index)"
          />
          <div
            id="cloud-value${index}"
            @click="handleClick(index)"
            class="position-absolute display-6 fw-bold text-black cloud-value"
            :class="{ clicked: circle.clicked, show: circle.show }"
          >
            {{ circle?.name }} 
          </div>
        </div>
        
      </div>
      <div class="d-flex justify-content-center">
        <button class="btn-blue" @click="sendRecommendList">결과 보러가기</button>

      </div>

    </div>
    
  </div>
</template>

<style scoped>
.container .circle-container {
  overflow: hidden;
  font-family: "Nanum Gothic", sans-serif !important;
}
.circle {
  width: 200px;
  height: 200px;
  background-color: #ffffff00;
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
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, 1fr);

  row-gap: 40px;
  z-index: 9999;
}

.cloud-value {
  top: 40%;
  left: 20%;
  font-size: 1.5rem;
  cursor: pointer;
}

button{
  width : 30%;
  height : 50px;
  margin-bottom : 15px;
  border : none;
  z-index:9999;
  border-radius : 5px;
  color: #272727;
  font-size: 2rem;
  font-weight:bold;
  transition : background-color ease-in-out 0.5s; 
}

.btn-blue{
  background-color : #d7ecff;
}




</style>

<script>
import _ from "lodash";
import gsap from "gsap";

export default {
  data() {
    return {
      valueList : [],
      valueIndex : 8,
      genres: [
        // {
        //   name: "모험",
        //   count: 1000,
        //   value: [
        //     "스릴",
        //     "활발함",
        //     "신남",
        //     "설렘",
        //     "모험",
        //     "스릴",
        //     "위험",
        //     "탐험",
        //     "자유로움",
        //     "열정",
        //     "도전",
        //     "흥미진진",
        //   ],
        // },
        {
          name: "판타지",
          count: 999,
          value: [
            "이세계",
            "마법",
            "상상력",
            "마법사",
            "몽환적",
            "미스테리",
            "전설",
            "마법",
            "환상",
          ],
        },
        {
          name: "애니메이션",
          count: 0,
          value: [
            "이세계",
            "귀여움",
            "감동",
            "판타지",
            "모험",
            "로맨스",
            "코미디",
            "웃음",
            "흥미진진",
          ],
        },
        // { name: "SF", count: 999, value:['마블',	'디시',	'과학',	'미래',	'우주',	'외계',	'과학',	'시간여행',	'변이',	'디스토피아',	'로봇',	'인공지능',] },

        { name: "드라마", count: 0, value:['감동', '인간성', '현실', '갈등', '성장', '감정적'] },
        // { name: "공포", count: 0, value:['무서움', '긴장감', '공포감', '귀신', '불안', '공포'] },
        { name: "액션", count: 0, value:['스릴', '전투', '위험', '속도', '폭발'] },
        { name: "코미디", count: 0, value:['무생각', '유머', '웃음', '유쾌', '흥미로움'] },
        // { name: "범죄", count: 0, value:['DC', 'MARVEL', '수사', '복수', '음모', '잔인'] },
        { name: "로맨스", count: 0, value:['사랑',	'감정',	'진심',	'만남',	'이별',	'슬픔',	'인연',	'성장',	'긴장감',	'아름다움',	'행복',	'설렘']},
        // { name: "가족", count: 0, value:['협력',	'성장',	'웃음',	'감동',	'성숙',	'변화',	'헌신',	'희생',	'우정'] },
      ],
      circles: [
        {
          clicked: false,
       
          
          imageUrl: require("@/assets/cloud1.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud2.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud3.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud4.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud6.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud6.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud7.png"),
        },
        {
          clicked: false,
          color: "",
          name: "강",
          imageUrl: require("@/assets/cloud1.png"),
        },
        // 원하는 개수의 동그라미를 추가할 수 있습니다.
      ],
    };
  },
  methods: {
    handleClick(index) {
      const circle = this.circles[index];
      if (!circle.clicked) {
        circle.clicked = true;
      }
      setTimeout((index) => {
        let newName = _.sample(_.range(1, 8));

        circle.clicked = false;
        circle.name = this.valueList[this.valueIndex]
        this.valueIndex+=1
        this.genres.forEach(genre=>{
          if (genre.value.includes(circle.name)){
            genre.count += 1
          }
        })
   
        circle.imageUrl = require(`@/assets/cloud${newName}.png`);
      }, 1000);
    },
    sendRecommendList(){
      
      this.genres.sort((a, b)=>{
        if (a.count >= b.count) return -1;
        if (a.count < b.count) return 1;
      })

      const recommendList = this.genres.slice(0, 4).map(genre=>{
        return genre.name
      })
      console.log(this.genres.slice(0,4))
      this.$store.dispatch('saveRecommendList', _.cloneDeep(recommendList))
      this.$router.push({name : 'recommend'})
    }
  },
  mounted() {
      this.genres.forEach((genre)=>{
        genre.value.forEach((el, index)=>{
          if (!this.valueList.includes(el)){
            this.valueList.push(el)
            if(index < this.circles.length){
            
              this.circles[index].name = el
            }
          }
        })
      })
    this.circles.forEach((circle) => {
      const newColor = _.sample(this.colorList);
      circle.color = newColor;
    });
  },
  
};
</script>
