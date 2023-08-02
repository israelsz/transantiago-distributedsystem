<template>
  <v-container>
    <v-col>
      <v-row justify="center">
        <div>
          <h1 class="component-title">Transantiago Distributed App</h1>
        </div>
      </v-row>
      <v-row justify="center">
        <div>
          <img class="zamorano" src="../assets/img/Zamorano.jpg">
          <p class="text-h6">Transantiago Distributed App es una aplicación distribuida que tiene el objetivo de entregar información de los paraderos y servicios a sus usuarios siendo capaz de procesar una gran cantidad de datos, tener una alta disponibilidad y tolerancia a fallos.</p>
        </div>
      </v-row>
      
      <v-row justify="center">
        <div>
          <h1 class="component-title">Especificaciones de la App</h1>
        </div>
      </v-row>

      <v-row justify="center">
        <v-divider></v-divider>
        <div>
          <p class="text-h6">La especificación de las máquinas y las tecnologías es la siguiente:</p>
          <img class="tecnologias" src="../assets/img/tecnlogias.png">
        </div>
      </v-row>

      <v-row justify="center">
        <v-divider></v-divider>
        <div>
          <p class="text-h6">El pipeline de datos sigue el siguiente flujo:</p>
          <img class="tecnologias" src="../assets/img/pipeline.png">
        </div>
      </v-row>

      <v-divider class="mt-4"></v-divider>
      <v-row justify="center" class="mt-4">
        <div class="text-h6">
          <p class="text-h6">Puede utilizar los servicios de la aplicación disponibles en la barra de navegación.</p>
        </div>
      </v-row>

    </v-col>
  </v-container>
</template>

<script>
export default {
}
</script>

<style>
.zamorano {
height: 200px;
width: 400px;
}
</style>