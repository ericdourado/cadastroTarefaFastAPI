

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand">Logo</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <div class="menu">
            <li class="nav-item">
              <a class="nav-link" href="/tarefas">Tarefas</a>
            </li>
            <button @click="logout" class="btn text-secondary">{{ verificaLogin }}</button>
          </div>
        </ul>
      </div>
    </div>
  </nav>
</template>


<style>
.menu {
  display: flex;
  justify-content: space-between;

}
</style>


<script>
export default {
  props: {
    verificaLogin: {
      type: String,
    },
    rota: {
      type: String,
    },
  },
  data() {
    return {

    }
  },
  mounted() {

  },
  methods: {
    logout(e) {
      document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      this.$router.push('/login');
    }
  }

}
</script>


<style scoped></style>
