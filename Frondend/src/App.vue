<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>


    <div class="wrapper">
          <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
               <RouterLink to="/" ><a class="nav-link" aria-current="page">Home</a></RouterLink>
              </li>
              <li class="nav-item">
              <RouterLink to="/about"><a class="nav-link">Sobre</a></RouterLink> 
              </li>
              <li class="nav-item">
               <RouterLink to="/desenhos"><a class="nav-link">Disabled</a></RouterLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>

     
  
     
    </div>
  <RouterView />

  
</template>

