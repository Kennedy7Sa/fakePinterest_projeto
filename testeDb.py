from fakepinterest import database,app
from fakepinterest.models import Usuario,Foto
import secrets

with app.app_context():
    database.create_all()

#print(secrets.token_hex(16))