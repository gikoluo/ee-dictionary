<template>
  <div class="dashboard">
    <div class="header">
      <h1>ChatGPT Dictionary</h1>
      <div class="login-button">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </div>
    </div>
    <div class="word-list">
      <WordList :words="words" />
    </div>
  </div>
</template>

<script>
import WordList from '@/components/WordList.vue';
import axios from 'axios';

export default {
  name: 'DashboardPage',
  components: {
    WordList,
  },
  data() {
    return {
      words: [],
    };
  },
  mounted() {
    this.fetchWords();
  },
  methods: {
    async fetchWords() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/words/');
        this.words = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style>
.dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 20px;
}

h1 {
  font-size: 2.5rem;
}

.login-button {
  margin-left: auto;
}

.word-list {
  margin-top: 50px;
  max-width: 800px;
}
</style>
