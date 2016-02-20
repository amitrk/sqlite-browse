from flask import render_template
import sqlite3
from . import app

@app.errorhandler(404)
def page_not_found_handler(error):
    return "Error!! page not found"

@app.route('/')
def index():
    conn = sqlite3.connect('appdata.db')
    cur = conn.execute("SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type='table'")
    query_results = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('index.html', tables = query_results)

@app.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html')
