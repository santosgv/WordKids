<template>
    <div class="Desenho container-fluid">
      <h1 class="text-center">Por Categoria</h1>
      <div class="row row justify-content-center">
        
        <div v-for="desenho in desenhos.results" :key="desenho.id" class="card text-center mb-3" style="width: 15rem;">
          <div class="card-body text-center">
            <img :src="desenho.arquivo" class="img-fluid tmg" alt="previa">
            <h5 class="card-title">{{ desenho.nome }}</h5>
            <p class="card-text">{{ desenho.descricao }}</p>
          
            <RouterLink :to="`/desenho/${desenho.id}/`"><a class="nav-link">Link</a></RouterLink>
          </div>
        </div>
        <div class="pagination justify-content-center">
          <button @click="loadPage(desenhos.previous)" :disabled="!desenhos.previous">Anterior</button>
          <span>{{ desenhos.current_page }}</span> / <span>{{ desenhos.count }}</span>
          <button @click="loadPage(desenhos.next)" :disabled="!desenhos.next">Próxima</button>
        </div>

      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, watch } from 'vue'
import { RouterLink,useRoute } from 'vue-router'


const route = useRoute();
const desenhos = ref([])

const loadPage = async (url) => {
  if (url) {
    const response = await fetch(url)
    const data = await response.json()
    desenhos.value = data
  }
}

const fetchDesenhos = async () => {
  const apiUrl = `http://localhost:8000/api/categorias/${route.params.id}/categoria_desenho/`;

  // Simule uma chamada à API (substitua pelo código real para obter dados da sua API)
  const response = await fetch(apiUrl);
  const data = await response.json();

  // Atualize a variável de estado com os dados da API
  desenhos.value = data
};

onMounted(fetchDesenhos);
watch(() => route.params.id, fetchDesenhos);

</script>
  
  <style scoped>
  .card {
    margin-right: 5px;
  }
  
  .tmg {
    max-height: 150px; /* Ajuste conforme necessário */
    width: auto;
  }
  </style>
  