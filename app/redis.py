import redis

r = redis.Redis(host="redis", port=6379)

def insert_temp(tmsp, tmp, rcd):
    r.set(rcd.timestamp(), "(temperature {}, timestamp {})".format(tmp, tmsp.timestamp()) )
    print(rcd)

# función para parsear el valor de los records de temperatura. Se empleará en una
# futura versión.
