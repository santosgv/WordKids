<template>
  <form class="d-flex" @submit.prevent="search">
    <input v-model="searchTerm" class="form-control me-2" type="search" placeholder="Ex: Carrinho" aria-label="Search">
    <button class="btn btn-success" type="submit">Procurar</button>
  </form>
  <div class="Desenho container-fluid">
    <h1 class="text-center">Mundo Colorido Kids</h1>
    <div class="row justify-content-center">

      <div v-for="desenho in desenhos.results" :key="desenho.id" class="card text-center mb-3" v-show="matchesSearch(desenho)" style="width: 15rem;">
        <div class="card-body text-center">
          <img :src="desenho.arquivo" class="img-fluid tmg" alt="previa">
          <h5 class="card-title">{{ desenho.nome }}</h5>
          <p class="card-text">{{ desenho.descricao }}</p>

          <RouterLink :to="`/desenho/${desenho.id}/`"><a class="nav-link">Link</a></RouterLink>
        </div>
      </div>
    </div>

    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item"><button class="page-link" @click="loadPage(desenhos.previous)" :disabled="!desenhos.previous">Anterior</button></li>
        <li class="page-item"><a class="page-link">{{ desenhos.count }}</a></li>
        <li class="page-item"><button class="page-link" @click="loadPage(desenhos.next)" :disabled="!desenhos.next">Próxima</button></li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
const desenhos = ref({ results: [], previous: null, next: null, current_page: 1 })
const searchTerm = ref('')

const loadPage = async (url) => {
  if (url) {
    const response = await fetch(url)
    const data = await response.json()
    desenhos.value = data
  }
}

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:8000/api/imagens/')
  const data = await response.json()
  desenhos.value = data
})

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
  max-height: 150px;
  width: auto;
}
.pagination {
  margin-top: 10px;
  text-align: center;
}
.pagination button {
  margin: 0 5px;
}
</style>