<template>
  <v-data-table
      :headers="headers"
      :items="trades"
      :items-per-page="20"
      class="elevation-1"
      sort-by="datetime"
      :loading="loading"
      loading-text="Loading data . . ."
  >
    <template slot="progress">
      <v-progress-linear
          color="secondary"
          height="5"
          indeterminate
      />
    </template>
    <template v-slot:item.profit="{ item }">
      <v-chip
          outlined
          :color="getColor(item.profit)"
      >
        €{{ item.profit }}
      </v-chip>
    </template>
    <template v-slot:item.action="{ item }">
      <router-link :to="'trade/'+ item.id + '/' + item.timestamp" class="nav-link">
        <v-icon
            small
            class="mr-2"
        >
          mdi-arrow-right
        </v-icon>
      </router-link>
    </template>
  </v-data-table>
</template>

<script>
import axios from "axios";
import lodash from "lodash";

export default {
  name: "Trade",
  mounted() {
    try {
      axios.get('http://127.0.0.1:5000/api/trade/browse').then(response => {
        let trades = response.data['trades']
        console.log(trades)
        lodash.forEach(trades, (trade) => {
          let trade_obj = {}
          if (trade['original'] === 1) {
            trade_obj['id'] = trade['trade_id']
            trade_obj['timestamp'] = trade['timestamp']
            trade_obj['datetime'] = new Date(parseInt(trade['timestamp']))
            trade_obj['takerside'] = trade['taker_side'] === 0 ? 'Short' :  'Long'
            trade_obj['pattern'] = trade['pattern']
            trade_obj['profit'] = 2.54
            this.trades.push(trade_obj)
          }
          // console.log(trade_obj)
        })
        this.loading = false
      })
      // console.log(this.chart_data)
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
  data: () => ({
    headers: [
      {
        text: 'ID',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      {
        text: 'Datetime',
        align: 'start',
        sortable: false,
        value: 'datetime',
      },
      {
        text: 'Long/short',
        align: 'start',
        sortable: false,
        value: 'takerside',
      },
      {
        text: 'Pattern',
        align: 'start',
        sortable: false,
        value: 'pattern',
      },
      {
        text: 'Profit/loss',
        align: 'start',
        sortable: false,
        value: 'profit',
      },
      {
        text: 'Details',
        align: 'start',
        sortable: false,
        value: 'action',
      },
    ],
    trades: [],
    loading: true
  }),
  methods: {
    getColor (profit) {
      return profit >= 0 ? '#388ee3' : '#ce3e47'
    },
  },
}
</script>

<style scoped>

</style>