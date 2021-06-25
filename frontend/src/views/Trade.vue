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
          dark
      >
        ${{ item.profit }}
      </v-chip>
    </template>
    <template v-slot:item.action="{ item }">
      <router-link :to="'trade/'+ item.original_id" class="nav-link">
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
        // console.log(trades)
        lodash.forEach(trades, (trade) => {
          let trade_obj = {}
          if (trade['original'] === 0) {
            trade_obj['id'] = trade['trade_id']
            trade_obj['original_id'] = trade['original_id']
            trade_obj['original'] = trade['original']
            trade_obj['datetime'] = trade['timestamp']
            trade_obj['takerside'] = trade['taker_side'] === 0 ? 'Long' :  'Short'
            trade_obj['wallet'] = trade['wallet_usd_value']
            trade['taker_side'] === 0 ? trade_obj['profit'] = trade['usd_value'] - 100 : trade_obj['profit'] = 100 - trade['usd_value']
            this.trades.push(trade_obj)
            console.log(trade_obj['profit'])
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
        text: 'Profit',
        align: 'start',
        sortable: false,
        value: 'profit',
      },{
        text: 'Wallet value after',
        align: 'start',
        sortable: false,
        value: 'wallet',
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