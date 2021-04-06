from web import db

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40),nullable=False)
    first_name = db.Column(db.String(30),nullable=False)
    last_name = db.Column(db.String(30),nullable=False)
    phone_no = db.Column(db.String(20),nullable=False)
    emails = db.relationship("Email",backref="contact",lazy=True)

    def __str__(self):
        return self.username

class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(60),nullable=False)
    contact_id = db.Column(db.Integer,db.ForeignKey("contact.id"))

    def __str__(self):
        return self.email