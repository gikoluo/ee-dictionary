<template>
    <div class="search-bar">
      <input type="text" v-model="searchTerm" @input="handleInput" placeholder="Search for a word">
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchBar',
    data() {
      return {
        searchTerm: '',
      };
    },
    methods: {
      handleInput() {
        this.$emit('search', this.searchTerm);
      },
    },
  };
  </script>
  
  <style>
  .search-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 20px;
  }
  
  input[type="text"] {
    width: 80%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
  }
  </style>
  