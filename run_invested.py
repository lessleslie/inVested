from datetime import datetime
from datetime import timedelta
from datetime import date
import psycopg2
import sentiment_test as sentiment
import db_stock_data as stock_loader

#connection 
print("running")
try:
    connect = psycopg2.connect(database="postgres", user="postgres", password="CapStoneRDS", 
    host="database-1.ciomlblnrvsp.us-east-2.rds.amazonaws.com", port='5432')
except:
    print("no good")
cursor = connect.cursor()

#get the last date that the schema was generated 
#generated_date_query = "select * from last_generated_date"
#cursor.execute(generated_date_query)
#records = cursor.fetchall()
#generated_date = datetime.strptime(records[len(records)-1][0], '%Y-%m-%d').date()
#print(generated_date)
#get today's date

#companies of interest
# TODO: type in company name from website to pull data
companies = ['Google', 'Facebook', 'Microsoft']
# create dictionary from company name to stock symbol
company_dict = {}
company_dict['Google'] = 'GOOGL'
company_dict['Amazon'] = 'AMZN'
company_dict['Microsoft'] = 'MSFT'

#get dates 
current_date = date.today()
drop_date = current_date -timedelta(days = 7)
print(drop_date)

#drop old schema 
<<<<<<< HEAD
cursor.execute('DROP SCHEMA if exists ' + drop_date.strftime('%b%d%y') + ' cascade')
=======
>>>>>>> b18d04c458e31b141b72512526acbd7f1b0ce142
cursor.execute('DROP SCHEMA if exists ' + current_date.strftime('%b%d%y') + ' cascade')
connect.commit()

#create schema for the day 
cursor.execute('CREATE SCHEMA ' + current_date.strftime('%b%d%y')) 
#cursor.execute("insert into last_generated_date (date) values (%s) ", (str_date,))
connect.commit()

connect.close()

# insert the stock data
load_stocks = stock_loader.stock_data(company_dict, current_date)
load_stocks.create_insert_stock_data()

#process sentiment
get_sentiment = sentiment.sentiment_analysis(companies, current_date, current_date - timedelta(days=7))
get_sentiment.process_sentiment()




