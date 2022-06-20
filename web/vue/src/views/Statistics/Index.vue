<template>
  <div class="d-flex justify-center">
    <app-data-grid
      v-if="data.length"
      theme="compact"
      export-file-name="description_stats"
      :rows="data"
      :columns="columns"
      :height="600"
      class="mb-4"
    />
    <app-loader v-else />
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import AppDataGrid from "../../components/App/AppDataGrid.vue";
import AppLoader from "@/components/App/AppLoader.vue";
import api from "@/api";

let data = ref([]);

const columns = reactive([
  {
    prop: "_attribute",
    name: "Atrybut",
    size: 150,
  },
  {
    prop: "_min",
    name: "Minimum",
  },
  {
    prop: "_max",
    name: "Maximum",
  },
  {
    prop: "_avg",
    name: "Średnia",
  },
  {
    prop: "_stdv",
    name: "Odchylenie standardowe",
    size: 220,
  },
  {
    prop: "_median",
    name: "Mediana",
  },
  {
    prop: "_iqr",
    name: "IQR",
  },
  {
    prop: "_q1",
    name: "Q1",
  },
  {
    prop: "_q3",
    name: "Q3",
  },
]);

api.getStatistics().then((res) => {
  data.value = res.data;
});
</script>
