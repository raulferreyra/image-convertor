<template>
    <div class="console-window" :class="{ active: props.consoleWindow }">
        <div class="header">
            Procesando...
            <div class="close-button" @click="handleCloseConsole"></div>
        </div>
        <div class="content">
            <p v-for="(line, index) in visibleLines" :key="index">{{ line }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
    consoleWindow: Boolean
})

const emit = defineEmits(['closeConsole'])

const handleCloseConsole = () => {
    emit('closeConsole')
}

const consoleLines = [
    'Iniciando proceso...',
    'Leyendo archivos...',
    'Procesando archivo 1...',
    'Archivo 1 procesado con éxito.',
    'Procesando archivo 2...',
    'Archivo 2 procesado con éxito.',
    'Finalizando...',
    '✔ Proceso completado.'
]

const visibleLines = ref([])
let lineIndex = 0
let intervalId = null

const startConsoleOutput = () => {
    visibleLines.value = []
    lineIndex = 0
    if (intervalId) clearInterval(intervalId)
    intervalId = setInterval(() => {
        if (lineIndex < consoleLines.length) {
            visibleLines.value.push(consoleLines[lineIndex])
            lineIndex++
        } else {
            clearInterval(intervalId)
        }
    }, 500)
}

watch(() => props.consoleWindow, (newVal) => {
    if (newVal) {
        startConsoleOutput()
    }
})
</script>

<style lang="css" scoped>
* {
    font-family: "Courier New", Courier, monospace;
    background-color: #000;
    color: green;
    font-size: 1.2rem;
}

.console-window {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100%;
    max-width: 400px;
    height: 100%;
    max-height: 300px;
    transform: translate(-50%, -50%);
    border: 2px solid #fff;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all .3s ease-in-out;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    color: #FFF;
    font-family: Orgon-Bold, Arial, Helvetica, sans-serif;
    background-color: blue;
}

.header .close-button {
    cursor: pointer;
    font-size: 1.5rem;
    background-color: #F00;
    width: 20px;
    height: 20px;
    transition: all .3s ease-in-out;
}

.header .close-button:hover {
    background-color: rgb(153, 2, 2);
}

.header .close-button:before {
    width: 100%;
    content: 'X';
    color: #FFF;
    font-size: 1rem;
    font-family: Orgon-Regular, Arial, Helvetica, sans-serif;
    text-align: center;
    display: block;
    line-height: 20px;
}

.content {
    padding: 10px 20px;
}
</style>