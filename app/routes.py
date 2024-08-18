from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Todo

# Creating a Blueprint for the main routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Querying incomplete todos
    incomplete = Todo.query.filter_by(complete=False).all()
    # Querying completed todos
    complete = Todo.query.filter_by(complete=True).all()

    # Rendering the index page with incomplete and complete todos
    return render_template('index.html', incomplete=incomplete, complete=complete)


@main.route('/add', methods=['POST'])
def add():
    # Creating a new todo item with data from the form
    todo = Todo(text=request.form['todoitem'], complete=False)
    # Adding the new todo to the database session
    db.session.add(todo)
    # Committing the new todo to the database
    db.session.commit()

    # Redirecting to the index page
    return redirect(url_for('main.index'))


@main.route('/complete/<int:id>')
def complete(id):
    # Querying the todo item by its ID
    todo = Todo.query.filter_by(id=id).first()
    # Checking if the todo exists
    if todo:
        # Setting the todo item as complete
        todo.complete = True
        # Committing the change to the database
        db.session.commit()

    # Redirecting to the index page
    return redirect(url_for('main.index'))


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Querying the todo item by its ID
    todo = Todo.query.filter_by(id=id).first()
    # Checking if the request method is POST
    if request.method == 'POST':
        # Checking if the todo exists
        if todo:
            # Updating the todo item's text
            todo.text = request.form['todoitem']
            # Committing the change to the database
            db.session.commit()
        # Redirecting to the index page
        return redirect(url_for('main.index'))
    
    # Rendering the edit page with the todo item
    return render_template('edit.html', todo=todo)


@main.route('/delete/<int:id>')
def delete(id):
    # Querying the todo item by its ID
    todo = Todo.query.filter_by(id=id).first()
    # Checking if the todo exists
    if todo:
        # Deleting the todo item from the database session
        db.session.delete(todo)
        # Committing the change to the database
        db.session.commit()
    # Redirecting to the index page
    return redirect(url_for('main.index'))
