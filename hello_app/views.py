from flask import render_template, request, redirect
from datetime import datetime
from . import app
from .database import get_db, close_connection, query_db, insert_database

@app.teardown_appcontext
def close_db_connection(exception):
    close_connection(exception=exception)


@app.route("/", methods=["GET", "POST"])
def home():
    db = get_db()  # Establish a database connection
    data = query_db("SELECT id, title, content FROM tasks", one=False)
    
    if request.method == "POST":
        if "remove" in request.form:
            id = request.form["remove"]
            
            query_db("DELETE FROM tasks WHERE id = ?", (id, ), one=True)

        else:
            title = request.form["title"]
            content = request.form["content"]

            insert_database(db, title, content)

        return redirect("/")

    db.close()  # Close the database connection

    return render_template("home.html", data=data)

