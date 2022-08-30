<template>
    <div>
        <div id="content_news" ref="content_news">
            <p v-if="news.length < 30">
                ...در حال بارگیری
            </p>

            <div class="tile is-ancestor">

                <div class="tile is-parent">
                    <NewsObject :newsObject="news[1]" />
                </div>

                <div class="tile is-parent is-6">
                    <NewsObject :newsObject="news[0]" />
                </div>

                <div class="tile is-parent">
                    <NewsObject :newsObject="news[2]" />
                </div>

            </div><!-- end of 3 part row -->

            
            <div class="tile is-ancestor">

                <div class="tile is-parent is-5">
                    <NewsObject :newsObject="news[3]" />
                </div>

                <div class="tile is-parent is-5">
                    <NewsObject :newsObject="news[5]" />
                </div>

                <div class="tile is-parent is-2">
                    <NewsObject :newsObject="news[4]" />
                </div>

            </div><!-- end of 3 part row -->

            <div class="tile is-ancestor">
                <div class="tile is-parent is-4">
                    <NewsObject :newsObject="news[6]" />
                </div>
                <div class="tile is-parent">
                    <NewsObject :newsObject="news[7]" />
                </div>
            </div>
            <!-- end of 2 part in a row  -->
            
            <div class="tile is-ancestor">
                <div class="tile is-parent">
                    <NewsObject :newsObject="news[8]" />
                </div>
                <div class="tile is-parent is-4">
                    <NewsObject :newsObject="news[9]" />
                </div>
            </div>
            <!-- end of 2 part in a row  -->
            <!-- <div class="tile is-ancestor">

                <div class="tile is-parent is-8">
                    <NewsObject :newsObject="news[10]" />
                </div>

                <div class="tile is-4 is-vertical is-parent">
                    
                    <NewsObject :newsObject="news[8]" />
                    
                    <NewsObject :newsObject="news[9]" />
                </div>

            </div>end of 3 -->

            <!-- for news -->
            <div class="tile is-ancestor is-flex-wrap-wrap">
                <div class="tile is-parent is-3 is-vertical" v-for="(n, index) in sliceItems(10 ,30)" :key="index">
                    <NewsObject :newsObject="n" />
                </div>
            </div>
            
            <!-- here is for adding the load next 30 news (how to detect user scrold till the tend of page) (also reload icon)-->

            <div v-if="news[31]" class="tile is-ancestor is-flex-wrap-wrap">
                <div class="tile is-parent is-3 is-vertical" v-for="(n, index) in sliceItems(30 , news.length)" :key="index">
                    <NewsObject :newsObject="n" />
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import NewsObject from './NewsObject.vue'

export default {
    name: "News",

    computed: mapState({
        news: state => state.news.news,
    }),

    components: {
        NewsObject
    },
    
    mounted() {
        this.$nextTick( () => {
            //console.log(this.$refs.content_news)
            window.addEventListener("scroll", () => {
            
            var totalPageHeight = document.body.scrollHeight; 
            var scrollPoint = window.scrollY + window.innerHeight;

            if(scrollPoint >= totalPageHeight)
            {   
                //console.log("at bottom");
                this.getNextNews()
            }
        }, { passive: false });
        })
    },

    methods: {
        ...mapActions('news', ["getNextNews"]),
        sliceItems: function (start, end) {
            return this.news.slice(start, end);
        },
    },

}

</script>

<style scoped>

</style>