import sqlite3

TABLE_NAME="raws_numbers"

def createTable(cursor):
    cursor.execute(""" 
        SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';
    """)
    if(len(cursor.fetchall())==0):
        cursor.execute(""" 
            CREATE TABLE '{TABLE_NAME}' (
                type text UNIQUE,
                array text
            );
        """)

def dropTable(cursor):
    cursor.execute(""" 
        SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';
    """)
    if(len(cursor.fetchall())>0):
        cursor.execute(""" 
            DROP TABLE '{TABLE_NAME}';
        """)

def readTable(cursor):
    cursor.execute(""" 
        SELECT * FROM '{TABLE_NAME}'
    """)
    for item in cursor.fetchall():
        print(item[0]+"\t:\t"+item[1])

def storeArr(cursor,name_type,arr):
    if(len(arr)%2!=0):
        print("Número Impar de Datos en el Arreglo")
        return
    arr.sort()
    only_values=str(arr)[1:-1]
    cursor.execute("INSERT INTO '{TABLE_NAME}' VALUES (?,?)",[name_type,only_values])

def deleteArr(cursor,name_type):
    cursor.execute("DELETE FROM '{TABLE_NAME}' WHERE (type=?)",[name_type])

def getArrsObject(cursor):
    cursor.execute(""" 
        SELECT * FROM '{TABLE_NAME}'
    """)
    obj={}
    for item in cursor.fetchall():
        obj[item[0]]=[int(numeric_string) for numeric_string in item[1].split(",")]
    return(obj)

conn = sqlite3.connect("raws_numbers.db")
c=conn.cursor()

#dropTable(c)
#createTable(c)

#getArrsObject(c)

# deleteArr(c,"Materno")
# storeArr(c,"Salud Mental",[11, 12, 15, 21, 28, 53, 59, 63, 67, 90, 94, 103, 107, 110, 115, 119, 121, 122, 126, 140, 142, 148, 155, 159, 161, 166, 171, 183, 188, 190, 195, 198, 204, 205, 208, 209, 214, 219, 221, 223, 230, 236, 240, 242, 246, 248, 252, 255, 257, 258, 261, 262, 267, 269, 271, 272, 279, 286, 288, 289, 292, 293, 296, 297, 299, 304, 309, 313, 317, 319, 324, 332, 337, 353, 357, 370, 375, 387, 392, 402, 406, 423, 428, 452])

readTable(c)

conn.commit()
conn.close()


#EXAMPLES
#storeArr(c,"Niños",[13, 16, 21, 29, 33, 45, 50, 58, 63, 71, 76, 86, 90, 114, 119, 135, 140, 150, 155, 159, 165, 166, 173, 180, 187, 194, 200, 201, 206, 209, 214, 215, 223, 229, 233, 238, 245, 246, 252, 255, 260, 262, 267, 284, 287, 291, 296, 305, 310, 315, 319, 323, 329, 331, 338, 349, 355, 357, 362, 364, 369, 371, 376, 387, 392, 394, 400, 401, 407, 408, 415, 419, 425, 428])
#storeArr(c,"Nutricion",[11, 20, 24, 27, 32, 37, 40, 58, 61, 74, 78, 98, 101, 130, 134, 163, 167, 182, 185, 193, 197,201,205,206,209, 216, 222, 234, 238, 244, 247, 253])