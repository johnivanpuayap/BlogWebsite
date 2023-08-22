import requests
from flask import Flask, render_template

from post import Post

app = Flask(__name__)

# Get Blog Data
response = requests.get("https://api.npoint.io/2dbe04c9b494e0ec69b4")
blog_data = response.json()
posts = []
for blog in blog_data:
    post = Post(blog_id=int(blog["id"]), title=blog["title"], subtitle=blog["subtitle"], body=blog["body"])
    posts.append(post)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None

    for post_data in posts:
        print(post_data.blog_id)
        print(index)
        if post_data.blog_id == index:
            requested_post = post_data
            print("Printing Requested Post")
            print(requested_post)
            break

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
