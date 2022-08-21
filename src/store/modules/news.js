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
         .then((data) => {
            commit('setNews', data)
         })
    },
}

const mutations = {
    setNews (state, data) {
        state.news = data.news,
        state.today_date = data.today_date
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }