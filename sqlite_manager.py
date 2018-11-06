import sqlite3
from sqlite3 import Error

class SqliteManage:
    database = "../hummingbird/db.sqlite3"
    conn = None

    def create_connection(self):
        

        try:
            conn = sqlite3.connect(self.database)
            return conn
        except Error as e:
            print(e)
    
        return None
 
 
    def select_all_tasks(self,  conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM geckotask")
    
        rows = cur.fetchall()
    
        for row in rows:
            print(row)
    
    
    def select_task_by_priority(self,  conn, priority):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        print('')
        cur.execute("SELECT * FROM geckotask_parser; ")
        rows = cur.fetchall()
        
        for row in rows:
            print(row)
        
    def set_db(self, db_path):
        self.database = db_path    
