import evadb
from os import listdir

# Connect to EvaDB and get a database cursor for running queries
cursor = evadb.connect().cursor()

# print(cursor.query("DROP TABLE Image;").df())
print(cursor.query("DROP TABLE IF EXISTS Image;").df())

print(cursor.query("LOAD IMAGE './img/sample_img_1.png' INTO Image").df())
# loading a corrupted file between clean files -- the remaining file will not be loaded to the table. 
print(cursor.query("LOAD IMAGE './img/sample_img_corrupt.png' INTO Image").df())
print(cursor.query("LOAD IMAGE './img/sample_img_2.png' INTO Image").df())

# path = "./img/"
# file_list = listdir(path)

# # load files including the corrupted one; should cause an error 
# for file_name in file_list:
#     cmd = "LOAD IMAGE '" + path + file_name + "' INTO IMAGE;"
#     print(cursor.query(cmd).df())
#     break

# print(cursor.query("SELECT name, data FROM Image;").df())