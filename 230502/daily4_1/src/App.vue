<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class='box'>
      <h2>예약 페이지</h2>
      <br>
      <h3>시간 선택</h3>
      <div class='row'>
        <div class="col-2" v-for="(time, index) in times" :key="index">
          <p :class="{ 'selected':checktime[index] }" @click="toggleActive(time, index)">{{time}}</p>
        </div>
      </div>
    </div>
    <hr>
    <div>
      <span v-for='reser in reservation' :key="reser">{{reser}}</span>
    </div>
  </div>
</template>
<script>

export default {
  name: 'App',
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      checktime: new Array(30).fill(false),
      reservation:[],
    }
  },
  methods: {
    toggleActive(time, index) {
      if(this.reservation.length>4){
        if (this.checktime[index] === true) {
          this.reservation.splice(this.reservation.indexOf(time), 1)
        }
        else{
        alert('더 선택할 수 없습니다.')}
      }
      else{
        if (this.checktime[index] === true) {
          this.reservation.splice(this.reservation.indexOf(time), 1)
        } else {
          this.reservation.push(time)
        }
          this.$set(this.checktime, index, !this.checktime[index])
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.box{
    border: 1px solid black;
}
.selected {
  background-color: green;
  color: #0F4C81;
}
</style>
