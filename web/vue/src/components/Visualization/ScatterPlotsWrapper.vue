<template>
  <label class="mr-1">Atrybut 1</label>
  <select v-model="firstOption">
    <option v-for="(opt, idx) in options" :key="idx">{{ opt }}</option>
  </select>
  <label class="ml-2 mr-1">Atrybut 2</label>
  <select v-model="secondOption">
    <option v-for="(opt, idx) in options" :key="idx">{{ opt }}</option>
  </select>
  <scatter-plot
    :first-name="firstData.name"
    :second-name="secondData.name"
    :first-data="firstData.data"
    :second-data="secondData.data"
    :predict-data="predictData"
  />
</template>

<script setup>
// vue
import { ref, watch, onMounted } from "vue";
// components
import ScatterPlot from "@/components/Plots/ScatterPlot.vue";
// api service
import api from "@/api";

const options = ref([
  "koi_fpflag_nt",
  "koi_fpflag_ss",
  "koi_fpflag_co",
  "koi_fpflag_ec",
  "koi_period",
  "koi_time0bk",
  "koi_impact",
  "koi_duration",
  "koi_depth",
  "koi_prad",
  "koi_teq",
  "koi_insol",
  "koi_model_snr",
  "koi_steff",
  "koi_slogg",
  "koi_srad",
  "ra",
  "dec",
  "koi_kepmag",
]);
let firstOption = ref("koi_kepmag");
let secondOption = ref("koi_depth");
let firstData = ref([]);
let secondData = ref([]);
let predictData = ref([]);

watch(firstOption, (newVal) => {
  getData();
});
watch(secondOption, (newVal) => {
  getData();
});

function getData() {
  api.getValues(firstOption.value).then((res) => {
    firstData.value = res.data;
  });
  api.getValues(secondOption.value).then((res) => {
    secondData.value = res.data;
  });
  api
    .getSimpleLinearRegression(firstOption.value, secondOption.value)
    .then((res) => {
      predictData.value = res.data;
    });
}

onMounted(() => {
  getData();
});
</script>
