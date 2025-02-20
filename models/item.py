from db import db

class ItemModel(dn.Model): # mapping between a row in a table to a python class/object
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) # will give automatically increasing value to id when we add new items
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precisio=2), unique=False, nullabe=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False) # link btw items and stores table in a one(stores.is) to many(items.store_id) manner
    store = db.relationship("StoreModel", back_populates="items") # will automatically populate the store variable with a StoreModel object whose id matches that of the foreign key
    

