<template>
  <apexchart :height="550" :options="options" :series="series" />
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

const series = toRef(props, "data");
</script>
