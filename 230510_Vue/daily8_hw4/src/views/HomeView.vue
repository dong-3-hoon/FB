<template>
  <div>
    <button @click="getCatImg">Get Cat</button>
    <br>
    <img :src="catImgUrl" alt="">
    <h1>CatImg</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CatView',
  data() {
    return {
      catImgUrl: '',
    };
  },
  methods: {
    getCatImg(){
      const catImageURL = `https://api.thecatapi.com/v1/images/search`
      axios({
        method: 'get',
        url: catImageURL
      })
      .then((response)=>{
        const catImgUrl = response.data[0].url
        this.catImgUrl = catImgUrl
      })
    },
  },
  created(){
    this.getCatImg()
  },
  watch: {
    catImgUrl(newVal) {
      console.log('Image URL updated:', newVal);
    }
  }
};
</script>

<style>

</style>