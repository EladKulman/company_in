import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CompanyView from "../views/CompanyView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  { path: '/:companyName',
   component: CompanyView }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
