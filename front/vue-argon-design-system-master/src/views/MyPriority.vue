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
                        {{ topic.main_category }}
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
                        {{ topic.main_category }}
                    </label>
                </div>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <footer>
                <base-button type="primary" :disabled="invalid" @click="onSubmit">등록</base-button>
                <base-button type="primary" v-if="insmod" @click="closeModal()">닫기</base-button>
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
        insmod: false,
        priorityList: {
            nature: [
            ],
            engineering: [
            ]
        }
    }),
    computed: {
        check_login() { return this.$store.getters.getIsAuth }
    },
    watch: {
        check_login(val) {
            this.changeSelection(val)
        }
    },
    methods: {
        closeModal() {
            this.$emit('closemodal')
        },
        async onSubmit() {
            var favoritesList = []
            for (var i in this.selectedList) {
                var s = {}
                s.favorites_id = this.selectedList[i]
                s.ranking = i
                favoritesList.push(s)
            }
            let success = await this.$store.dispatch('setFavorites', {favorites: favoritesList, insmod: this.insmod})
            if (this.insmod == false && success == true) {
                this.insmod = true
            }
            this.closeModal()
        },
        changeSelection(val) {
            if (this.$store.getters.getIsAuth == true) {
                this.$axios.get('/api/favorites/users/').then(response => {
                    if (response.data.length < 3) {
                        this.insmod = false
                        this.selectedList = []
                    }
                    else {
                        for (var i in response.data) {
                            this.selectedList.push(response.data[i].favorites.id)
                        }
                        this.insmod = true
                    }
                })
            }
            else {
                this.insmod = false
                this.selectedList = []
            }
        }
    },
    created() {
        this.$axios.get('/api/favorites/').then(response => {
            for (var i in response.data) {
                if (response.data[i].sub_category == "자연과학") {
                    this.priorityList.nature.push(response.data[i])
                }
                else if (response.data[i].sub_category == "공학") {
                    this.priorityList.engineering.push(response.data[i])
                }
            }
        })
        this.changeSelection(this.$store.getters.getIsAuth)
    }
}
</script>

<style>

</style>