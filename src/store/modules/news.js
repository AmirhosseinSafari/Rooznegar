import newsService from "../../services/newsService"

const state = {
    news: [],
    news_next: [],
    today_date: "",
    page: 2,
    page_total_count: 2,
    showLoading: "",
}

const getters = {
    news: state => {
        return state.news
    }
}

const actions = {
    getNews ({ commit }) {
        let payload = true
        commit('setLoading', payload)

        newsService.fetchNews()
         .then((data) => {
            commit('setNews', data)
            payload = false
            commit('setLoading', payload)
        })
    },
    getNextNews ({commit}) {
        // console.log(state.page_total_count);
        let payload = true
        commit('setLoading', payload)
        if (state.page <= state.page_total_count){
        newsService.fetchNextNews(state.page)
         .then((data) => {
            commit('setNextNews', data)
            payload = false
            commit('setLoading', payload)
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
    // setNoInternet (state, res) {
    //     //console.log(res.statusCode);
    // },
    setNextNews (state, data) {
        state.news = state.news.concat(data.data.news);
        state.page = state.page + 1;
    },
    setLoading(state, payload) {
        //console.log(payload);
        state.showLoading = payload;
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }