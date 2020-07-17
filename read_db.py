import pymysql as ms
from pandas import DataFrame as Df

myDb = ms.connect(host='localhost',user='root_admin', passwd='Secured_V@ult10',db='data', port=3306)

select = "SELECT * FROM product_data"

cursor = myDb.cursor()
cursor.execute(select)
result = cursor.fetchall()

df = Df(result, columns=['Id', 'Type','Brand', 'Price per unit', 'Stock', 'Total stock price']).set_index("Id")

print(f'{df}\n')
