<template>
    <button type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalCriadoSucesso">
        Cadastrar
    </button>
    <div class="modal fade" id="modalCriadoSucesso" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="modalCriadoSucessoLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="modalCriadoSucessoLabel">Mensagem</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    {{ mensagem }}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                        v-on:click="redirect(event)">Fechar</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        mensagem: {
            type: String,
        },
        sucess: {
            type: Boolean,
        },
    },
    methods: {
        redirect() {
            if (this.sucess == true){
                this.$router.push('/login');
            }
            
        }
    }



}

</script>



