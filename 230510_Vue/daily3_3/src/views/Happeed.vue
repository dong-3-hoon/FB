<template>
  <div class="wrap">
    <h2>시작</h2>
    <div class="detail d-flex">
        <div class="prev d-flex align-items-center"><span class="btn" @click="toHome">이전</span></div>
        <div><img src="../assets/happeed.png" alt="" class="image"/></div>
        <div class="next d-flex align-items-center"><span class="btn" @click="next">다음</span></div>
    </div>
    <h2>해피드</h2>
  </div>
</template>

<script>
export default {
    name: "Happeed",
    methods:{
        toHome(){
            this.$router.push({name: "Home"})
        },
        next(){
            this.$router.push({name:"happling"})
        }
    }
}
</script>

<style>
.image{
    width: 400px;
}
.d-flex{
    display: flex;
}
.btn{
    border: 1px solid black;
    border-radius: 5px;
    padding: 10px;
    background-color: azure;
}
.align-items-center{
    align-items: center;
}
.wrap{
    margin-top: 50px;
    text-align: center;
    border: 1px solid gray;
    padding: 20px;
    border-radius: 5px;
    box-shadow: lightgray 6px 6px 12px 12px;
}
.btn{
    cursor: pointer;
}
</style>