<template>
  <div class="text-center">
    <v-snackbar
        v-model="snackbar"
        :multi-line="multiline"
        :timeout="timeout"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
            color="loss"
            text
            v-bind="attrs"
            @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
  export default {
    name: "error_snackbar",
    props: {
      snackbar: {
        type: Boolean,
        default: false
      },
      multiline: {
        type: Boolean,
        default: false
      },
      text: {
        type: String,
        default: "Error; something went wrong"
      },
      timeout: {
        type: Number,
        default: 2000
      }
    },
    data: () => ({

    })
  }
</script>

<style scoped>

</style>