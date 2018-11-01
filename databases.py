from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, desc, quant, price):
  if price < 1000:
    p = Product(name=name, description=desc, quantity=quant, price=price)
    session.add(p)
    session.commit()
  else:
    print("ERROR: 'PRICE TOO HIGH'")

def update_product(id, quant):
  #TODO: complete the functions (you will need to change the function's inputs)
  prod = session.query(Product).filter_by(id=2).first()
  prod.quantity=quant
  session.commit()

def delete_product(id):
  session.query(Product).filter_by(id=id).delete()
  session.commit()

def get_product(id):
  prod = session.query(Product).filter_by(id=id).first()
  return prod
