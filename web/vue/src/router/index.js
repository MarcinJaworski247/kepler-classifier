import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: "/data",
  },
  {
    path: "/data",
    name: "data",
    component: () => import("../views/Data/Index.vue"),
  },
  {
    path: "/statistics",
    name: "statistics",
    component: () => import("../views/Statistics/Index.vue"),
  },
  {
    path: "/visualization",
    name: "visualization",
    component: () => import("../views/Visualization/Index.vue"),
  },
  {
    path: "/classification",
    name: "classification",
    component: () => import("../views/Classification/Index.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
