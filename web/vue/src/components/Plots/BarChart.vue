<template>
  <apexchart
    type="bar"
    :series="series"
    :options="chartOptions"
    :height="250"
  />
</template>
<script setup>
import { toRef, ref } from "vue";
const props = defineProps({
  data: {
    type: Array,
    required: false,
    default: [],
  },
});

const chartData = toRef(props, "data");
const series = ref([]);
const methods = ref([]);
const chartOptions = ref({});

chartData.value.forEach((el) => {
  methods.value.push(el.method);
});

const accuracy = [];
chartData.value.forEach((el) => {
  accuracy.push(el.accuracy);
});

const balanced_accuracy = [];
chartData.value.forEach((el) => {
  balanced_accuracy.push(el.balanced_accuracy);
});

series.value.push({
  name: "Accuracy",
  data: accuracy,
});

series.value.push({
  name: "Balanced accuracy",
  data: balanced_accuracy,
});

chartOptions.value = {
  chart: {
    type: "bar",
    height: 350,
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: "55%",
      endingShape: "rounded",
    },
  },
  dataLabels: {
    enabled: true,
  },
  stroke: {
    show: true,
    width: 2,
    colors: ["transparent"],
  },
  xaxis: {
    categories: methods.value,
  },
  yaxis: {
    max: 1,
    tick: 0.1,
  },
};
</script>
