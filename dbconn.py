import pyodbc                                           # Library for connecting to SQL
import pandas as pd                                     # Library for handling dataframes

driver = "{SQL Server}"                                 # Database driver
server = "server name or direction"                     # Database IP or DNS
database = "database name"                              # Database name
usr = "user"                                            # Database user
passw = "pass"                                          # Database password
table = "mytable"                                       # Table to access


conn_string = 'DRIVER=' + driver + ';Server=' + server + ';DATABASE=' + database  +';UID=' + usr + ';PWD=' + passw              # String with parameters to be passed for connection
connection = pyodbc.connect(conn_string)                                                                                        # Creates connections with the BD
df = pd.read_sql("SELECT * FROM %s" %(table), con = connection)                                                                 # launches the query and saves the data in a dataframe
connection.close()                                                                                                              # Closing the connection

