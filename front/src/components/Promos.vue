<template>
  <h1>Nossas promoções</h1>
  <v-row>
    <v-col class="col-4" v-for="product in products">
      <v-card class="mx-auto" max-width="400">
        <v-img
          class="align-end text-white"
          height="200"
          :src=product.img
          cover
        >
          <v-card-title>{{ product.title }}</v-card-title>
        </v-img>

        <v-card-actions class="dflex justify-end">
          <v-btn color="orange"> {{ product.price }} </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
        products: [
            {id: 1, img: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', title: 'Card 1', price: 50.00},
            {id: 2, img: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', title: 'Card 2', price: 150.00},
            {id: 3, img: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg', title: 'Card 3', price: 99.99}
        ]
    };
  },
};
</script>