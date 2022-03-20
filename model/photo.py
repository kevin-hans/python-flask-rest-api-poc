from globalapp import db

class Photo(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    img = db.Column("img", db.String(1000), unique=False, nullable=False)
    title = db.Column("title", db.String(120), unique=False, nullable=False)
    author = db.Column("author", db.String(120), unique=False, nullable=True) 
    rows = db.Column("rows", db.Integer, unique=False, nullable=True)
    cols = db.Column("cols", db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<Photo %r %r >' % (self.title ,self.img) 