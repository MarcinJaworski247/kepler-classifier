<template>
  <div v-show="visible" class="modal__backdrop">
    <div class="modal">
      <header class="modal__header">
        <span class="modal__header--title">
          Wyniki klasyfikacji przy użyciu {{ method }}
        </span>
        <span
          class="material-icons-outlined modal__button--close"
          @click="close"
        >
          close
        </span>
      </header>
      <div class="modal__body">
        <div v-if="data.length" class="d-flex justify-center">
          <data-grid
            theme="compact"
            :export-file-name="`classification_res_${method}`"
            :rows="data"
            :columns="columns"
            :height="600"
            style="width: 90%"
          />
        </div>
        <div v-else>
          <app-loader />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// vue
import { reactive, ref } from "vue";

// components
import DataGrid from "../../components/App/AppDataGrid.vue";
import AppLoader from "@/components/App/AppLoader.vue";

const emit = defineEmits(["close"]);

function close() {
  emit("close");
}

const props = defineProps({
  visible: {
    type: Boolean,
    required: false,
    default: false,
  },
  method: {
    type: String,
    required: false,
    default: "",
  },
  data: {
    type: Array,
    required: false,
    default: () => [],
  },
});

const columns = reactive([
  {
    prop: "RESULT",
    name: "Wynik",
    size: 200,
  },
  {
    prop: "kepoi_name",
    name: "kepoi_name",
  },
  {
    prop: "kepler_name",
    name: "kepler_name",
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
</script>

<style lang="scss" scoped>
.modal {
  background: #fff;
  box-shadow: 1px 1px 20px 1px;
  border-radius: 4px;
  overflow-x: auto;
  width: 80%;

  &__backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  &__header {
    padding: $space-size 2 * $space-size;
    display: flex;
    border-bottom: 1px solid $light-grey;
    justify-content: space-between;
    align-items: center;
    height: 48px;

    &--title {
      font-size: 1.5rem;
    }
  }

  &__body {
    padding: 6 * $space-size 1 * $space-size;
  }

  &__button {
    &--close {
      cursor: pointer;
      color: $green;
    }
  }
}
</style>
