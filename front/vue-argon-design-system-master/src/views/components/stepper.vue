<template>
<div class="steps">
  <div class="step">
    <div class="step-header">
      <div class="header">Hello This is step one!</div>
      <div class="subheader">Hopefully this looks cool</div>
    </div>
    <div class="step-content one">
      <button class="next-btn">Next</button>
    </div>
  </div>
  <div class="step minimized">
    <div class="step-header">
      <div class="header">This is step two!</div>
      <div class="subheader">The content is a little bigger!</div>
    </div>
    <div class="step-content two">
      <button class="next-btn">Next</button>
    </div>
  </div>
  <div class="step minimized">
    <div class="step-header">
      <div class="header">And finally step three!</div>
      <div class="subheader">Last but not the least!</div>
    </div>
    <div class="step-content three">
      <button class="close-btn">Close</button>
    </div>
  </div>
</div>
  
</template>

<script>
export default {
    mounted() {
        let curOpen;

$(document).ready(function() {
  curOpen = $('.step')[0];
  
  $('.next-btn').on('click', function() {
    let cur = $(this).closest('.step');
    let next = $(cur).next();
    $(cur).addClass('minimized');
    setTimeout(function() {
      $(next).removeClass('minimized');
      curOpen = $(next);
    }, 400);
  });
  
  $('.close-btn').on('click', function() {
    let cur = $(this).closest('.step');
    $(cur).addClass('minimized');
    curOpen = null;
  });
  
  $('.step .step-content').on('click' ,function(e) {
    e.stopPropagation();
  });
  
  $('.step').on('click', function() {
    if (!$(this).hasClass("minimized")) {
      curOpen = null;
      $(this).addClass('minimized');
    }
    else {
      let next = $(this);
      if (curOpen === null) {
        curOpen = next;
        $(curOpen).removeClass('minimized');
      }
      else {
        $(curOpen).addClass('minimized');
        setTimeout(function() {
          $(next).removeClass('minimized');
          curOpen = $(next);
        }, 300);
      }
    }
  });
})
    },
}
</script>

<style>
:root {
  --background-color: #FFFFFF;
  --primary-color: #E66A53;
}

*{
  box-sizing: border-box;
}

body {
  margin: 0;
  height: 100%;
  width: 100vw;
  background-color: rgba(0, 0, 0, 0.08);
  font-family: Arial;
  display: flex;
}

.steps {
  width: 500px;
  box-shadow: 0px 10px 15px -5px rgba(0, 0, 0, 0.3);
  background-color: #FFF;
  padding: 24px 0;
  position: relative;
  margin: auto;
}

.steps::before {
  content: '';
  position: absolute;
  top: 0;
  height: 24px;
  width: 1px;
  background-color: rgba(0, 0, 0, 0.2);
  left: calc(50px / 2);
  z-index: 1;
}

.steps::after {
  content: '';
  position: absolute;
  height: 13px;
  width: 13px;
  background-color: var(--primary-color);
  box-shadow: 0px 0px 5px 0px var(--primary-color);
  border-radius: 15px;
  left: calc(50px / 2);
  bottom: 24px;
  transform: translateX(-45%);
  z-index: 2;
}

.step {
  padding: 0 20px 24px 50px;
  position: relative;
  transition: all 0.4s ease-in-out;
  background-color: #FFF;
}

.step::before {
  content: '';
  position: absolute;
  height: 13px;
  width: 13px;
  background-color: rgb(198, 198, 198);
  border-radius: 15px;
  left: calc(50px / 2);
  transform: translateX(-45%);
  z-index: 2;
}

.step::after {
  content: '';
  position: absolute;
  height: 100%;
  width: 1px;
  background-color: rgb(198, 198, 198);
  left: calc(50px / 2);
  top: 0;
  z-index: 1;
}

.step.minimized {
  background-color: #FFF;
  transition: background-color 0.3s ease-in-out;
  cursor: pointer;
}

.header {
  user-select: none;
  font-size: 16px;
  color: rgba(0, 0, 0, 0.6);
}

.subheader {
  user-select: none;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.4);
}

.step-content {
  transition: all 0.3s ease-in-out;
  overflow: hidden;
  position: relative;
}

.step.minimized > .step-content {
  height: 0px;
}

.step-content.one {
  height: 460px;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
  margin-top: 10px;
}

.step-content.two {
  height: 600px;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
  margin-top: 10px;
}

.step-content.three {
  height: 400px;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
  margin-top: 10px;
}

.next-btn {
  position: absolute;
  top: 50%;
  left: 50%;
  border: 0;
  padding: 10px 20px;
  border-radius: 4px;
  background-color: red;
  box-shadow: 0 5px 10px -3px rgba(0, 0, 0, 0.3);
  color: #FFF;
  transition: background-color 0.3s ease-in-out;
  cursor: pointer;
  transform: translate(-50%, -50%);
}

.close-btn {
  position: absolute;
  top: 50%;
  left: 50%;
  border: 0;
  padding: 10px 20px;
  border-radius: 4px;
  background-color: rgb(255, 0, 255);
  box-shadow: 0 5px 10px -3px rgba(0, 0, 0, 0.3);
  color: #FFF;
  transition: background-color 0.3s ease-in-out;
  cursor: pointer;
  transform: translate(-50%, -50%);
}

/* Irrelevant styling things */
.close-btn:hover {
  background-color: rgba(255, 0, 255, 0.6);
}

.close-btn:focus {
  outline: 0;
}

.next-btn:hover {
  background-color: rgba(255, 0, 0, 0.6);
}

.next-btn:focus {
  outline: 0;
}

.step.minimized:hover {
  background-color: rgba(0, 0, 0, 0.06);
}
</style>