<template>
  <v-container fluid>
    <v-item-group>
      <v-row dense>
        <v-col
            md="4"
            class="dashboard-card"
        >
          <v-card
            elevation="2"
            dark
            :loading="trade['loading']"
            color="accent"
            height="400"
          >
            <template slot="progress">
              <v-progress-linear
                  color="secondary"
                  height="5"
                  indeterminate
              />
            </template>
            <v-card-title>{{ trade['title'] }}</v-card-title>
            <v-card-subtitle class="pb-0">
              ID: {{ trade_id }}
            </v-card-subtitle>
            <v-card-text>
              <div>Datetime: {{ trade['datetime'] }}</div>
              <div>Pattern: {{ trade['pattern'] }}</div>
              <div>Position: {{ trade['taker_side'] }}</div>
              <div>Profit: €{{ trade['profit'] }}</div>
              <div>Value of wallet: €{{ trade['wallet_usd_value'] }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col
            md="12"
            class="dashboard-card"
        >
          <candlestick-chart
              v-if="!candles_loading"
              :loading="candles_loading"
              :series="chart_data"
              title="Dogecoin/DOGE"
              text="Dogecoin value up until the moment of the trade"
          />
        </v-col>
      </v-row>
    </v-item-group>
  </v-container>
</template>

<script>

import axios from 'axios'
// import moment from 'moment'
import lodash from 'lodash'

import CandlestickChart from '@/components/dashboard/chart/Candlestick'

export default {
  name: "Chart",
  components: {
    CandlestickChart
  },
  data: () => ({
    candles_loading: true,
    chart_data: [{
      name: 'Dogecoin koers',
      data: []
    }],
    trade_id: '',
    timestamp: null,
    trade: {},
  }),
  async mounted() {
    this.trade_id = this.$route.params.id
    try {
      axios.get('http://127.0.0.1:5000/api/trade/'+this.trade_id).then(response => {
        console.log(response)
        let trades = response.data['trade']
        let new_wallet_value = []
        let old_wallet_value = []
        lodash.forEach(trades, (trade) => {
          if (trade['original'] === 0) {
            new_wallet_value = trade['wallet_usd_value']
          } else {
            this.trade['pattern'] = trade['pattern']
            this.trade['taker_side'] = trade['taker_side'] === 0 ? 'Long' :  'Short'
            old_wallet_value = trade['wallet_usd_value']
            this.trade['datetime'] = trade['timestamp']
          }
        })
        this.trade['title'] = 'Dogecoin/DOGE'
        this.trade['wallet_usd_value'] = new_wallet_value
        this.trade['profit'] = new_wallet_value - old_wallet_value
        this.trade["loading"] = false
        this.timestamp = new Date(this.trade['datetime']).getTime()
        if (this.timestamp) {
          try {
            axios.get('http://127.0.0.1:5000/api/candlestick/browse/'+this.timestamp).then(response => {
              let candles = response.data['candlesticks']
              console.log(candles)
              lodash.forEach(candles, (candle) => {
                // console.log(candle)
                let candle_object = {}
                candle_object['x'] = new Date(parseInt(candle['timestamp']))
                candle_object['y'] = []
                candle_object['y'].push(candle['open'], candle['high'], candle['low'], candle['close'])
                // console.log(candle_object)
                this.chart_data[0].data.push(candle_object)
              })
            })
            // console.log(this.chart_data)
            this.candles_loading = false
          } catch (e) {
            console.error(e)
          }
        }
      })
      // console.log(this.chart_data)
    } catch (e) {
      console.error(e)
    }
  },
  methods: {
    getColor (profit) {
      return profit >= 0 ? '#388ee3' : '#ce3e47'
    },
  },
}
</script>

<style scoped>

</style>