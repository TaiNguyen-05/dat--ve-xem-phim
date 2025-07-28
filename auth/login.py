from flask import Blueprint, request, render_template, redirect, session, flash
import hashlib
from database import connect

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user'] = {
                'id': user[0],
                'username': user[1],
                'role': user[5]
            }
            flash('Đăng nhập thành công!')

            # Phân quyền
            if user[5] == 'admin':
                return redirect('/dashboard/admin')
            elif user[5] == 'nhanvien':
                return redirect('/dashboard/nhanvien')
            else:
                return redirect('/dashboard/khachhang')
        else:
            flash('Sai tài khoản hoặc mật khẩu!')
    return render_template('login.html')
