<template>
  <div>
    <h1 class="title-css">This is my home page!</h1>
    <hr>
    <div class="row">
        <div class="card mx-3 my-3" style="width: 18rem;" v-for="blog in allblogs" >
            <div class="card-body">
                <h5 class="card-title">{{blog.title}}</h5>
                <hr>
                <p class="card-text">{{ blog.description }}</p>
            </div>
            
            <!-- Button trigger modal FOR EDITING POST -->
                <button @click="this.triggerBinding(blog.id, blog.title, blog.description)" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop_edit">
                Edit 
                </button>

                <!-- Modal -->
                <div class="modal fade" id="staticBackdrop_edit" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h3>Edit your post</h3>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input type="text" class="form-control" placeholder="Title of your post" v-model="this.title">
                        <textarea class="form-control" placeholder="Enter your description" v-model="this.description"></textarea>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="this.editBlog(this.id)" data-bs-dismiss="modal">Confirm edit</button>
                    </div>
                    </div>
                </div>
                </div>
            
            <!-- Button trigger modal FOR DELETING POST-->
            <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="this.triggerBinding(blog.id, blog.title, blog.description)">
                Delete
                </button>

                <!-- Modal -->
                <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="staticBackdropLabel">Delete your post</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        {{this.title}}
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="this.deleteBlog(id)">Confirm delete</button>
                    </div>
                    </div>
                </div>
                </div>
        </div>
    </div>

  </div>
</template>

<script>
export default {
    data() {
        return {
            allblogs: [],
            id: null,
            title: null,
            description: null
        }
    },
    methods : {
        getAllBlogs() {
            fetch('http://127.0.0.1:5000/view', {
                headers: {
                    "Content-type": "application/json"
                },
                method: "GET"
            }).then(res => res.json())
            .then(res => {
                this.allblogs.push(...res)
            })
            .catch(err => console.log(err))
        },

        editBlog(id) {
            fetch(`http://127.0.0.1:5000/edit/${id}`, {
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
                this.allblogs = []
                this.getAllBlogs()
            })
            .catch(err => console.log(err))
        },

        deleteBlog(id) {
            fetch(`http://127.0.0.1:5000/delete/${id}`, {
                headers: {
                    "Content-type": "application/json"
                },
                method: "POST"
            }).then(res => res.json())
            .then(res => {
                this.allblogs = []
                this.getAllBlogs()
            })
            .catch(err => console.log(err))
        },

        triggerBinding(id, title, description) {
            this.id = id
            this.title = title
            this.description = description
        }
    },
    created() {
        this.getAllBlogs()
    }
    
}
</script>

<style>

</style>