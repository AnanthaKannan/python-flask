
import curd.curd as CURD
import query.qry as qry

# result = CURD.insert(qry.insert_customers_data, None)

CURD.read(qry.select_all_customers)
# name = ('kannan',)
# CURD.read(qry.select_customer_by_name, name)