import tablib
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='work_order')
from datetime import datetime
import calendar
cursor=conn.cursor()

start_month=input("请输入要导出数据的开始月份\n")
format='%Y-%m-%d %H:%M:%S'
current_year = str(datetime.now())[0:4]
if len(start_month)<2:
    new_start_month="0"+start_month
last_day=calendar.monthrange(int(current_year),eval(start_month))[1]
start=datetime.strptime(current_year+"-"+new_start_month+"-"+"01"+" 00:00:00",format)
end=str(datetime.now())[0:19]
date_args=(start,end)
sql_data = """select date_time,channel,from_source,type,description,classify,process_method,time,`status`,processor from record where date_time > '%s'
 and date_time < '%s'
 """ % date_args
cursor.execute(sql_data)
count=cursor.rowcount
data=cursor.fetchall()
dataset=tablib.Dataset()
dataset.headers=['处理时间','渠道','提出机构','业务类型','问题描述','问题分类','解决办法','处理状态','处理人','处理时间']

for row in data:
    dataset.lpush(row)
with open("work_order_2024{}.xlsx".format(new_start_month), 'wb') as f:
    f.write(dataset.export('xlsx'))
print('共导出{}条数据'.format(count))