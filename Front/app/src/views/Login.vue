<template>
    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Login</div>
                    <div class="card-body">
                        <form @submit.prevent="login">
                            <div class="form-group row mb-2">
                                <label for="email" class="col-md-4 col-form-label text-md-right">E-mail</label>

                                <div class="col-md-6">
                                    <input id="email" type="email" class="form-control" name="email" required
                                        autocomplete="email" v-model="email">
                                </div>
                            </div>

                            <div class="form-group row mb-4">
                                <label for="password" class="col-md-4 col-form-label text-md-right">Senha</label>

                                <div class="col-md-6">
                                    <input id="password" type="password" class="form-control" name="password" required
                                        autocomplete="current-password" v-model="password">
                                </div>
                            </div>
                            <ErroMsgAlert :errorMessage="errorMessage" v-if="showModal"></ErroMsgAlert>
                            <div class="form-group row">
                                <div class="col-md-6 offset-md-4">
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="remember" id="remember">

                                        <label class="form-check-label" for="remember">
                                            Mantenha-me conectado
                                        </label>
                                    </div>
                                </div>
                            </div>

                            <div class="form-group row mb-0">
                                <div class="col-md-8 offset-md-4">
                                    <div class="col-md-12 d-flex">
                                        <button type="submit" class="btn btn-primary mx-1">
                                            Login
                                        </button>
                                        <button class="btn btn-primary mx-1">
                                            <a class="text-white no-decoration" href="/registrar">Registrar</a>
                                        </button>
                                        <a class="btn btn-link mx-1" href="">
                                            Esqueci a senha
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.no-decoration {
    text-decoration: none
}
</style>

<script>
import ErroMsgAlert from "../components/ErroMsgAlert.vue";
import navBar from '../components/NavBar.vue'
import axios from 'axios'
export default {
    components: {
        ErroMsgAlert,
        navBar
    },
    data() {
        return {
            email: '',
            password: '',
            showModal: false,
            errorMessage: '',
        }
    },
    mounted() {
       
    },
    methods: {
        login(e) {
            let urlBase = 'http://localhost:8080/api/v1/usuarios/login';
            let configuracao = {
                method: 'post',
                body: new URLSearchParams({
                    'username': this.email,
                    'password': this.password
                })
            }

            let formData = new FormData();
            formData.append('username', this.email)
            formData.append('password', this.password)
            let config = {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Accept': 'application/json',
                }
            }
            axios.post(urlBase, formData, config)
                .then(response => {
                    if (response.data.access_token) {
                        document.cookie = 'token=' + response.data.access_token
                        this.$router.push('/tarefas');
                    }
                })
                .catch(errors => {
                    this.errorMessage = errors.response.data.detail
                    this.showModal = true
                })

        }
    }
}
</script>