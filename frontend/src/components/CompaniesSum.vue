<template>
  <div>
    <v-card style="width: 30%; margin: auto">
      <v-card-title>Add new company</v-card-title>
      <br /><br />
      <v-card-text>
        <v-form>
          <v-row align="center" class="mx-0">
            <v-col
              ><v-text-field
                v-model="formDomain"
                label="Company Domain"
              ></v-text-field
            ></v-col>
            <v-spacer />
            <v-btn :loading="fromIsPending" @click="onSubmit" color="success"
              >Add</v-btn
            >
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
    <v-card style="width: 70%; margin: 100px auto auto auto">
      <v-card-title>Companies Summary</v-card-title>
      <br /><br />
      <v-card-text>
        <v-row align="center" class="mx-0">
          <v-col></v-col>
          <v-col></v-col>
          <v-col style="color: black; font-weight: bold">Company Type</v-col>
        </v-row>
        <v-row
          v-for="(company, index) in companies"
          :key="index"
          align="center"
          class="mx-0"
        >
          <v-col
            ><v-img
              @click="onCompanyClick(company.name)"
              alt=""
              class="shrink mr-2"
              contain
              :src="company.logo"
              transition="scale-transition"
              width="60"
          /></v-col>
          <v-col style="color: black; font-weight: bold">{{
            company.name
          }}</v-col>
          <v-col>{{ company.type }}</v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CompaniesSum",
  components: {},
  mounted() {
    console.log("CompaniesSum mounted ");
    let url = this.apiUrl + "/company/summary/all";
    axios
      .get(url)
      .then((response) => {
        this.companies = response.data;
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
  data() {
    return {
      companies: [],
      formDomain: "",
      fromIsPending: false,
    };
  },
  methods: {
    onCompanyClick(companyName) {
      this.$router.push({ path: "/" + companyName });
    },
    onSubmit() {
      let url = this.apiUrl + "/company";
      this.fromIsPending = true;
      axios
        .post(url, { domain: this.formDomain })
        .then((response) => {
          this.companies.push(response.data);
          // this.formDomain = ''
          this.$store.dispatch("snackbar/setSnackbar", {
            color: "success",
            text: `חברה נוספה בהצלחה`,
          });
        })
        .catch(() => {
          this.$store.dispatch("snackbar/setSnackbar", {
            color: "red",
            text: `אירעה שגיאה`,
          });
        })
        .finally(() => {
          this.fromIsPending = false;
        });
    },
  },
};
</script>

<style></style>
