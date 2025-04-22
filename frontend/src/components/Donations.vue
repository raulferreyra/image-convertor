<template>
    <div class="overflow" :class="{ active: isActive }">
        <div class="frame">
            <div class="close-button" @click="handleCloseOverflow()">X</div>
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

<script>
import { ref, watch } from 'vue';

export default {
    props: {
        overflowStage: {
            type: Boolean,
            default: false
        }
    },
    setup(props, { emit }) {
        const isActive = ref(false);

        watch(() => props.overflowStage, (newValue) => {
            isActive.value = newValue;
        });

        const handleCloseOverflow = () => {
            isActive.value = false;
        };

        return {
            isActive,
            handleCloseOverflow
        };
    }
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
    height: 100%;
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
    transition: all .3s ease-in-out;
}
</style>