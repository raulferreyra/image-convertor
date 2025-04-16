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
                    <label for="file_dest" class="dest Boxing_folder">🖼️ <span>Carpeta de Destino</span></label>
                    <input type="file" class="file_hidden" name="file_orig" id="file_orig" aria-hidden="true">
                    <input type="file" class="file_hidden" name="file_dest" id="file_dest" aria-hidden="true">
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
                        <label for="max_weight">Peso Máximo: </label>
                        <input type="number" name="max_weight" id="max_weight" min="0" max="1000000" step="1" value=""
                            placeholder="2">
                        <label for="max_weight">MB</label>
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
                    <div class="row">
                        <label for="red_width">Ancho: </label>
                        <input type="number" name="red_width" id="red_width" placeholder="Ancho" value="" min="1"
                            max="1000000">
                        <label for="red_width">PX</label>
                    </div>
                    <div class="row">
                        <label for="red_height">Alto: </label>
                        <input type="number" name="red_height" id="red_height" placeholder="Alto" value="" min="1"
                            max="1000000">
                        <label for="red_height">PX</label>
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
    font-size: 1.4em;
    font-weight: 700;
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

#settings .folder_box .Boxing_folder:hover {
    background-color: var(--primary-color-2);
}

#settings .folder_box .Boxing_folder span {
    margin: 10px auto 0;
    font-size: .4em;
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

#settings #convert {
    background: var(--button-gradient);
    border: 2px solid var(--primary-color-2);
    color: white;
    padding: 12px 30px;
    border-radius: 30px;
    cursor: pointer;
    margin: 0 0 0 auto;
    display: flex;
    transition: all 0.3s ease;
}

#settings #convert:hover {
    background: var(--color-button-3);
    transform: scale(1.05);
}
</style>