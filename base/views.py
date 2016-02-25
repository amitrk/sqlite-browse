from flask import render_template
import sqlite3
from . import app


@app.errorhandler(404)
def page_not_found_handler(error):
    ''' Handle 404 errors for routes not defined '''
    return "Error!! page not found"+error


@app.route('/')
def index():
    ''' Route for the index page. This route will handle display
    the list of DB objects in the SQLite DB file provided
    when the flask app is started '''
    conn = sqlite3.connect(app.config['SQLITE_DB_FILE'])
    cur = conn.execute(
        "SELECT type, tbl_name FROM sqlite_master WHERE type='table'")
    query_results = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('index.html', db_objects=query_results)


@app.route('/details/<object_name>')
def show_object(object_name):
    ''' Route for the DB object details page. This route will handle
    display details of the DB objct selected '''
    conn = sqlite3.connect('appdata.db')
    sql_query = "pragma table_info(%s)" % object_name
    cur = conn.execute(sql_query)
    query_results = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('details.html', object_name=object_name, query_results=query_results)
