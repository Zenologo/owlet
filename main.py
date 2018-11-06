from sqlite_manager import SqliteManage


def main():
    
    sqlite = SqliteManage()
    sqlite.database = "../hummingbird/db.sqlite3"
    
    # create a database connection
    sqlite.conn = sqlite.create_connection()
    with sqlite.conn:


        print("1. Query task by priority:")
        sqlite.select_task_by_priority(sqlite.conn, 1)
 
        #print("2. Query all tasks")
        #sqlite.select_all_tasks(conn)
 
if __name__ == '__main__':
    main()
