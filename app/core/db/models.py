from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Allergen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.Text)
    is_dangerous = db.Column(db.Boolean())

    def __repr__(self):
        return f'<Allergen {self.title}>'


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    title = db.Column(db.String(64))
    description = db.Column(db.Text())
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'))

    def __repr__(self):
        return f'<Dish {self.title}>'


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.Text())
    # is_dangerous = db.Column(db.Boolean())
    # cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'))
    allergen_rating = db.Column(db.Integer())

    def __repr__(self):
        return f'<Restaurant {self.title}>'


class Cuisine(db.Model):
    # cuisine acts as a category to the restaurant
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    allergen_rating = db.Column(db.Integer()) # 1 to 5
    # type = db.Column(db.String(32))
