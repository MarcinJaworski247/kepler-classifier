<template>
  <app-header text="Współczynniki korelacji Pearsona" />
  <heat-map-wrapper />
  <app-header text="Wykresy pudełkowe" />
  <box-plots-wrapper />
  <app-header text="Histogramy wartości" />
  <histograms-wrapper />
  <app-header text="Prosta regresja liniowa" />
  <scatter-plots-wrapper />
</template>

<script setup>
import AppHeader from "@/components/App/AppHeader.vue";
import BoxPlotsWrapper from "@/components/Visualization/BoxPlotsWrapper.vue";
import HeatMapWrapper from "@/components/Visualization/HeatMapWrapper.vue";
import HistogramsWrapper from "@/components/Visualization/HistogramsWrapper.vue";
import ScatterPlotsWrapper from "@/components/Visualization/ScatterPlotsWrapper.vue";
</script>
