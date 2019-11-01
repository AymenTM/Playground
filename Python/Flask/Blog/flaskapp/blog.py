# Credits: Youtube - Corey Schafer - Python Flask Tutorial (14 Part Series)

# Blog Post Websites

from flask import Flask, render_template, url_for
app = Flask(__name__)

content = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Sam Carter',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 21, 2018'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=content)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

