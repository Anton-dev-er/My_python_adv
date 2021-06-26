from flask import Flask, render_template

my_app = Flask("my_app")


@my_app.route("/1")
def main():
    return "<h1>asdsad</h1>"


if __name__ == "__main__":
    my_app.run(debug=True)