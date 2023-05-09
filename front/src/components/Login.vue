<template>
  <v-container class="fill-height">
    <v-container fluid>
      <v-row dense flex class="justify-center">
        <v-card class="pa-8 me-4 w-75"> 
          <v-form @submit.prevent="tryLogin">
            <v-text-field
              v-model="user"
              label="Usuario"
              :rules="userRules"
            ></v-text-field>

            <v-text-field
              v-model="password"
              label="Senha"
              :rules="passwordRules"
            ></v-text-field>

            <v-btn type="submit" block class="mt-2">Submit</v-btn>
          </v-form>
        </v-card>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    login: "",
    password: "",
    loginRules: [
      (value) => {
        if (value) return true
        return "Usuario precisa ser preenchido";
      },
    ],
    passwordRules: [
      (value) => {
        if (value) return true
        return "A senha precisa ser preenchida.";
      },
    ],
  }),
  methods: {

    login (login, password) {

        const dados = fetch('http://localhost:8000/auth', (
            method: "POST",
            headers: {"Content-type": "application/json; charset=UTF-8"},
            body: JSON.stringify({login, password})
        ))

        console.log(dados)
    },
    async tryLogin(){
        const login = await login($this.login, $this.password);
        console.log(login)
    }

  }
};
</script>
