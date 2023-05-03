<template>
<div>
    <h2>산출세액: 만원</h2>
    <h2>세액감면: (-) 만원</h2>
    <hr>
    <Finaltax/>
</div>
</template>

<script>
import Finaltax from '@/components/Finaltax.vue'
export default {
    components:{
        Finaltax,
    }

}
</script>

<style>

</style>