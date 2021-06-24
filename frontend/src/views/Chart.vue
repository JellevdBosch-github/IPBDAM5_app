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
              :loading="wallet['loading']"
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
            <v-card-title>{{ wallet['title'] }}</v-card-title>
            <v-card-subtitle class="pb-0">
              ID: {{ wallet['id'] }}
            </v-card-subtitle>
            <v-card-text>
              <div>Datetime: {{ wallet['datetime'] }}</div>
              <div>EUR value: {{ wallet['eur_value'] }}</div>
              <div>USD value: {{ wallet['usd_value'] }}</div>
              <div>DOGE value: €{{ wallet['doge_value'] }}
              </div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col
            md="4"
            class="dashboard-card"
        >
          <v-card
              elevation="2"
              dark
              :loading="currency['loading']"
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
            <v-card-title>{{ currency['title'] }}</v-card-title>
            <v-card-text>
              <div>Datetime: {{ currency['datetime'] }}</div>
              <div>Price change: {{ currency['priceChange'] }}</div>
              <div>Price change (percentage): {{ currency['priceChangePercent'] }}</div>
              <div>Weighted average price: €{{ currency['weightedAvgPrice'] }}</div>
              <div>Previous close price: €{{ currency['prevClosePrice'] }}</div>
              <div>Last price: €{{ currency['lastPrice'] }}</div>
              <div>Last quantity amount: €{{ currency['lastQty'] }}</div>
              <div>Bid price: €{{ currency['bidPrice'] }}</div>
              <div>Ask price: €{{ currency['askPrice'] }}</div>
              <div>Open price: €{{ currency['openPrice'] }}</div>
              <div>High price: €{{ currency['highPrice'] }}</div>
              <div>Low price: €{{ currency['lowPrice'] }}</div>
              <div>Volume: €{{ currency['volume'] }}</div>
              <div>Quote volume: €{{ currency['quoteVolume'] }}</div>
            </v-card-text>
          </v-card>
        </v-col>
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
              <div>Position: {{ trade['taker_side'] }}</div>
              <div>Pattern: {{ trade['pattern'] }}</div>
              <div>Profit: €{{ trade['profit'] }}
              </div>
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
    wallet: {
      id: 1,
      title: 'Wallet value',
      datetime: '1-1-2020',
      eur_value: 10003.00,
      usd_value: 10019.00,
      doge_value: 400000.00,
      loading: true
    },
    trade: {},
    currency: {},
  }),
  async mounted() {
    this.trade_id = this.$route.params.id
    this.timestamp = this.$route.params.timestamp
    try {
      axios.get('http://127.0.0.1:5000/api/candlestick/browse/'+this.timestamp).then(response => {
        let candles = response.data['candlesticks']
        // console.log(candles)
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
    try {
      axios.get('http://127.0.0.1:5000/api/currency/DOGE/'+this.timestamp).then(response => {
        let currency = response.data['currency'][0]
        console.log(currency)
        this.currency = currency
        this.currency['title'] = 'Dogecoin/DOGE'
        // TODO: fix datetime, invalid date
        this.currency['datetime'] = new Date(currency['endTime'])
        this.currency["loading"] = false
      })
      // console.log(this.chart_data)
      this.candles_loading = false
    } catch (e) {
      console.error(e)
    }
    try {
      axios.get('http://127.0.0.1:5000/api/trade/'+this.trade_id).then(response => {
        let trade = response.data['trade'][0]
        console.log(trade)
        this.trade = trade
        this.trade['title'] = 'Dogecoin/DOGE'
        // TODO: fix datetime, invalid date
        this.trade['datetime'] = new Date(this.timestamp)
        this.trade['profit'] = 5.00,
        this.trade["loading"] = false
      })
      // console.log(this.chart_data)
      this.candles_loading = false
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