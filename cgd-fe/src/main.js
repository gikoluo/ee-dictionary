// import Vue from 'vue';

// import SearchBar from './components/SearchBar.vue';

// Vue.config.productionTip = false;

// new Vue({
//   router,
//   components: {
//     SearchBar,
//   },
//   render: h => h(App),
// }).$mount('#app');

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(router);
app.mount('#app');

