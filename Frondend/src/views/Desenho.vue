<style setup>

.tamanho{
  width: 50%;
  height: 50%;
}
</style>

<template>
  <div class="Desenho">
    <div class="text-center">
      <h1>Desenho</h1>
      <p class="text-center"><RouterLink to="/">&lt; Back</RouterLink></p>
      <img :src="desenho.arquivo" class="img-fluid tamanho" fluid alt="Fluid image">
      <p>{{ desenho.nome }}</p>
      <p>{{ desenho.descricao }}</p>
      <p>{{ desenho.afiliado }}</p>
      <a :href="`http://127.0.0.1:8000/imprimir/${$route.params.id}`" download="NomeDoArquivo" class="down-cv">Download</a>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const desenho = ref({});
const route = useRoute();

onMounted(async () => {
  const response = await fetch(`http://127.0.0.1:8000/api/imagens/${route.params.id}`);
  const data = await response.json();
  desenho.value = data;
});
</script>
