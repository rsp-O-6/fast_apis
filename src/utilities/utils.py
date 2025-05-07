import psycopg
import base64
import json
import yaml
from decimal import Decimal
import os
import pandas as pd



with open("config.yaml") as yaml_data_file:
    config = yaml.safe_load(yaml_data_file)

    conn_string = config["database"]


def execute_query(query, params=None) -> dict[str, pd.DataFrame]:
    result = {}

    try:
        with psycopg.connect(conn_string) as conn:
            print("✅ Successfully connected to database")

            with conn.cursor() as cur:
                cur.execute(query, params)
                print("✅ Query executed")

                rows = cur.fetchall()
                print(f"🟡 Raw Rows Fetched: {rows}")

                if rows:
                    df = pd.DataFrame(rows, columns=[desc.name for desc in cur.description])
                    result["data"] = df
                    print("\n✅ DataFrame Created:")
                    print(df)
                else:
                    result["data"] = pd.DataFrame()
                    print("⚠️ No data found, returning empty DataFrame.")

    except (Exception, psycopg.Error) as error:
        print("❌ Error occurred:", error)

    print("📴 Database connection closed\n")
    return result




def save_error_message(msg: str):
    if msg is not None:
        execute_query("call usp_save_api_error_log(_error_msg => %s)", (msg, ))


