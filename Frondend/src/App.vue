<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'

const categorias = ref([])

onMounted(async () => {
  try {
    // Substitua 'https://seufront.com' pelo seu domínio real
    const response = await fetch('https://api.mundocoloridokids.com.br/api/categorias/', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    })

    if (response.ok) {
      const data = await response.json()
      categorias.value = data
    } else {
      console.error('Erro ao buscar categorias:', response.statusText)
    }
  } catch (error) {
    console.error('Erro na solicitação:', error.message)
  }
})
</script>

<template>
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg navbar-color" style="color:beige">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <img src="../src/assets/logo.png" alt="" width="60" height="60" class="d-inline-block align-text-top">
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
              <RouterLink to="/" ><a class="nav-link" aria-current="page">Inicio</a></RouterLink>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Categorias
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <div v-for="categoria in categorias" :key="categoria.id">
                  <li> <RouterLink :to="`/categoria/${categoria.id}/`"><a class="dropdown-item">{{categoria.nome}}</a></RouterLink></li>
                </div>
                </ul>
              </li>
              <RouterLink to="/about"><a class="nav-link">Sobre</a></RouterLink> 
            </ul>
          </div>
        </div>
      </nav>
  
     
    </div>
  <RouterView />

  
</template>
