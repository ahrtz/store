<template>
    <div>
        <validation-observer v-slot="{ invalid }">
            <header>
                <h3 class="modal-title" id="exampleModalLabel">회원가입</h3>
            </header>
            <validation-provider name="uid" rules="required|minmax:6,12" v-slot="{ errors }">
                <base-input type="text" v-model="uid" label="아이디"/>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <validation-provider name="password" rules="required|minmax:8,16|verify_password" v-slot="{ errors }">
                <base-input type="password" v-model="password" label="패스워드"/>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <validation-provider name="password-verify" rules="required|minmax:8,16|verify_password|password_confirm:@password" v-slot="{ errors }">
                <base-input type="password" v-model="passwordVerify" label="패스워드 확인"/>
                <base-alert type="danger" v-if="errors[0]">
                    {{ errors[0] }}
                </base-alert>
            </validation-provider>
            <footer>
                <base-button type="primary" :disabled="invalid" @click="onSubmit">가입</base-button>
                <base-button type="primary" @click="closeModal()">닫기</base-button>
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
        uid: '',
        password: '',
        passwordVerify: ''
    }),
    methods: {
        closeModal() {
            this.$emit('closemodal')
        },
        onSubmit() {
            let successful = this.$store.dispatch('signUp', {username: this.uid, password1: this.password, password2: this.passwordVerify})
            if (successful) {
                this.uid = ''
                this.password = ''
                this.passwordVerify = ''
                this.selectedList = ''
                this.closeModal()
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