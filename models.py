# models.py
import mysql.connector
from mysql.connector import Error
from config import Config

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_tables():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100),
            username VARCHAR(50),
            password VARCHAR(100),
            level_akses VARCHAR(50)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Karyawan (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100),
            nomor_telepon VARCHAR(15),
            email VARCHAR(100)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PesananLaundry (
            pesanan_id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100),
            nomor_telepon VARCHAR(15),
            alamat TEXT,
            tanggal_pemesanan DATE,
            tanggal_pengambilan DATE,
            berat(kg) DECIMAL(10, 2),
            total_harga DECIMAL(10, 2),
            uang_bayar DECIMAL(10, 2),
            kembalian DECIMAL(10, 2),
            status VARCHAR(50)
            keterangan VARCHAR(100)
            type_id int FOREIGN KEY REFERENCES Type(id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Type (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100),
        )
        """)

        connection.commit()
        cursor.close()
        connection.close()

        
if __name__ == "__main__":
    create_tables()
