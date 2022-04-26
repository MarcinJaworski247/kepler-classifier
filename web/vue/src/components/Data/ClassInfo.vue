<template>
  <div class="info-tile">
    <app-header text="Zmienna decyzyjna" />
    <div class="info-tile__item">
      <span class="info-tile__item__label">
        Ilość rekordów o klasie "CANDIDATE": {{ classInfo.candidates }}
      </span>
    </div>
    <div class="info-tile__item">
      <span class="info-tile__item__label">
        Ilość rekordów o klasie "FALSE POSITIVE":
        {{ classInfo.false_positives }}
      </span>
    </div>
    <div>
      <class-pie-chart
        :candidates="classInfo.candidates"
        :false-positives="classInfo.false_positives"
      />
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import AppHeader from "@/components/App/AppHeader.vue";
import ClassPieChart from "@/components/Data/ClassPieChart.vue";
import api from "@/api";
let classInfo = ref({});
api.getClassInfo().then((res) => {
  classInfo.value = res.data;
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
