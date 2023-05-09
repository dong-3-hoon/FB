<template>
  <div class="alltodopage">
    <h1>모든 할 일</h1>
    <hr>
    <div v-for="(todo,index) in todoList" :key="index">
      <br>
      <button @click="check(todo.id)">{{todo.isCompleted}}</button>
      {{todo.content}}
      <button @click="important(todo.id)">{{todo.isImportant}}</button>
      <br>
    </div>
  </div>
</template>

<script>
export default {
  name: "AllTodoPage",
  computed:{
    todoList(){
      return this.$store.state.todo.list;
    }
  },
  methods:{
    important(id){
      this.$store.dispatch("important", id)
    },
    check(id){
      this.$store.dispatch("check", id)
    }
  }
}
</script>

<style>

</style>