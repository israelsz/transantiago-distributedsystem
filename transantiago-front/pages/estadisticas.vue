<template>
  <div class="container">
    <!-- Container for Color component (60% width) -->
    <div class="component-container color-container">
      <h1 class="component-title">Color de micro más repetido</h1>
      <Color />
    </div>

    <!-- Vertical separator -->
    <div class="vertical-separator"></div>

    <!-- Container for NoDisponible component (40% width) -->
    <div class="component-container no-disponible-container">
      <h1 class="component-title">Recorridos con más micros no disponibles</h1>
      <NoDisponible />
    </div>
  </div>
</template>

<script>
import Color from '~/components/Color.vue';
import NoDisponible from '~/components/NoDisponible.vue';

export default {
  components: { Color, NoDisponible },
};
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
}

.component-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex-grow: 1; /* Each component container takes up the available space */
}

.color-container {
  flex-basis: 60%; /* Color component container takes 60% width */
}

.no-disponible-container {
  flex-basis: 40%; /* NoDisponible component container takes 40% width */
}

.component-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.vertical-separator {
  border-left: 1px solid #ccc;
  flex-basis: 0; /* Allow the separator to take up remaining space */
  flex-grow: 1; /* Stretch the separator to fill remaining vertical space */
  margin: 0 20px;
}
</style>
