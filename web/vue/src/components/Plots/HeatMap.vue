<template>
  <apexchart :height="550" :options="options" :series="dataRef" />
</template>

<script setup>
import { toRef, reactive } from "vue";

const props = defineProps({
  data: {
    type: Array,
    required: false,
    default: [],
  },
});

const options = reactive({
  chart: {
    type: "heatmap",
  },
  colors: ["#008FFB"],
});

const dataRef = toRef(props, "data");
</script>
