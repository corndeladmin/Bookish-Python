from flask import Flask
from flask_migrate import Migrate, upgrade, migrate
from app.models.book import Book, BookSchema


from app.models import db

def _update_and_apply_migrations():
    # We upgrade() twice - first to apply any migrations that might have been manually added
    # since the app was last run, then to apply migrations created in the migrate() step.
    upgrade()
    migrate()
    upgrade()

app = Flask(__name__)
app.config.from_object('app.config.Config')

db.init_app(app)
Migrate(app, db)

with app.app_context():
    _update_and_apply_migrations()


# define routes
@app.route('/books')
def get_books():
    books = Book.query.all()
    schema = BookSchema(many=True)
    return schema.dump(books)
