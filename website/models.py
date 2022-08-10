from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email_addr = db.Column(db.String(10000))
    first_name = db.Column(db.String(10000))
    last_name = db.Column(db.String(10000))
    age=  db.column(db.integer)
    user_street_name = db.Column(db.String(10000))
    user_city  = db.Column(db.String(10000))
    user_state = db.Column(db.String(10000))
    user_zipcode = db.Column(db.integer)
    user_email = db.Column(db.String(10000))
    user_phone = db.Column(db.integer)




class Health_Expert(db.Model):
    health_expert_id =db.Column(db.integer,primary_key=True)
    he_first_name = db.Column(db.String(10000))
    he_last_name = db.Column(db.String(10000))
    age = db.column(db.integer)
    he_join_date= db.Column(db.DateTime(timezone=true), default=func.now())
    he_type = db.Column(db.String(10000))
    he_phone = db.column(db.integer)
    he_email = db.Column(db.String(10000))


class Health_Report(db.Model):
    status_id = db.Column(db.integer, primary_key =True)
    user_bp_level =db.Column(db.float)
    user_height =db.Column(db.float)
    user_weight = db.Column(db.float)
    user_haemoglobin = db.Column(db.float)
    user_allergic_items = db.Column(db.float)
    user_cholesterol_level = db.Column(db.float)
    user_body_mass_index = db.Column(db.float)
    user_id = db.Column(db.integer, db.ForeignKey('user.user_id'))

class Expert_User (db.Model):
    exp_rep_id = db.Column(db.integer, primary_key =True)
    req_vitamins= db.Column(db.float)
    req_calories = db.Column(db.datetime.date())
    avoidable_items = db.Column()
    fat_intake = db.Column(db.integer)
    suggested_items = db.Column()
    req_sugar_levels = db.Column(db.integer)
    health_expert_id =db.Column(db.integer, db.ForeignKey('user.health_expert_id'))

class chef(db.Model):
    ch_id =db.Column(db.integer, primary_key =True)
    ch_first_name=db.Column(db.String(10000))
    ch_last_name = db.Column(db.String(10000))
    ch_qualification =db.Column(db.String(10000))
    ch_expertise = db.Column(db.String(10000))
    ch_email= db.Column(db.String(10000))
    exp_rep_id = db.Column(db.integer, db.ForeignKey('user.exp_rep_id'))

class Employee(db.Model):
    emp_id = db.Column(db.integer, primary_key =True)
    emp_first_name= db.Column(db.String(10000))
    emp_last_name = db.Column(db.String(10000))
    emp_type = db.Column(db.String(10000))
    emp_phone= db.Column(db.integer)
    emp_email = db.Column(db.String(10000))

class Menu(db.Model):
    menu_id = db.Column(db.integer, primary_key =True)
    item_name = db.Column(db.String(10000))
    item_id = db.Column(db.String(10000))
    item_qty = db.Column(db.String(10000))
    item_price = db.Column(db.integer)
    ch_id = db.Column(db.integer, db.ForeignKey('user.ch_id'))

class payment(Model):
    p_id = db.Column(db.integer, primary_key =True)
    user_id= db.Column(db.integer)
    name = db.Column(db.String(10000))
    card_number =  db.Column(db.integer)
    card_expiry_date = db.Column(db.datetime.date())
    card_cvv = db.Column(db.integer)
    or_id = db.Column(db.integer, db.ForeignKey('user.or_id'))

class Order(db.Model):
    or_id = db.Column(db.integer, primary_key =True)
    or_time = db.Column(db.datetime.date())
    or_cost = db.Column(db.float)
    user_id =db.Column(db.integer, db.ForeignKey('user.or_id'))
    or_id = db.Column(db.integer, db.ForeignKey('user.or_id'))

class Delivery(db.Model):
    de_id =db.Column(db.integer, primary_key =True)
    de_street=db.Column(db.String(10000))
    de_city=db.Column(db.String(10000))
    de_state=db.Column(db.String(10000))
    de_zipcode =db.Column(db.integer)
    emp_id =db.Column(db.integer, db.ForeignKey('user.or_id'))
    or_id=db.Column(db.integer, db.ForeignKey('user.or_id'))

class User_Taste(db.Model):
    user_int_id=db.Column(db.integer, primary_key =True)
    int_cusine=db.Column(db.String(10000))
    int_dish_desc=db.Column(db.String(10000))
    int_veg_desc=db.Column(db.String(10000))
    int_fruits_desc=db.Column(db.String(10000))
    int_flavours_desc=db.Column(db.String(10000))
    ch_id=db.Column(db.integer, db.ForeignKey('user.or_id'))
    user_id=db.Column(db.integer, db.ForeignKey('user.or_id'))





