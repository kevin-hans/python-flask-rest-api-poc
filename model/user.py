from globalapp import db

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    lastName = db.Column("last_name", db.String(120), unique=False, nullable=False)
    firstName = db.Column("first_name", db.String(120), unique=False, nullable=False)
    age = db.Column("age", db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r %r >' % (self.firstName ,self.lastName) 

    def as_dict(self):
        # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}