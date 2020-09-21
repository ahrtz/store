<template>
    <div>
        <validation-observer v-slot="{ invalid }">
            <header>
                <h3 class="modal-title" id="exampleModalLabel">회원가입</h3>
            </header>
            <validation-provider name="uid" rules="required|minmax:6,12" v-slot="{ errors }">
                <base-input type="text" v-model="formData.uid" label="아이디"/>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <validation-provider name="password" rules="required|minmax:8,16|verify_password" v-slot="{ errors }">
                <base-input type="password" v-model="formData.password" label="패스워드"/>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <validation-provider name="password-verify" rules="required|minmax:8,16|verify_password|password_confirm:@password" v-slot="{ errors }">
                <base-input type="password" v-model="formData.passwordVerify" label="패스워드 확인"/>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <validation-provider name="priority" rules="required" v-slot="{ errors }">
                <h4>선호 주제 (최대 3개)</h4>
                <h5>자연과학</h5>
                <div
                    v-for="topic in priorityList.nature"
                    :key="topic"
                    style="display: inline-block; width: 150px"
                >
                    <input
                        type="checkbox"
                        v-model="formData.selectedList"
                        :value="topic"
                        :disabled="formData.selectedList.length >= 3 && formData.selectedList.indexOf(topic) == -1"
                    >
                    <label style="margin-left: 10px">
                        {{ topic }}
                    </label>
                </div>
                <h5>공학</h5>
                <div
                    v-for="topic in priorityList.engineering"
                    :key="topic"
                    style="display: inline-block; width: 150px"
                >
                    <input
                        type="checkbox"
                        v-model="formData.selectedList"
                        :value="topic"
                        :disabled="formData.selectedList.length >= 3 && formData.selectedList.indexOf(topic) == -1"
                    >
                    <label style="margin-left: 10px">
                        {{ topic }}
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
import store from "../store/modules/user/store"

extend('required', {
  ...required,
  message: '필수 입력 칸입니다'
})

extend('minmax', {
    validate(value, {min, max}) {
        return value.length <= max && value.length >= min;
    },
    params: ['min', 'max'],
    message: "길이는 {min} 이상, {max} 이하로 작성해 주세요"
})

extend('regex', {
    ...regex,
})    

extend('verify_password', {
    validate: value => {
        var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,16})");
        return strongRegex.test(value);
    },
    message: '대문자, 소문자, 숫자를 각각 1개 이상 입력해 주세요'
});

extend('password_confirm', {
    params: ['target'],
    validate(value, {target}) {
        return value === target
    },
    message: '패스워드가 일치하지 않습니다'
});

export default {
    components: {
        ValidationProvider,
        ValidationObserver,
        Navigation,
        CustomControls
    },
    data: () => ({
        value: '',
        formData: {
            uid: '',
            password: '',
            passwordVerify: '',
            selectedList: []
        },
        priorityList: {
            nature: [
                '기타자연과학', '대기과학', '물리학', '생물학', '생활과학', '수학', '자연과학', '자연과학일반', '지구과학', '지질학', '천문학', '통계학', '해양학', '화학'
            ],
            engineering: [
                '건축공학', '고분자공학', '공학', '공학일반', '교통공학', '금속공학', '기계공학', '기타공학', '농공학', '산림공학', '산업공학', '생물공학', '섬유공학', '안전공학', '원자력공학', '의공학', '자동차공학', '자원공학', '재료공학', '전기공학', '전자/정보통신공학', '제어계측공학', '조선공학', '컴퓨터학', '토목공학', '항공우주공학', '해양공학', '화학공학', '환경공학'
            ]
        }
    }),
    methods: {
        onSubmit() {
            let successful = store.dispatch('signUp', {formData: this.formData})
            if (successful) {
                this.formData.uid = ''
                this.formData.password = ''
                this.formData.passwordVerify = ''
                this.formData.selectedList = ''
                store.dispatch('login', this.formData)
            }
            else {
                alert("회원가입에 실패하였습니다")
            }
        }
    }
}
</script>

<style>

</style>