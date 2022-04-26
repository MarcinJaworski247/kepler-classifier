<template>
  <apexchart type="pie" width="400" :options="options" :series="series" />
</template>
<script setup>
import { toRef, reactive, computed } from "vue";

const props = defineProps({
  candidates: {
    type: Number,
    required: false,
    default: 50,
  },
  falsePositives: {
    type: Number,
    required: false,
    default: 50,
  },
});

let candidates = toRef(props, "candidates");
let falsePositives = toRef(props, "falsePositives");
let series = computed(() => {
  return [candidates.value, falsePositives.value];
});

const options = reactive({
  labels: ["CANDIDATE", "FALSE POSITIVE"],
});
</script>
