<template>
  <select v-model="selectedOption" class="custom-input">
    <option v-for="(opt, idx) in options" :key="idx">{{ opt }}</option>
  </select>
  <box-plot :name="data.name" :data="data.data" />
</template>

<script setup>
// vue
import { ref, watch } from "vue";
// components
import BoxPlot from "@/components/Plots/BoxPlot.vue";
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
let selectedOption = ref("koi_kepmag");
let data = ref([]);

watch(selectedOption, (newVal) => {
  api.getValues(selectedOption.value).then((res) => {
    data.value = res.data;
  });
});

api.getValues(selectedOption.value).then((res) => {
  data.value = res.data;
});
</script>
