<script setup>
import { ref } from 'vue'
import Home from './components/Home.vue'
import Donations from './components/Donations.vue'

const overflowStage = ref(false)

const handleOpenOverflow = () => {
  overflowStage.value = true
}

const handleCloseOverflow = () => {
  overflowStage.value = false
}
</script>

<template>
  <Home :overflowStage="overflowStage" @openOverflow="handleOpenOverflow" />
  <Donations :overflowStage="overflowStage" @closeOverflow="handleCloseOverflow" />
</template>
