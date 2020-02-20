from app import app, db
from app.models import User, Post

# TODO: fix this
@app.shell_context_processor
def make_shell_context():
    context = {'db': db, 'User': User, 'Post': Post}
    return context
