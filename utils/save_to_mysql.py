import pymysql
import hashlib
# 建立与MySQL的连接
from utils.process import tools
t = tools()

class mysql_util():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='work_order')
    member_list = {
        'zhongbin310':'钟彬',
        'quda435252':'税务曲达',
        'wxid_1eq4se6iz4lm22':'刘建华',
        'wxid_ajmx25pochdy22':'医保-创智扎西',
        'wxid_f4dfmviveae712':'医保-陈立军',
        'wxid_o4ey6k93qd9421':'医保-刘怀顺',
        'wxid_i7c5h1hnqd5q22':'医保-陈泽森',
        'wxid_bjp1uw5616di22':'医保-黄文',
        'wxid_20rjnpxxyrt012':'医保-王润峰',
        'wxid_on3go3ryopen21':'杨宇',
        'wxid_r5vfllltf2xy22':'索朗',
        'wxid_i5zk3ccpmbek22':'高萌',
        'wxid_m3b926cfeacp21':'肖体旭',
        'wxid_n06g80luyryn21':'邓华杰',
        'wxid_iewrefcj52tk21':'王林',
    }
    def save_record_to_mysql(self, data):
        if data is not None:
            try:
                msg = t.check_msg(data['msg'])
                print(msg)
                if data.get('from_member_wxid'):
                    wxid=data.get('from_member_wxid')
                if data.get('from_wxid'):
                    wxid = data.get('from_wxid')
                name=self.member_list.get(wxid,'医保-陈立军')
                if msg is not None:
                    if self.conn is None:
                        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='work_order')
                    cursor = self.conn.cursor()
                    # 执行SQL语句
                    m=hashlib.md5()
                    m.update(data['msg'].encode('utf-8'))
                    m_key=m.hexdigest()
                    # print(m_key)
                    data_one = (
                    data['time'],m_key, '微信', name, '居民医保', msg, '数据运维问题', '查询城乡缴费', '已处理','1')
                    # sql = "insert into record('key','channel','from','type','description','classify','process_method','status','time') values('"+m_key+"','微信','"+data['from_chatroom_nickname']+"','居民医保','"+data['msg']+"','数据运维问题','查询城乡缴费','已处理','1')"
                    sql = """insert into record
                    (date_time,m_key,channel,from_source,type,description,classify,process_method,status,time)
                     values
                     ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                    # print(sql % data_one)
                    cursor.execute(sql % data_one)
                    self.conn.commit()
                    return '1'
                else:
                    return '0'
            except Exception as e:
                print("Error:", str(e))
                return '0'
        return '0'

# data = {'time': "2024/1/19  12:18:23", 'msg': "54212119830301003X，542121196810050117，542121197508110072 老师 帮忙查一下这几个低保24年有缴费记录嘛？",
#             'from_wxid': 'wxid_m3b926cfeacp21', 'from_nickname': '扎西',
#             'from_chatroom_nickname': '扎西'}
# mysql_util().save_record_to_mysql(data)
