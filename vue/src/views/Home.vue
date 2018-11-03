<template lang="pug">
.home
  HelloWorld(msg="Welcome to Your Vue.js App")
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>
