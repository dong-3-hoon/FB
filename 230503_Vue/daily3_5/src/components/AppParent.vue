<template>
  <div id="parent">
    <h2>AppParent</h2>
    <input type="text" v-model="parentData" @input="parentChanged">
    <div>appData:{{appData}}</div>
    <div>parentData: {{parentData}}</div>
    <div>childData: {{childData}}</div>
    <AppChild :parent-data="parentData" :app-data="appData" @childChanged="childChanged"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name: "AppParent",
  props:{
    appData: String,
  },
  data(){
    return{
      parentData: "",
      childData: "",
    }
  },
  components: {
    AppChild
  },
  methods:{
    parentChanged(){
      this.$emit("parentChanged", this.parentData)
    },
    childChanged(childData){
      this.childData = childData
      this.$emit("childChanged", this.childData)
    }
  }
}
</script>

<style>
#parent{
  border: 1px solid red;
}
</style>