# message = {
#     'user': 'wxid_rfcg3rg1jfjr22',
#     'type': 'msg::single',
#     'data': {
#         'data_type': '1',
#         'send_or_recv': '0+[收到]',
#         'from_wxid': 'wxid_f4dfmviveae712',
#         'time': '2024-01-23 11:13:16',
#         'msg': '54019910204704  这个职工身份证号码发我',
#         'msg_byte_hex': '35343031393931303230343730342020D5E2B8F6D6B0B9A4C9EDB7DDD6A4BAC5C2EBB7A2CED2',
#         'from_nickname': '每天吃不饱。'
#     }
# }


# if message['data']['from_wxid']=='wxid_f4dfmviveae712':
#     if message['data']['send_or_recv'][0]=='0':
#         print(message['data']['msg'])

"""
群聊
'from_chatroom_wxid':'20031586753@chatroom'
'send_or_recv': '0+[收到]'

个人
陈立军:'from_wxid': 'wxid_f4dfmviveae712' 
刘怀顺：'from_member_wxid': 'wxid_o4ey6k93qd9421',
陈泽森：'from_member_wxid': 'wxid_i7c5h1hnqd5q22'
医保-黄文：'from_member_wxid': 'wxid_bjp1uw5616di22'
阿里王润峰：'from_member_wxid': 'wxid_on3go3ryopen21'
杨宇：'from_member_wxid': 'wxid_20rjnpxxyrt012'
索朗：'from_member_wxid': 'wxid_r5vfllltf2xy22'

体旭哥：wxid_m3b926cfeacp21
华杰哥：wxid_n06g80luyryn21  
王林哥：wxid_iewrefcj52tk21
"""

"""
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'friend::person', 'data': {'wx_id': 'wxid_n06g80luyryn21', 'wx_id_search': 'Vc08866', 'wx_nickname': '止歌', 'wx_avatar': 'http://wx.qlogo.cn/mmhead/ver_1/6B087T7v9wGiaV7MKufe5yFyz75PyX1KKTdicGlgOdFMnexvNSP4TnOicNEC3fz8OYRicMd6IiceiaYI7rZSCvkMawJxax8JiaX8v3YibpwERX1ZRbA/132', 'remark_name': '邓华杰'}}
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'friend::chatroom', 'data': {'chatroom_id': '25302656702@chatroom', 'chatroom_name': '人社税务技术群', 'chatroom_avatar': 'http://wx.qlogo.cn/mmcrhead/icXtjp9jsR5S5kW0EOwhkZWzm2D4bp8icEazicrjibiayunL1DPsxpvZicNPLjm1MBTiao0j0ZcHMP4nNX8Lfict9WnHXjNHDfjmoYmy/0'}}
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'friend::person', 'data': {'wx_id': 'wxid_i7c5h1hnqd5q22', 'wx_id_search': 'czs1998830', 'wx_nickname': 'xixi', 'wx_avatar': 'http://wx.qlogo.cn/mmhead/ver_1/XvX0IwhfwL7ghuDjyGyZQrKvNTWRPIMgnJ33ZduZvibibySU9YRiavLIDAj2YQuRzv3IY6lhAhLtvIZict8AXOvyFA/132', 'remark_name': '陈泽森'}}
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'friend::person', 'data': {'wx_id': 'wxid_bjp1uw5616di22', 'wx_id_search': 'stccpbqyblyh', 'wx_nickname': 'X', 'wx_avatar': 'http://wx.qlogo.cn/mmhead/ver_1/k8Z0bgpHGTa7icJ4JSiau8ymmgQFV0M3rRf01SsaNIG09Mx9ia8zHmGnL57wVJVSxlp9LtPicwtdic7W79Br88ncAwHmOCLfJtwzkNXe4E3oxf64/132', 'remark_name': '医保-黄文'}}
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'friend::person', 'data': {'wx_id': 'wxid_iewrefcj52tk21', 'wx_id_search': 'lin411324', 'wx_nickname': '明天去放羊', 'wx_avatar': 'http://wx.qlogo.cn/mmhead/ver_1/jjqaicU5onOK8HEh2DAfUnTh0GicribnRqejCick7nt7W0uwhNLIPVpqQHh3v1XCmewFcwSZlwa3ibqe61ocHfWFQjSqiaAXH2ibne0hFnFSK2iaDSWWyY1VKvWNZNVK8Er6pjonmeKiauIBNmJvQ6ib8v9CWiaOw/132', 'remark_name': '王林'}}
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'friend::person', 'data': {'wx_id': 'wxid_on3go3ryopen21', 'wx_id_search': 'xiaofeng40701', 'wx_nickname': '爱吃火锅', 'wx_avatar': 'http://wx.qlogo.cn/mmhead/ver_1/P4JHdkJI1uxt0e9RrsVfRJBGm5aMJxIWM2Leu1B2BR8uYBgtuUPsDBPPuBHCmrqzU36nzcbMhbPke8A8NqunMJyBU8DTRmvZtfabahwktbYrMekHCwoQ8yXWVwRpxPYXVicDhYicticrMkGR93NfEU1iaw/132', 'remark_name': '阿里王润峰'}}
{'user': 'wxid_rfcg3rg1jfjr22', 'type': 'msg::chatroom', 'data': {'data_type': '1', 'send_or_recv': '0+[收到]', 'from_chatroom_wxid': '20031586753@chatroom', 'from_member_wxid': 'wxid_m3b926cfeacp21', 'time': '2024-01-23 11:43:15', 'msg': '@税友-苏西川?', 'msg_byte_hex': '40CBB0D3D12DCBD5CEF7B4A83F', 'from_chatroom_nickname': '城乡医保缴费确认'}} 体旭哥

"""
# 体旭哥：wxid_m3b926cfeacp21
# 华杰哥：wxid_n06g80luyryn21
# 王林哥：wxid_iewrefcj52tk21

