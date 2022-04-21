<template>
  <div class="header">{{ text }}</div>
</template>

<script setup>
const props = defineProps({
  text: {
    type: String,
    required: false,
    default: "",
  },
});
</script>

<style lang="scss" scoped>
.header {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 2 * $space-size;
}
</style>
