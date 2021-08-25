<script>
import { Bar } from 'vue-chartjs'
export default {
  extends: Bar,
  name: "BarChart",
  components: {
    Bar
  },
  props: {
    data: {
      type: Object,
      defaults: null
    },
    options: {
      type: Object,
      defaults: null
    },
  },
  data: () => ({

  }),
  mounted () {
    // console.log(this.data)
    this.renderChart(this.data, this.options)
  }
}
</script>

<style scoped>

</style>