import pyodbc

server = "NTB-479\SQLEXPRESS"
database = "DevLocal"
username = ""
password = ""

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
)

def conexao():
    return conn