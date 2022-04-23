<template>
  <heat-map v-if="pearsonCorrData.length" :data="pearsonCorrData" />
  <app-loader v-else />
</template>
<script setup>
// vue
import { ref } from "vue";
// components
import HeatMap from "@/components/Plots/HeatMap.vue";
import AppLoader from "@/components/App/AppLoader.vue";
// api service
import api from "@/api";

let pearsonCorrData = ref([]);
api.getPearsonCorr().then((res) => {
  pearsonCorrData.value = res.data;
});
</script>
