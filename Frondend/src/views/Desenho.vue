<style setup>

.tamanho{
  width: 50%;
  height: 50%;
}
</style>

<template>
  <div class="Desenho">
    <div class="text-center">
      <h1>This is an Desenho</h1>
      <p>{{ desenho.categoria }}</p>
      <p>{{ desenho.data_upload }}</p>
      <img :src="desenho.arquivo" class="img-fluid tamanho" fluid alt="Fluid image">
      <p>{{ desenho.nome }}</p>
      <p>{{ desenho.descricao }}</p>
      <p>{{ desenho.afiliado }}</p>
      <a :href="`http://127.0.0.1:8000/imprimir/${$route.params.id}`" download="NomeDoArquivo" class="down-cv">Download</a>
    </div>
    <p><RouterLink to="/desenhos">&lt; Back</RouterLink></p>
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
