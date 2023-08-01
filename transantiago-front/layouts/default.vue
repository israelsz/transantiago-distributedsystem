<template>
  <v-app>
    <div>
      <v-toolbar dark>
        <v-toolbar-title> <v-icon>mdi-bus-multiple</v-icon> Transantiago Distributed App</v-toolbar-title>

        <v-spacer></v-spacer>

        <template v-slot:extension>
          <v-tabs align-with-title>
            <v-tab :to="{path: '/'}">Inicio</v-tab>
            <v-tab :to="{path: '/detalles'}">Consultar Paradero</v-tab>
            <v-tab :to="{path: '/estadisticas'}">Estadisticas de Paraderos</v-tab>
          </v-tabs>
        </template>
      </v-toolbar>
    </div>
    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
    }
  },
}
</script>
