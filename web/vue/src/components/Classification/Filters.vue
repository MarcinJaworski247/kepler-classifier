<template>
  <div class="filters">
    <app-header text="Konfiguracja" />
    <div class="filters__item">
      <div class="d-flex flex-column">
        <label class="filters__item__header">Procent danych testowych</label>
        <input
          type="number"
          max="100"
          min="20"
          v-model="filters.testDataPercentage"
          class="custom-input"
        />
      </div>
      <pie-chart
        :test-data-percentage="filters.testDataPercentage"
        :train-data-percentage="trainDataPercentage"
      />
    </div>
    <div class="filters__item">
      <div class="d-flex flex-column">
        <label class="filters__item__header">Walidacja krosowa</label>
        <Toggle v-model="filters.isCrossValidation" class="toggle-purple" />
        <template v-if="filters.isCrossValidation">
          <label class="mt-1">Ilość foldów</label>
          <input
            type="number"
            min="2"
            max="50"
            v-model="filters.foldsCount"
            class="custom-input"
          />
        </template>
      </div>
    </div>
    <div class="filters__item">
      <div class="d-flex flex-column">
        <label class="filters__item__header">Ilość drzew w lesie losowym</label>
        <input
          type="number"
          min="2"
          max="50"
          v-model="filters.treesCount"
          class="custom-input"
        />
      </div>
    </div>
    <div class="filters__item">
      <div class="d-flex flex-column">
        <label class="filters__item__header"
          >Ilość sąsiadów w algorytmie KNN</label
        >
        <input
          type="number"
          min="2"
          max="50"
          v-model="filters.neighboursCount"
          class="custom-input"
        />
      </div>
    </div>
    <div class="filters__item">
      <div class="d-flex flex-column">
        <label class="filters__item__header"
          >Algorytm użyty do obliczania odległości w algorytmie KNN</label
        >
        <select v-model="filters.knnDistanceAlgorithm" class="custom-input">
          <option v-for="(opt, idx) in knnAlgorithms" :key="idx">
            {{ opt }}
          </option>
        </select>
      </div>
    </div>
    <div class="filters__item">
      <div class="d-flex flex-column">
        <label class="filters__item__header">Kernel algorytmu SVC</label>
        <select v-model="filters.svcKernel" class="custom-input">
          <option v-for="(opt, idx) in svcKernels" :key="idx">
            {{ opt }}
          </option>
        </select>
      </div>
    </div>
    <div class="mt-2">
      <button class="custom-button" @click="classify">Wygeneruj wyniki</button>
    </div>
  </div>
</template>

<script setup>
// vue
import { reactive, computed, ref } from "vue";
// components
import Toggle from "@vueform/toggle";
import PieChart from "@/components/Plots/PieChart.vue";
import AppHeader from "../App/AppHeader.vue";

const emits = defineEmits(["classify"]);

let filters = reactive({
  isCrossValidation: false,
  treesCount: 100,
  testDataPercentage: 50,
  foldsCount: 10,
  neighboursCount: 3,
  svcKernel: "rbf",
  knnDistanceAlgorithm: "auto",
});

const knnAlgorithms = ref(["auto", "ball_tree", "kd_tree", "brute"]);

const svcKernels = ref(["linear", "poly", "rbf", "sigmoid"]);

let trainDataPercentage = computed(() => {
  return 100 - filters.testDataPercentage;
});

function classify() {
  emits("classify", filters);
}
</script>
<style src="@vueform/toggle/themes/default.css"></style>
<style lang="scss" scoped>
.filters {
  width: 80%;
  border: 1px solid $dark-font;
  padding: $space-size;

  &__header {
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 2 * $space-size;
  }

  &__item {
    margin-bottom: 2 * $space-size;

    &__header {
      margin-bottom: $space-size;
      border-left: 3px solid $purple;
      padding-left: $space-size;
    }
  }
}

.toggle-purple {
  --toggle-bg-on: #a438fc;
  --toggle-border-on: #a438fc;
}
</style>
