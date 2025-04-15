<template>
    <div class="home-init">
        <header>
            <img :src="logo" alt="URAS" title="URAS">
            <h1>CONVERSOR DE IMÁGENES</h1>
        </header>
        <form id="settings">
            <div class="folders">
                <h2>Seleccione las carpetas</h2>
                <div class="folder_box">
                    <label for="file_orig" class="orig Boxing_folder">📚 <span>Carpeta de Origen</span></label>
                    <label for="file_dest" class="dest Boxing_folder">🪄 <span>Carpeta de Destino</span></label>
                    <input type="file" class="file_hidden" name="file_orig" id="file_orig" aria-hidden="true">
                    <input type="file" class="file_hidden" name="file_dest" id="file_dest" aria-hidden="true">
                </div>
            </div>
            GITHUB CAN YOU HEAR ME?
        </form>
    </div>
</template>


<script setup>
import logo from '@/assets/logo.png';
</script>

<style scoped>
.home-init {
    display: flex;
    flex-direction: column;
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
    font-weight: 700;
}

#settings {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 0 auto;
    padding: 0 40px 40px;
    box-sizing: border-box;
}

#settings h2 {
    text-align: left;
    width: 100%;
}

#settings .folders {
    width: 100%;
    max-width: 700px;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    align-items: center;
    justify-content: center;
    text-align: left;
}

#settings .folder_box {
    height: auto;
    max-width: 700px;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    margin: 0 auto;
    padding: 20px;
    box-sizing: border-box;
    border: 1px solid var(--color-white);
    border-radius: 50px;
    background: var(--primary-color-3);
}

#settings .folder_box .file_hidden {
    display: none;
    opacity: 0;
    visibility: hidden;
}

#settings .folder_box .Boxing_folder {
    border: 1px solid var(--color-white);
    width: 300px;
    height: 100%;
    font-size: 3em;
    border-radius: 50px;
    padding: 20px 0;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: all 0.3s ease-in-out;
}

#settings .folder_box .Boxing_folder:hover {
    background-color: var(--primary-color-2);
}

#settings .folder_box .Boxing_folder span {
    margin: 10px auto 0;
    font-size: .4em;
}
</style>