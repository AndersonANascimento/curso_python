#-*- encoding=UTF-8 -*-
import pandas as pd
from db import DemoDB

database = DemoDB()

database.tables
print database.tables

clientes = database.tables.Customer
print 'type(clientes)', type(clientes)
print clientes

clientes = database.tables.Customer.all()
print 'type(clientes)', type(clientes)
print clientes
<<<<<<< HEAD

clientes_query = database.query('SELECT * FROM Customer WHERE CustomerId < 5')
print 'type(clientes_query)', type(clientes_query)
print clientes_query
=======
#
# clientes_query = database.query('SELECT * FROM Customer WHERE CustomerId < 5')
# print 'type(clientes_query)', type(clientes_query)
# print clientes_query
>>>>>>> 48baed94f2f899c1516249f4f2e6c54864a5338d