# message={
# 	'user': 'wxid_rfcg3rg1jfjr22',
# 	'type': 'msg::chatroom',
# 	'data': {
# 		'data_type': '1',
# 		'send_or_recv': '0+[收到]',
# 		'from_chatroom_wxid': '20031586753@chatroom',
# 		'from_member_wxid': 'wxid_i7c5h1hnqd5q22',
# 		'time': '2024-01-23 11:56:13',
# 		'msg': '540102198703020519这个职工 帮忙在540100205557这个单位停保一下 停到23年12月31日',
# 		'msg_byte_hex': '353430313032313938373033303230353139D5E2B8F6D6B0B9A420B0EFC3A6D4DA353430313030323035353537D5E2B8F6B5A5CEBBCDA3B1A3D2BBCFC220CDA3B5BD3233C4EA3132D4C23331C8D5',
# 		'from_chatroom_nickname': '城乡医保缴费确认'
# 	}
# }

# message={
# 	'user': 'wxid_rfcg3rg1jfjr22',
# 	'type': 'msg::chatroom',
# 	'data': {
# 		'data_type': '1',
# 		'send_or_recv': '0+[收到]',
# 		'from_chatroom_wxid': '25302656702@chatroom',
# 		'from_member_wxid': 'wxid_n06g80luyryn21',
# 		'time': '2024-01-23 12:25:45',
# 		'msg': '@税友-苏西川?',
# 		'msg_byte_hex': '40CBB0D3D12DCBD5CEF7B4A83F',
# 		'from_chatroom_nickname': '人社税务技术群'
# 	}
# }



# def to_save(data):
#     pass

