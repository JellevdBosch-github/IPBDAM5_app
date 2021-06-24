<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      clipped-left
    >
      <div class="d-flex align-center">
        <v-img
          alt="Placeholder Logo"
          class="mr-2"
          contain
          src="./assets/logo_placeholder.png"
          transition="scale-transition"
          width="120"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/JellevdBosch-github/IPBDAM5_app"
        target="_blank"
        text
      >
        <span class="mr-2">Github repository</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-card>
      <v-navigation-drawer
          app
          v-model="side_drawer"
          class="pt-0"
          color="primary"
          mini-variant
          mini-variant-width=80
          clipped
      >
        <v-list
            nav
            style="padding: 0"
        >
          <v-list-item-group
              color="secondary"
          >
            <v-list-item
                active-class="active"
                v-for="(item, i) in items"
                :key="i"
                class="px-0 ma-0"
            >
              <router-link :to="item.route" class="nav-link">
                <v-list-item-icon
                    class="ma-0 py-4"
                >
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-icon
                        x-large
                        color="icon"
                        class="ma-0"
                        v-bind="attrs"
                        v-on="on"
                      >
                        {{ item.icon }}
                      </v-icon>
                    </template>
                    <span>{{ item.tooltip }}</span>
                  </v-tooltip>
                </v-list-item-icon>
              </router-link>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-card>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  mounted() {
    this.model = 0;
  },
  data: () => ({
    side_drawer: true,
    items: [
      {
        icon: 'mdi-view-dashboard',
        tooltip: 'dashboard',
        text: 'dashboard',
        route: '/'
      },
      {
        icon: 'mdi-table',
        tooltip: 'trades',
        text: 'trades',
        route: '/trade'
      }
    ],
  }),

};
</script>
<style scoped>
  .active {
    /*border-right: 4px solid #bb8961 !important;*/
    box-shadow: #bb8961 inset -2px 0 0 0;
  }
</style>