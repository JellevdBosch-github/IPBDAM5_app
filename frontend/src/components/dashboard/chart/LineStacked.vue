<script>
import { Line } from 'vue-chartjs'
export default {
  extends: Line,
  name: "LineChartStacked",
  components: {
    Line
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
    this.renderChart(this.data, this.options)
  }
}
</script>

<style scoped>

</style>