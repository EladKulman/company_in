<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/antwjlzjqrmt8h4riew4"
          transition="scale-transition"
          width="60"
        />

        <!-- <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        /> -->
      </div>
        <v-tabs style="margin-left:50px">
           <v-tab to="/"><div>Home</div></v-tab>
        </v-tabs>
      <!-- <div id="nav">
        <router-link to="/"><span style="color:white">aaaa</span></router-link>
        <router-link to="/about">About</router-link>
      </div> -->

      <!-- <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn> -->
    </v-app-bar>

    <v-main>
      <router-view />
      <snackbar />
    </v-main>
  </v-app>
</template>

<script>
import snackbar from "./components/snackbar";
export default {
  name: 'App',
  components: { snackbar },
  data: () => ({
    //
  }),
};
</script>
