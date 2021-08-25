<template>
  <v-card
      :loading="loading"
      elevation="2"
      dark
  >
    <template slot="progress">
      <v-progress-linear
          color="secondary"
          height="5"
          indeterminate
      />
    </template>
    <v-sheet
        color="background"
        elevation="12"
        height="300"
    >
      <v-sparkline
          :labels="labels"
          :value="value"
          color="#ffffff"
          font-size="13"
          line-width="2"
          style="max-height: 300px"
          padding="16"
          stroke-linecap="round"
          type="trend"
          smooth
      ></v-sparkline>
    </v-sheet>
    <v-card-title class="title font-weight-light mb-2">
      {{ title }}
    </v-card-title>
    <v-card-text class="subheading font-weight-light secondary--text">
      {{ text }}
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: "Sparkline",
    props: {
      title: {
        type: String,
        default: "SPARKLINE TITLE"
      },
      loading: {
        type: Boolean,
        default: true
      },
      text: {
        type: String,
        default: "SPARKLINE TEXT"
      },
      labels: {
        type: Array,
        default: () => []
      },
      value: {
        type: Array,
        default: () => []
      }
    },
    data: () => ({

    })
  }
</script>

<style scoped>


</style>