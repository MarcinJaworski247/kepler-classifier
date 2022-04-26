<template>
  <div class="d-flex justify-center mb-3">
    <filters @classify="classify" />
  </div>
  <div
    v-if="data.length"
    v-for="(res, index) in data"
    :key="index"
    class="d-flex justify-center mb-3"
  >
    <result
      :title="res.method"
      :accuracy="res.accuracy"
      :balanced-accuracy="res.balanced_accuracy"
      :brier-score-loss="res.brier_score_loss"
      :f1-score="res.f1_score"
    />
  </div>
  <div class="d-flex justify-center" v-if="data.length">
    <div class="chart-section">
      <app-header text="Porównanie wyników" />
      <bar-chart :data="data" />
      <app-data-grid :rows="data" :columns="resultColumns" class="ml-1" />
    </div>
  </div>
</template>

<script setup>
// vue
import { ref } from "vue";
// api service
import api from "@/api";
// components
import Result from "@/components/Classification/Result.vue";
import Filters from "@/components/Classification/Filters.vue";
import BarChart from "@/components/Plots/BarChart.vue";
import AppHeader from "@/components/App/AppHeader.vue";
import AppDataGrid from "@/components/App/AppDataGrid.vue";

let data = ref([]);

async function classify(_params) {
  api.getClassificationResult(_params).then((res) => {
    data.value = res.data;
  });
}

const resultColumns = ref([
  {
    prop: "method",
    name: "Atrybut",
    size: 200,
  },
  {
    prop: "accuracy",
    name: "Accuracy",
  },
  {
    prop: "balanced_accuracy",
    name: "Balanced accuracy",
    size: 200,
  },
  {
    prop: "brier_score_loss",
    name: "Brier score loss",
    size: 200,
  },
  {
    prop: "f1_score",
    name: "F1 score",
  },
]);
</script>
<style lang="scss" scoped>
.chart-section {
  width: 80%;
  border: 1px solid $dark-font;
  padding: $space-size;

  &__header {
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 2 * $space-size;
  }
}
</style>
