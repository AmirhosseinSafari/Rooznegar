<template>
    <div class="">
        <p v-if="news.length === 0">No Messages</p>
        <div class="" v-for="(n, index) in news" :key="index">
            <p class="">[{{index}}]</p>
            <p class="" v-html="n.title"></p>
            <p class="" v-html="n.url"></p>
            <p class="" v-html="n.news_time"></p>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "News",

    computed: mapState({
        news: state => state.news.news
    }),
    methods: mapActions('news', []),

    created() {
        this.$store.dispatch('news/getNews')
    }

}

</script>

<style>

</style>