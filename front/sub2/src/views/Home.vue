<template>
  <v-app id="inspire">

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-toolbar-title>논문 분석 시스템</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="text-center">
              <template>
                <v-file-input
                    label="File input"
                    filled
                    prepend-icon="mdi-file-pdf"
                    accept=".pdf"
                ></v-file-input>
              </template>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
    }),
  }
</script>