<template>
  <div>
    <v-btn v-if="loading" :disabled="loading">
      <v-progress-circular v-if="loading" indeterminate color="white"></v-progress-circular>
      Actualizar</v-btn>
    <v-btn v-else @click="getColores()">Actualizar</v-btn>
    <v-container class="cont">
      <v-row>
        <v-col v-for="(item, index) in jsonData" :key="index" cols="12" sm="6" md="4" lg="6">
          <v-card class="mx-auto" max-width="344">
            <div class="color-div" :style="{ backgroundColor: item.color }" height="200px"></div>

            <div v-if="item.color == 'No hay color mas repetido'"><v-card-title>Sin color más repetido</v-card-title>
            </div>
            <div v-else><v-card-title> {{ index + 1 }}° color más repetido </v-card-title></div>

            <v-card-subtitle>
              Cantidad de paraderos: {{ item.cantidad }}
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data: () => ({
    jsonData: [],
    loading: false,
  }),
  async created() {
    //Obtener listado de pacientes según el usuario logeado
    try {
      this.getColores();
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    async getColores() {
      this.loading = true;
      try {
        const response = await axios.get('http://144.22.50.180/color/');
        this.jsonData = response.data;
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
  },
}
</script>


<style>
.color-div {
  height: 200px;
  width: 100%;
}

.cont {
  margin-top: 50px;
}
</style>