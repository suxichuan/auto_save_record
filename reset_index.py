from utils import redis_c

redis_inst = redis_c(host="localhost", port=6379, db=0).redis_inst

def reset_index_method(index):
    redis_inst.set("rowindex",index)


if __name__ == '__main__':
    offset=input('请输入重置的偏移量\n')
    reset_index_method(offset)
    print('重置成功')