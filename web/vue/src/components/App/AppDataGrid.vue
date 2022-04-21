<template>
  <div :style="`height: ${height}px`">
    <div v-if="export" class="d-flex flex-end mb-1">
      <span
        class="material-icons-outlined icon mr-1"
        title="Eksportuj do CSV"
        @click="exportData"
      >
        file_download
      </span>
    </div>
    <v-grid
      theme="material"
      :source="rowsRef"
      :columns="columnsRef"
      :resize="true"
      :exporting="true"
      ref="vGridRef"
    />
  </div>
</template>

<script setup>
import { toRef, ref } from "vue";
import VGrid from "@revolist/vue3-datagrid";

const props = defineProps({
  rows: {
    type: Array,
    required: false,
    default: [],
  },
  columns: {
    type: Array,
    required: false,
    default: [],
  },
  height: {
    type: Number,
    required: false,
    default: 300,
  },
  export: {
    type: Boolean,
    required: false,
    default: true,
  },
});

const rowsRef = toRef(props, "rows");
const columnsRef = toRef(props, "columns");
const vGridRef = ref(null);

function exportData() {
  const grid = vGridRef.value.$el;
  grid.getPlugins().then((plugins) => {
    plugins.forEach((p) => {
      if (p.exportFile) {
        const exportPlugin = p;
        exportPlugin.exportFile({ filename: "keppler-classification" });
      }
    });
  });
}
</script>
<style lang="scss" scoped>
.icon {
  cursor: pointer;
}
</style>
