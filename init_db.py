from app import create_app, db
from app.models import User  # Import all your models here

app = create_app()
app.app_context().push()  # This pushes an application context manually

db.create_all()
