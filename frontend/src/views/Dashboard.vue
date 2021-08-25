<template>
  <v-container fluid style="padding: 1px 5px">
    <v-item-group>
      <v-row dense>
        <v-col
          md="3"
          class="dashboard-card"
        >
          <card :title="wallet['title']" :text="wallet['text']" :loaded="wallet['loading']"></card>
        </v-col>
        <v-col
            md="3"
            class="dashboard-card"
        >
          <card :title="candle_count['title']" :text="candle_count['text']" :loaded="candle_count['loading']"></card>
        </v-col>
        <v-col
            md="3"
            class="dashboard-card"
        >
          <card :title="trade_count['title']" :text="trade_count['text']" :loaded="trade_count['loading']"></card>
        </v-col>
        <v-col
            md="3"
            class="dashboard-card"
        >
          <card :title="pattern_count['title']" :text="pattern_count['text']" :loaded="pattern_count['loading']"></card>
        </v-col>
      </v-row>
      <v-row dense class="mt-1">
        <v-col
            md="6"
            class="dashboard-card"
        >
          <candlestick v-if="!candlestick_series[0]['loading']" :loading="candlestick_series[0]['loading']" :title="candlestick_series[0]['title']" :series="candlestick_series" :text="candlestick_series[0]['text']"></candlestick>
        </v-col>
        <v-col
            md="6"
            class="dashboard-card"
        >
          <sparkline v-if="!wallet_sparkline['loading']" :value="wallet_sparkline['values']" :labels="wallet_sparkline['labels']" :title="wallet_sparkline['title']" :text="wallet_sparkline['text']"></sparkline>
        </v-col>
      </v-row>
      <v-row dense class="mt-1">
        <v-col
            md="6"
            class="dashboard-card"
        >
          <v-card
              :loading="pattern_ranking_data['loading']"
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
            >
              <bar-chart v-if="!pattern_ranking_data['loading']" :options="pattern_ranking_options" :data="pattern_ranking_data"></bar-chart>
            </v-sheet>
            <v-card-title class="title font-weight-light mb-2">
              {{ pattern_ranking_title }}
            </v-card-title>
            <v-card-text class="subheading font-weight-light secondary--text">
              {{ pattern_ranking_text }}
            </v-card-text>
          </v-card>
        </v-col>
        <v-col
            md="6"
            class="dashboard-card"
        >
          <v-card
              :loading="pattern_occu_data['loading']"
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
            >
              <bar-chart v-if="!pattern_occu_data['loading']" :options="pattern_occu_options" :data="pattern_occu_data"></bar-chart>
            </v-sheet>
            <v-card-title class="title font-weight-light mb-2">
              {{ pattern_occu_title }}
            </v-card-title>
            <v-card-text class="subheading font-weight-light secondary--text">
              {{ pattern_occu_text }}
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row dense class="mt-1">
        <v-col
            md="6"
            class="dashboard-card"
        >
          <v-card
              :loading="aex_doge_loading"
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
            >
              <line-chart-stacked :options="aex_doge_options" :data="aex_doge_data"></line-chart-stacked>
            </v-sheet>
            <v-card-title class="title font-weight-light mb-2">
              {{ aex_doge_title }}
            </v-card-title>
            <v-card-text class="subheading font-weight-light secondary--text">
              {{ aex_doge_text }}
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-item-group>

    <ErrorSnackbar
        :snackbar="snackbar"
        :text="snackbar_text"
        :multi-line="false"
    />
  </v-container>

</template>

