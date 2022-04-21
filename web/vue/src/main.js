import { createApp } from "vue";
import App from "./App.vue";

// icons
import "material-icons/iconfont/material-icons.css";

const app = createApp(App);

import VueApexCharts from "vue3-apexcharts";
app.use(VueApexCharts);

// router
import router from "./router";
app.use(router);

app.mount("#app");
