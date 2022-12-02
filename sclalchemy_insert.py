import sql_alchemy
from sqlalchemy.orm import sessionmaker  # this library add data to database
import random

# new session
Session = sessionmaker(bind=sql_alchemy.engine)
session = Session()

# adding data

regis = sql_alchemy.Registration("firstname0", "lastname0", "username0")
session.add(regis)

# save changes into database
session.commit()
