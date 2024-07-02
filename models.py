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
        CREATE TABLE IF NOT EXISTS Pelanggan (
            pelanggan_id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100),
            alamat TEXT,
            nomor_telepon VARCHAR(15),
            email VARCHAR(100)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PesananLaundry (
            pesanan_id INT AUTO_INCREMENT PRIMARY KEY,
            tanggal_pemesanan DATE,
            nama_pelanggan VARCHAR(100),
            jenis_layanan VARCHAR(100),
            jumlah_cucian INT,
            harga_total DECIMAL(10, 2),
            status_pesanan VARCHAR(50)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS InventarisBahanBaku (
            bahan_baku_id INT AUTO_INCREMENT PRIMARY KEY,
            nama_bahan_baku VARCHAR(100),
            jumlah_stok INT,
            harga_beli DECIMAL(10, 2)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Laporan (
            laporan_id INT AUTO_INCREMENT PRIMARY KEY,
            jenis_laporan VARCHAR(100),
            tanggal_laporan DATE,
            data_laporan TEXT
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

        connection.commit()
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_tables()
