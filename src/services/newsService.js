import api from '@/services/api'

export default {
    fetchNews() {
        return api.get('news/')
                    .then(response => response.data)
    }
}