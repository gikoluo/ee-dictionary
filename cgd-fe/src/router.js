import { createRouter, createWebHistory } from 'vue-router';
import SearchBar from './components/SearchBar.vue';
import WordList from './components/WordList.vue';
import WordDetails from './components/WordDetails.vue';
import LoginForm from '@/components/LoginForm.vue';
import SignupForm from './components/SignupForm.vue';
import DashboardPage from './components/DashboardPage.vue';

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/search', component: SearchBar },
  { path: '/words', component: WordList },
  { path: '/word/:word', name: 'WordDetails', component: WordDetails, props: true },
  {
    path: '/login',
    name: 'login',
    component: LoginForm,
  },
  { path: '/signup', component: SignupForm },
  { path: '/dashboard', component: DashboardPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
