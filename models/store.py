from db import db

class StoreModel(dn.Model): # mapping between a row in a table to a python class/object
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True) # links to store_id in items table
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic") # dynamic will only populate when its told