#处理微信群的消息
# if message['type']=='msg::chatroom':
#     data = {}
#     # 城乡医保确认群：
#     if message['data']['from_chatroom_wxid']=='20031586753@chatroom' and message['data']['send_or_recv'][0]=='0':
#             if message['data']['from_member_wxid'] not in ['wxid_m3b926cfeacp21','wxid_n06g80luyryn21','wxid_iewrefcj52tk21']:
#                 data['time']=message['data']['time']
#                 data['msg']=message['data']['msg']
#                 data['from_member_wxid']=message['data']['from_member_wxid']
#                 data['from_chatroom_nickname']=message['data']['from_chatroom_nickname']
#                 to_save(data)
#
#     #人社税务技术群
#     if message['data']['from_chatroom_wxid']=='25302656702@chatroom' and message['data']['send_or_recv'][0]=='0':
#             if message['data']['from_member_wxid'] not in ['wxid_m3b926cfeacp21','wxid_n06g80luyryn21','wxid_iewrefcj52tk21']:
#                 data['time']=message['data']['time']
#                 data['msg']=message['data']['msg']
#                 data['from_member_wxid']=message['data']['from_member_wxid']
#                 data['from_chatroom_nickname']=message['data']['from_chatroom_nickname']
#                 to_save(data)


# message={
# 	'user': 'wxid_rfcg3rg1jfjr22',
# 	'type': 'msg::single',
# 	'data': {
# 		'data_type': '1',
# 		'send_or_recv': '0+[收到]',
# 		'from_wxid': 'wxid_i7c5h1hnqd5q22',
# 		'time': '2024-01-23 11:53:24',
# 		'msg': '单位没有职工有效险种嘛',
# 		'msg_byte_hex': 'B5A5CEBBC3BBD3D0D6B0B9A4D3D0D0A7CFD5D6D6C2EF',
# 		'from_nickname': 'xixi'
# 	}
# }
# #处理个人聊天的消息
# single_list=['wxid_f4dfmviveae712','wxid_o4ey6k93qd9421','wxid_i7c5h1hnqd5q22','wxid_bjp1uw5616di22','wxid_on3go3ryopen21']
# if message['type']=='msg::single':
#     if message['data']['from_wxid'] in single_list and message['data']['send_or_recv'][0] == '0':
#         data['time'] = message['data']['time']
#         data['msg'] = message['data']['msg']
#         data['from_wxid'] = message['data']['from_wxid']
#         data['from_nickname'] = message['data']['from_nickname']
#         print(data)
#         to_save(data)



# 陈立军:'from_wxid': 'wxid_f4dfmviveae712'
# 刘怀顺：'from_member_wxid': 'wxid_o4ey6k93qd9421',
# 陈泽森：'from_member_wxid': 'wxid_i7c5h1hnqd5q22'
# 医保-黄文：'from_member_wxid': 'wxid_bjp1uw5616di22'
# 阿里王润峰：'from_member_wxid': 'wxid_on3go3ryopen21'

# keys=['证件号码','编号','姓名','单位','单位编码','这个人','包号','麻烦','未到账','税务编码','个人编号','人员姓名','职工','医保','居民','灵活就业','企业','停保','帮忙','缴费','缴费记录','身份证','数据包','数据包号']
# msg='\n人员姓名:白玛曲吉\n证件号码:542122199206190025  540521000000010626 \n个人编号:54010038894062\n单位编号:540100265619\n单位类型:10企业\n单位名称:西藏永辉超市有限公司\n经办机构:540100\n参保险种:11,21,41\n参保状态:1参保缴费\n\n这个人有两个编号， 上面那个是正确的， 54010038894059 需要注销 91540125MAB03M5F8下午帮忙处理一下。\n\n@税友-邓华杰?'.replace('\n',',')
# for i in keys:
#     if i in msg:
#         print(True)
#     break
#
#
# pat_id= r"\d{18}|\d{17}[xX]|\d{15}"
# import re
# res=re.findall(pat_id,msg)
# print(res)
#
#
# print(len('540103000000004786'))
#
# danwei_id = r"\d{18}"
# res=re.findall(danwei_id,msg)
# import re
# pat=r"\d+"
# print(re.findall(pat, """540100210671
# 540102197506260519
# 人社险种只到了养老，还缺工伤，失业"""))
from datetime import datetime

# start_str=input("请输入要导出数据的开始时间")
# start=start_str+" 00:00:00"
# format='%Y-%m-%d %H:%M:%S'
#
# print(datetime.strptime(start,format))

# import calendar
#
# print(calendar.monthrange(2024, 2))


import calendar

print(calendar.monthrange(2024, 1)[1])

current_year = datetime.now()
print(str(current_year)[0:19])