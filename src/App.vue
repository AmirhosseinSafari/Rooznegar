<template>
  <div id="app">
    <div id="nav">
      <section class="hero is-primary">
        <div class="hero-body">
          <p class="title">
            روزنگار
          </p>
          <p class="subtitle">
            خبرنامه‌ی آنلاین برگرفته از چندین روزنامه‌ی داخلی ایران
          </p>
        </div>
      </section>
      
      <hr>
        <div>
            {{today_date}}
        </div>
      <hr>

    </div>

    <div class="contetnt">
      <router-view/>
    </div>

  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

hr{
  background-color: #00d1b2 !important;
  margin: 0.5rem 0 !important;
}

.contetnt{
  padding: 0 2%;
}

</style>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "App",

    computed: mapState({
        today_date: state => state.news.today_date
    }),
    methods: mapActions('news', []),

    created() {
        this.$store.dispatch('news/getNews')
    }

}
</script>