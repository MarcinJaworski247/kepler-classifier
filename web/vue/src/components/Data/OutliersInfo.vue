<template>
  <div class="info-tile">
    <app-header text="Punkty oddalone" />
    <div class="info-tile__item">
      <span class="info-tile__item__label">
        Ilość punktów oddalonych: {{ outliers.count }}
      </span>
    </div>
    <div class="info-tile__item">
      <span class="info-tile__item__label">
        Procent punktów oddalonych: {{ outliers.percentage }}%
      </span>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import AppHeader from "@/components/App/AppHeader.vue";
import api from "@/api";

let outliers = ref({});

api.getOutliers().then((res) => {
  outliers.value = res.data;
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
