<template>
    <div class="overflow">
        <div class="frame">
            <div class="close-button">X</div>
            <div class="message">
                <h2 class="title">Si te gusta mi herramienta</h2>
                <h3 class="subtitle">por favor apóyame</h3>
                <div class="buttons-row">
                    <a href="https://" target="_blank" rel="noopener noreferrer">Por Plin (Solo Perú)</a>
                    <a href="https://" target="_blank" rel="noopener noreferrer">PayPal (Otros Países)</a>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="css" scoped>
.overflow {
    position: absolute;
    top: 0;
    left: 0;
    background: rgba(200, 200, 200, .2);
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    transition: all .3s ease-in-out;
}
</style>