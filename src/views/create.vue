<template>
<div>
  <h1 class="title-css">Create new post...</h1>
  <hr>
  <div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Title of your post" v-model="this.title">
    </div>
    <br>
  <div class="input-group">
  <textarea class="form-control" placeholder="Enter your description" v-model="this.description"></textarea>
    </div>
    <br>
    <button type="button" class="btn btn-success" @click="this.addBlogs()">Create post</button></div>
</template>

<script>
export default {
data () {
    return {
        title: '',
        description: ''
    }
},
methods : {
    addBlogs() {
        fetch('http://127.0.0.1:5000/add', {
                headers: {
                    "Content-type": "application/json"
                },
                method: "POST",
                body: JSON.stringify({
                    "title": this.title,
                    "description": this.description
                })
            }).then(res => res.json())
            .then(res => {
                this.title = ''
                this.description  = ''
            })
            .catch(err => console.log(err))
    }
}
}
</script>

<style scoped>
.title-css {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #a39e51;
}
</style>