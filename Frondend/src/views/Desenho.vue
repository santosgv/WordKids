

<template>
  <div class=" Desenho">
    <div class="text-center">
      <div class="row justify-content-center">
      <h1 class="text-center titulo">Desenho</h1>
      <p class="text-center"><RouterLink to="/">&lt; Back</RouterLink></p>
      <div class="card" style="width: 45rem;">
        <br>
      <img :src="desenho.arquivo" class="img-fluid tamanho" fluid alt="Fluid image">
      <p class="card-body">{{ desenho.nome }}</p>
      <p>{{ desenho.descricao }}</p>
      <div v-html="desenho.afiliado" class="filiado"></div>
      <br>
      <div>
      <a :href="`https://meuemenus.com.br/imprimir/${$route.params.id}`" download="NomeDoArquivo" class="btn btn-success">Baixar</a>
    </div>
    <br>
    </div>
  </div>
  <br>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const desenho = ref({});
const route = useRoute();

onMounted(async () => {
  const response = await fetch(`https://meuemenus.com.br/api/imagens/${route.params.id}`);
  const data = await response.json();
  desenho.value = data;
});
</script>
