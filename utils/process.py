import re


class tools():
    keys = ['证件号码', '编号', '姓名', '单位', '单位编码', '这个人', '包号', '麻烦', '未到账', '税务编码', '个人编号', '人员姓名', '职工', '医保', '居民',
            '灵活就业', '企业', '停保', '帮忙', '缴费', '缴费记录', '身份证', '数据包', '数据包号', '保险', '工伤', '社保', '职业年金', '养老', '医疗补助', '险种']

    processors = ['@税友-邓华杰', '@税友-苏西川', '@税友-王林', '@税友-肖体旭', '@税友-日落夕碎','华杰']

    # processors = ['邓华杰', '苏西川 ', '王林', '肖体旭', '日落夕碎']

    def check_msg(self, msg):
        is_reply = self.is_reply(msg)
        if is_reply is None:
            return is_reply
        try:
            flag = False
            # new_msg=self.remove_blank_lines(msg)
            for i in self.keys:
                if i in msg:
                    flag = True
                    break
            pat_id = r"\d{18}|\d{17}[xX]|\d{15}"
            id_list = re.findall(pat_id, msg)
            # 匹配数字
            danwei_or_other_code = r"\d+"
            danwei_list = re.findall(danwei_or_other_code, msg)
            if flag and (len(id_list) > 0 or len(danwei_list) > 0):
                text1 = self.remove_processor(msg)
                text2 = self.remove_sensitive_info(text1)
                # text3 = self.remove_blank_lines(text2)
                if all([text1, text2]):
                    return text2
                if text1 is not None:
                    return text1
            else:
                return None
        except Exception as e:
            print(e)
            return None

    ##移除空行
    # def remove_blank_lines(self, text):
    #     try:
    #         lines = text.split('\n')
    #         non_empty_lines = []
    #         for line in lines:
    #             line = line.strip()
    #             if line:
    #                 non_empty_lines.append(line)
    #         return '\n'.join(non_empty_lines)
    #     except Exception as e:
    #         print(e)
    #         return None

    # 屏蔽敏感信息
    def remove_sensitive_info(self, text):
        try:
            pat_id = r"\d{18}|\d{17}[xX]|\d{15}"
            id_list = re.findall(pat_id, text)
            repl = '{}'
            new_text = re.sub(pattern=pat_id, repl=repl, string=text)
            for id in id_list:
                new_id = id[0:6] + '******' + id[-6:]
                new_text = re.sub(pattern=pat_id, repl=new_id, string=text)
            return new_text
        except Exception as e:
            print(e)
            return None

    ##移除处理问题的人@
    def remove_processor(self, text):
        try:
            ls=[text]
            for processor in self.processors:
                if len(re.findall(processor, ls[-1]))>0:
                    ls.append(ls[-1].replace(processor, ''))
            return ls[-1]

        except Exception as e:
            print(e)
            return None

    def is_reply(self, text):
        if '- - - - - - - - - - - - - - -' in text:
            return None
        return text


# t = tools()
# msg = '540599106956@税友-苏西川?帮查下这个单位12月缴费包呢,@税友-王林511602199802282116整个单位职工没到账'
# s = t.remove_processor(msg)
# print(s)
# for i in t.processors:
#     # print(i)
#     if len(re.findall(i,msg))>0:
#         print("ok")
