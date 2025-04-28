import sqlite3 as sql

if __name__ == "__main__":
    try:
        conn = sql.connect("ProgramacionSobreRedes-PFO1.db") #establece la conexion y crea la BD si no existe
        conn.commit() #guarda los cambios
        cursor = conn.cursor()
        cursor.execute("""
                        CREATE TABLE message (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        contenido TEXT,
                        fecha_envio TEXT,
                        ip_cliente TEXT)""")
        conn.commit()
        conn.close()
    except: 
        print("Error connecting database")

def saveMessage(message,date,ip):
    try:
        conn = sql.connect("ProgramacionSobreRedes-PFO1.db")
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO message (contenido,fecha_envio,ip_cliente) VALUES('{message}','{date}','{ip}')""")
        conn.commit()
        conn.close()
    except: 
        print("Error saving message")