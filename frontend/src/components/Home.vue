<template>
    <div class="home-init">
        <header>
            <img :src="logo" alt="URAS" title="URAS">
            <h1>CONVERSOR DE IMÁGENES</h1>
        </header>
    </div>
</template>


<script setup>
import logo from '@/assets/logo.png';
</script>

<style scoped>
.home-init {
    display: flex;
    justify-content: center;
    align-items: center;
    height: auto;
    width: 100%;
    margin: 0 auto;
    padding: 0;
    background-color: var(--primary-color);
    color: var(--color-white);
}

header {
    display: flex;
    flex-direction: row;
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: .5rem 1rem;
    background: var(--color-white);
    color: var(--primary-color);
    border-radius: 1rem;
    margin: .8rem auto;
}

header img {
    width: 5rem;
    object-fit: cover;
    height: auto;
}

header h1 {
    font-size: 2em;
}
</style>