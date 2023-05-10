<template>
  <div class="wrap">
    <h2>2단계</h2>
    <div class="detail d-flex">
        <div class="prev d-flex align-items-center"><span class="btn" @click="goTob">이전</span></div>
        <div><img src="../assets/happlossome.png" alt="" class="image"/></div>
        <div class="next d-flex align-items-center"><span class="btn" @click="next">다음</span></div>
    </div>
    <h2>해플라썸</h2>
  </div>
</template>

<script>
export default {
    name: "Happeed",
    methods:{
        goTob(){
            alert("이전 단계로 돌아갈 수 없습니다.")
        },
        next(){
            this.$router.push({name:'happlower'})
        }
    }
}
</script>
<style>

</style>