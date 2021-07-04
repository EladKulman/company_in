import Vue from "vue";
import Vuex from "vuex";
import snackbar from "./modules/snackbar";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiUrl: "http://localhost:8888",
  },
  mutations: {},
  actions: {},
  modules: { snackbar },
});
