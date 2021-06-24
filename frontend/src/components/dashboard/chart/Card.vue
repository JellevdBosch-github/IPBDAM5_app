<template>
  <v-card
    elevation="2"
    dark
    :loading="loaded"
    color="accent"
    height="100"
  >
    <template slot="progress">
      <v-progress-linear
          color="secondary"
          height="5"
          indeterminate
      />
    </template>
    <v-card-title>{{title}}</v-card-title>
    <v-card-text class="secondary--text">{{text}}</v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "card",
  props: {
    title: {
      type: String,
      default: "TITLE"
    },
    text: {
      type: String,
      default: "TEXT"
    },
    loaded: {
      type: Boolean,
      default: true
    }
  }
}
</script>

<style scoped>

</style>