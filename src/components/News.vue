<template>
    <div>
        <div class="">
            <p v-if="news.length === 0">No Messages</p>

            <div class="tile is-ancestor">
                <div class="tile is-parent">
                    <a v-bind:href="`${news[1].url}`">
                        <article class="tile is-child box boxbox">
                            <!--<img class="image is-1by1" v-bind:src="`${news[0].image}`">-->
                            <p class="title">{{news[1].title}}</p>
                            <p class="subtitle">{{news[1].news_time}}</p>
                            <div class="content">
                                <p>{{news[1].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[1].predicted_category}}
                            </span>
                        </article>
                    </a>
                </div>

                <div class="tile is-parent is-6">
                    <a v-bind:href="`${news[0].url}`">
                        <article class="tile is-child is-centered box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[0].image}`">
                            <p class="title">{{news[0].title}}</p>
                            <p class="subtitle">{{news[0].news_time}}</p>
                            <div class="content">
                                <p>{{news[0].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[0].predicted_category}}
                            </span>
                        </article>
                    </a>
                </div>

                <div class="tile is-parent">
                    <a v-bind:href="`${news[2].url}`">
                        <article class="tile is-child box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[2].image}`">
                            <p class="title">{{news[2].title}}</p>
                            <p class="subtitle">{{news[2].news_time}}</p>
                            <div class="content">
                                <p>{{news[2].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[2].predicted_category}}
                            </span>
                        </article>
                    </a>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "News",

    computed: mapState({
        news: state => state.news.news,
    }),
    //methods: mapActions('news', []),

    //created() {
    //    this.$store.dispatch('news/getNews')
    //}

}

</script>

<style scoped>
img{
    padding-top: 0 !important;
    padding-bottom: 3%;
}

.boxbox{
    border: 1px solid #00d1b2 !important;
    /* box-shadow: 0px 0px 4px 1px #00D1B2; */
}

.tagtag{
    color: #45a29e !important;
}
</style>