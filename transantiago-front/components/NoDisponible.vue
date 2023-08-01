<template>
    <div><v-btn @click="getMicros()">Actualizar</v-btn>
        <v-container class="cont">
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
                            <v-list-item-subtitle>{{ item.cantidad }} micros no disponibles</v-list-item-subtitle>
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
        items: [
            {
                "cantidad": 79,
                "micro": "203N"
            },
            {
                "cantidad": 47,
                "micro": "926"
            },
            {
                "cantidad": 40,
                "micro": "G13"
            },
            {
                "cantidad": 34,
                "micro": "203C1"
            },
            {
                "cantidad": 32,
                "micro": "203"
            },
            {
                "cantidad": 30,
                "micro": "203E"
            },
            {
                "cantidad": 27,
                "micro": "F14"
            },
            {
                "cantidad": 26,
                "micro": "517"
            },
            {
                "cantidad": 26,
                "micro": "E11"
            },
            {
                "cantidad": 25,
                "micro": "208C"
            },
            {
                "cantidad": 25,
                "micro": "514C"
            },
            {
                "cantidad": 24,
                "micro": "C07"
            },
            {
                "cantidad": 24,
                "micro": "J01"
            },
            {
                "cantidad": 23,
                "micro": "208"
            },
            {
                "cantidad": 23,
                "micro": "J01C"
            },
            {
                "cantidad": 22,
                "micro": "432N"
            },
            {
                "cantidad": 22,
                "micro": "206C"
            },
            {
                "cantidad": 21,
                "micro": "G09"
            },
            {
                "cantidad": 20,
                "micro": "I07"
            },
            {
                "cantidad": 19,
                "micro": "1041"
            }
        ],
    }),
    async created() {
        this.getMicros();
    },
    methods: {
        async getMicros() {
            try {
                console.log("getMicros");
                // const response = await axios.get('http://144.22.50.180/micros/');
                // this.items = response.data;
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>