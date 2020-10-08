<template>
  <!-- v-for="(card, index) in cards"
        :key="index"
        :ref="`card_${index}`"
        @mouseover="hoverCard(index)"
        @mouseout="hoverCard(-1)" -->
  <router-link :to="'/showdetail/' + sid.id">
    <div class="card">
      <img class="card-image" src="@/assets/images/category/건축공학.jpg" v-if="sid.subject == '건축공학'"/>
      <img class="card-image" src="@/assets/images/category/고분자공학.jpg" v-else-if="sid.subject == '고분자공학'"/>
      <img class="card-image" src="@/assets/images/category/공학.png" v-else-if="sid.subject == '공학'"/>
      <img class="card-image" src="@/assets/images/category/교통공학.jpg" v-else-if="sid.subject == '교통공학'"/>
      <img class="card-image" src="@/assets/images/category/금속공학.jpg" v-else-if="sid.subject == '금속공학'"/>
      <img class="card-image" src="@/assets/images/category/기계공.jpg" v-else-if="sid.subject == '기계공' || sid.subject == '기계공학'"/>
      <img class="card-image" src="@/assets/images/category/기타자연과학.png" v-else-if="sid.subject == '기타자연과학' || sid.subject == '자연과학' || sid.subject == '자연과학일반'"/>
      <img class="card-image" src="@/assets/images/category/농공학.jpg" v-else-if="sid.subject == '농공학'"/>
      <img class="card-image" src="@/assets/images/category/대기과학.jpg" v-else-if="sid.subject == '대기과학'"/>
      <img class="card-image" src="@/assets/images/category/물리학.jpg" v-else-if="sid.subject == '물리학'"/>
      <img class="card-image" src="@/assets/images/category/산림공학.jpg" v-else-if="sid.subject == '산림공학'"/>
      <img class="card-image" src="@/assets/images/category/산업공학.jpg" v-else-if="sid.subject == '산업공학'"/>
      <img class="card-image" src="@/assets/images/category/생물학.jpg" v-else-if="sid.subject == '생물학' || sid.subject == '생물공학'"/>
      <img class="card-image" src="@/assets/images/category/생활과학.jpg" v-else-if="sid.subject == '생활과학'"/>
      <img class="card-image" src="@/assets/images/category/섬유공학.jpg" v-else-if="sid.subject == '섬유공학'"/>
      <img class="card-image" src="@/assets/images/category/수학.jpg" v-else-if="sid.subject == '수학'"/>
      <img class="card-image" src="@/assets/images/category/안전공학.jpg" v-else-if="sid.subject == '안전공학'"/>
      <img class="card-image" src="@/assets/images/category/원자력공학.jpg" v-else-if="sid.subject == '원자력공학'"/>
      <img class="card-image" src="@/assets/images/category/의공학.jpg" v-else-if="sid.subject == '의공학'"/>
      <img class="card-image" src="@/assets/images/category/자동차공학.jpg" v-else-if="sid.subject == '자동차공학'"/>
      <img class="card-image" src="@/assets/images/category/자원공학.jpg" v-else-if="sid.subject == '자원공학'"/>
      <img class="card-image" src="@/assets/images/category/재료공학.jpg" v-else-if="sid.subject == '재료공학'"/>
      <img class="card-image" src="@/assets/images/category/전기공학.jpg" v-else-if="sid.subject == '전기공학'"/>
      <img class="card-image" src="@/assets/images/category/전자정보통신공학.jpg" v-else-if="sid.subject == '전자/정보통신공학'"/>
      <img class="card-image" src="@/assets/images/category/제어계측공학.jpg" v-else-if="sid.subject == '제어계측공학'"/>
      <img class="card-image" src="@/assets/images/category/조선공학.jpg" v-else-if="sid.subject == '조선공학'"/>
      <img class="card-image" src="@/assets/images/category/지구과학.jpg" v-else-if="sid.subject == '지구과학'"/>
      <img class="card-image" src="@/assets/images/category/지질학.jpg" v-else-if="sid.subject == '지질학'"/>
      <img class="card-image" src="@/assets/images/category/천문학.jpg" v-else-if="sid.subject == '천문학'"/>
      <img class="card-image" src="@/assets/images/category/컴퓨터학.jpg" v-else-if="sid.subject == '컴퓨터학'"/>
      <img class="card-image" src="@/assets/images/category/토목공학.jpg" v-else-if="sid.subject == '토목공학'"/>
      <img class="card-image" src="@/assets/images/category/통계학.jpg" v-else-if="sid.subject == '통계학'"/>
      <img class="card-image" src="@/assets/images/category/항공우주공학.jpg" v-else-if="sid.subject == '항공우주공학'"/>
      <img class="card-image" src="@/assets/images/category/해양공학.jpg" v-else-if="sid.subject == '해양공학'"/>
      <img class="card-image" src="@/assets/images/category/해양학.jpg" v-else-if="sid.subject == '해양학'"/>
      <img class="card-image" src="@/assets/images/category/화학.jpg" v-else-if="sid.subject == '화학' || sid.subject == '화학공학'"/>
      <img class="card-image" src="@/assets/images/category/환경공학.jpg" v-else-if="sid.subject == '환경공학'"/>

      <div class="card-footer">
        <p class="card-text">{{ sid.subject }}</p>
        <p class="card-title">{{ sid.title_kor.substring(0,20) }}</p>
        <p class="card-text">
          by
          <!-- :class="{ selected: isSelected(index) }" -->
          <span class="card-author">{{ sid.main_author }}</span>
        </p>
      </div>
    </div>
  </router-link>
