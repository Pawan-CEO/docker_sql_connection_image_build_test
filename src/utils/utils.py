
from flask import Flask, jsonify , request
import pyodbc
import pandas as pd
import os
import json
# import request


class WorkUtils:
    def __init__(self):
        # Connection parameters  
        file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","config","config.json")
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        self.config=config


    def test_process(self):
        try:
            query = """
                SELECT top 1 *
                FROM synd.CompetitivePricingData
                """
            print(query)
            # Execute the query and fetch the results
            # Establish the database connection using the config
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config["server"]};DATABASE={self.config["database"]};UID={self.config["username"]};PWD={self.config["password"]}'
            connection = pyodbc.connect(conn_str)
            cursor = connection.cursor()
            cursor.execute(query)
            
            results = cursor.fetchall()
            print(results)
            return {"Message":"Code is Working"}


        except Exception as e:
            print(e)