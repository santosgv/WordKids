<template>
  <div class="Desenho container-fluid">
    <h1 class="text-center titulo">Mundo Colorido Kids</h1>
    <div class="form-row text-center">
      <form class="form-group mx-sm-3 mb-2" @submit.prevent="search">
        <input v-model="searchTerm" class="form-group col-md-6" type="search" placeholder="Ex: Carro" aria-label="Search">
      </form>
      </div>
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
        <li class="page-item" :class="{ 'disabled': !desenhos.previous }">
          <a class="page-link" @click="loadPage(desenhos.previous)" :disabled="!desenhos.previous">Volta</a>
        </li>
        <li class="page-item" :class="{ 'disabled': !desenhos.next }">
          <a class="page-link" @click="loadPage(desenhos.next)" :disabled="!desenhos.next">Proximo</a>
        </li>
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
  const response = await fetch('https://meuemenus.com.br/api/imagens/')
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
</style>