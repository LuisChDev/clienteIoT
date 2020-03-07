import redis

r = redis.Redis()

def insert_temp(tmsp, tmp, rcd):
    r.set(rcd.timestamp(), "(temperature {}, timestamp {})".format(tmp, tmsp.timestamp()) )
    print(rcd)
