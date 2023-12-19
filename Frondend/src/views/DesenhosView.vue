<template>
    <div class="Desenho container-fluid">
      <h1 class="text-center" style="color:var(--azul-celeste);">Por Categoria</h1>
      <div class="form-row text-center">
        <form class="form-group mx-sm-3 mb-2" @submit.prevent="search">
          <input v-model="searchTerm" class="form-group col-md-6" type="search" placeholder="Ex: Natal" aria-label="Search">
        </form>
        </div>
      <div class="row row justify-content-center">
        
        <div v-for="desenho in desenhos.results" :key="desenho.id" class="card text-center mb-3" v-show="matchesSearch(desenho)" style="width: 15rem;">
          <div class="card-body text-center">
            <img :src="desenho.arquivo" class="img-fluid tmg" alt="previa">
            <h5 class="card-title">{{ desenho.nome }}</h5>
            <p class="card-text">{{ desenho.descricao }}</p>
          
            <RouterLink :to="`/desenho/${desenho.id}/`"><a class="nav-link">Link</a></RouterLink>
          </div>
        </div>

    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ 'disabled': !desenhos.previous }">
          <a class="page-link" @click="loadPage(desenhos.previous)" :disabled="!desenhos.previous">Anterior</a>
        </li>
        <li class="page-item" :class="{ 'disabled': !desenhos.next }">
          <a class="page-link" @click="loadPage(desenhos.next)" :disabled="!desenhos.next">Próxima</a>
        </li>
      </ul>
    </nav>

      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, watch } from 'vue'
import { RouterLink,useRoute } from 'vue-router'


const route = useRoute();
const desenhos = ref([])
const searchTerm = ref('')

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

const matchesSearch = (desenho) => {
  const lowerCaseSearch = searchTerm.value.toLowerCase()
  return (
    desenho.nome.toLowerCase().includes(lowerCaseSearch) ||
    desenho.descricao.toLowerCase().includes(lowerCaseSearch)
  )
}

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
  