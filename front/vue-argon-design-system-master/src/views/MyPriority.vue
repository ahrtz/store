<template>
    <div>
        <validation-observer v-slot="{ invalid }">
            <validation-provider name="required|priority" rules="check3" v-slot="{ errors }">
                <h3>선호 주제 (3개 선택)</h3>
                <h5>자연과학</h5>
                <div
                    v-for="topic in priorityList.nature"
                    :key="topic.id"
                    style="display: inline-block; width: 150px"
                >
                    <input
                        type="checkbox"
                        v-model="selectedList"
                        :value="topic.id"
                        :disabled="selectedList.length >= 3 && selectedList.indexOf(topic.id) == -1"
                    >
                    <label style="margin-left: 10px">
                        {{ topic.sub_category }}
                    </label>
                </div>
                <h5>공학</h5>
                <div
                    v-for="topic in priorityList.engineering"
                    :key="topic.id"
                    style="display: inline-block; width: 150px"
                >
                    <input
                        type="checkbox"
                        v-model="selectedList"
                        :value="topic.id"
                        :disabled="selectedList.length >= 3 && selectedList.indexOf(topic.id) == -1"
                    >
                    <label style="margin-left: 10px">
                        {{ topic.sub_category }}
                    </label>
                </div>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <footer>
                <base-button type="primary" :disabled="invalid" @click="onSubmit">가입</base-button>
            </footer>
        </validation-observer>
    </div>
</template>

<script>
import { ValidationProvider, ValidationObserver, extend } from 'vee-validate';
import { required, min, max, regex } from 'vee-validate/dist/rules';
import Navigation from "./components/Navigation.vue";
import CustomControls from "./components/CustomControls"

extend('required', {
  ...required,
  message: '필수 입력 칸입니다'
})

extend('check3', {
    validate(value) {
        return value.length === 3
    },
    message: "3개의 선호 주제를 선택해 주세요"
})

export default {
    components: {
        ValidationProvider,
        ValidationObserver,
        Navigation,
        CustomControls
    },
    data: () => ({
        value: '',
        selectedList: [],
        priorityList: {
            nature: [
            ],
            engineering: [
            ]
        }
    }),
    methods: {
        onSubmit() {
            var favoritesList = []
            for (var i in this.selectedList) {
                var s = {}
                s.favorites_id = this.selectedList[i]
                s.ranking = i
                favoritesList.push(s)
            }
            this.$store.dispatch('setFavorites', {favorites: favoritesList})
            this.$emit('closemodal')
        }
    },
    created() {
        this.$axios.get('/api/favorites/').then(response => {
            for (var i in response.data) {
                if (i < 14) {
                    this.priorityList.nature.push(response.data[i])
                }
                else {
                    this.priorityList.engineering.push(response.data[i])
                }
            }
        })
    }
}
</script>

<style>

</style>