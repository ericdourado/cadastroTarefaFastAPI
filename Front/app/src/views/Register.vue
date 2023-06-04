<template>
    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Registrar</div>
                    <div class="card-body">
                        <form @submit.prevent="registrar">

                            <div class="form-group row mb-2">
                                <label for="nome" class="col-md-4 col-form-label text-md-right">Nome</label>
                                <div class="col-md-6">
                                    <input id="nome" type="text" class="form-control" name="nome" required v-model="nome">
                                </div>
                            </div>

                            <div class="form-group row mb-2">
                                <label for="email" class="col-md-4 col-form-label text-md-right">E-mail</label>
                                <div class="col-md-6">
                                    <input id="email" type="email" class="form-control" name="email" required
                                        autocomplete="email" v-model="email">
                                </div>
                            </div>

                            <div class="form-group row mb-2">
                                <label for="password" class="col-md-4 col-form-label text-md-right">Senha</label>
                                <div class="col-md-6">
                                    <input id="password" type="password" class="form-control" name="password" required
                                        autocomplete="current-password" v-model="password">
                                </div>
                            </div>

                            <div class="form-group row mb-2">
                                <label for="imagem" class="col-md-4 col-form-label text-md-right">Imagem</label>
                                <div class="col-md-6">
                                    <input id="imagem" type="file" class="form-control form-control-file"
                                        @change="carregarImagem($event)" name="imagem">
                                </div>
                            </div>

                            <div class="form-group row mb-0">
                                <div class="col-md-8 offset-md-4">
                                    <div class="col-md-12 d-flex">
                                        <modal :mensagem="mensagem" :sucess="sucess"></modal>
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

<style scoped></style>

<script>
import axios from 'axios'
import modal from '../components/Modal.vue'

export default {
    components: {
        modal
    },
    data() {
        return {
            nome: '',
            imagem: [],
            email: '',
            password: '',
            mensagem: '',
            sucess: false
        }
    },
    mounted() {

    },
    methods: {
        carregarImagem(e) {
            this.imagem = e.target.files
        },

        registrar(e) {
            let urlBase = 'http://localhost:15400/api/v1/usuarios/signup'

            let formData = new FormData();
            formData.append('nome', this.nome)
            formData.append('email', this.email)
            formData.append('senha', this.password)
            formData.append('file', this.imagem[0])
            let config = {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Accept': 'application/json',
                }
            }

            axios.post(urlBase, formData, config)
                .then(response => {
                    if (response.status == 201) {
                        this.mensagem = 'Usuário criado com sucesso';
                        this.sucess = true;
                    }
                })
                .catch(errors => {
                    this.errorMessage = errors.response.data.detail;
                    this.mensagem = 'Não foi possivel realizar o cadastro';
                    this.sucess = false;
                })
        }
    }
}
</script>