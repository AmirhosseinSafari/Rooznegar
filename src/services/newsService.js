import api from '@/services/api'

export default {
    fetchNews() {
        return api.get('news/')
                    .then(response => response.data)
    },

    fetchNextNews(page) {
        // http://localhost:8000/api/news/?page=2
        return api.get(`news/?page=${page}`)
    }
}