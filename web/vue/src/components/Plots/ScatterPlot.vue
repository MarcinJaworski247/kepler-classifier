<template>
  <app-header v-if="title" :text="title" />
  <div id="scatterPlot"></div>
</template>

<script setup>
import { toRef, watch } from "vue";
import AppHeader from "@/components/App/AppHeader.vue";
import Plotly from "plotly.js-dist-min";

const props = defineProps({
  firstData: {
    type: Array,
    required: false,
    default: [],
  },
  secondData: {
    type: Array,
    required: false,
    default: [],
  },
  firstName: {
    type: String,
    required: false,
    default: "",
  },
  secondName: {
    type: String,
    required: false,
    default: "",
  },
  predictData: {
    type: Array,
    required: false,
    default: [],
  },
  title: {
    type: String,
    required: false,
    default: "",
  },
});

const firstData = toRef(props, "firstData");
const secondData = toRef(props, "secondData");
const firstName = toRef(props, "firstName");
const secondName = toRef(props, "secondName");
const predictData = toRef(props, "predictData");

watch(
  () => [...firstData.value],
  (newVal) => {
    if (newVal) {
      renderScatterPlot();
    }
  },
  {
    deep: true,
  }
);
watch(
  () => [...secondData.value],
  (newVal) => {
    if (newVal) {
      renderScatterPlot();
    }
  },
  {
    deep: true,
  }
);
watch(
  () => [...predictData.value],
  (newVal) => {
    if (newVal) {
      renderScatterPlot();
    }
  },
  {
    deep: true,
  }
);

function renderScatterPlot() {
  Plotly.newPlot("scatterPlot", [
    {
      x: firstData.value,
      y: secondData.value,
      mode: "markers",
      type: "scatter",
      name: `x - ${firstName.value}, y - ${secondName.value}`,
    },
    {
      x: firstData.value,
      y: predictData.value,
      mode: "lines",
      type: "scatter",
      name: "Y predictions",
    },
  ]);
}
</script>
