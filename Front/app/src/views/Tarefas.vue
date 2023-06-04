<template>
    <div class="container">
        <h1 class="mt-5 text-center">Lista de Tarefas</h1>
        <div>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalAdicionarTarefa">
                Adicionar Tarefa
            </button>
            <div class="modal fade" id="modalAdicionarTarefa" ref="modalAdicionarTarefa" data-bs-backdrop="static"
                data-bs-keyboard="false" tabindex="-1" aria-labelledby="modalAdicionarTarefaLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="modalAdicionarTarefaLabel">Adicionar Tarefa</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="form-group">
                                <label for="nomeTarefa">Nome da Tarefa:</label>
                                <input type="text" class="form-control" id="nomeTarefa" v-model="novaTarefa.nome">
                            </div>
                            <div class="form-group">
                                <label for="descricaoTarefa">Descrição da Tarefa:</label>
                                <textarea class="form-control" id="descricaoTarefa" rows="3"
                                    v-model="novaTarefa.descricao"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="statusTarefa">Status da Tarefa:</label>
                                <select class="form-control" id="statusTarefa" v-model="novaTarefa.concluido">
                                    <option value="concluido">Concluído</option>
                                    <option value="nao-concluido">Não Concluído</option>
                                </select>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                            <button type="button" class="btn btn-primary" @click="salvarTarefa">Salvar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>



        <!-- editartarefa -->
        <div>
            <div class="modal fade" id="modalEditarTarefa" ref="modalEditarTarefa" data-bs-backdrop="static"
                data-bs-keyboard="false" tabindex="-1" aria-labelledby="modalEditarTarefaLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="modalEditarTarefaLabel">Editar/Visualizar</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="form-group">
                                <label for="nomeTarefa">Nome da Tarefa:</label>
                                <input type="text" class="form-control" id="nomeTarefa" v-model="editarTarefa.nome">
                            </div>
                            <div class="form-group">
                                <label for="descricaoTarefa">Descrição da Tarefa:</label>
                                <textarea class="form-control" id="descricaoTarefa" rows="3"
                                    v-model="editarTarefa.descricao"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="statusTarefa">Status da Tarefa:</label>
                                <select class="form-control" id="statusTarefa" v-model="editarTarefa.concluido">
                                    <option value="concluido">Concluído</option>
                                    <option value="nao-concluido">Não Concluído</option>
                                </select>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                            <button type="button" class="btn btn-primary" @click="putTarefa">Salvar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>



        <ul class="list-group mt-4">
            <li class="list-group-item d-flex justify-content-between align-items-center " v-for="tarefa in tarefas"
                :key="tarefa.id">
                <div class="form-check">
                    <input type="checkbox" @change.native="concluiTarefa($event, tarefa.id)" class="form-check-input"
                        v-model="tarefa.concluido">
                    <label class="form-check-label"> {{ tarefa.nome }} </label>
                </div>
                <div>
                    <button type="button" class="btn btn-secondary ms-auto me-2" data-bs-toggle="modal"
                        data-bs-target="#modalEditarTarefa" @click="pegaTarefa(tarefa.id)">
                        Editar
                    </button>
                    <button class="btn btn-secondary ms-auto me-2" @click="excluirTarefa(tarefa.id)">Excluir</button>
                </div>
            </li>
        </ul>

        <nav aria-label="Navegação de página" class="mt-4">
            <ul class="pagination justify-content-center">
                <li class="page-item" :class="{ disabled: paginaAtual === 1 }">
                    <a class="page-link" href="#" @click="trocarPagina(paginaAtual - 1)">Anterior</a>
                </li>
                <li class="page-item" :class="{ active: pagina === paginaAtual }" v-for="pagina in paginas" :key="pagina">
                    <a class="page-link" href="#" @click="trocarPagina(pagina)">{{ pagina }}</a>
                </li>
                <li class="page-item" :class="{ disabled: paginaAtual === paginas.length }">
                    <a class="page-link" href="#" @click="trocarPagina(paginaAtual + 1)">Próxima</a>
                </li>
            </ul>
        </nav>


    </div>
</template>
  
  
<script>
import axios from 'axios'

