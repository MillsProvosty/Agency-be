from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app
from app import db
from app.api.errors import bad_request
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
        form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    # import ipdb; ipdb.set_trace()
    if 'first_name' not in data or 'last_name' not in data or 'email' not in data or 'password_hash' not in data or 'phone_number' not in data:
        return bad_request('Error: Missing fields')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('That email is in use, please pick another.')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response
