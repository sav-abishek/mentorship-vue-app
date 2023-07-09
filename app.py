from flask import Flask, jsonify, request, make_response
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))

class BlogSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description")

blogs_schema = BlogSchema(many=True)

# ROUTE TO ADD TO DB


@app.route('/add', methods=["POST"])
def addBlog():
    try:
        title = request.json["title"]
        des = request.json["description"]

        blogToAdd = Blog(title=title, description=des)
        db.session.add(blogToAdd)
        db.session.commit()
        return make_response({"msg": "Post was added successfully"}, 200)
    except:
        return make_response({"error": "Somethinng went wrong"})

# ROUTE TO EDIT A DB


@app.route('/edit/<id>', methods=["POST", "PUT", "PATCH"])
def editBlog(id):
    try:
        title = request.json["title"]
        des = request.json["description"]
        blogToEdit = Blog.query.filter_by(id=id).first()
        blogToEdit.title = title
        blogToEdit.description = des
        db.session.commit()
        return make_response({"msg": "Post edited successfully"}, 200)
    except:
        return make_response({"error": "something went wrong"}, 400)

# ROUTE TO DELETE


@app.route('/delete/<id>', methods=["POST", "DELETE"])
def deleteBlog(id):
    blogToDelete = Blog.query.filter_by(id=id).first()
    db.session.delete(blogToDelete)
    db.session.commit()
    return make_response({"msg": "Post deleted successfully"}, 200)

# ROUTE TO VIEW ALL
@app.route('/view', methods=["GET"])
def viewBlogs():
    allBlogs = Blog.query.all()
    return jsonify(blogs_schema.dump(allBlogs))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
