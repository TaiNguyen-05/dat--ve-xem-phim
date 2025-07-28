from flask import Blueprint, render_template, session , redirect
from database import connect

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def profile():
    if 'user' not in session:
        return redirect('/login')
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, phone, role FROM users WHERE id=?", (session['user']['id'],))
    user = cursor.fetchone()
    conn.close()

    return render_template('profile.html', user=user)
