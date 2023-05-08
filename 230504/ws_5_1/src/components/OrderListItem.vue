<template>
  <li class="d-flex justify-content-bw order-item">
    <div class="d-flex">
      <img class="menu-img" :src="order.menu.image" alt="" />
      <div class="d-flex flex-column">
        <p>{{ order.menu.title }}</p>
        <p>사이즈: {{ order.size.name }}</p>
        <p>옵션</p>
        <p v-for="option in optionList" :key="option.type" :option="option">{{option.type}}: {{option.count}}</p>
      </div>
    </div>
    <div>가격: {{ totalPrice }}원</div>
  </li>
</template>

<script>
export default {
  name: "OrderListItem",
  props: {
    order: Object,
    stk: Number,
  },
  computed: {
    optionList() {
      return this.$store.state.optionList;
    },
    totalPrice() {
      let stk = 0
      for(const option of this.optionList){
        stk = stk + option.count * option.price
      }
      return this.order.menu.price + this.order.size.price + stk;
    },
  },
};
</script>

<style>
.order-item {
  padding: 10px;
}

.flex-column {
  flex-direction: column;
}
</style>