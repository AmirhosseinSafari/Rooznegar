<template>
    <div>
        <div class="">
            <p v-if="news.length === 0">No Messages</p>

            <div class="tile is-ancestor">

                <div class="tile is-parent">
                    <!-- <a v-if="news[1]" v-bind:href="`${news[1].url}`"> -->
                        <article v-if="news[1]" class="tile is-child box boxbox">
                            <!--<img class="image is-1by1" v-bind:src="`${news[0].image}`">-->
                            <p class="title">{{news[1].title}}</p>
                            <p class="subtitle">{{news[1].news_time}}</p>
                            <div class="content">
                                <p>{{news[1].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[1].predicted_category}}
                            </span>
                            <span class="tag tagtag">
                                {{news[1].source}}
                            </span>
                        </article>
                    <!-- </a> -->
                </div>

                <div class="tile is-parent is-6">
                    <!-- <a v-if="news[0]" v-bind:href="`${news[0].url}`"> -->
                        <article v-if="news[0]" class="tile is-child is-centered box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[0].image}`">
                            <p class="title">{{news[0].title}}</p>
                            <p class="subtitle">{{news[0].news_time}}</p>
                            <div class="content">
                                <p>{{news[0].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[0].predicted_category}}
                            </span>
                            <span class="tag tagtag">
                                {{news[0].source}}
                            </span>
                        </article>
                    <!-- </a> -->
                </div>

                <div class="tile is-parent">
                    <!-- <a v-if="news[2]" v-bind:href="`${news[2].url}`"> -->
                        <article v-if="news[2]" class="tile is-child box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[2].image}`">
                            <p class="title">{{news[2].title}}</p>
                            <p class="subtitle">{{news[2].news_time}}</p>
                            <div class="content">
                                <p>{{news[2].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[2].predicted_category}}
                            </span>
                            <span class="tag tagtag">
                                {{news[2].source}}
                            </span>
                        </article>
                    <!-- </a> -->
                </div>

            </div><!-- end of 3 part row -->

            
            <div class="tile is-ancestor">

                <div class="tile is-parent is-5">
                    <!-- <a v-if="news[3]" v-bind:href="`${news[3].url}`"> -->
                        <article v-if="news[3]" class="tile is-child box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[3].image}`">
                            <p class="title">{{news[3].title}}</p>
                            <p class="subtitle">{{news[3].news_time}}</p>
                            <div class="content">
                                <p>{{news[3].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[3].predicted_category}}
                            </span>
                            <span class="tag tagtag">
                                {{news[3].source}}
                            </span>
                        </article>
                    <!-- </a> -->
                </div>

                <div class="tile is-parent is-5">
                    <!-- <a v-if="news[5]" v-bind:href="`${news[5].url}`"> -->
                        <article v-if="news[5]" class="tile is-child is-centered box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[5].image}`">
                            <p class="title">{{news[5].title}}</p>
                            <p class="subtitle">{{news[5].news_time}}</p>
                            <div class="content">
                                <p>{{news[5].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[5].predicted_category}}
                            </span>
                            <span class="tag tagtag">
                                {{news[5].source}}
                            </span>
                        </article>
                    <!-- </a> -->
                </div>

                <div class="tile is-parent is-2">
                    <!-- <a v-if="news[4]" v-bind:href="`${news[4].url}`"> -->
                        <article v-if="news[4]" class="tile is-child box boxbox">
                            <img class="image is-1by1" v-bind:src="`${news[4].image}`">
                            <p class="title">{{news[4].title}}</p>
                            <p class="subtitle">{{news[4].news_time}}</p>
                            <div class="content">
                                <p>{{news[4].short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{news[4].predicted_category}}
                            </span>
                            <span class="tag tagtag">
                                {{news[4].source}}
                            </span>
                        </article>
                    <!-- </a> -->
                </div>

            </div><!-- end of 3 part row -->

            <div class="tile is-ancestor">
                <div class="tile is-parent is-4">
                    <!-- <a v-if="news[6]" v-bind:href="`${news[6].url}`"> -->
                    <article v-if="news[6]" class="tile is-child box boxbox">
                        <img class="image is-1by1" v-bind:src="`${news[6].image}`">
                        <p class="title">{{news[6].title}}</p>
                        <p class="subtitle">{{news[6].news_time}}</p>
                        <div class="content">
                            <p>{{news[6].short_description}}</p>
                        </div>
                        <span class="tag tagtag">
                            موضوع: {{news[6].predicted_category}}
                        </span>
                        <span class="tag tagtag">
                            {{news[6].source}}
                        </span>
                    </article>
                    <!-- </a> -->
                </div>
                <div class="tile is-parent">
                    <!-- <a v-if="news[7]" v-bind:href="`${news[7].url}`"> -->
                    <article v-if="news[7]" class="tile is-child box boxbox">
                        <img class="image is-1by1" v-bind:src="`${news[7].image}`">
                        <p class="title">{{news[7].title}}</p>
                        <p class="subtitle">{{news[7].news_time}}</p>
                        <div class="content">
                            <p>{{news[7].short_description}}</p>
                        </div>
                        <span class="tag tagtag">
                            موضوع: {{news[7].predicted_category}}
                        </span>
                        <span class="tag tagtag">
                            {{news[7].source}}
                        </span>
                    </article>
                    <!-- </a> -->
                </div>
            </div>
            <!-- end of 2 part in a row  -->
            
            <div class="tile is-ancestor">

                <div class="tile is-parent is-8">
                    <!-- <a v-if="news[10]" v-bind:href="`${news[10].url}`"> -->
                    <article v-if="news[10]" class="tile is-child box boxbox">
                        <img class="image is-1by1" v-bind:src="`${news[10].image}`">
                        <p class="title">{{news[10].title}}</p>
                        <p class="subtitle">{{news[10].news_time}}</p>
                        <div class="content">
                            <p>{{news[10].short_description}}</p>
                        </div>
                        <span class="tag tagtag">
                            موضوع: {{news[10].predicted_category}}
                        </span>
                        <span class="tag tagtag">
                            {{news[10].source}}
                        </span>
                    </article>
                    <!-- </a> -->
                </div>

                <div class="tile is-4 is-vertical is-parent">
                    
                    <!-- <a v-if="news[8]" v-bind:href="`${news[8].url}`"> -->
                    <article v-if="news[8]" class="tile is-child box boxbox">
                        <!-- <img class="image is-1by1" v-bind:src="`${news[8].image}`"> -->
                        <p class="title">{{news[8].title}}</p>
                        <p class="subtitle">{{news[8].news_time}}</p>
                        <div class="content">
                            <p>{{news[8].short_description}}</p>
                        </div>
                        <span class="tag tagtag">
                            موضوع: {{news[8].predicted_category}}
                        </span>
                        <span class="tag tagtag">
                            {{news[8].source}}
                        </span>
                    </article>
                    <!-- </a> -->
                    
                    <!-- <a v-if="news[9]" v-bind:href="`${news[9].url}`"> -->
                    <article v-if="news[9]" class="tile is-child box boxbox">
                        <!-- <img class="image is-1by1" v-bind:src="`${news[9].image}`"> -->
                        <p class="title">{{news[9].title}}</p>
                        <p class="subtitle">{{news[9].news_time}}</p>
                        <div class="content">
                            <p>{{news[9].short_description}}</p>
                        </div>
                        <span class="tag tagtag">
                            موضوع: {{news[9].predicted_category}}
                        </span>
                        <span class="tag tagtag">
                            {{news[9].source}}
                        </span>
                    </article>
                    <!-- </a> -->
                </div>

            </div><!-- end of 3 -->

            <!-- for news -->
            <div class="tile is-ancestor is-flex-wrap-wrap">
                <div class="tile is-parent is-3 is-vertical" v-for="(n, index) in sliceItems(11 ,30)" :key="index">
                        <!-- <a v-if="news[index+2]" v-bind:href="`${news[index+2].url}`"> -->
                        <article v-if="n" class="tile is-child box boxbox">
                            <img class="image is-1by1" v-bind:src="`${n.image}`">
                            <p class="title">{{n.title}}</p>
                            <p class="subtitle">{{n.news_time}}</p>
                            <div class="content">
                                <p>{{n.short_description}}</p>
                            </div>
                            <span class="tag tagtag">
                                موضوع: {{n.predicted_category}}
                            </span>

                            <span class="tag tagtag">
                                {{n.source}}
                            </span>
                        </article>
                        <!-- </a> -->
                    
                </div>
            </div>
            
            <!-- here is for adding the load next 30 news (how to detect user scrold till the tend of page) (also reload icon)-->
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

    methods: {
        ...mapActions(["getNextNews"]),
        sliceItems: function (start, end) {
            return this.news.slice(start, end);
        }
    }
    //methods: mapActions('news', []),

    //created() {
    //    this.$store.dispatch('news/getNews')
    //}

}

</script>

<style scoped>
img{
    display: initial;
    padding-top: 0 !important;
    padding-bottom: 3%;
}

.boxbox{
    border: 1px solid #00d1b2 !important;
    /* box-shadow: 0px 0px 4px 1px #00D1B2; */
}

.tagtag{
    color: #45a29e !important;
    margin: 1%;
}
</style>