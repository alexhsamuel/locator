<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <br>
    <UserSelect/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import UserSelect from '@/components/UserSelect.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
    UserSelect,
  }
}
</script>
