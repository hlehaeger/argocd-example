<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div v-if="data">
      <h2>Messages from Producer:</h2>
      <pre>{{ data }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      data: null
    };
  },
  async created() {
    try {
      const response = await axios.get('http://backend-consumer-svc/consume');
      this.data = response.data;
      console.log(this.data);
    } catch (error) {
      console.error(error);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
