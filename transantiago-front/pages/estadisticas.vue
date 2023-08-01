<template>
  <div class="container">
    <!-- Container for Color component -->
    <div class="component-container">
      <h1 class="component-title">Color Component</h1>
      <Color />
    </div>

    <!-- Vertical separator -->
    <div class="vertical-separator"></div>

    <!-- Container for NoDisponible component -->
    <div class="component-container">
      <h1 class="component-title">NoDisponible Component</h1>
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
.container {
  display: flex;
  justify-content: center;
  align-items: flex-start; /* Align items at the top of the container */
}

.component-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex-grow: 1; /* Allow the component container to take up available space */
}

.component-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.vertical-separator {
  border-left: 1px solid #ccc;
  height: 200px;
  margin: 0 20px;
}
</style>
