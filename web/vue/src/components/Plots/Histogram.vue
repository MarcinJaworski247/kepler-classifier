<template>
  <app-header v-if="title" :text="title" />
  <div id="histogram"></div>
</template>

<script setup>
import { toRef, watch } from "vue";
import AppHeader from "@/components/App/AppHeader.vue";
import Plotly from "plotly.js-dist-min";

const props = defineProps({
  data: {
    type: Array,
    required: false,
    default: [],
  },
  name: {
    type: String,
    required: false,
    default: "",
  },
  title: {
    type: String,
    required: false,
    default: "",
  },
});

const data = toRef(props, "data");
const name = toRef(props, "name");

watch(
  () => [...data.value],
  (newVal) => {
    if (newVal) {
      renderHistogram(newVal);
    }
  },
  {
    deep: true,
  }
);

function renderHistogram(data) {
  Plotly.newPlot("histogram", [
    {
      x: data,
      type: "histogram",
      histnorm: "probability",
      name: name.value,
    },
  ]);
}
</script>
