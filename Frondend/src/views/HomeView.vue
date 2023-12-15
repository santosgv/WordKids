<template>
  <div class="Desenho container-fluid">
    <h1 class="text-center">Mundo Colorido Kids</h1>
    <div class="row justify-content-center">
      
      <div v-for="desenho in desenhos.results" :key="desenho.id" class="card text-center mb-3" style="width: 15rem;">
        <div class="card-body text-center">
          <img :src="desenho.arquivo" class="img-fluid tmg" alt="previa">
          <h5 class="card-title">{{ desenho.nome }}</h5>
          <p class="card-text">{{ desenho.descricao }}</p>
        
          <RouterLink :to="`/desenho/${desenho.id}/`"><a class="nav-link">Link</a></RouterLink>
        </div>
      </div>
    </div>

    <!-- Adicione a navegação para a página anterior e próxima -->
    <div class="pagination justify-content-center">
      <button @click="loadPage(desenhos.previous)" :disabled="!desenhos.previous">Anterior</button>
      <span>{{ desenhos.current_page }}</span> / <span>{{ desenhos.count }}</span>
      <button @click="loadPage(desenhos.next)" :disabled="!desenhos.next">Próxima</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

const desenhos = ref({ results: [], previous: null, next: null, current_page: 1 })

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