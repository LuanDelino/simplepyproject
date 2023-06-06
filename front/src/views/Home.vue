<template>
  <Header />

  <v-container>
    <Carrosel />
    <Products />
    <Promos />
    <Promos />
    <Promos />
    
  </v-container>

  <Footer />
</template>

<script setup>
  import Header from '@/components/Header.vue'
  import Carrosel from '@/components/Carrosel.vue'
  import Promos from '@/components/Promos.vue'
  import Footer from '@/components/Footer.vue'
</script>
