from flask import Flask,render_template,redirect,url_for,request    
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Tuğba Kayaoğlu/Desktop/todoApp/todo.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    todos = todo.query.all()
    return render_template("index.html",todos = todos)

@app.route("/complete/<string:id>")
def CompleteTodo(id):
    tododo = todo.query.filter_by( id = id).first()
    """if todo.complete == True:
         todo.complete == False
    else: 
        todo.complete == True"""
    tododo.complete = not tododo.complete

    db.session.commit()

    return redirect(url_for("index"))

@app.route("/add",methods = ["POST"])
def AddTodo():
    title = request.form.get("title")
    newTodo = todo(title = title ,complete = False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deletetodo(id):
    tododo = todo.query.filter_by( id = id).first()
    db.session.delete(tododo)
    db.session.commit()
    return redirect(url_for("index"))

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all()   #her  defa tekrar çalışır ama oluşmuş tabloları tekrar tekrar oluşturmaz.
    app.run(debug=True)


 