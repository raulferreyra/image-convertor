<template>
    <div class="home-init">
        <div class="hat">
            <img :src="logo" alt="URAS" title="URAS">
            <h1>CONVERSOR DE IMÁGENES</h1>
        </div>
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

.hat {
    display: flex;
    flex-direction: row;
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    background: var(--color-white);
    color: var(--primary-color);
    border-radius: .5rem 1rem;
    margin: .8rem auto;
}

.hat img {
    width: 120px;
    object-fit: cover;
    height: auto;
}

.hat h1 {
    font-size: 2em;
}
</style>