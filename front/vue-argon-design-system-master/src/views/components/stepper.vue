<template>
  <div id="Stepper_Vertical">
    <v-app id="inspire">
      <v-stepper v-model="count" vertical>
        <v-stepper-step :complete="count > 1" step="1">
          Question 1
          <small>Specify</small>
        </v-stepper-step>
        <v-stepper-content step="1">
          <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
          <v-btn color="primary" @click="count = 2">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step :complete="count > 2" step="2"
          >Question 2
          <small>Specify</small>
        </v-stepper-step>
        <v-stepper-content step="2">
          <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
          <v-btn color="primary" @click="count = 3">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step :complete="count > 3" step="3"
          >Question 3
          <small>Specify</small>
        </v-stepper-step>
        <v-stepper-content step="3">
          <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
          <v-btn color="primary" @click="count = 4">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="4"
          >Question 4
          <small>Specify</small>
        </v-stepper-step>
        <v-stepper-content step="4">
          <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
          <v-btn color="primary" @click="count = 1">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper>
    </v-app>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 1,
    };
  },
};
</script>

<style lang="sass">

</style>