<template>
    <v-app>
      <v-container class="cont">
        <v-row>
          <!-- Loop through the data array and create a card for each item -->
          <v-col
            v-for="(item, index) in jsonData"
            :key="index"
            cols="12"
            sm="6"
            md="4"
          >
            <v-card class="mx-auto" max-width="344">
              <div
                class="color-div"
                :style="{ backgroundColor: item.color }"
                height="200px"
              ></div>

              <div v-if="item.color == 'No hay color mas repetido'"><v-card-title>Sin color más repetido </v-card-title></div>
              <div v-else><v-card-title> {{ index+1 }}° color más repetido </v-card-title></div>

              <v-card-subtitle>
                Cantidad de micros: {{ item.cantidad }}
              </v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>

  <script>
    export default {
      data: () => ({
        jsonData: [
          {
            cantidad: 282,
            color: '#CF152D',
          },
          {
            cantidad: 218,
            color: '#00A77E',
          },
          {
            cantidad: 213,
            color: '#0077BB',
          },
          {
            cantidad: 104,
            color: '#0093B3',
          },
          {
            cantidad: 67,
            color: '#F7941D',
          },
          {
            cantidad: 46,
            color: '#FFD400',
          },
          {
            cantidad: 16,
            color: '#ED1C24',
          },
          {
            cantidad: 4,
            color: 'No hay color mas repetido',
          },
        ],
      }),
      methods: {},
    }
  </script>

  <style>
    /* Add this CSS for the color-div */
    .color-div {
      height: 200px;
      width: 100%; /* Adjust the width if needed */
    }
    .cont {
      margin-top: 50px;
    }
  </style>
