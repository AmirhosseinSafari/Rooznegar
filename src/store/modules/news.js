import newsService from "../../services/newsService"

const state = {
    news: [],
    today_date: ""
}

const getters = {
    news: state => {
        return state.news
    }
}

const actions = {
    getNews ({ commit }) {
        newsService.fetchNews()
         .then((news, today_date) => {
            commit('setNews', news, today_date)
         })
    },
}

const mutations = {
    setNews (state, news, today_date) {
        state.news = news.news,
        state.today_date = news.today_date
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }