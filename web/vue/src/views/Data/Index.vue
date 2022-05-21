<template>
  <div v-if="data.length" class="d-flex justify-center">
    <data-grid
      theme="compact"
      export-file-name="kepler_prepared_data"
      :rows="data"
      :columns="columns"
      :height="600"
      style="width: 80%"
    />
  </div>
  <div v-else>
    <app-loader />
  </div>
  <div class="d-flex justify-center mt-5 mb-2">
    <outliers-info />
  </div>
  <div class="d-flex justify-center mb-2">
    <empty-cells-info />
  </div>
  <div class="d-flex justify-center">
    <class-info />
  </div>
</template>

<script setup>
// vue
import { reactive, ref } from "vue";
// components
import DataGrid from "../../components/App/AppDataGrid.vue";
import AppLoader from "@/components/App/AppLoader.vue";
import OutliersInfo from "@/components/Data/OutliersInfo.vue";
import ClassInfo from "@/components/Data/ClassInfo.vue";
import EmptyCellsInfo from "@/components/Data/EmptyCellsInfo.vue";
// api service
import api from "@/api";

let data = ref([]);

const columns = reactive([
  {
    prop: "kepid",
    name: "kepid",
  },
  {
    prop: "kepoi_name",
    name: "kepoi_name",
  },
  {
    prop: "kepler_name",
    name: "kepler_name",
    size: 180,
  },
  {
    prop: "koi_disposition",
    name: "koi_disposition",
    size: 180,
  },
  {
    prop: "koi_fpflag_nt",
    name: "koi_fpflag_nt",
  },
  {
    prop: "koi_fpflag_ss",
    name: "koi_fpflag_ss",
  },
  {
    prop: "koi_fpflag_co",
    name: "koi_fpflag_co",
  },
  {
    prop: "koi_fpflag_ec",
    name: "koi_fpflag_ec",
  },
  {
    prop: "koi_period",
    name: "koi_period",
  },
  {
    prop: "koi_time0bk",
    name: "koi_time0bk",
  },
  {
    prop: "koi_impact",
    name: "koi_impact",
  },
  {
    prop: "koi_duration",
    name: "koi_duration",
  },
  {
    prop: "koi_depth",
    name: "koi_depth",
  },
  {
    prop: "koi_prad",
    name: "koi_prad",
  },
  {
    prop: "koi_teq",
    name: "koi_teq",
  },
  {
    prop: "koi_insol",
    name: "koi_insol",
  },
  {
    prop: "koi_model_snr",
    name: "koi_model_snr",
  },
  {
    prop: "koi_steff",
    name: "koi_steff",
  },
  {
    prop: "koi_slogg",
    name: "koi_slogg",
  },
  {
    prop: "koi_srad",
    name: "koi_srad",
  },
  {
    prop: "ra",
    name: "ra",
  },
  {
    prop: "dec",
    name: "dec",
  },
  {
    prop: "koi_kepmag",
    name: "koi_kepmag",
  },
]);

api.getData().then((res) => {
  data.value = res.data;
  data.value.forEach((el) => {
    el.koi_disposition =
      el.koi_disposition == 1 ? "CANDIDATE" : "FALSE POSITIVE";
  });
});
</script>
