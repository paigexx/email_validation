from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect("/user")

@app.route('/user')
def homepage():
    return render_template("index.html")

@app.route("/user/sign_up", methods=['POST'])
def user_sign_up():
    print(request.form)

    if not User.validate_data(request.form):
        print("invalid email")
        return redirect("/")

    user_id = User.create_user(request.form)
    data = {
        "user_id": user_id
    }
    user = User.get_user(data)
    return render_template("review_user.html", user = user)

@app.route("/user/all_users")
def show_all_users():
    all_users = User.get_users()
    print(all_users)
    return render_template("show_users.html", all_users = all_users)

@app.route("/user/delete/<int:user_id>")
def delete_user(user_id):
    data = {
        "user_id": user_id
    }
    User.delete_user(data)
    return redirect("/user/all_users")
