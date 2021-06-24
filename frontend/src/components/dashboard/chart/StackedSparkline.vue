<template>
  <v-card
      class="mt-4 mx-auto"
  >
    <v-sheet
        class="v-sheet--offset mx-auto stackSheet"
        color="accent"
        elevation="12">
      <v-sparkline
          :labels="labels"
          :value="value"
          color="secondary"
          line-width="2"
          padding="16"
      ></v-sparkline>
      <v-sparkline
          class="stackSpark"
          :labels="labels"
          :value="value1"
          color="white"
          line-width="2"
          padding="16"
      ></v-sparkline>
    </v-sheet>
    <v-card-text class="pt-0">
      <div class="title font-weight-light mb-2">Wallet value</div>
      <div class="subheading font-weight-light secondary--text">Verloop van de wallet value</div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    labels: {
      type: Array,
      default: () => [
        '12am',
        '3am',
        '6am',
        '9am',
        '12pm',
        '3pm',
        '6pm',
        '9pm',
      ]
    },
    value: {
      type: Array,
      default: () => [
        210,
        678,
        610,
        590,
        390,
        460,
        450,
        440,
      ]
    },
    value1: {
      type: Array,
      default: () => [
        200,
        675,
        410,
        390,
        310,
        460,
        250,
        240,
      ]
    }
  }
}
</script>
<style lang="css" scoped>
.stackSheet {
  position: relative;
}
.stackSpark {
  position: absolute;
  top: 0;
  left: 0;
}
</style>