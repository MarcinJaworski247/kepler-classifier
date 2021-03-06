<template>
  <div class="result-tile">
    <app-header :text="title" />
    <div class="result-tile__item">
      <span class="result-tile__item__label"> Accuracy: {{ accuracy }} </span>
    </div>
    <div class="result-tile__item">
      <span class="result-tile__item__label">
        Balanced accuracy:
        {{ balancedAccuracy }}
      </span>
    </div>
    <div class="result-tile__item">
      <span class="result-tile__item__label">
        Brier score loss:
        {{ brierScoreLoss }}
      </span>
    </div>
    <div class="result-tile__item">
      <span class="result-tile__item__label">
        F1 score:
        {{ f1Score }}
      </span>
    </div>
    <div class="result-tile__item">
      <span class="result-tile__item__label">
        Najistotniejsze atrybuty:
        <template v-if="featureImp.length">
          <div v-for="(item, index) in featureImp" class="mt-1">
            {{ item.name }} - {{ item.value }}
          </div>
        </template>
        <template v-else>-</template>
      </span>
    </div>
    <button @click="classifyData" class="custom-button mt-2">
      Użyj modelu do klasyfikacji
    </button>
  </div>
</template>
<script setup>
import { toRef } from "vue";
import AppHeader from "../App/AppHeader.vue";
// api service
import api from "@/api";

const emits = defineEmits(["classify"]);

const props = defineProps({
  title: {
    type: String,
    required: false,
    default: "",
  },
  accuracy: {
    type: Number,
    required: false,
    default: 0,
  },
  balancedAccuracy: {
    type: Number,
    required: false,
    default: 0,
  },
  brierScoreLoss: {
    type: Number,
    required: false,
    default: 0,
  },
  f1Score: {
    type: Number,
    required: false,
    default: 0,
  },
  featureImportance: {
    type: Array,
    required: false,
    default: () => [],
  },
});

const title = toRef(props, "title");
const accuracy = toRef(props, "accuracy");
const balancedAccuracy = toRef(props, "balancedAccuracy");
const brierScoreLoss = toRef(props, "brierScoreLoss");
const f1Score = toRef(props, "f1Score");
const featureImp = toRef(props, "featureImportance");

function classifyData() {
  emits("classify", title.value);
}
</script>
<style lang="scss" scoped>
.result-tile {
  width: 80%;
  border: 1px solid $dark-font;
  padding: $space-size;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;

  &__header {
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 16px;
  }

  &__item {
    margin-bottom: 8px;

    &__label {
      border-left: 3px solid $purple;
      padding-left: $space-size;
    }
  }
}

.button {
  background: $purple;
  border-radius: 5px;
  border-style: none;
  outline: none;
  padding: $space-size $space-size;
  cursor: pointer;
  color: $white;
  &:hover {
    background-color: $light-purple;
  }
  &:focus {
    background-color: $light-purple;
  }
}
</style>
