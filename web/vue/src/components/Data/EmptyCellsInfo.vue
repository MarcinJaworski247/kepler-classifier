<template>
  <div class="info-tile">
    <app-header text="Puste wartości" />
    <div class="info-tile__item">
      <span class="info-tile__item__label">
        Ilość pustych wartości: {{ emptyCells.count }}
      </span>
    </div>
    <div class="info-tile__item">
      <span class="info-tile__item__label">
        Procent pustych wartości: {{ emptyCells.percentage }}%
      </span>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import AppHeader from "@/components/App/AppHeader.vue";
import api from "@/api";

let emptyCells = ref({});

api.getEmptyCells().then((res) => {
  emptyCells.value = res.data;
});
</script>
<style lang="scss" scoped>
.info-tile {
  width: 80%;
  border: 1px solid $dark-font;
  padding: $space-size;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;

  &__item {
    margin-bottom: 8px;

    &__label {
      border-left: 3px solid $purple;
      padding-left: $space-size;
    }
  }
}
</style>
