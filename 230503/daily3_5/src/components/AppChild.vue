<template>
  <div>
    <h3>AppChild 컴포넌트</h3>
    <p>App 컴포넌트에서 입력한 숫자: {{ childNumber }}</p>
  </div>
</template>

<script>
export default {
  props: {
    childNumber: Number,
  },
};
</script>

<style>

</style>