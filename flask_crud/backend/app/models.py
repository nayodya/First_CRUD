from . import db

class PersonalDetail(db.Model):
    __tablename__ = "personal_details"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)

    def __repr__(self):
        return f"<PersonalDetail {self.name}>"