<script>
import { RouterLink, RouterView } from 'vue-router'
import navBar from './components/NavBar.vue'

export default {
  components: {
    navBar
  },
  data() {
    return {
      verificaLogin: '',
      rota: '',
    }
  },
  mounted() {
    let token = document.cookie;
    let arr_token = token.split('token=');
    fetch('http://localhost:8080/api/v1/usuarios/me', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'bearer ' + arr_token[1]
      }
    }).then(response => {
      if (response.status == 200) {
        this.verificaLogin = 'Sair'
        this.rota = '/sair'
        this.$router.push('/tarefas');

      } else {
        this.verificaLogin = 'Entrar'
        this.rota = '/login'
        if (this.$route.path != '/registrar') {
          this.$router.push('/login');
        }

      }
    }).catch(error => {
      this.showModal = true
      this.errorMessage = 'Ocorreu um erro interno'
    })
  },
}
</script>

<template>
  <header>
    <header>
      <navBar :verificaLogin="verificaLogin" :rota="rota"></navBar>
    </header>
  </header>

  <RouterView />
</template>

<style scoped></style>
