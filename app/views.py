from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import Participant, Attendance
from app.forms import AttendanceForm, RegistrationForm, LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        participant = Participant(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            correo=form.correo.data,
            numero_estudiante=form.numero_estudiante.data,
            carrera=form.carrera.data,
            password=hashed_password
        )
        db.session.add(participant)
        db.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        participant = Participant.query.filter_by(correo=form.correo.data).first()
        if participant and check_password_hash(participant.password, form.password.data):
            login_user(participant)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Inicio de sesión inválido. Verifica tus credenciales.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/attendance', methods=['GET', 'POST'])
@login_required
def attendance():
    form = AttendanceForm()
    if form.validate_on_submit():
        participant = Participant.query.filter_by(correo=form.correo.data).first()
        if participant and check_password_hash(participant.password, form.password.data):
            attendance = Attendance(participant_id=participant.id)
            db.session.add(attendance)
            db.session.commit()
            flash('Asistencia marcada con éxito.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Credenciales incorrectas. Verifica tu correo electrónico y contraseña.', 'danger')
    return render_template('attendance.html', form=form)
