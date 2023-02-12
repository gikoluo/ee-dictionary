<template>
    <div class="word-details">
      <h1>{{ word }}</h1>
      <p>{{ definition }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'WordDetails',
    data() {
      return {
        word: '',
        definition: '',
      };
    },
    mounted() {
      this.fetchWordDetails();
    },
    methods: {
      async fetchWordDetails() {
        const word = this.$route.params.word;
        const response = await fetch(`/api/words/${word}`);
        const data = await response.json();
        this.word = data.word;
        this.definition = data.definition;
      },
    },
  };
  </script>
  
  <style>
  .word-details {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 10px;
  }
  
  p {
    font-size: 1.2rem;
  }
  </style>
  