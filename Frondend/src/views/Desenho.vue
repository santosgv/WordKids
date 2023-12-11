
<template>
    <div class="Desenho">
        <div class="text-center">
      <h1>This is an Desenho</h1>
  <a href="http://127.0.0.1:8000/imprimir/3" download="Currículo - Vitor Gomes Dev/Analyst" class="down-cv">Download</a>
      <img src="http://127.0.0.1:8000/media/Imagens/img-fundo-software.jpg" class="img-fluid" alt="...">
          {{ $route.params.id }} aki
          <button @click="showPostId" >mostrar id</button>
    </div>
    <p><RouterLink to="/desenhos">&lt; Back</RouterLink></p>
    </div>
  </template>
  
  <script setup>
import { useRoute } from 'vue-router';

const route = useRoute()

const showPostId = () =>{
  alert(`Esse id e :${route.params.id}`)
}
</script>
  