import pymysql

# --- Config ---
_host = "localhost"
_user = "root"
_pass = ""
_database = "db_global_test"
_table = "tbl_lorem"

class Database:
    def connect(self):
        return pymysql.connect(host=_host, user=_user, password=_pass, database=_database, charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM tbl_lzw order by id asc")
            else:
                cursor.execute("SELECT * FROM tbl_lzw where id = %s order by id asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO tbl_lzw(file_name,file_size) VALUES(%s, %s)",
                           (data['file_name'], data['file_size']))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE tbl_user set nama = %s, nik = %s, alamat = %s, jk = %s, hari = %s, tanggal = %s, tempat = %s, penyebab = %s where id = %s",
                           (data['nama'], data['nik'], data['alamat'], data['jk'], data['hari'], data['tanggal'], data['tempat'], data['penyebab'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, name):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM tbl_lzw where file_name = %s", (name))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()