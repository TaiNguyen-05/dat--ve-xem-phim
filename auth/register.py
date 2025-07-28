from flask import Blueprint, request, render_template, redirect, flash, session
import hashlib
from database import connect

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        email = request.form['email']
        phone = request.form['phone']
        role = request.form['role']

        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, email, phone, role) VALUES (?, ?, ?, ?, ?)",
                           (username, password, email, phone, role))
            conn.commit()
            flash('Đăng ký thành công!')
            return redirect('/login')
        except:
            flash('Tài khoản đã tồn tại!')
        finally:
            conn.close()
    return render_template('register.html')
