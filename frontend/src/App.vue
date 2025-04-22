<script setup>
import Home from './components/Home.vue'
import Donations from './components/Donations.vue'
</script>

<template>
  <Home :overflowStage="overflowStage"2 />
  <Donations :overflowStage="overflowStage" />
</template>

<script>
export default {
  components: {
    Home,
    Donations
  },
  data() {
    return {
      overflowStage: false
    }
  },
}
</script>
