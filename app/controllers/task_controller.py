from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.task import Task
from app.models.user import User
from app.models.db import db

task_bp = Blueprint('task', __name__)


@task_bp.route('/tasks')
def tasks():
    if 'user_id' not in session:
        flash('Veuillez vous connecter', 'error')
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    tasks = Task.query.filter_by(user_id=user.id).all()
    return render_template('tasks.html', tasks=tasks)


@task_bp.route('/create-task', methods=['POST'])
def create_task():
    if 'user_id' not in session:
        flash('Veuillez vous connecter', 'error')
        return redirect(url_for('auth.login'))
    title = request.form.get('title')
    description = request.form.get('description', '')

    if not title:
        flash('Le titre est obligatoire', 'error')
        return redirect(url_for('task.tasks'))

    new_task = Task(
        title=title,
        description=description,
        user_id=session['user_id']
    )

    db.session.add(new_task)
    db.session.commit()
    flash('Tâche créée avec succès', 'success')
    return redirect(url_for('task.tasks'))


@task_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        flash('Veuillez vous connecter', 'error')
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)

    if task.user_id != session['user_id']:
        flash('Accès non autorisé', 'error')
        return redirect(url_for('task.tasks'))

    db.session.delete(task)
    db.session.commit()
    flash('Tâche supprimée', 'success')
    return redirect(url_for('task.tasks'))
