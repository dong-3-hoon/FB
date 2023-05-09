<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <chlid-component name="임준환" @money="giveMoney"></chlid-component>
    <child-component-2></child-component-2>
  </div>
</template>

<script>
  import ChildComponent2 from './components/ChildComponent2.vue'
  import ChlidComponent from './components/ChlidComponent.vue'
  export default {
    name: 'App',
    components: {
      ChlidComponent,
      ChildComponent2,
    },
    methods:{
      giveMoney(money){
        alert(`용돈 ${money}원`)
      }
    },
    created(){
      console.log("APP CREATED")
    },
    mounted(){
      console.log("APP MOUNTED")
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
</style>
