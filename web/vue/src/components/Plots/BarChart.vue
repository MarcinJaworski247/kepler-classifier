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

const brier_score_loss = [];
chartData.value.forEach((el) => {
  brier_score_loss.push(el.brier_score_loss);
});

const f1_score = [];
chartData.value.forEach((el) => {
  f1_score.push(el.f1_score);
});

series.value.push({
  name: "Accuracy",
  data: accuracy,
});

series.value.push({
  name: "Balanced accuracy",
  data: balanced_accuracy,
});

series.value.push({
  name: "Brier score loss",
  data: brier_score_loss,
});

series.value.push({
  name: "F1 score",
  data: f1_score,
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
