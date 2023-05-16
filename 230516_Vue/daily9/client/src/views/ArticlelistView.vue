<template>
  <div>
    <h1>게시물 목록</h1>
  </div>
</template>

<script>
export default {
    name: 'ArticlelistView',
    data() {
        return{
            articles: null,
        }
    },
    methods:{
        signup(){
            axios({
                method: "get",
                url: 'http://127.0.0.1:8000/articles/',
                data: {
                    title: this.title,
                    content: this.content,
                    created_at: this.created_at,
                },
            })
            .then((res)=>{
            console.log(res.data)})
            .catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>