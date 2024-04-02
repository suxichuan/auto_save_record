from WechatPCAPI import WechatPCAPI
from utils.save_to_file import to_save
from utils.save_to_mysql import mysql_util
import time

single_list = ['wxid_f4dfmviveae712', 'wxid_o4ey6k93qd9421', 'wxid_i7c5h1hnqd5q22', 'wxid_bjp1uw5616di22',
               'wxid_on3go3ryopen21', 'wxid_juae8umnqr3e22', 'wxid_m3b926cfeacp21','wxid_n06g80luyryn21','wxid_i5zk3ccpmbek22']
# single_list = ['wxid_juae8umnqr3e22']
self_list = ['wxid_m3b926cfeacp21', 'wxid_n06g80luyryn21', 'wxid_iewrefcj52tk21','zhongbin310']
filehelper = 'filehelper'


def on_message(message):
    # print(message)
    # 处理微信群的消息
    if message.get("data") is None:
        print('无有效数据')
        return
    if message['type'] == 'msg::chatroom':
        # 城乡医保确认群：
        if message['data']['from_chatroom_wxid'] == '20031586753@chatroom' and message['data']['send_or_recv'][
            0] == '0':
            data = {}
            if message.get("data") is not None and message['data']['from_member_wxid'] not in self_list:
                print(message)
                data['time'] = message['data']['time']
                data['msg'] = message['data']['msg']
                data['from_member_wxid'] = message['data']['from_member_wxid']
                data['from_chatroom_nickname'] = message['data']['from_chatroom_nickname']
                data['from'] = '医保'
                p = process_data()
                res = p.process_to_mysql(data)
                if res == '1':
                    print('{}的发送的记录已经保存成功'.format(message['data']['from_chatroom_nickname']))
            else:
                print('无有效数据')
    #

        # 人社税务技术群
        if message['data']['from_chatroom_wxid'] == '25302656702@chatroom' and message['data']['send_or_recv'][
            0] == '0':
            data = {}
            if message.get("data") is not None and message['data']['from_member_wxid'] not in self_list:
                print(message)
                data['time'] = message['data']['time']
                data['msg'] = message['data']['msg']
                data['from_member_wxid'] = message['data']['from_member_wxid']
                data['from_chatroom_nickname'] = message['data']['from_chatroom_nickname']
                data['from'] = '人社'
                p = process_data()
                res = p.process_to_mysql(data)
                if res == '1':
                    print('{}的发送的记录已经保存成功'.format(message['data']['from_chatroom_nickname']))
            else:
                print('无有效数据')


    if message['type'] == 'msg::single':
        if message.get("data") is not None and message['data']['from_wxid'] in single_list and message['data']['send_or_recv'][0] == '0':
            p = process_data()
            res=p.process_single_to_mysql(message)
            if res == '1':
                print('{}的发送的记录已经保存成功'.format(message['data']['from_nickname']))
        if message.get("data") is not None and message['data']['from_wxid'] == filehelper and message['data']['send_or_recv'][0] == '1':
            p = process_data()
            res=p.process_single_to_mysql(message)
            if res == '1':
                print('{}的发送的记录已经保存成功'.format(message['data']['from_nickname']))


def main_wechat_control():
    wx_ins = WechatPCAPI(on_message=on_message)
    wx_ins.start_wechat(block=True)
    wx_ins.update_frinds()
    while not wx_ins.get_myself():
        time.sleep(5)


main_wechat_control()

class process_data():

    def process_single_to_excel(self,message):
        data = {'time': message['data']['time'], 'msg': message['data']['msg'],
                'from_wxid': message['data']['from_wxid'], 'from_nickname': message['data']['from_nickname'],
                'from_chatroom_nickname': message['data']['from_nickname']}
        print(data)
        res = to_save(data)
        return res

    def process_single_to_mysql(self,message):
        # data = {'time': message['data']['time'], 'msg': message['data']['msg'],
        #         'from_wxid': message['data']['from_wxid'], 'from_nickname': message['data']['from_nickname'],
        #         'from_chatroom_nickname': message['data']['from_nickname']}
        data={}
        if message.get("data"):
            data['time']=message['data']['time']
            data['msg']=message['data']['msg']
            data['from_wxid']=message['data']['from_wxid']
            data['from_nickname']=message['data']['from_nickname']
            data['from_chatroom_nickname']=message['data']['from_nickname']
        else:
            return '0'
        res = mysql_util().save_record_to_mysql(data)
        return res

    def process_to_mysql(self,data):
        res = mysql_util().save_record_to_mysql(data)
        return res


