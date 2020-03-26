from flask import Flask

from route.admin import admin_route

app = Flask(__name__)
app.register_blueprint(admin_route, url_prefix='/admin')

if __name__ == "__main__":
    app.run(port=5000, debug=True)

# import curd.curd as CURD
# import query.qry as qry

# CURD.read(qry.select_all_customers)
# name = ('kannan',)
# CURD.read(qry.select_customer_by_name, name)