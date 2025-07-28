from flask import Flask , session ,render_template, request, redirect, url_for
from database import init_db
from auth.login import login_bp
from auth.register import register_bp
from auth.logout import logout_bp
from auth.change_password import change_password_bp
from auth.profile import profile_bp

app = Flask(__name__)
app.secret_key = 'secret_key'

# Khởi tạo DB
init_db()

# Register các Blueprint
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(change_password_bp)
app.register_blueprint(profile_bp)

# Dashboard theo vai trò
@app.route('/dashboard/<role>')
def dashboard(role):
    if 'user' not in session or session['user']['role'] != role:
        return "Bạn không có quyền truy cập!", 403
    return f"Chào mừng {role.title()} - {session['user']['username']}"

if __name__ == '__main__':
    app.run(debug=True)
