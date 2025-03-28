from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session, flash
from ..models.user import User
from ..models.db import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('auth.profile'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('auth.home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        name = request.form.get('name', '')

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        else:
            new_user = User(username=username, email=email, name=name)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please login to view this page', 'error')
        return redirect(url_for('auth.login'))

    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)


@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('auth.login'))


@auth_bp.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('home.html', authenticated=True, user=user)
    else:
        return render_template('home.html', authenticated=False)


@auth_bp.route('/users')
def list_users():
    if 'user_id' not in session:
        flash('Please login to view this page', 'error')
        return redirect(url_for('auth.login'))

    users = User.query.all()  # Get all users from database
    return render_template('users.html', users=users)


@auth_bp.route('/api/users')
def api_list_users():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    users = User.query.all()
    users_list = [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'name': user.name
    } for user in users]

    return jsonify(users_list)
