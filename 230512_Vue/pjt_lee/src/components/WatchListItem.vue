<template>
    <div >
      
          <li>
              <span @click="complete" :class="{watched : watchMovie.is_completed}">{{watchMovie.title}}</span>
          </li>
    </div>
  </template>
  
  <script>
  export default {
      data(){
          return{
          }
      },
      props : {
          watchMovie:Object
      },
  
      methods:{
          complete(){
              this.$store.dispatch('watched', this.watchMovie)
                  }
      }
  
  }
  </script>
  
  <style>
  li {
      list-style: none;
  }
  .watched {
      text-decoration: line-through;
  }
  </style>