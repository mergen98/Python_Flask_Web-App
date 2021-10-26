from flask import Flask, render_template, url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5ae59be79d269533e420b55fba2db9c'

posts = [
    {
        "author": "Mergen",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "October 26 2021",
    },
    {
        "author": "Mergen",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "October 26 2021",
    }
]


@app.route("/")  # those two route being handle by the same function it
@app.route(
    "/home"
)  # it means in browser we can do '/' either '/home' it give same function
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Register',form=form)

if __name__ == "__main__":
    app.run(debug=True)