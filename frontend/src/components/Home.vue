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
                    <div class="folder-item">
                        <label for="file_orig" class="Boxing_folder">📁 Carpeta de Origen</label>
                        <input type="file" id="file_orig" webkitdirectory directory class="file_hidden">
                        <p class="folder-path" id="origin-path">Ninguna carpeta seleccionada</p>
                    </div>
                    <div class="folder-item">
                        <label for="file_dest" class="Boxing_folder">📁 Carpeta de Destino</label>
                        <input type="file" id="file_dest" webkitdirectory directory class="file_hidden">
                        <p class="folder-path" id="dest-path">Ninguna carpeta seleccionada</p>
                    </div>
                </div>
            </div>

            <div class="changes">
                <div class="column">
                    <h2>Peso y Formato</h2>
                    <div class="row">
                        <label for="lot_convert">Conversión de imágenes por lotes: </label>
                        <select name="lot_convert" id="lot_convert">
                            <option value="png">PNG</option>
                            <option value="jpg">JPG</option>
                            <option value="gif">GIF</option>
                            <option value="avif">AVIF</option>
                            <option value="webp">WEBP</option>
                        </select>
                    </div>
                    <div class="row">
                        <div class="row input-unit">
                            <label for="max_weight">Peso Máximo:</label>
                            <div class="input-wrapper">
                                <input type="number" name="max_weight" id="max_weight" placeholder="1" />
                                <span class="unit">MB</span>
                            </div>
                        </div>
                    </div>
                    <div class="row message">
                        <ul>
                            <li>
                                <label for="max_weight">Si este campo se deja en blanco se considera como un peso máximo
                                    de 1MB.</label>
                            </li>
                            <li>
                                <label for="max_weight">Todos los números acá ingresados se considera como MB.</label>
                            </li>
                            <li>
                                <label for="max_weight">Use 0. para reducir por debajo de 1MB el peso de la
                                    imagen.</label>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="column">
                    <h2>Redimensionamiento</h2>
                    <div class="row message">
                        <ul>
                            <li>
                                <p>Todas las imágenes tendrán el mismo tamaño que coloques en esta sección.</p>
                            </li>
                            <li>
                                <p>Si dejas el tamaño de Ancho en blanco, no se moficará ese tamaño.</p>
                            </li>
                            <li>
                                <p>Si dejas el tamaño de Alto en blanco, no se moficará ese tamaño.</p>
                            </li>
                            <li>
                                <p>Todas las imágenes se trabajan en Píxeles (px).</p>
                            </li>
                        </ul>
                    </div>
                    <div class="row input-unit">
                        <label for="red_width">Ancho:</label>
                        <div class="input-wrapper">
                            <input type="number" name="red_width" id="red_width" placeholder="Ancho" />
                            <span class="unit">PX</span>
                        </div>
                    </div>
                    <div class="row input-unit">
                        <label for="red_height">Alto:</label>
                        <div class="input-wrapper">
                            <input type="number" name="red_height" id="red_height" placeholder="Alto" />
                            <span class="unit">PX</span>
                        </div>
                    </div>
                    <div class="row">
                        <label for="red_prop">¿Desea Mantener la Proporción?</label>
                        <input type="checkbox" name="red_prop" id="red_prop">
                    </div>
                    <div class="row message">
                        <ul>
                            <li>
                                <label for="red_prop">No coloque Ancho y Alto, no funciona de esa forma.</label>
                            </li>
                            <li>
                                <label for="red_prop">Elija solo uno.</label>
                            </li>
                            <li>
                                <label for="red_prop">En caso escribir los 2 campos, solo el Ancho tendrá
                                    prioridad.</label>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="changes">
                <div class="row">
                    <input type="button" value="Convertir" id="convert" name="convert">
                </div>
            </div>
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
    margin: 0 auto;
}

header img {
    width: 5rem;
    object-fit: cover;
    height: auto;
}

header h1 {
    margin-left: 1rem;
    font-size: 1.6em;
    line-height: 1.2;
    font-weight: 700;
    font-family: Orgon-Bold, Arial, Helvetica, sans-serif;
    transition: all 0.3s ease-in-out;
}

@media (min-width: 768px) {
    header h1 {
        font-size: 2em;
    }
}

#settings {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 0 auto;
    padding: 0 40px;
    box-sizing: border-box;
}

.home-init,
#settings {
    animation: fadeInUp 0.6s ease both;
}

#settings h2 {
    text-align: left;
    width: 100%;
}

#settings .folders,
#settings .changes {
    width: 100%;
    max-width: 700px;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    align-items: center;
    justify-content: center;
    text-align: left;
}

#settings .changes {
    flex-direction: column;
}

@media (min-width: 768px) {
    #settings .changes {
        flex-direction: row;
        align-items: flex-start;
    }
}

#settings .column {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    padding: 1rem;
    width: 100%;
}

@media (min-width: 768px) {
    #settings .column {
        width: 50%;
    }
}

#settings .folder_box {
    height: auto;
    max-width: 700px;
    display: flex;
    flex-direction: column;
    gap: 20px;
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

@media (min-width: 768px) {
    #settings .folder_box {
        flex-direction: row;
    }
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
    color: var(--secondary-color);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: all 0.3s ease-in-out;
}

#settings .folder-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: .8em;
    gap: 10px;
    width: 100%;
    max-width: 300px;
}

#settings .folder-path {
    font-size: 0.85em;
    color: var(--color-white);
    text-align: center;
    max-width: 100%;
    word-break: break-word;
    font-style: italic;
    padding: 0 10px;
}

#settings .row {
    width: 100%;
    margin: 0 auto 10px;
}

#settings .row ul {
    margin: 0;
    padding: 0 0 0 20px;
}

#settings .row.message {
    font-size: 10px;
    color: var(--color-red);
}

#settings .row.message ul {
    list-style: none;
    background: var(--color-gray);
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
}

#settings .row.message ul li {
    margin-bottom: 5px;
    padding-left: 15px;
    position: relative;
}

#settings .row.message ul li::before {
    content: '💡';
    position: absolute;
    left: 0;
}

#settings input[type="number"],
#settings select {
    background-color: var(--color-white);
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
    padding: 8px 10px;
    border-radius: 10px;
    width: 100%;
    box-sizing: border-box;
    font-size: 1rem;
    transition: all .3s ease-in-out;
}

#settings input[type="number"]:focus,
#settings select:focus {
    outline: none;
    border-color: var(--primary-color-2);
    box-shadow: 0 0 0 3px var(--color-gray-3);
}

#settings .input-unit .input-wrapper {
    position: relative;
    width: 100%;
    display: flex;
    align-items: center;
}

#settings .input-unit .input-wrapper input {
    width: 100%;
    padding-right: 40px;
    box-sizing: border-box;
}

#settings .input-unit .input-wrapper .unit {
    position: absolute;
    right: 10px;
    color: var(--color-gray-light, #aaa);
    font-size: 0.9em;
}

#settings #convert {
    background: var(--button-gradient);
    border: 2px solid var(--primary-color-2);
    color: white;
    padding: 12px 30px;
    border-radius: 30px;
    cursor: pointer;
    margin: 0 0 0 auto;
    display: flex;
    font-size: 1.1rem;
    font-weight: 600;
    box-shadow: 0 4px 10px var(--color-black);
    transition: all 0.3s ease;
}

#settings #convert:hover {
    background: var(--color-button-3);
    transform: scale(1.05);
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>