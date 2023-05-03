<template>
<div>
    <div>
        <p>연봉 입력 (만원): <input v-model.number="dusqhd" type="nunber"></p>
    </div>
    <div>
        <p>세액감면액 (만원): <input v-model.number="tprkador" type="number"></p>
    </div>
    
    <hr>
    <h2>종합소득금액: {{dusqhd}} 만원</h2>
    <h2>종합소득공제: (-) 150 만원</h2>
    <h2>과세표준: {{standard > 0 ? standard:0}}</h2>
    <hr>
    <Taxrate/>
</div>
</template>

<script>
import Taxrate from '@/components/Taxrate.vue'
export default {
    components:{
        Taxrate,
    },
    data: function(){
        return{
            dusqhd:0,
            tprkador:0,
        }
    },
    //계산식은 여기에
    computed:{
        standard(){
            return this.dusqhd-150
        }
    }
}
</script>

<style>

</style>