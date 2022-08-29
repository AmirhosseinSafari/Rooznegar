import newsService from "../../services/newsService"

const state = {
    news: [],
    news_next: [],
    today_date: "",
    page: 2,
    page_total_count: 2
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
        // console.log(state.page_total_count);
        if (state.page <= state.page_total_count){
        newsService.fetchNextNews(state.page)
         .then((data) => {
            commit('setNextNews', data)
        })
    }
    }
}

const mutations = {
    setNews (state, data) {
        state.news = data.news;
        state.today_date = data.today_date;
        state.page_total_count = parseInt(data.page_total_count);
    },
    setNextNews (state, data) {
        state.news = state.news.concat(data.data.news);
        state.page = state.page + 1;
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }