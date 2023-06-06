<template>
  <div class="row g-4">
        <ArticleListItem v-for="article in articles" :key="article.id" :article="article" />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
  display: flex;
  flex-wrap: wrap;
}

.article-list .col-md-6 {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  padding-right: 15px;
  padding-left: 15px;
}

.article-list .col-md-6::before {
  content: "";
  flex-grow: 1;
}

.article-list .col-md-6:last-child::before {
  height: 100%;
}
</style>