<template>
  <v-app-bar color="teal-darken-4">
    <router-link :to="{ name: 'Home' }">
      <v-app-bar-title>
        <v-btn color="white">
          <v-text>Empresa</v-text>
        </v-btn>
      </v-app-bar-title>
    </router-link>
    <v-spacer></v-spacer>
    <router-link :to="{ name: 'Login' }">
      <v-btn color="white">
        <v-icon>mdi-account</v-icon>
        <v-text>Login</v-text>
      </v-btn>
    </router-link>
  </v-app-bar>
</template>

<script setup>
//
</script>
