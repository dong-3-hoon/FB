<template>
  <div>
    <h2>산출세액: {{tkscnftpdor}}만원</h2>
    <h2>세액감면: (-){{tprkador}} 만원</h2>

    <hr>
    <Finaltax :rufwjdtpdor="rufwjdtpdor"/>
  </div>
</template>

<script>
import Finaltax from '@/components/Finaltax.vue'

export default {
  components: {
    Finaltax,
  },
  props: {
    rhktpvywns: Number,
    tprkador: Number,
  },
  computed: {
    rufwjdtpdor(){
        return this.tkscnftpdpr - this.tprkador
    },
    tkscnftpdor() {
      if (this.rhktpvywns <= 1200) {
        return Math.round(this.rhktpvywns * 0.06)
      } else if (1200 < this.rhktpvywns <= 4600) {
        return Math.round(this.rhktpvywns * 0.15) - 108
      } else if (4600 < this.rhktpvywns <= 8800) {
        return Math.round(this.rhktpvywns * 0.24 - 522)
      } else if (8800 < this.rhktpvywns <= 15000) {
        return Math.round(this.rhktpvywns * 0.35 - 1490)
      } else if (15000 < this.rhktpvywns <= 30000) {
        return Math.round(this.rhktpvywns * 0.38 - 1940)
      } else if (30000 < this.rhktpvywns <= 50000) {
        return Math.round(this.rhktpvywns * 0.40 - 2540)
      } else if (50000 < this.rhktpvywns <= 100000) {
        return Math.round(this.rhktpvywns * 0.42 - 3540)
      } else {
        return Math.round(this.rhktpvywns * 0.45 - 6540)
      }
    }
  }
}
</script>

<style>

</style>