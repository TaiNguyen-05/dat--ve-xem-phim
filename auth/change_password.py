from flask import Blueprint, render_template, request, session, flash, redirect
import hashlib
from database import connect

change_password_bp = Blueprint('change_password', __name__)

@change_password_bp.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        old = hashlib.sha256(request.form['old_password'].encode()).hexdigest()
        new = hashlib.sha256(request.form['new_password'].encode()).hexdigest()

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=? AND password=?", (session['user']['id'], old))
        if cursor.fetchone():
            cursor.execute("UPDATE users SET password=? WHERE id=?", (new, session['user']['id']))
            conn.commit()
            flash('Đổi mật khẩu thành công!')
        else:
            flash('Mật khẩu cũ không đúng!')
        conn.close()
    return render_template('change_password.html')
