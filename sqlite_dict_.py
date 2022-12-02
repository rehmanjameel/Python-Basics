from sqlitedict import SqliteDict

db = SqliteDict("example_dict.sqlite")

db["1"] = {"first_name", "John"}
db["2"] = {"last_name", "doe"}
db["3"] = {"user_name", "johndoe"}

db.commit()

print("There are %d items in the db" % len(db))

for key, item in db.items():
    print("%s=%s" % (key, item))

db.close()
