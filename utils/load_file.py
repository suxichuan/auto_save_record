import tablib
import pymysql
import hashlib
from utils.process import tools
t = tools()
dataset=tablib.Dataset().load(open('D:\\PycharmProjects\\auto_save_record\\maintenance_work_order_202401.xlsx','rb').read(),'xlsx')
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='work_order')

if dataset is not  None:
        for row in dataset:
            cursor=conn.cursor()
            try:
                msg = t.check_msg(row[4])
                m = hashlib.md5()
                m.update(row[4].encode('utf-8'))
                m_key = m.hexdigest()
                data_one = (
                    row[0], m_key, '微信', row[2], '居民医保', msg, '数据运维问题', '查询城乡缴费', '已处理', '1')
                sql = """insert into record
                                    (date_time,m_key,channel,from_source,type,description,classify,process_method,status,time)
                                     values
                                     ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                cursor.execute(sql % data_one)
                conn.commit()
            except Exception as e:
                print(e)
                continue