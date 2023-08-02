<template>
    <v-container>
        <v-col>
            <v-row>
                <div>
                    <h1 class="component-title">Detalles de paradero:</h1>
                    <p>(Actualizados constantemente)</p>
                </div>
            </v-row>
            <v-row>
                <v-autocomplete :items="paraderos" item-text="label" label="Seleccione paradero" v-model="selectedParadero"
                    return-object @input="cargarParaderoEspecifico()">
                </v-autocomplete>
            </v-row>
            <v-row justify="center">
                <v-card class="mx-auto mt-7" width="1200" v-if="isParaderoSelected">
                    <v-card-text>
                        <p class="text-h4 text--primary">
                            Paradero: {{ selectedParadero }}
                        </p>

                        <div class="text--primary">
                            <b>Fecha y hora de la información:</b> {{ infoSelectedParadero.fechaprediccion }} | {{
                                infoSelectedParadero.horaprediccion }} <br>
                            <b>Estado Paradero:</b> {{ infoSelectedParadero.respuestaParadero }} <br>
                            <b>Ubicación:</b> {{ infoSelectedParadero.nomett }} <br>
                            <a
                                :href="'https://www.google.com/maps/search/' + infoSelectedParadero.x + ',' + infoSelectedParadero.y + '/@' + infoSelectedParadero.x + ',' + infoSelectedParadero.y + ',18z?entry=ttu'">Ver
                                en mapa</a> <br>
                            <div class="d-flex">
                                <b>Color más repetido del paradero:</b>
                                <div class="cuadradete" :style="{ backgroundColor: infoSelectedParadero.colorMasRepetido }">
                                </div>
                            </div> <br>
                            <b>Servicios no disponibles:</b> <br>
                            <div class="text-center" v-for="micro in infoSelectedParadero.microsNoDisponibles">
                                {{ micro }}
                            </div>

                            <b>Servicios de este paradero:</b>
                            <div class="text-center" v-for="servicio in infoSelectedParadero.servicios.item">
                                <v-divider></v-divider>
                                Servicio: {{ servicio.servicio }} <br>
                                Destino: {{ servicio.destino }} <br>
                                <div class="d-flex justify-center">
                                    Color de Micro: <div class="cuadradete" :style="{ backgroundColor: servicio.color }">
                                    </div>
                                </div>
                                Estado: {{ servicio.respuestaServicio }} <br> <br>
                                Distancia Bus N°1: {{ servicio.distanciabus1 }}[m] <br>
                                Tiempo Llegada Estimado Bus N°1: {{ servicio.horaprediccionbus1 }} <br>
                                Patente Bus N°1: {{ servicio.ppubus1 }} <br> <br>
                                Distancia Bus N°2: {{ servicio.distanciabus2 }}[m] <br>
                                Tiempo Llegada Estimado Bus N°2: {{ servicio.horaprediccionbus2 }} <br>
                                Patente Bus N°2: {{ servicio.ppubus2 }} <br>
                                <v-divider></v-divider>

                            </div>
                        </div>
                    </v-card-text>
                </v-card>
            </v-row>
        </v-col>
    </v-container>
</template>
  
<script>
export default {
    name: 'IndexPage',
    data() {
        return {
            selectedParadero: null,
            paraderos: [],
            infoSelectedParadero: null,
            isParaderoSelected: false
        }
    },
    methods: {
        async cargarParaderos() {
            let response = await this.$axios.get("/paraderos/")
            this.paraderos = response.data
        },
        async cargarParaderoEspecifico() {
            let response = await this.$axios.get("/paradero/" + this.selectedParadero)
            console.log(response.data)
            this.infoSelectedParadero = response.data
            this.isParaderoSelected = true
        }
    },
    mounted() {
        this.cargarParaderos()
    }
}
</script>

<style>
.cuadradete {
    height: 20px;
    width: 20px;
}
</style>