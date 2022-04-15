<template>
  <div class="bar__wrapper">
    <div class="bar d-flex space-between align-center">
      <router-link
        :to="{ name: 'data' }"
        class="bar__item"
        :class="{ 'bar__item--active': routeActive('data') }"
      >
        Dane
      </router-link>
      <router-link
        :to="{ name: 'statistics' }"
        class="bar__item"
        :class="{ 'bar__item--active': routeActive('statistics') }"
      >
        Statystyki opisowe</router-link
      >
      <router-link
        :to="{ name: 'visualization' }"
        class="bar__item"
        :class="{ 'bar__item--active': routeActive('visualization') }"
      >
        Wizualizacja danych
      </router-link>
      <router-link
        :to="{ name: 'classification' }"
        class="bar__item"
        :class="{ 'bar__item--active': routeActive('classification') }"
      >
        Klasyfikacja
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
const route = useRoute();

function routeActive(param) {
  return param === route.name;
}
</script>

<style lang="scss" scoped>
.bar {
  width: 100%;
  height: 80px;

  &__wrapper {
    padding-left: 4 * $space-size;
    padding-right: 4 * $space-size;
    background: $purple;
  }

  &__item {
    letter-spacing: 2px;
    font-size: 1.2rem;
    text-decoration: none;
    color: $white;

    &:active {
      color: $white;
      border-bottom: 1px solid $white;
    }

    &:hover {
      border-bottom: 1px solid $white;
    }

    &--active {
      border-bottom: 1px solid $white;
    }
  }
}
</style>
