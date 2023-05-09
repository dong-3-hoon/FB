<template>
  <div class="option-list">
    <h1>3. 옵션을 고르세요.</h1>
      <OptionListItem
      v-for="option in optionList"
      :key="option.type"
      :option="option"
      @increase="increase"
      @decrease="decrease"
      ></OptionListItem>
  </div>
</template>

<script>
import OptionListItem from "@/components/OptionListItem";
export default {
  name: 'OptionList',
  components: {
    OptionListItem
  },
  computed: {
    optionList: function () {
      return this.$store.state.optionList
    },
  },
  methods: {
    increase: function (option) {
      option.count++;
    },
    decrease: function (option) {
      option.count = Math.max(option.count - 1, 0);
    },
  },
}
</script>

<style>
.option-list {
  padding: 20px;
  background-color: white;
  border-radius: 10px;
}
</style>