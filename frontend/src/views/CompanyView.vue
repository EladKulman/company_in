<template>
  <CompanyDetails :companyName="$route.params.companyName"/>
</template>

<script>
import CompanyDetails from "../components/CompanyDetails.vue";

export default {
  name: "Home",

  components: {
    CompanyDetails,
  },
};
</script>
