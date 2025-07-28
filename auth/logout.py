from flask import Blueprint, redirect, session

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')
