<template>
  <div class="d-flex justify-center">
    <app-data-grid
      v-if="data.length"
      theme="compact"
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
  },
  {
    prop: "_min",
    name: "min",
  },
  {
    prop: "_max",
    name: "max",
  },
  {
    prop: "_avg",
    name: "avg",
  },
  {
    prop: "_stdv",
    name: "stdv",
  },
  {
    prop: "_median",
    name: "mediana",
  },
  {
    prop: "_iqr",
    name: "iqr",
  },
  {
    prop: "_q1",
    name: "q1",
  },
  {
    prop: "_q3",
    name: "q3",
  },
]);

api.getStatistics().then((res) => {
  data.value = res.data;
});
</script>
