import psycopg2
import configparser
import pandas as pd
from sqlalchemy import create_engine

config=configparser.ConfigParser()
config.read('config.ini')
print('db : ', config['DEFAULT']['db_name'])


columns = ["imo_number","timestamp","latitude","longitude"]
df = pd.read_csv("positions.csv",names=columns)

print('df :',df)

engine = create_engine('postgresql://postgres:my_password@localhost:5432/iris')

user = config['DEFAULT']['user']
pwd = config['DEFAULT']['password']
host = config['DEFAULT']['host']
port = config['DEFAULT']['port']
print('port type :', type(port))
db_name = config['DEFAULT']['db_name']

connection_string = f'postgresql://{user}:{pwd}@{host}:{int(port)}/{db_name}'

print('connection string is : ', connection_string)

engine=create_engine(connection_string)

df.to_sql('vessel',engine,index=False,if_exists='append')


# conn = psycopg2.connect(database=config.db_name,
# 						user=config.user, password=config.password,
# 						host=config.host, port=config.port
# )

# conn.autocommit = True
# cursor = conn.cursor()



# # assuming that the table in the Db exists as a pre-requisite

# sql = '''COPY details(employee_id,employee_name,\
# employee_email,employee_salary)
# FROM '/private/tmp/details.csv'
# DELIMITER ','
# CSV HEADER;'''

# # cursor.execute(sql)

# # sql3 = '''select * from details;'''
# # cursor.execute(sql3)
# # for i in cursor.fetchall():
# # 	print(i)

# # conn.commit()
# conn.close()
