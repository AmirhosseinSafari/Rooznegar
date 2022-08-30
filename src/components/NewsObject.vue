<template> 
    <!-- <a v-if="news[1]" v-bind:href="`${news[1].url}`"> -->
    <article v-if="newsObject" class="tile is-child box boxbox">
        <img class="image is-1by1" v-bind:src="`${newsObject.image}`">
        <p class="title">{{newsObject.title}}</p>
        <p class="subtitle">{{newsObject.news_time}}</p>
        <div class="content">
            <p>{{newsObject.short_description}}</p>
        </div>

        <div id="id_handler" style="display: none;">
            {{newsObject.id}}
        </div>

        <button
            class="js-modal-trigger button is-primary" 
            :data-target="newsObject.id">
            بیشتر بخوانید
        </button>
        <br />

        <span class="tag tagtag">
            موضوع: {{newsObject.predicted_category}}
        </span>
        <span class="tag tagtag">
            {{newsObject.source}}
        </span>

        <div class="modal" :id="newsObject.id">
            <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head" style="justify-content: center;">
                    <p class="modal-card-title" style="display: contents;">{{newsObject.title}}</p>
                    <button class="delete" aria-label="close"></button>
                </header>
                <section class="modal-card-body">
                    <!-- Content here... -->
                    <img class="image is-1by1" v-bind:src="`${newsObject.image}`">
                    <!-- ToDO: fix the position if you may-->
                    <p style="font-size: 1.25em;">منبع خبر:
                        <a v-bind:href="`${newsObject.url}`">{{newsObject.source}}</a>
                    </p>
                    <p class="subtitle" style="font-size: 1rem;">
                        {{newsObject.news_time}}
                    </p>

                    <hr />
                    <!-- <br /> -->
                    <p>{{newsObject.body}}</p>
                </section>
            </div>
        </div>
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
    },
  },

  mounted() {
        this.$nextTick( () => {
        
        //document.addEventListener('DOMContentLoaded', () => {
        // Functions to open and close a modal
        function openModal($el) {
            $el.classList.add('is-active');
        }

        function closeModal($el) {
            $el.classList.remove('is-active');
        }

        function closeAllModals() {
            (document.querySelectorAll('.modal') || []).forEach(($modal) => {
            closeModal($modal);
            });
        }

        // Add a click event on buttons to open a specific modal
        (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
            //console.log($trigger); checked: true
            const modal = $trigger.dataset.target;
            //console.log(modal); checked: true
            const $target = document.getElementById(modal);

            $trigger.addEventListener('click', () => {
            //console.log($target);
            if ($target !== null){
                openModal($target);
            }
            });
        });

        // Add a click event on various child elements to close the parent modal
        (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
            const $target = $close.closest('.modal');

            $close.addEventListener('click', () => {
            closeModal($target);
            });
        });

        // Add a keyboard event to close all modals
        document.addEventListener('keydown', (event) => {
            const e = event || window.event;

            if (e.keyCode === 27) { // Escape key
            closeAllModals();
            }
        });

        });
    //});
  },
}
</script>

<style scoped>
img{
    display: initial;
    padding-top: 0 !important;
    padding-bottom: 3%;
}

button {
    margin: 3%;
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

