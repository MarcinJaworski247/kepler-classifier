<template>
  <app-header v-if="title" :text="title" />
  <div id="boxplot"></div>
</template>

<script setup>
import { toRef, watch, ref, onBeforeMount, onMounted } from "vue";
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
      renderBoxPlot(newVal);
    }
  },
  {
    deep: true,
  }
);

function renderBoxPlot(data) {
  console.log("render");
  Plotly.newPlot("boxplot", [
    {
      y: data,
      type: "box",
      name: name.value,
    },
  ]);
}
</script>