<script>
  // import HelloWorld from '../components/HelloWorld'
  import ErrorSnackbar from '../components/snackbar/Error'
  import Card from '../components/dashboard/chart/Card'
  import Candlestick from "@/components/dashboard/chart/Candlestick";
  import Sparkline from "@/components/dashboard/chart/Sparkline";
  import BarChart from "@/components/dashboard/chart/Bar";
  import LineChartStacked from "@/components/dashboard/chart/LineStacked";
  // import StackSparkline from "@/components/dashboard/chart/StackedSparkline";
  import axios from "axios";
  import lodash from "lodash";
  // import lodash from "lodash";

  export default {
    name: 'Dashboard',

    components: {
      Card,
      ErrorSnackbar,
      Candlestick,
      Sparkline,
      BarChart,
      LineChartStacked
      // StackSparkline
    },
    async mounted() {
      try {
        axios.get('http://127.0.0.1:5000/api/wallet/1').then(response => {
          let wallet = response.data['wallet'][0]
          // console.log(wallet)
          let wallet_object = {}
          wallet_object['title'] = '€' + wallet['eur_value'].toString() + ' / $' + wallet['usd_value'].toString()
          wallet_object['text'] = 'Current value of wallet'
          wallet_object['id'] = 1
          wallet_object['eur_value'] = wallet['eur_value']
          wallet_object['usd_value'] = wallet['usd_value']
          wallet_object['doge_value'] = wallet['doge_value']
          wallet_object['loading'] = false
          // console.log(wallet_object)
          this.wallet = wallet_object
        })
      } catch (e) {
        console.error(e)
        this.snackbar_text = "Something went wrong when getting wallet data!"
        this.snackbar = true
      }
      try {
        axios.get('http://127.0.0.1:5000/api/candlestick/count').then(response => {
          let candle_count = response.data['count']
          let count_object = {}
          count_object['title'] = candle_count.toString() + " candlesticks"
          count_object['text'] = 'Total amount of candlesticks'
          count_object['count'] = candle_count
          count_object['loading'] = false
          this.candle_count = count_object
        })
      } catch (e) {
        console.error(e)
        this.snackbar_text = "Something went wrong when getting candlestick count data!"
        this.snackbar = true
      }
      try {
        axios.get('http://127.0.0.1:5000/api/trade/count').then(response => {
          let count_object = {}
          let total_trades = response.data['count']
          count_object['title'] = total_trades.toString() + " trades"
          count_object['text'] = 'Total amount of trades made'
          count_object['loading'] = false
          this.trade_count = count_object
        })
      } catch (e) {
        console.error(e)
        this.snackbar_text = "Something went wrong when getting trade count data!"
        this.snackbar = true
      }
      try {
        axios.get('http://127.0.0.1:5000/api/pattern/count').then(response => {
          // console.log(response)
          let count_object = {}
          let total_patterns = response.data['count']
          count_object['title'] = total_patterns.toString() + " patterns"
          count_object['text'] = 'Total amount of unique patterns recognized'
          count_object['loading'] = false
          this.pattern_count = count_object
        })
      } catch (e) {
        console.error(e)
        this.snackbar_text = "Something went wrong when getting pattern count data!"
        this.snackbar = true
      }
      try {
        axios.get('http://127.0.0.1:5000/api/candlestick/browse').then(response => {
          let candles = response.data['candlesticks']
          // console.log(candles.length)
          lodash.forEach(candles, (candle) => {
            // console.log(candle)
            let candle_object = {}
            candle_object['x'] = new Date(parseInt(candle['timestamp']))
            candle_object['y'] = []
            candle_object['y'].push(candle['open'], candle['high'], candle['low'], candle['close'])
            // console.log(candle_object)
            this.candlestick_series[0].data.push(candle_object)
          })
          this.candlestick_series[0]['name'] = "Dogecoin"
          this.candlestick_series[0]['title'] = "Dogecoin/DOGE"
          this.candlestick_series[0]['text'] = "The price of Dogecoin over time"
          this.candlestick_series[0]['loading'] = false
        })
        this.loaded = true
      } catch (e) {
        console.error(e)
      }
      try {
        axios.get('http://127.0.0.1:5000/api/pattern/browse').then(response => {
          let patterns = response.data['patterns']
          // console.log(candles.length)
          lodash.forEach(patterns, (pattern) => {
            // console.log(pattern)
            this.pattern_ranking_data.labels.push(pattern['pattern'])
            this.pattern_occu_data.labels.push(pattern['pattern'])
            this.pattern_ranking_data.datasets[0].data.push(parseFloat(pattern['profit']))
            this.pattern_occu_data.datasets[0].data.push(pattern['occurences'])
            parseFloat(pattern['profit']) > 0 ? this.pattern_ranking_data.datasets[0].backgroundColor.push('#388ee3') : this.pattern_ranking_data.datasets[0].backgroundColor.push('#ce3e47')
            parseFloat(pattern['profit']) > 0 ? this.pattern_ranking_data.datasets[0].borderColor.push('#388ee3') : this.pattern_ranking_data.datasets[0].borderColor.push('#ce3e47')
          })
          this.pattern_ranking_data['loading'] = false
          this.pattern_occu_data['loading'] = false
          // console.log(this.pattern_occu_data)
        })
      } catch (e) {
        console.error(e)
      }
    },
    data: () => ({
      wallet_sparkline: {
        title: "Wallet value over time",
        text: "The course of the wallet value over time",
        loading: false,
        labels: ['20-6-2021', '21-6-2021', '22-6-2021', '23-6-2021', '24-6-2021'],
        values: [10000, 9997.23, 10012.86, 10010.40, 10013.50]
      },
      candlestick_series: [{
        title: '',
        text: '',
        name: '',
        data: [],
      }],
      pattern_ranking_title: "Pattern earnings",
      pattern_occu_title: "Pattern occurences",
      pattern_ranking_text: "The amount of profit or loss made from each pattern",
      pattern_occu_text: "The amount of times each pattern was recognized",
      aex_doge_loading: true,
      aex_doge_title: "AEX vs Dogecoin",
      aex_doge_text: "The value of the AEX compared to the value of the Dogecoin in order to compare the two.",
      snackbar: false,
      snackbar_text: 'test error',
      wallet: {},
      candle_count: {},
      trade_count: {},
      pattern_count: {},
      pattern_ranking_data: {
        loading: true,
        labels: [],
        datasets: [{
          label: 'Profit/loss',
          data: [],
          color: '#ffffff',
          backgroundColor: [],
          borderColor: [],
          borderWidth: 1
        }]
      },
      pattern_occu_data: {
        loading: true,
        labels: [],
        datasets: [{
          label: 'Occurences',
          data: [],
          color: '#ffffff',
          backgroundColor: '#6db1e3',
          borderColor: '#6db1e3',
          borderWidth: 1
        }]
      },
      pattern_ranking_options: {
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 20,
            bottom: 0
          }
        },
        scales: {
          xAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Pattern',
              fontColor:'#ffffff',
              fontSize: 14
            },
            gridLines: {
              color: "#333333",
              display: false
            },
            ticks: {
              fontColor: "#ffffff",
              fontSize: 18
            }
          }],
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Amount of profit in Euro\'s',
              fontColor:'#ffffff',
              fontSize: 14
            },
            gridLines: {
              color: "#373737",
            },
            ticks: {
              fontColor: "#ffffff",
              fontSize: 18
            }
          }],
        },
        legend: {
          display: false,
        },
        responsive: true,
        maintainAspectRatio: false
      },
      pattern_occu_options: {
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 20,
            bottom: 0
          }
        },
        scales: {
          xAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Pattern',
              fontColor:'#ffffff',
              fontSize: 14
            },
            gridLines: {
              color: "#333333",
              display: false
            },
            ticks: {
              fontColor: "#ffffff",
              fontSize: 18
            }
          }],
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Occurences per pattern',
              fontColor:'#ffffff',
              fontSize: 14
            },
            gridLines: {
              color: "#373737",
            },
            ticks: {
              fontColor: "#ffffff",
              fontSize: 18
            }
          }],
        },
        legend: {
          display: false,
        },
        responsive: true,
        maintainAspectRatio: false
      },
      aex_doge_data: {
        labels: ['01-01-2021', '02-01-2021', '03-01-2021', '04-01-2021', '05-01-2021', '06-01-2021'],
        datasets: [
          {
            label: 'Price of the AEX',
            data: [100, 105, 115, 120, 150, 145],
            color: '#ffffff',
            fill: false,
            backgroundColor: [
              '#6db1e3',
            ],
            borderColor: [
              '#6db1e3',
            ],
            borderWidth: 2
          },
          {
            label: 'Price of the Dogecoin',
            data: [40, 46, 50, 60, 81, 63],
            color: '#ffffff',
            fill: false,
            backgroundColor: [
              '#225378',
            ],
            borderColor: [
              '#225378',
            ],
            borderWidth: 2
          },
        ]
      },
      aex_doge_options: {
        scales: {
          xAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Date time',
              fontColor:'#ffffff',
              fontSize: 14
            },
            gridLines: {
              color: "#333333",
              display: false
            },
            ticks: {
              fontColor: "#ffffff",
              fontSize: 18
            }
          }],
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Price in EUR',
              fontColor:'#ffffff',
              fontSize: 14
            },
            gridLines: {
              color: "#373737",
            },
            ticks: {
              fontColor: "#ffffff",
              fontSize: 18
            }
          }],
        },
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        stacked: false
      }
    })
  }
</script>
<style>
  .dashboard-card {
    padding: 4px 1px 0 1px !important;
  }
</style>