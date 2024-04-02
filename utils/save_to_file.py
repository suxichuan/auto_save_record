from utils.process import tools
from utils import redis_c
import tablib

redis_inst = redis_c(host="localhost", port=6379, db=0).redis_inst
t = tools()


def to_save(row):
    msg = t.check_msg(row['msg'])
    if msg is None:
        return '0'
    print(msg)
    rowindex = int(redis_inst.get('rowindex'))
    data_one = (row['time'], '微信', row['from_chatroom_nickname'], '居民医保', msg, '数据运维问题', '查询城乡缴费', '已处理', '', '1')
    res = '0'
    try:
        with open("maintenance_work_order_202401.xlsx", "rb") as r:
            dataset = tablib.Dataset().load(r)
        dataset.insert(rowindex, data_one)
        # 循环插入数据
        with open("maintenance_work_order_202401.xlsx", 'wb') as f:
            f.write(dataset.export('xlsx'))
        rowindex = rowindex + 1
        redis_inst.set('rowindex', str(rowindex))
        res = '1'
    except Exception as e:
        print(e)
        with open("maintenance_work_order_202401_bak.xlsx", 'wb') as f:
            f.write(dataset.export('xlsx'))
            rowindex = rowindex + 1
        res = '1'
    return res

# data_one = ('2024/1/23 9:51:23', '微信', 'suxichuan','居民医保',
#      '54212119830301003X，542121196810050117，542121197508110072 老师 帮忙查一下这几个低保24年有缴费记录嘛？',
#      '数据运维问题','查询城乡缴费','已处理','','1')
# print(to_save(data_one))
