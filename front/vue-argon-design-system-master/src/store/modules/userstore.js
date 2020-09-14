import Vuex from 'vuex';
import Vue from 'vue';
import router from '../../router';
import Constant from '../../Constant.js';
import http from '../../http-common.js';
Vue.use(Vuex);
const storage = window.sessionStorage;
const userstore = {
  state: {
    userNick: '',
    userid: '',
    token: '',
    followings: [],
    followers: [],
    messageList: [],
    users: [],
    news: [],
    logined: true,
    logining: false,
    loginError: '',
    mesDetail: [],
    bubbleS: '1',
    mesdetailid: "",
    mesviewdetail: false,
    bubbleNew: false,
    interest: [],
    usergit: '',
    userintro: '',
    recommendedPJT: [],
    recommendedUser: []
  },

  actions: {
    // 사이트init
    init: (store) => {

      if (window.localStorage.getItem("jwt-auth-token") !== '') {
        // 로그인 검증 폼 생기면 바꾸기
        store.commit('init', {
          userNick: window.localStorage.getItem("userNick"),
          userid: window.localStorage.getItem("userid"),
          token: window.localStorage.getItem('jwt-auth-token')
        })
        storage.setItem("jwt-auth-token", window.localStorage.getItem("jwt-auth-token"));
        storage.setItem("idvalid", window.localStorage.getItem("idvalid"));
        storage.setItem("userState", window.localStorage.getItem("userState"));
        storage.setItem("userid", window.localStorage.getItem("userid"));
        storage.setItem("userNick", window.localStorage.getItem("userNick"));
        storage.setItem("intro", window.localStorage.getItem("intro"));
        storage.setItem("usergit", window.localStorage.getItem("usergit"));
        store.dispatch("update")
        store.dispatch("getFollow");
        store.dispatch("getFollower");
      } else if (window.localStorage.getItem("autologin") === 't') {
        store.dispatch("login", {
          id: window.localStorage.getItem("id"),
          pw: window.localStorage.getItem("pw")
        });
      }
    },
    update: (store) => {
      // 메세지
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http.get('/api/message/' + storage.getItem("userid"), config).then(res => {
        store.commit('loadMesList', {
          messageList: res.data
        })
        // 알림
        http.get(`/api/message/message/${storage.getItem("userid")}/admin`, config).then(res => {
          if (res.data) {

            store.commit('loadNews', {
              list: res.data
            })
          }
        }).catch(exp => { })
      }).catch(exp => [])
    },
    // 유저 관련
    kakao: (store, payload) => {
      let num = payload.kakaoid * 1
      http.post('/api/userinfo/login/kakao', num).then(res => {
        if (res.data.data) {
          window.localStorage.setItem("jwt-auth-token", res.headers["jwt-auth-token"]);
          window.localStorage.setItem("userNick", res.data.data.nickname)
          window.localStorage.setItem("userid", res.data.data.id)
          window.localStorage.setItem("idvalid", "true"); //response.data.data.valid);
          window.localStorage.setItem("userState", res.data.data.state);
          window.localStorage.setItem("userintro", res.data.data.intro);
          window.localStorage.setItem("usergit", res.data.data.git);
          document.querySelector(".login").classList.remove('active')
          store.commit('loginError', {
            e: ''
          })
          storage.setItem('kakaosignup', 'f')
          storage.setItem('kakaosignupID', "")
          storage.setItem('kakaosignupEmail', "")
          store.dispatch("init")
          router.go()
        } else {
          window.localStorage.setItem("jwt-auth-token", "");
          window.localStorage.setItem("userNick", "")
          window.localStorage.setItem("userid", "")
          window.localStorage.setItem("idvalid", "");
          window.localStorage.setItem("userState", "");
          document.querySelector('.login').classList.remove('active')
          document.querySelector('body div').classList.remove('nav-open')
          storage.setItem('kakaosignup', 'true')
          storage.setItem('kakaosignupID', payload.kakaoid * 1)
          storage.setItem('kakaosignupEmail', payload.email)
          setTimeout(() => {
            router.push({
              path: '/signup'
            })
          }, 1000)
        }
        
      })
      // .catch(e => console.log(e))
    },
    login: (store, payload) => {
      http.post('/api/userinfo/signin', {
        id: payload.id,
        pw: payload.pw
      })
      .then(response => {
        if (response.data.data) {
          window.localStorage.setItem("jwt-auth-token", response.headers["jwt-auth-token"]);
          window.localStorage.setItem("userNick", response.data.data.nickname)
          window.localStorage.setItem("userid", response.data.data.id)
            window.localStorage.setItem("idvalid", "true"); //response.data.data.valid);
            window.localStorage.setItem("userState", response.data.data.state);
            window.localStorage.setItem("userintro", response.data.data.intro);
            window.localStorage.setItem("usergit", response.data.data.git);
            document.querySelector(".login").classList.remove('active')
            store.commit('loginError', {
              e: ''
            })
            store.dispatch("init")
            router.go()
          } else {
            window.localStorage.setItem("jwt-auth-token", "");
            window.localStorage.setItem("userNick", "")
            window.localStorage.setItem("userid", "")
            window.localStorage.setItem("idvalid", "");
            window.localStorage.setItem("userState", "");
            store.commit('loginError', {
              e: '아이디나 존재하지 않거나 비밀번호가 다릅니다.'
            })
          }
        })
      // .catch(exp => {
      //   store.commit('loginError', {
      //     e: '오류 발생' + exp
      //   })
      //   window.localStorage.setItem("jwt-auth-token", "");
      //   window.localStorage.setItem("userNick", "")
      //   window.localStorage.setItem("userid", "")
      // });
    },
    logout: (store) => {
      store.dispatch("init")
      router.go({
        path: '/main'
      });
      storage.setItem("jwt-auth-token", "");
      storage.setItem("userNick", "")
      storage.setItem("userid", "")
      window.localStorage.setItem("jwt-auth-token", "");
      window.localStorage.setItem("userNick", "")
      window.localStorage.setItem("userid", "")
      window.localStorage.setItem("autologin", "f")
    },
    signup: (store, payload) => {
      const dataURLtoFile = (dataurl, fileName) => {

        var arr = dataurl.split(','),
          mime = arr[0].match(/:(.*?);/)[1],
          bstr = atob(arr[1]),
          n = bstr.length,
          u8arr = new Uint8Array(n);

        while (n--) {
          u8arr[n] = bstr.charCodeAt(n);
        }

        return new File([u8arr], fileName, {
          type: mime
        });
      }

      //Usage example:
      let file2 = dataURLtoFile("data:image/png;base64,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", payload.id + '.png');

      window.localStorage.setItem("userid", payload.id)
      http
        .post("/api/userinfo/", {
          id: payload.id,
          pw: payload.pw,
          nickname: payload.nickname,
          name: payload.name,
          address1: payload.address1,
          address2: payload.address2,
          phone: payload.phone,
          git: payload.git,
          responsibility: payload.responsibility,
          state: true,
          kakaoId: payload.kakaoId,
          y: payload.y,
          x: payload.x
        })
        .then((res) => {
          http.post('/api/userinfo/signin', {
            id: payload.id,
            pw: payload.pw
          })
            .then(response => {
              if (response.data.data) {
                const config = {
                  headers: {
                    "jwt-auth-token": response.headers["jwt-auth-token"]
                  }
                }
                window.localStorage.setItem("jwt-auth-token", response.headers["jwt-auth-token"]);
                window.localStorage.setItem("userNick", response.data.data.nickname)
                window.localStorage.setItem("userid", response.data.data.id)
                window.localStorage.setItem("usergit", response.data.data.git)
                window.localStorage.setItem("userintro", response.data.data.intro)
                window.localStorage.setItem("idvalid", "true"); //response.data.data.valid);
                window.localStorage.setItem("userState", response.data.data.state);
                document.querySelector(".login").classList.remove('active')
                store.commit('loginError', {
                  e: ''
                })
                /////// 프로필 페이지 생성
                store.dispatch("init")
                store.commit('upBoardFiles', {
                  file: file2
                })
                store.dispatch(Constant.ADD_BOARD, {
                  //bno : auto increase
                  // bwriter : this.board.bwriter, 임시로 ssafy foreign key때문
                  bwriter: response.data.data.id,
                  btitle: response.data.data.nickname,
                  bcontent: "프로필 초기",
                  bview: "",
                  bfile: "",
                  bstate: "profile",
                  makeDay: new Date(),
                  // changeDay : this.board.changeday,
                  makeId: response.data.data.id,
                  // changeId : this.board.changeid

                });
                router.push({
                  path: "/main"
                })
                ////
                store.state.interest.forEach((el) => {
                  http
                    .post("/api/interest/", {
                      id: payload.id,
                      interest: el,
                    }, config).then(res => {

                    }).catch(e => { })
                })
              } else {
                window.localStorage.setItem("jwt-auth-token", "");
                window.localStorage.setItem("userNick", "")
                window.localStorage.setItem("userid", "")
                window.localStorage.setItem("usergit", "")
                window.localStorage.setItem("userintro", "")
                window.localStorage.setItem("idvalid", "true"); //response.data.data.valid);
                window.localStorage.setItem("userState", "");
                store.commit('loginError', {
                  e: '회원가입에 오류가 있습니다 문의해주세요'
                })
                document.querySelector('#spinner1122').classList.remove('active')
              }
            })
          // .catch(exp => {
          //   document.querySelector('#spinner1122').classList.remove('active')
          //   store.commit('loginError', {
          //     e: '오류 발생' + exp
          //   })
          //   storage.setItem("jwt-auth-token", "");
          //   storage.setItem("userNick", "")
          //   storage.setItem("userid", "")
          // });




        })
      // .catch((e) => {
      //   document.querySelector('#spinner1122').classList.remove('active')

      // });
    },

    getFollow: (store, payload) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http
        .get("/api/userinfo/", config)
        .then((response) => {

          http.get('/api/following/' + storage.getItem("userid"), {
            headers: {
              "jwt-auth-token": storage.getItem("jwt-auth-token")
            }
          }).then(res => {
            store.commit('loadfollowings', {
              followings: res.data,
              users: response.data
            })
            res.data.forEach(item => {
              // store.dispatch(Constant.GET_CHATROOMONETOONE, {
              //   uid1: storage.getItem("userid"),

              //   uid2: item.target,

              // });
            })
          }).catch(exp => { })
        })
      // .catch((exp) => alert("에러" + exp));
    },

    getFollower: (store) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http
        .get("/api/userinfo/", config)
        .then((response) => {

          http.get('/api/following/target/' + storage.getItem("userid"), {
            headers: {
              "jwt-auth-token": storage.getItem("jwt-auth-token")
            }
          }).then(res => {
            store.commit('loadfollowers', {
              followers: res.data,
              users: response.data
            })

            // res.data.forEach(item => {
            //   store.dispatch(Constant.GET_CHATROOMONETOONE, {
            //     uid1: storage.getItem("userid"),
            //     uid2: item.target,
            //   });
            // })
          }).catch(exp => { })
        })
      // .catch((exp) => alert("에러" + exp));
    },
    getRecommendedUser: (store) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http
        .get("/api/userinfo/", config)
        .then((response) => {
          // console.log("보냈어!");
          http.get('/api/userinfo/getRecommended/User/' + storage.getItem("userid"), {
            headers: {
              "jwt-auth-token": storage.getItem("jwt-auth-token")
            }
          }).then(res => {
            // console.log("받아줘!");
            store.commit('loadRecommendedUser', {
              recommendedUser: res.data,
              users: response.data
            })

            // res.data.forEach(item => {
            //   store.dispatch(Constant.GET_CHATROOMONETOONE, {
            //     uid1: storage.getItem("userid"),
            //     uid2: item.target,
            //   });
            // })
          }).catch(exp => { })
        })
      // .catch((exp) => alert("에러가 발생했습니다." + exp));
    },
    getRecommendedPJT: (store) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }

      http
        .get("/api/userinfo/", config)
        .then((response) => {
          // console.log("보냈다고!");
          http.get('/api/userinfo/getRecommended/PJT/' + storage.getItem("userid"), {
            headers: {
              "jwt-auth-token": storage.getItem("jwt-auth-token")
            }
          }).then(res => {
            // console.log("받아줘!");
            store.commit('loadRecommendedPJT', {
              recommendedPJT: res.data,
              users: response.data
            })

            // res.data.forEach(item => {
            //   store.dispatch(Constant.GET_CHATROOMONETOONE, {
            //     uid1: storage.getItem("userid"),
            //     uid2: item.target,
            //   });
            // })
          }).catch(exp => { })
        })
      // .catch((exp) => alert("에러가 발생했습니다." + exp));
    },
    leave: (store, payload) => {

      let config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }

      http.post('/api/userinfo/signin', {
        id: storage.getItem("userid"),
        pw: payload.pw,
      }, config)
        .then(response => {
          if (response.data.data) {
            http.delete('api/userinfo/' + storage.getItem("userid"), config = {
              headers: {
                "jwt-auth-token": storage.getItem("jwt-auth-token")
              }
            })
              .then(() => {

                store.dispatch("logout");
                router.push({
                  path: "/main"
                });
              }).catch(exp => { })
          } else {
            alert("비밀번호가 다릅니다.")
          }
        })
      // .catch(exp => {
      //   alert("오류가 발생했습니다." + exp)
      // })
    },
    follow: (store, payload) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http.post('/api/following/', {
        target: payload.target,
        uid: storage.getItem("userid")
      }, config).then(res => {
        store.commit('newFollow', {
          followings: res.data
        })
        alert('팔로우 되었습니다!')
        store.dispatch('getFollow')
      }).catch(exp => { })
    },
    delFollow: (store, payload) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      // console.log(config + " " + payload.target + " " + window.localStorage.getItem('userid'));
      http.delete('/api/following/delete/' + payload.uid + "/" + payload.target, config).then(res => {
        alert("팔로우가 취소되었습니다");
        store.dispatch('getFollow')
      }).catch(exp => { })
    },
    // 메세지
    sendMes: (store, payload) => {

      if (!payload.content) {
        if (!storage.getItem("jwt-auth-token")) {
          alert("로그인이 필요합니다.")
          document.querySelector(".login").classList.remove("active");
          document.querySelector(".login").classList.add("active");
        } else {
          document.querySelector(".bubble").classList.remove("active")
          document.querySelector(".bubble").classList.add("active")
          store.commit('bubbleState', {
            st: '4'
          })
          store.commit("viewMes", {
            id: payload.toUser,
            view: true
          })
          store.dispatch("detailMes", {
            other: payload.toUser
          });
        }
      } else if (payload.other) {
        const config = {
          headers: {
            "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
          }
        }
        http.post('/api/message/', {
          content: payload.content,
          fromUser: storage.getItem("userid"),
          toUser: payload.other,
          read: false,
        }, config)
          .then(response => {
            store.commit('pushDetailMes', {
              mes: {
                fromUser: storage.getItem("userid"),
                time: "방금",
                content: payload.content,
                mnum: 9999999
              }
            })
          })
        // .catch(exp => {
        //   alert('메세지 전송에 실패하였습니다.' + exp)
        // });
      }

    },
    detailMes: (store, payload) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http.get(`/api/message/message/${storage.getItem("userid")}/${payload.other}`, config).then(res => {
        store.commit('loadDetailMes', {
          list: res.data
        })
      }).catch(exp => { })
    },
    delMes: (store, payload) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http.delete(`/api/message/${payload.mnum}`, config).then(res => {
        alert("메세지가 삭제되었습니다." + res.data)
      }).catch(exp => { })
    },
    mesRead: (store, payload) => {
      const config = {
        headers: {
          "jwt-auth-token": window.sessionStorage.getItem("jwt-auth-token")
        }
      }
      http.put(`/api/message/${payload.mnum}`, {
        read: true,
        mnum: payload.mnum,
        fromUser: "admin",
        toUser: storage.getItem("userid")
      }, config).then(res => { }).catch(exp => { })
    },
  },

  mutations: {
    loginError: (state, payload) => {
      state.loginError = payload.e;
      state.logining = false;
    },
    loadMesList: (state, payload) => {
      if (storage.getItem("userid") !== "admin") {
        state.messageList = payload.messageList.filter(item => item.fromUser !== "admin" && item.toUser !== "admin");
      } else {
        state.messageList = payload.messageList;
      }
      state.bubbleNew = false
      if (state.messageList.find(item => item.fromUser !== storage.getItem("userid") && item.read === false)) {
        state.bubbleNew = true
      }
    },
    loadDetailMes: (state, payload) => {
      state.mesDetail = payload.list;
    },
    loadNews: (state, payload) => {
      state.news = payload.list.filter(item => item.fromUser == "admin");
      if (!state.bubbleNew) {
        if (state.news.find(item => item.read === false)) {
          state.bubbleNew = true
        }
      }
    },
    pushDetailMes: (state, payload) => {
      if (typeof (state.mesDetail) == typeof ([])) {
        state.mesDetail.push(payload.mes);
      } else {
        state.mesDetail = [payload.mes];
      }
    },
    loadfollowings: (state, payload) => {
      let tmp = [];
      payload.followings.forEach(item => {
        tmp.push(item.target)
      })
      state.followings = payload.users.filter(item => item.leaveUser === false).filter(item =>
        (tmp.indexOf(item.id) > -1)
      );
    },
    loadfollowers: (state, payload) => {
      let tmp = [];
      payload.followers.forEach(item => {
        tmp.push(item.uid)
      })
      state.followers = payload.users.filter(item => item.leaveUser === false).filter(item =>
        (tmp.indexOf(item.id) > -1)
      );
    },
    loadRecommendedUser: (state, payload) => {
      let tmp = [];
      payload.recommendedUser.forEach(item => {
        tmp.push(item.id)
      })
      state.recommendedUser = payload.users.filter(item => item.leaveUser === false).filter(item =>
        (tmp.indexOf(item.id) > -1)
      );
    },
    loadRecommendedPJT: (state, payload) => {
      // let tmp = [];
      // payload.recommendedPJT.forEach(item => {
      //   tmp.push(item)
      // })
      state.recommendedPJT = payload.recommendedPJT;
      // state.recommendedUser = payload.users.filter(item => item.leaveUser === false).filter(item =>
      //   (tmp.indexOf(item.id) > -1)
      // );
    },
    newFollow: (state, payload) => {
      state.followings.push(payload.followings);
    },
    loadUsers: (state, payload) => {
      state.users = payload.users.filter(item => item.leaveUser === false);
    },
    init: (state, payload) => {
      if (state.userid !== window.localStorage.getItem('userid')) {
        state.userNick = payload.userNick;
        state.userid = payload.userid;
        state.token = payload.token
        state.mesDetail = [];
        state.followings = [];
        state.messageList = [];
        state.users = [];
        state.news = [];
      }
    },
    interest: (state, payload) => {
      state.interest = payload.picks
    },

    viewMes: (state, payload) => {
      state.mesdetailid = payload.id
      state.mesviewdetail = payload.view
    },
    bubbleState: (state, payload) => {
      state.bubbleS = payload.st
    },
  },

  modules: {}
};

export default userstore;
