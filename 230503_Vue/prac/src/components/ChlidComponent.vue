<template>
    <div>부모에서 지어준 이름: {{name}}
        <button @click="giveMeMoney">부모한테 돈주라고 하기</button>
        <button @click="sendToC2('나 용돈 5만원 받았다')">다른 아이한테 메시지 전달</button>
    </div>
</template>

<script>
import EventBus from "@/EventBus"

export default {
    name : "ChildComponent",
    props:{
        name : String
    },
    methods:{
        giveMeMoney(){
            this.$emit("money", 50000)
        },
        sendToC2(message){
            // 여러개 보내려면 object로
            EventBus.$emit("fromC1", message)
        }
    },
    created(){
        console.log("C1 CREATED")
    },
    mounted(){
        console.log("C1 MOUNTED")
    }
}
</script>

<style>

</style>