from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'miclavesecreta'

# Información de usuarios de ejemplo (en un escenario real, deberías usar una base de datos)
usuarios = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verifica las credenciales
    if username in usuarios and usuarios[username] == password:
        session['username'] = username  # Almacena el nombre de usuario en la sesión
        flash(f'Bienvenido, {username}!', 'success')
        return redirect(url_for('welcome'))
    else:
        flash('Nombre de usuario o contraseña incorrectos.', 'danger')
        return redirect(url_for('index'))

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    return render_template('welcome.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)  # Elimina el usuario de la sesión
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
