<template>
  <div>data</div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "@/api";

let data = ref(null);

onMounted(async () => {
  data = await api.getData();
});
</script>
