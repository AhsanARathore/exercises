from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

    db.create_all()

class Cupcake(db.Model):
    """cupcake table model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        """serizalize cupcake for jsonification"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating' : self.rating,
            'image': self.image
        }
