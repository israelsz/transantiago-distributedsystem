<template>
  <div class="container">
    <!-- Container for Color component (60% width) -->
    <div class="component-container color-container">
      <h1 class="component-title">Color de micro más repetido por paradero</h1>
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
  flex-grow: 1;
}

.color-container {
  flex-basis: 60%;
}

.no-disponible-container {
  flex-basis: 40%;
}

.component-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.vertical-separator {
  border-left: 1px solid #ccc;
  flex-basis: 0;
  flex-grow: 1;
  margin: 0 20px;
}
</style>
