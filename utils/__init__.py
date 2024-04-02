import redis


class redis_c:
     host='localhost'
     port=6379
     db=0
     redis_inst=None

     def __init__(self,host,port,db):
         self.host=host
         self.port=port
         self.db=db
         self.redis_inst=redis.Redis(host=self.host, port=self.port, decode_responses=True, db=self.db)



     # def get_redis_inst(self):
     #    if self.redis_inst==None:
     #        self.redis_inst = redis.Redis(host=self.host, port=self.port, decode_responses=True,db=self.db)
     #    return self.redis_inst

redis_inst=redis_c(host="localhost",port=6379,db=0).redis_inst
# print(redis_inst.get('rowindex'))
