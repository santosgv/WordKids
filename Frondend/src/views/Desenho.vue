
<template>
  <div class="Desenho">
    <div class="text-center">
      <h1>This is an Desenho</h1>
      <a :href="`http://127.0.0.1:8000/imprimir/${$route.params.id}`" download="NomeDoArquivo" class="down-cv">Download</a>
      <img :src="desenho.arquivo" class="img-fluid" alt="...">
      <p>{{ desenho.nome }}</p>
      <p>{{ desenho.descricao }}</p>
      <button @click="showPostId">Mostrar ID</button>
    </div>
    <p><RouterLink to="/desenhos">&lt; Back</RouterLink></p>
  </div>
</template>
  
<script setup>
import { useRoute, ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';

const route = useRoute();
const desenho = ref({});

const showPostId = () => {
  alert(`Esse id é: ${route.params.id}`);
};

onMounted(async () => {
  // Substitua a chamada da API com a lógica para obter os detalhes do desenho pelo ID
  const response = await fetch(`URL_DA_SUA_API/${route.params.id}`);
  const data = await response.json();
  desenho.value = data;
});
</script>