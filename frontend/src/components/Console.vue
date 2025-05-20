<template>
    <div class="console-window" :class="{ active: props.consoleWindow }">
        <div class="header">
            <h1>Console</h1>
            <div class="close-button" @click="handleCloseOverflow"></div>
        </div>
        <div class="content">
            <p>Console output will be displayed here.</p>
            <p>Press Ctrl+C to exit.</p>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    consoleWindow: Boolean
})

const emit = defineEmits(['closeOverflow'])

const handleCloseOverflow = () => {
    emit('closeOverflow')
}
</script>

<style lang="css" scoped>
* {
    font-family: "Courier New", Courier, monospace;
    background-color: #000;
    color: green;
    font-size: 1.2rem;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    color: #FFF;
    background-color: blue;
}

.header .close-button {
    cursor: pointer;
    font-size: 1.5rem;
    background-color: #F00;
    transition: all .3s ease-in-out;
}

.header .close-button:hover {
    background-color: rgb(153, 2, 2);
}

header.close-button:before {
    content: 'X';
    color: #FFF;
    font-size: 1.5rem;
}
</style>