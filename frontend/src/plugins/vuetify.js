import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            dark: {
                primary: '#262626',
                secondary: '#bb8961',
                accent: '#333333',
                accent1: '#131313',
                background: '#121212',
                profit: '#388ee3',
                loss: '#ce3e47',
                grid: '#373737',
                icon: '#7c7c7c',
                chart1: '#6db1e3',
                chart2: '#225378',
            }
        },
        dark: true,
    }
});
