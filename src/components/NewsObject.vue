<template> 
    <!-- <a v-if="news[1]" v-bind:href="`${news[1].url}`"> -->
    <article v-if="newsObject" class="tile is-child box boxbox">
        <img class="image is-1by1" v-bind:src="`${newsObject.image}`">
        <p class="title">{{newsObject.title}}</p>
        <p class="subtitle">{{newsObject.news_time}}</p>
        <div class="content">
            <p>{{newsObject.short_description}}</p>
        </div>
        <span class="tag tagtag">
            موضوع: {{newsObject.predicted_category}}
        </span>
        <span class="tag tagtag">
            {{newsObject.source}}
        </span>
    </article>
    <!-- </a> -->
</template>

<script>
export default {
  name: "NewsObject",
  props: {
    newsObject: {
        type: Object,
        default: () => ({})
    }
  },
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

