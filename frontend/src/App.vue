<script setup>
import { ref } from 'vue'
import Home from './components/Home.vue'
import Donations from './components/Donations.vue'
const overflowStage = ref(false)
</script>

<template>
  <Home :overflowStage="overflowStage" />
  <Donations :overflowStage="overflowStage" />
</template>
