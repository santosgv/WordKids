<style setup>

.tamanho{
  width: 50%;
  height: 50%;
}
</style>

<template>
  <div class="Desenho">
    <div class="text-center">
      <h1 style="color:var(--azul-celeste);">Desenho</h1>
      <p class="text-center"><RouterLink to="/">&lt; Voltar</RouterLink></p>
      <img :src="desenho.arquivo" class="img-fluid tamanho" fluid alt="Fluid image">
      <p>{{ desenho.nome }}</p>
      <p>{{ desenho.descricao }}</p>
      <div v-html="desenho.afiliado" class="filiado"></div>
      <br>
      <div>
      <button :href="`http://127.0.0.1:8000/imprimir/${$route.params.id}`" download="NomeDoArquivo" class="btn btn-success">Baixar</button>
    </div>
    <br>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const desenho = ref({});
const route = useRoute();

onMounted(async () => {
  const response = await fetch(`http://127.0.0.1:8000/api/imagens/${route.params.id}`);
  const data = await response.json();
  desenho.value = data;
});
</script>
