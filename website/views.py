from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def user_home():
    if current_user.user_type == '1':
        return render_template("home.html", login=current_user)
    elif current_user.user_type == '2':
        return render_template("expert_home.html", login=current_user)
    elif current_user.user_type == '3':
        return render_template("chef_home.html", login=current_user)


@views.route('/update', methods=['GET', 'POST'])
@login_required
def update_account():
    if current_user.user_type == '1':
        return render_template("update_user.html", login=current_user)
    elif current_user.user_type == '2':
        return render_template("update_expert.html", login=current_user)
    elif current_user.user_type == '3':
        return render_template("update_chef.html", login=current_user)
