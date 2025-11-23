from sqlalchemy import Column,Integer,String,Float,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from app.db import Base
import datetime

class Customer(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False,)
    email=Column(String(50),nullable=False)
    sales=relationship("Sales",back_populates="customer")

class Product(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)
    price= Column(Float,nullable=False)
    sales=relationship("Sales",back_populates="products")

class Sales(Base):
    __tablename__="sales"
    id= Column(Integer,primary_key=True,index=True)
    customer_id=Column(Integer,ForeignKey("customers.id"))
    product_id=Column(Integer,ForeignKey("products.id"))
    quantity=Column(Integer,nullable=False)
    timestamp=Column(DateTime,default=datetime.datetime.utcnow)

    customer= relationship("Customer",back_populates="sales")
    product= relationship("Product",back_populates="sales")