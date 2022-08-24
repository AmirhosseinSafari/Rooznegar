import newsService from "../../services/newsService"

const state = {
    news: [],
    today_date: "",
    page: 2
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
    getNextNews ({commit}) {
        newsService.fetchNextNews(state.page)
         .then((data) => {
            commit('setNews', data)
         })
    }
}

const mutations = {
    setNews (state, data) {
        state.news = data.news,
        state.today_date = data.today_date
    },
    setNextNews (state, data) {
        state.news.push(data.news),
        state.today_date = data.today_date,
        state.page = state.page + 1
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }