<template>
  <div class="login-form">
    <h2>Login</h2>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    handleSubmit() {
      this.$emit('login', {
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<style>
.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

div {
  margin: 10px;
}

label {
  font-size: 1.2rem;
  margin-right: 10px;
}

input[type="email"], input[type="password"] {
  padding: 10px;
  font-size: 1.2rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 300px;
  max-width: 100%;
  box-sizing: border-box;
}

button[type="submit"] {
  padding: 10px;
  font-size: 1.2rem;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}
</style>
