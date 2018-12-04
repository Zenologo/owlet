#
# Environement: python3.6
#
import configparser

from sqlite_manager import SqliteManage

def main():
    cf = configparser.ConfigParser()
    cf.read("conf.cfg")
    print(cf.get("db_sqlite", "database"))
    
    sqlite = SqliteManage()
    sqlite.database = cf.get("db_sqlite", "database")
    
    # create a database connection
    sqlite.conn = sqlite.create_connection()
    with sqlite.conn:
        print("1. Query task by priority:")
        sqlite.get_task_by_priority(sqlite.conn)
 
        #print("2. Query all tasks")
        #sqlite.select_all_tasks(conn)
 
if __name__ == '__main__':
    main()
