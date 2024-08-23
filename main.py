# TODO add click attribute, add support for post and other ones
from flask import Flask, render_template, render_template_string
import posttiltes
from posttiltes import post_tiltes

app = Flask(__name__)

button = """
<div hx-get="/post"> here's my new post</div>
"""

def format_post(title):
    return f"""
<div class="post">
<h3> {title}</h3>
</div>
"""

def format_posts(titles):
    r = ""
    for title in titles:
        r += f"""
        <tr>
            <td>{title}</td>
        </tr>"""
    return f"""
    <div class="post">
        <table>
            <th>Post</th>
            {r}
        </table>
    </div>"""

@app.route("/replace")
def getme():
    ex = "Show HN: Ruroco – like port knocking, but better"

    return format_posts(post_tiltes) 

    # return '''<h2> how this works all this does is call /replace to the server, <br> 
    # replaces current html element with whatever the server responds with</h2>'''
@app.route("/")
def index():
    return render_template("index.html",post_title="tesilated")

@app.route("/post")
def post():
    return button

@app.errorhandler(404)
def page_not_found(error):
    return """404""", 404
@app.route("/post/<int:post_id>")
def postst(post_id):
    print(post_id)
    current_post = posttiltes.post_tiltes[post_id]
    return format_post(current_post)
app.run("0.0.0.0", port=3000,debug=True)