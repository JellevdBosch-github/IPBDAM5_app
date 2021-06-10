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
                profit: '#388ee3',
                loss: '#ce3e47'
            }
        },
        dark: true,
    }
});
