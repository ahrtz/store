<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-email</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>논문 분석 시스템</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container
        class="fill-height"
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col class="text-center">
              <template>
                <v-file-input
                    label="논문을 pdf로 업로드해 주세요"
                    filled
                    prepend-icon="mdi-file-pdf"
                    accept=".pdf"
                ></v-file-input>
              </template>
          </v-col>
        </v-row>
        <v-row>
          <v-row>
            <v-col>
              <v-card>
                <v-tabs
                  v-model="tab"
                  fixed-tabs
                  background-color="indigo"
                  centered
                  dark
                  icons-and-text
                >
                  <v-tabs-slider></v-tabs-slider>
                  <v-tab href="#tab-1">
                    요약 전체
                    <v-icon>mdi-animation</v-icon>
                  </v-tab>
                  <v-tab href="#tab-2">
                    연구 주제
                    <v-icon>mdi-message-alert</v-icon>
                  </v-tab>
                  <v-tab href="#tab-3">
                    연구 방법
                    <v-icon>mdi-flask-empty</v-icon>
                  </v-tab>
                  <v-tab href="#tab-4">
                    연구 결과
                    <v-icon>mdi-clipboard</v-icon>
                  </v-tab>
                  
                    <v-tabs-items v-model="tab">
                      <v-tab-item
                        v-for="i in 4"
                        :key="i"
                        :value="'tab-' + i"
                      >
                        <v-card flat>
                          <v-card-text>Hello World {{ i }}</v-card-text>
                        </v-card>
                      </v-tab-item>
                    </v-tabs-items>
                </v-tabs>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <wordcloud
                :data="defaultWords"
                nameKey="keyword"
                valueKey="frequency"
                :color="Accent"
                :wordClick="wordClickHandler">
              </wordcloud>
            </v-col>
          </v-row>
        </v-row>
        <v-row>
          <v-col>
            <div>
              <v-row justify="space-around">
                <v-icon @click="model--">mdi-minus</v-icon>
                {{ model }}
                <v-icon @click="model++">mdi-plus</v-icon>
              </v-row>
              <v-carousel v-model="model">
                <v-carousel-item
                  v-for="(color, i) in colors"
                  :key="color"
                >
                  <v-sheet
                    :color="color"
                    height="100%"
                    tile
                  >
                    <v-row
                      class="fill-height"
                      align="center"
                      justify="center"
                    >
                      <div class="display-3">Slide {{ i + 1 }}</div>
                    </v-row>
                  </v-sheet>
                </v-carousel-item>
              </v-carousel>
            </div>
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
  import wordcloud from 'vue-wordcloud'
  export default {
    props: {
      source: String,
    },
    components: {
      wordcloud
    },
    methods: {
      wordClickHandler(keyword, frequency, vm) {
        console.log('wordClickHandler', keyword, frequency, vm)
      }
    },
    data: () => ({
      drawer: null,
      colors: [
        'primary',
        'secondary',
        'yellow darken-2',
        'red',
        'orange',
      ],
      model: 0,
      defaultWords: [{
          "keyword": "Lux",
          "frequency": 26
        },
        {
          "keyword": "Syndra",
          "frequency": 17
        },
        {
          "keyword": "Orianna",
          "frequency": 14
        },
        {
          "keyword": "Lulu",
          "frequency": 8
        },
        {
          "keyword": "Viktor",
          "frequency": 7
        },
        {
          "keyword": "Ezreal",
          "frequency": 7
        },
        {
          "keyword": "Poppi",
          "frequency": 4
        },
        {
          "keyword": "Ryze",
          "frequency": 4
        },
        {
          "keyword": "Jayce",
          "frequency": 3
        },
      ]
    }),
  }
</script>