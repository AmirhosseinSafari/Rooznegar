import newsService from "../../services/newsService"

const state = {
    news: []
}

const getters = {
    news: state => {
        return state.news
    }
}

const actions = {
    getNews ({ commit }) {
        newsService.fetchNews()
         .then(news => {
            commit('setNews', news)
         })
    },
}

const mutations = {
    setNews (state, news) {
        state.news = news
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }