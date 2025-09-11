import psycopg2
import base64
import json
import yaml
from decimal import Decimal
import os
import pandas as pd



with open("config.yaml") as yaml_data_file:
    config = yaml.safe_load(yaml_data_file)

    db_conn_details = config["database"]

def execute_query(query, params=None) -> dict[str, pd.DataFrame]:
    # conn = psycopg2.connect(conn_string)
    conn = psycopg2.connect(dbname=db_conn_details["DBName"],
                            user=db_conn_details["user"],
                            password=db_conn_details["password"],
                            host= db_conn_details["host"],
                            port=db_conn_details["port"])

    result = {}
    try:
        cur = conn.cursor()
        cur.execute(query, params)

        cursor_names = cur.fetchall()

        if len(cursor_names)>0:

            cursor_names = cursor_names[0]

            for _cursor in cursor_names:
                try:

                    cur.execute(f'fetch all in {_cursor}')
                    d = cur.fetchall()
                    df = pd.DataFrame(d, columns=[i[0] for i in cur.description])

                    result[_cursor] = df
                except Exception as e:
                    print("Error in execute_query:",e)
                    # asyncio.run(log_async(logger.error, e.__str__()))
                    # asyncio.run(log_error(e, extra_info='execute_query', extra_data='Query => '+ query+', Params => '+(','.join(params))+', Cursor => '+_cursor))
        else:
            pass

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in execute_query:",error)
        # asyncio.run(log_async(logger.error, e.__str__()))
        # asyncio.run(log_error(error, extra_info='execute_query', extra_data='Query => '+ query+', Params => '+(','.join(params))))
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

    return result


# def save_error_message(msg: str):
#     if msg is not None:
#         execute_query("call usp_save_api_error_log(_error_msg => %s)", (msg, ))


