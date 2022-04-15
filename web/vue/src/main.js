import { createApp } from "vue";
import App from "./App.vue";

// icons
import "material-icons/iconfont/material-icons.css";

const app = createApp(App);

// router
import router from "./router";
app.use(router);

app.mount("#app");
