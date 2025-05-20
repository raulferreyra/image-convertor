<script setup>
import { ref } from 'vue'
import Home from './components/Home.vue'
import Donations from './components/Donations.vue'
import Console from './components/Console.vue'

const overflowStage = ref(false)
const consoleWindow = ref(false)

const handleOpenOverflow = () => {
  overflowStage.value = true
}

const handleCloseOverflow = () => {
  overflowStage.value = false
}

const handleOpenConsole = () => {
  consoleWindow.value = true
}

const handleCloseConsole = () => {
  consoleWindow.value = false
}
</script>

<template>
  <Home :overflowStage="overflowStage" :consoleWindow="consoleWindow" @openOverflow="handleOpenOverflow"
    @closeConsole="handleOpenConsole" />
  <Donations :overflowStage="overflowStage" @closeOverflow="handleCloseOverflow" />
  <Console :consoleWindow="consoleWindow" @closeConsole="handleCloseConsole" />
</template>
