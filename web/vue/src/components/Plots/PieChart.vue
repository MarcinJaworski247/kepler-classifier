<template>
  <apexchart type="pie" width="300" :options="options" :series="series" />
</template>
<script setup>
import { toRef, reactive, computed } from "vue";

const props = defineProps({
  testDataPercentage: {
    type: Number,
    required: false,
    default: 50,
  },
  trainDataPercentage: {
    type: Number,
    required: false,
    default: 50,
  },
});

let testData = toRef(props, "testDataPercentage");
let trainData = toRef(props, "trainDataPercentage");
let series = computed(() => {
  return [testData.value, trainData.value];
});

const options = reactive({
  labels: ["Dane testowe", "Dane uczące"],
});
</script>
