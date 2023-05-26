<template>
    <div class="alert alert-danger" role="alert">
        {{ errorMessage }}
    </div>
</template>


<script>
export default {
    props: {
        errorMessage: {
            type: String,
            required: true,
        },
    },
}
</script>