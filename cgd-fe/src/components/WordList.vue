
<template>
    <div class="word-list">
      <div class="word" v-for="(word, index) in words" :key="index">
        <router-link :to="{ name: 'WordDetails', params: { word: word.word } }">
          <div class="word-header">{{ word.word }}</div>
          <div class="word-description">{{ word.definition }}</div>
        </router-link>
      </div>
    </div>
  </template>
  
  <style>
  .word-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .word {
    background-color: #f4f4f4;
    border-radius: 10px;
    margin: 10px;
    padding: 10px;
    width: 300px;
  }
  
  .word:hover {
    box-shadow: 0 0 5px #aaa;
    cursor: pointer;
  }
  
  .word-header {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .word-description {
    font-size: 18px;
  }
  </style>



  <script>
  export default {
    name: 'WordList',
    props: {
      words: {
        type: Array,
        required: true,
      },
    },
  };
  </script>
  