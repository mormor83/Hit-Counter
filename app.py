from app import app
from app.helper_func import *
from config import Config

app.config['SECRET_KEY'] = Config.SECRET_KEY

if __name__ == "__main__":
    database = ('database.db')
    sql_create_projects_table  = """ CREATE TABLE IF NOT EXISTS hits_counter (hits integer ) """
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        insert_initial_value(conn,'0')
        reset_hit_count(conn)
    else:
        print("Error! cannot create the database connection.")
    app.run(debug=True, host="0.0.0.0")