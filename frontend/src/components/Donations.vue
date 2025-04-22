<template>
    <div class="overflow" :class="{ active: props.overflowStage }">
        <div class="frame">
            <div class="close-button" @click="handleCloseOverflow">X</div>
            <div class="message">
                <h2 class="title">Si te gusta mi herramienta</h2>
                <h3 class="subtitle">por favor apóyame</h3>
                <div class="buttons-row">
                    <a href="https://" target="_blank" rel="noopener noreferrer">
                        <img :src="plin" alt="PLIN" title="PLIN">
                        Por Plin (Solo Perú)
                    </a>
                    <a href="https://" target="_blank" rel="noopener noreferrer">
                        <img :src="paypal" alt="Paypal" title="Paypal">
                        PayPal (Otros Países)
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import paypal from '@/assets/paypal.png';
import plin from '@/assets/plin.png';

const props = defineProps({
    overflowStage: Boolean
})

const emit = defineEmits(['closeOverflow'])

const handleCloseOverflow = () => {
    emit('closeOverflow')
}
</script>

<style lang="css" scoped>
.overflow {
    position: absolute;
    top: 100%;
    left: 0;
    background: rgba(200, 200, 200, .2);
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    transition: all .3s ease-in-out;
    opacity: 0;
    visibility: hidden;
}

.overflow.active {
    top: 0;
    opacity: 1;
    visibility: visible;
}

.overflow .frame {
    background: var(--secondary-color);
    width: 100%;
    height: auto;
    max-width: 300px;
    max-height: 400px;
    margin: 0 auto;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    overflow: hidden;
    border: .2rem solid var(--primary-color);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 10px;
    box-sizing: border-box;
    transition: all .3s ease-in-out;
}

.overflow .frame .close-button {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
}

.overflow .frame h2.title {
    text-align: center;
    font-size: 1.2rem;
    margin: 1rem auto .4rem;
}

.overflow .frame h3.subtitle {
    text-align: center;
    font-size: 1rem;
    margin: 0 auto .3rem;
}
</style>