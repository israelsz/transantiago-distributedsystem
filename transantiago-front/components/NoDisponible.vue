<template>
    <v-container class="cont">
        <v-card class="mx-auto pa-2" max-width="350">
            <v-toolbar color="cyan-lighten-1">
                <v-toolbar-title>Top recorridos no disponibles</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
            <v-list>
                <template v-for="(item, i) in items">
                    <v-list-item :key="i" active-color="primary" rounded="xl">
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
</template>

<script>
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
            },
            {
                "cantidad": 19,
                "micro": "264N"
            },
            {
                "cantidad": 19,
                "micro": "B13"
            },
            {
                "cantidad": 18,
                "micro": "G23"
            },
            {
                "cantidad": 18,
                "micro": "302"
            },
            {
                "cantidad": 17,
                "micro": "428C"
            },
            {
                "cantidad": 17,
                "micro": "J16"
            },
            {
                "cantidad": 17,
                "micro": "216"
            },
            {
                "cantidad": 17,
                "micro": "990"
            },
            {
                "cantidad": 16,
                "micro": "271"
            },
            {
                "cantidad": 15,
                "micro": "J06"
            },
            {
                "cantidad": 15,
                "micro": "F01C"
            },
            {
                "cantidad": 15,
                "micro": "F91"
            },
            {
                "cantidad": 14,
                "micro": "E16"
            },
            {
                "cantidad": 14,
                "micro": "385"
            },
            {
                "cantidad": 13,
                "micro": "E02"
            },
            {
                "cantidad": 13,
                "micro": "442"
            },
            {
                "cantidad": 13,
                "micro": "422"
            },
            {
                "cantidad": 13,
                "micro": "302N"
            },
            {
                "cantidad": 13,
                "micro": "212"
            },
            {
                "cantidad": 13,
                "micro": "D03C"
            },
            {
                "cantidad": 12,
                "micro": "B05"
            },
            {
                "cantidad": 12,
                "micro": "C22"
            },
            {
                "cantidad": 12,
                "micro": "912"
            },
            {
                "cantidad": 12,
                "micro": "F90"
            },
            {
                "cantidad": 12,
                "micro": "B93"
            },
            {
                "cantidad": 11,
                "micro": "229"
            },
            {
                "cantidad": 11,
                "micro": "111"
            },
            {
                "cantidad": 11,
                "micro": "291"
            },
            {
                "cantidad": 11,
                "micro": "992"
            },
            {
                "cantidad": 11,
                "micro": "B12C"
            },
            {
                "cantidad": 11,
                "micro": "G05"
            },
            {
                "cantidad": 11,
                "micro": "E18"
            },
            {
                "cantidad": 11,
                "micro": "590"
            },
            {
                "cantidad": 10,
                "micro": "E04"
            },
            {
                "cantidad": 10,
                "micro": "G01C"
            },
            {
                "cantidad": 10,
                "micro": "450"
            },
            {
                "cantidad": 10,
                "micro": "D01"
            },
            {
                "cantidad": 10,
                "micro": "C17"
            },
            {
                "cantidad": 10,
                "micro": "H06"
            }
        ],
    }),
}
</script>