export default {
    data() {
        return {
            novaTarefa: {
                nome: '',
                descricao: '',
                concluido: ''
            },
            editarTarefa: {
                id: null,
                nome: '',
                descricao: '',
                concluido: ''
            },
            tarefas: [],
            paginas: [],
            paginaAtual: 1,
            mostrarModalCadastro: false,
            token: [],
        };
    },
    mounted() {
        this.token = document.cookie.split('token=');
        fetch(`http://localhost:15400/api/v1/tarefas?page=${this.paginaAtual}&page_size=10`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'bearer ' + this.token[1]
            }
        })
            .then(response => response.json())
            .then(data => {
                this.tarefas = data;
            })
            .catch(error => {
                this.showModal = true;
                this.errorMessage = 'Ocorreu um erro interno';
            });

    },
    methods: {
        trocarPagina(numeroPagina) {
            this.paginaAtual = numeroPagina;
            fetch(`http://localhost:15400/api/v1/tarefas?page=${this.paginaAtual}&page_size=10`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                }
            })
                .then(response => response.json())
                .then(data => {
                    this.tarefas = data;
                })

        },
        salvarTarefa() {
            const url = 'http://localhost:15400/api/v1/tarefas';
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                },
            };
            if (this.novaTarefa.concluido == 'concluido') {
                this.novaTarefa.concluido = true;
            } else {
                this.novaTarefa.concluido = false;
            }

            axios
                .post(url, this.novaTarefa, config)
                .then(response => {
                    this.novaTarefa.nome = '';
                    this.novaTarefa.descricao = '';
                    this.novaTarefa.concluido = '';
                    window.location.reload()
                })
                .catch(error => {
                    console.error('Erro ao salvar tarefa:', error);
                });
        },

        excluirTarefa(id) {
            fetch(`http://localhost:15400/api/v1/tarefas/${id}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                }
            })
            window.location.reload()
        },
        async concluiTarefa(event, id) {
            let alterarTarefa = {
                nome: '',
                descricao: '',
                concluido: ''
            }
            this.token = document.cookie.split('token=');
            await fetch(`http://localhost:15400/api/v1/tarefas/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                }
            })
                .then(response => response.json())
                .then(data => {
                    alterarTarefa.nome = data.nome
                    alterarTarefa.descricao = data.descricao
                    alterarTarefa.concluido = event.target.checked;
                })
            const url = `http://localhost:15400/api/v1/tarefas/${id}`; // Substitua pela URL correta do seu servidor
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                },
            };

            await axios
                .put(url, alterarTarefa, config)
                .then(response => {
                })
                .catch(error => {
                    console.error('Erro ao alterar tarefa:', error);
                });
        },

        async pegaTarefa(id) {
            this.token = document.cookie.split('token=');
            await fetch(`http://localhost:15400/api/v1/tarefas/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                }
            })
                .then(response => response.json())
                .then(data => {
                    this.editarTarefa.id = data.id
                    this.editarTarefa.nome = data.descricao
                    this.editarTarefa.descricao = data.descricao
                    this.editarTarefa.concluido = data.concluido
                    if (this.editarTarefa.concluido == true) {
                        this.editarTarefa.concluido = 'concluido'
                    } else {
                        this.editarTarefa.concluido = 'nao-concluido'
                    }
                })

        },
        async putTarefa() {

            const url = `http://localhost:15400/api/v1/tarefas/${this.editarTarefa.id}`;
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer ' + this.token[1]
                },
            };
            if (this.editarTarefa.concluido == 'concluido') {
                this.editarTarefa.concluido = true;
            } else {
                this.editarTarefa.concluido = false;
            }

            axios
                .put(url, this.editarTarefa, config)
                .then(response => {
                    this.editarTarefa.nome = '';
                    this.editarTarefa.descricao = '';
                    this.editarTarefa.concluido = '';
                    window.location.reload()
                })
                .catch(error => {
                    console.error('Erro ao editar tarefa:', error);
                });


        }
    }
};
</script>
  
<style>
h1 {
    margin-top: 50px;

}

.form-check-input[type="checkbox"] {
    margin-top: 0.2rem;
}
</style>
  