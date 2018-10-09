<template>
  <div class="home">
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
