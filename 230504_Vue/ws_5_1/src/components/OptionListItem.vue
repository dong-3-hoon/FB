<template>
  <div
    class="menu-item d-flex justify-content-bw"
    :class="{ selected: option.selected }"
    @click="selectOption"
  >
    <p>{{ option.type }}</p>
    <button class="size-item d-flex align-items-center justify-content-center" @click="increase">+</button>
    <p>{{ option.count }}회</p>
    <button class="size-item d-flex align-items-center justify-content-center" @click="decrease">-</button>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$emit('increase', this.option);
    },
    decrease() {
      this.$emit('decrease', this.option);
    },
    selectOption() {
      this.$emit('selectOption', this.option);
    },
  }
}
</script>

<style>
</style>