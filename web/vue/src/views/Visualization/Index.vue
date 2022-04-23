<template>
  <app-header text="Współczynniki korelacji Pearsona" />
  <heat-map-wrapper />
  <app-header text="Wykresy pudełkowe" />
  <box-plots-wrapper />
</template>

<script setup>
import AppHeader from "@/components/App/AppHeader.vue";
import BoxPlotsWrapper from "@/components/Classification/BoxPlotsWrapper.vue";
import HeatMapWrapper from "@/components/Classification/HeatMapWrapper.vue";
</script>
