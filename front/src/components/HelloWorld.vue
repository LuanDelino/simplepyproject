<template>
  <v-container class="fill-height">
    <v-container fluid>
      <v-row dense>
        <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
          <v-card>
            <v-img
              src="https://cdn.vuetifyjs.com/images/cards/house.jpg"
              class="align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
              cover
            >
              <v-card-title
                class="text-white"
                v-text="card.title"
              ></v-card-title>
            </v-img>

            <v-card-actions>
              <v-btn
                color="surface-variant"
                variant="text"
              >R$ {{card.price}}</v-btn>
              <v-spacer></v-spacer>

              <v-btn
                color="surface-variant"
                variant="text"
              >Comprar</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    cards: [
      {
        title: "Pre-fab homes",
        price: 20.55,
        src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        flex: 6,
      },
      {
        title: "Favorite road trips",
        price: 20.55,
        src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        flex: 6,
      },
      {
        title: "Best airlines",
        price: 20.55,
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6,
      },
    ],
  }),
};
</script>
