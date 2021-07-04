<template>
  <div>
    <v-card style="width: 30%; margin: auto">
      <v-card-title class="text-center">{{ companyName }}</v-card-title>
      <br /><br />
      <v-card-text>
        <v-row
          v-for="(value, key, index) in data"
          :key="index"
          align="center"
          class="mx-0"
        >
          <v-col>{{ key }}</v-col>
          <v-col v-if="key != 'logo'">{{ value }}</v-col>
          <v-col v-else>
            <v-img
              alt=""
              class="shrink mr-2"
              contain
              :src="value"
              transition="scale-transition"
              width="60"
            />
          </v-col>
        </v-row>
        <v-row
         >
          <v-col>Like</v-col>
          <v-col v-if="data.like == true"> <v-img
              alt=""
              class="shrink mr-2"
              contain
              src="data:image/png;base64,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"
              transition="scale-transition"
              width="60"
            /></v-col>
          <v-col v-else>
            <v-img
              alt=""
              class="shrink mr-2"
              contain
              src="https://toppng.com/uploads/preview/youtube-like-icon-116093838438u2joytndx.png"
              transition="scale-transition"
              width="60"
            />
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CompanyDetails",
  components: {},
  mounted() {
    console.log("CompanyDetails mounted ");
    let url = this.apiUrl + "/company/details/" + this.companyName;
    axios
      .get(url)
      .then((response) => {
        this.data = response.data;
      })
      .catch(() => {
        this.$store.dispatch("snackbar/setSnackbar", {
          color: "red",
          text: `אירעה שגיאה`,
        });
      });
  },
  computed: {
    apiUrl() {
      return this.$store.state.apiUrl;
    },
  },
  props: {
    companyName: {
      type: String,
      default: "",
    },
    data() {
      return {
        data: {},
      };
    },
    methods: {},
  },
};
</script>

<style></style>
