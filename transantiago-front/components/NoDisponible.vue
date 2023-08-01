<template>
    <div>
        <v-btn v-if="loading" :disabled="loading">
            <v-progress-circular v-if="loading" indeterminate color="white"></v-progress-circular>
            Actualizar</v-btn>
        <v-btn v-else @click="getMicros()">Actualizar</v-btn>
        <v-container class="cont" v-if="!loading">
            <v-card class="mx-auto pa-2" max-width="350">
                <v-toolbar color="cyan-lighten-1">
                    <v-toolbar-title>Top recorridos no disponibles</v-toolbar-title>
                    <v-spacer></v-spacer>
                </v-toolbar>
                <v-list>
                    <template v-for="(item, i) in items">
                        <v-list-item :key="i" active-color="primary" rounded="xl">
                            <!-- Display the index "i" on the left of each item -->
                            <v-list-item-avatar>
                                <v-icon>{{ i + 1 }}°</v-icon>
                            </v-list-item-avatar>
                            <v-list-item-content>
                                <v-list-item-title v-text="item.micro"></v-list-item-title>
                                <v-list-item-subtitle>{{ item.cantidad }} veces no disponible</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>

                        <!-- Agrega espacio entre los elementos utilizando el margen o padding en el CSS -->
                        <v-divider v-if="i !== items.length - 1" class="list-divider"></v-divider>
                    </template>
                </v-list>
            </v-card>
        </v-container>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    data: () => ({
        items: [],
        loading: false,
    }),
    async created() {
        this.getMicros();
    },
    methods: {
        async getMicros() {
            this.loading = true;
            try {
                const response = await axios.get('http://144.22.50.180/micro/');
                this.items = response.data.slice(0, 20);

            } catch (error) {
                console.error(error);
            }
            this.loading = false;
        }
    }
}
</script>