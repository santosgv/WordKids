import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
// Importe os estilos do BootstrapVue
import 'bootstrap-vue/dist/bootstrap-vue.css';

// Importe os estilos do Bootstrap


const app = createApp(App)

app.use(router);

app.mount('#app')