</template>

<script>
import Constant from "../../Constant.js";
import http from "@/http-common.js";
export default {
  data() {
    return {
      selectedCard: -1,
      
    };
  },
  props: {
    sid: {
      type: Object,
      required: true,
    },
  },
  created() {
    // console.log("개별 디스패치");
    // this.$store.dispatch(Constant.GET_NM, { sid: this.sid });
  },
  computed: {
    // scp() {
    //       console.log('개별 컴퓨티드');
    //   return this.$store.state.nmstore.nm;
    // },
  },
  methods: {
    hoverCard(selectedIndex) {
      this.selectedCard = selectedIndex;
      this.animateCards();
    },
    animateCards() {
      this.cards.forEach((card, index) => {
        const direction = this.calculateCardDirection(index, this.selectedCard);
        // TweenMax.to(this.$refs[`card_${index}`], 0.3, { x: direction * 50 });
      });
    },
    calculateCardDirection(cardIndex, selectedIndex) {
      if (selectedIndex === -1) {
        return 0;
      }

      const diff = cardIndex - selectedIndex;
      return diff === 0 ? 0 : diff / Math.abs(diff);
    },
    isSelected(cardIndex) {
      return this.selectedCard === cardIndex;
    },
  },
};
</script>

<style scoped>
body {
  background-color: #e1e7e7;
}

.card-row {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 780px;
  width: 100%;
  height: 500px;
}

.card {
  position: relative;
  background-color: #ffffff;
  height: 370px;
  width: 240px;
  margin: 10px;
  overflow: hidden;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.5);
  transition: height 0.3s, box-shadow 0.3s;
}

.card:hover {
  height: 410px;
  box-shadow: 20px 20px 40px 0px rgba(0, 0, 0, 0.5);
}

.card-image {
  /* center horizontally overflown image */
  position: absolute;
  left: -9999px;
  right: -9999px;
  margin: auto;

  height: 300px;
  min-width: 100%;
  transition: height 0.3s, opacity 0.3s;
}
.card-image.selected {
  height: 410px;
  opacity: 0.3;
}
.card-footer {
  position: absolute;
  bottom: 0;
  height: 130px;
  padding: 10px 15px;
  font-family: Helvetica;
}

.card-text {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.7);
}
.card-title {
  font-family: Serif;
}
.card-author {
  font-size: 14px;
  color: #bab096;
  transition: color 0.3s;
}
.card-author.selected {
  color: #6a6456;
}
</style>