<template>
  <div class="Desenho">
    <div class="text-center row fluid-content">
      <h1>Mundo Colorido Kids</h1>
      
      <div v-for="desenho in desenhos" :key="desenho.id" class="card text-center mb-3" style="width: 15rem;">
        <div class="card-body text-center">
          <img :src="desenho.arquivo" class="img-fluid tmg" alt="previa">
          <h5 class="card-title">{{ desenho.nome }}</h5>
          <p class="card-text">{{ desenho.descricao }}</p>
        
          <RouterLink :to="`desenho/${desenho.id}/`"><a class="nav-link">Link</a></RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

const desenhos = ref([])

onMounted(async () => {
  // Simule uma chamada à API (substitua pelo código real para obter dados da sua API)
  const response = await fetch('http://127.0.0.1:8000/api/imagens/')
  const data = await response.json()

  // Atualize a variável de estado com os dados da API
  desenhos.value = data
})
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
