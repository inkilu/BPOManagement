from flask import Flask
from public import public
from admin import admin
from company import company
from technical import technical
from customer_care import customer_care
# customer_care

app=Flask(__name__)

app.secret_key="secret_key"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(company,url_prefix="/company")
app.register_blueprint(technical,url_prefix="/technical")
app.register_blueprint(customer_care,url_prefix="/customer_care")

app.run(debug=True,port=5004)