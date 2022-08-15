from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email_addr = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.column(db.Integer)
    user_street_name = db.Column(db.String(100))
    user_city = db.Column(db.String(100))
    user_state = db.Column(db.String(100))
    user_zipcode = db.Column(db.Integer)
    user_email = db.Column(db.String(100))
    user_phone = db.Column(db.Integer)


class Login(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email_addr = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100))
    password = db.Column(db.String(150))
    user_type = db.Column(db.String(50))


class Expert_User_Report(db.Model):
    exp_rep_id = db.Column(db.Integer, primary_key=True)
    req_vitamins = db.Column(db.Float)
    req_calories = db.Column(db.Integer)
    avoidable_items = db.Column(db.String(100))
    fat_intake = db.Column(db.Integer)
    suggested_items = db.Column(db.String(100))
    req_sugar_levels = db.Column(db.Integer)


class Health_Expert(db.Model):
    health_expert_id = db.Column(db.Integer, primary_key=True)
    he_first_name = db.Column(db.String(100))
    he_last_name = db.Column(db.String(100))
    age = db.column(db.Integer)
    he_join_date = db.Column(db.DateTime(timezone=True), default=func.now())
    he_type = db.Column(db.String(100))
    he_phone = db.column(db.Integer)
    he_email = db.Column(db.String(100))


class User_Health_Report(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    user_bp_level = db.Column(db.Float)
    user_height = db.Column(db.Float)
    user_weight = db.Column(db.Float)
    user_haemoglobin = db.Column(db.Float)
    user_allergic_items = db.Column(db.Float)
    user_cholesterol_level = db.Column(db.Float)
    user_body_mass_index = db.Column(db.Float)


class Chef(db.Model):
    ch_id = db.Column(db.Integer, primary_key=True)
    ch_first_name = db.Column(db.String(100))
    ch_last_name = db.Column(db.String(100))
    ch_qualification = db.Column(db.String(100))
    ch_expertise = db.Column(db.String(100))
    ch_email = db.Column(db.String(100), unique=True)


class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_first_name = db.Column(db.String(100))
    emp_last_name = db.Column(db.String(100))
    emp_type = db.Column(db.String(100))
    emp_phone = db.Column(db.Integer)
    emp_email = db.Column(db.String(100))


class Menu(db.Model):
    menu_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    item_id = db.Column(db.String(100))
    item_qty = db.Column(db.String(100))
    item_price = db.Column(db.Integer)


class Payment(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    card_number = db.Column(db.Integer)
    card_expiry_date = db.Column(db.DateTime)
    card_cvv = db.Column(db.Integer)


class Order(db.Model):
    or_id = db.Column(db.Integer, primary_key=True)
    or_time = db.Column(db.DateTime)
    or_cost = db.Column(db.Float)


class Delivery(db.Model):
    de_id = db.Column(db.Integer, primary_key=True)
    de_street = db.Column(db.String(100))
    de_city = db.Column(db.String(100))
    de_state = db.Column(db.String(100))
    de_zipcode = db.Column(db.Integer)


class User_Taste_Form(db.Model):
    user_int_id = db.Column(db.Integer, primary_key=True)
    int_cusine = db.Column(db.String(100))
    int_dish_desc = db.Column(db.String(100))
    int_veg_desc = db.Column(db.String(100))
    int_fruits_desc = db.Column(db.String(100))
    int_flavours_desc = db.Column(db.String(100))
