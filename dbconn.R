library(RODBC)                                # Library for connecting to SQL
library(data.table)                           # Library for handling dataframes

driver <- "{SQL Server}"                      # Database driver
server <- "server name or direction"          # Database IP or DNS
database <- "database name"                   # Database name
usr <- "user"                                 # Database user
passw <- "pass"                               # Database password
table <- "mytable"                            # Table to access

conn_string <- paste0('DRIVER=', driver, ';Server=', server, ';DATABASE=', database, ';UID=', usr, ';PWD=', passw)             # String with parameters to be passed for connection
dbconnection <- odbcDriverConnect(conn_string)                                                                                 # Creates connections with the BD
df <- data.table(sqlQuery(dbconnection, paste0("select * from ", table)))                                                      # launches the query and saves the data in a dataframe

