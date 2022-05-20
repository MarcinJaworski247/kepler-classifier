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
      :feature-importance="res.feature_importance"
      @classify="classifyData"
    />
  </div>
  <div class="d-flex justify-center" v-if="data.length">
    <div class="chart-section">
      <app-header text="Porównanie wyników" />
      <bar-chart :data="data" />
      <app-data-grid
        :rows="data"
        :columns="resultColumns"
        export-file-name="models_comparision"
        class="ml-1"
      />
    </div>
  </div>
  <result-modal
    :method="method"
    :visible="modalVisible"
    :data="classificationRes"
    @close="onModalClose"
  />
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
import ResultModal from "@/components/Classification/ResultModal.vue";

let data = ref([]);

async function classify(_params) {
  api.getClassificationResult(_params).then((res) => {
    console.log(res.data);
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

let classificationRes = ref([]);
let method = ref("");
let modalVisible = ref(false);

function classifyData(_method) {
  method.value = _method;
  modalVisible.value = true;

  api.classifyData(_method).then((res) => {
    classificationRes.value = res.data;
    classificationRes.value.forEach((el) => {
      el.RESULT = el.RESULT === 1 ? "Jest exoplanetą" : "Nie jest exoplanetą";
    });
  });
}

function onModalClose() {
  modalVisible.value = false;
}
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
