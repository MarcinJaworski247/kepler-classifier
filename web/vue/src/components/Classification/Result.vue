<template>
  <div class="result-tile">
    <app-header :text="title" />
    <div class="result-tile__item">
      <span class="result-tile__item__label">
        Accuracy: {{ accuracy * 100 }}%
      </span>
    </div>
    <div class="result-tile__item">
      <span class="result-tile__item__label">
        Balanced accuracy:
        {{ balancedAccuracy * 100 }}%
      </span>
    </div>
  </div>
</template>
<script setup>
import { toRef } from "vue";
import AppHeader from "../App/AppHeader.vue";

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
});

const title = toRef(props, "title");
const accuracy = toRef(props, "accuracy");
const balancedAccuracy = toRef(props, "balancedAccuracy");
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
</style>
