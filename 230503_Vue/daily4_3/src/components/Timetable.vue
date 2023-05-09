<template>
<div class="card">
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <div class="d-flex justify-content-ev">
        <div class="t-button justify-content-ev d-flex align-items-center" :class="{selected : selectedTeacher==='Eric'}" @click="selectTeacher('Eric')"><div>Eric</div></div>
        <div class="t-button justify-content-ev d-flex align-items-center" :class="{selected : selectedTeacher==='Tony'}" @click="selectTeacher('Tony')"><div>Tony</div></div>
    </div>
    <div class="hr-b"></div>
    <h2>시간 선택</h2>
    <div class="time-box" :class="{'selected' : isSelected(time)}" v-for="time in times" :key="time" @click="selectTime(time)">{{time}}</div>
    <br>
    <br>
    <div class="t-button justify-content-ev d-flex align-items-center" style="margin: 0 auto;" @click="reservation">예약 확정</div>
    </div>
</template>

<script>
import EventBus from "@/EventBus"
export default {
  name: 'App',
  data() {
    return {
      times : ["09:00","09:30","10:00","10:30","11:00","11:30",
      "12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",
      "16:00","16:30","17:00","17:30"]
      ,
      selectedTeacher : "",
      selectedTimes : []
    }
  },
  methods : {
    selectTeacher(name) {
      this.selectedTeacher = name
      this.selectedTimes = []
    },
    selectTime(time) {
      if (this.selectedTimes.includes(time)) {
        const t_idx = this.selectedTimes.indexOf(time)
        this.selectedTimes.splice(t_idx, 1)
        return
      } else {
        if (this.selectedTimes.length === 5) {
          alert("5타임까지만 신청할 수 있습니다.")
          return
        }
        this.selectedTimes.push(time)
      }
    },
    isSelected(time) {
      return this.selectedTimes.includes(time)
    },
    reservation(){
      if(this.selectedTeacher.length===0){
        alert("의사를 선택하시오")
      }
      else if(this.selectedTimes.length===0){
        alert("시간을 선택하시오")
      }
      else{
        const ob = {'selectedTeacher':this.selectedTeacher, 'selectedTimes':this.selectedTimes}
        EventBus.$emit("mylist", ob)
      }
    }
  }
}
</script>

<style>

</style>