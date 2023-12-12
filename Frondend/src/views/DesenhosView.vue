<template>
  <div class="Desenho">
    <div class="text-center row fluid-content">
      <h1>This is an Desenho</h1>
      <!-- Utilize v-for para percorrer os dados da API e renderizar os cards -->
      <div v-for="desenho in desenhos" :key="desenho.id" class="card text-center mb-3" style="width: 18rem;">
        <div class="card-body">
          <!-- Utilize os dados dinâmicos para preencher o conteúdo dos cards -->
          <h5 class="card-title">{{ desenho.nome }}</h5>
          <p class="card-text">{{ desenho.descricao }}</p>
          <!-- Utilize RouterLink para criar links dinâmicos -->
          <RouterLink :to="`http://127.0.0.1:8000/api/imagens/${desenho.id}/`"><a class="nav-link">Link</a></RouterLink>
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