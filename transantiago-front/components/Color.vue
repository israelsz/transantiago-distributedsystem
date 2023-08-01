<template>
  <div>
    <v-btn @click="getData()">Actualizar</v-btn>
    <v-container class="cont">
      <v-row>
        <v-col v-for="(item, index) in jsonData" :key="index" cols="12" sm="6" md="4" lg="6">
          <v-card class="mx-auto" max-width="344">
            <div class="color-div" :style="{ backgroundColor: item.color }" height="200px"></div>

            <div v-if="item.color == 'No hay color mas repetido'"><v-card-title>Sin color más repetido</v-card-title>
            </div>
            <div v-else><v-card-title> {{ index + 1 }}° color más repetido </v-card-title></div>

            <v-card-subtitle>
              Cantidad de micros: {{ item.cantidad }}
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
    jsonData: [{
      "cantidad": 282,
      "color": "#CF152D"
    },
    {
      "cantidad": 218,
      "color": "#00A77E"
    },
    {
      "cantidad": 213,
      "color": "#0077BB"
    },
    {
      "cantidad": 104,
      "color": "#0093B3"
    },
    {
      "cantidad": 67,
      "color": "#F7941D"
    },
    {
      "cantidad": 46,
      "color": "#FFD400"
    },
    {
      "cantidad": 16,
      "color": "#ED1C24"
    },
    {
      "cantidad": 4,
      "color": "No hay color mas repetido"
    }
    ],
  }),
  async created() {
    //Obtener listado de pacientes según el usuario logeado
    try {
      this.getData();
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    async getData() {
      console.log('getData');
      // const response = await axios.get('http://144.22.50.180/color/');
      // this.jsonData = response.data;
    },
  },
}
</script>


<style>
/* Add this CSS for the color-div */
.color-div {
  height: 200px;
  width: 100%;
  /* Adjust the width if needed */
}

.cont {
  margin-top: 50px;
}
</style>