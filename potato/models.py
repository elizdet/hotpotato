from potato import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kerberos = db.Column(db.String(80), unique=True, nullable=False)
    opted_out = db.Column(db.Boolean)
