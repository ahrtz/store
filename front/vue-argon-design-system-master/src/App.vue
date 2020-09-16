<template>
    <div id="app">
        <router-view name="header"></router-view>
        <hero />
        <main>
            <fade-transition origin="center" mode="out-in" :duration="250">
                <router-view/>
            </fade-transition>
        </main>
        <router-view name="footer"></router-view>
    </div>
</template>
<script>
import { FadeTransition } from "vue2-transitions";
import Hero from "@/views/components/Hero";

export default {
  components: {
    FadeTransition,
    Hero
  }
};
</script>
