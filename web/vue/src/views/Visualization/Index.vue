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
import BoxPlotsWrapper from "@/components/Classification/BoxPlotsWrapper.vue";
import HeatMapWrapper from "@/components/Classification/HeatMapWrapper.vue";
import HistogramsWrapper from "@/components/Classification/HistogramsWrapper.vue";
import ScatterPlotsWrapper from "@/components/Classification/ScatterPlotsWrapper.vue";
</script>
