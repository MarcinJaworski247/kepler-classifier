<template>
  <div id="app">
    <the-top-bar />
    <div class="px-4 py-4 main-content">
      <router-view />
    </div>
  </div>
</template>
<script setup>
import TheTopBar from "@/components/Layout/TheTopBar.vue";
import "./assets/styles/main.scss";
</script>
<style lang="scss" scoped>
.main-content {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 3 * $space-size;
  margin-bottom: $space-size;
  padding: 2 * $space-size;
  background: $white;
  min-height: 300px;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  margin-top: 80px;
}
</style>
