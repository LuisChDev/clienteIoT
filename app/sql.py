from pony import orm

from datetime import datetime
myDb = orm.Database()

class TempRecord(myDb.Entity):
    timestamp = orm.Required(datetime)
    temperature = orm.Required(float)
    recorded = orm.PrimaryKey(datetime)

myDb.bind(provider='mysql', user='root', db='clienteIoT', passwd='dinero')
myDb.generate_mapping(create_tables=True)

# saves to database
@orm.db_session
def insert_temp(tmsp, tmp, rcd):
    tempMy = TempRecord(timestamp=tmsp,
                        temperature=tmp,
                        recorded=rcd)
    print(tempMy)
