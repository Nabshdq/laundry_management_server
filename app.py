# app.py
from flask import Flask, request, jsonify, session
from models import create_connection
from flask_session import Session

app = Flask(__name__)

#Endpoints untuk menambahkan user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO User (nama, username, password, level_akses) VALUES (%s, %s, %s, %s)",
            (data["nama"], data["username"], data["password"], data["level_akses"]),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "User added successfully"}), 201
    return jsonify({"message": "Error connecting to database"}), 500

#Endpoints untuk mendapatkan semua user
@app.route("/users", methods=["GET"])
def get_users():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users), 200
    return jsonify({"message": "Error connecting to database"}), 500

#Endpoints untuk memperbarui data user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE User SET nama = %s, username = %s, password = %s, level_akses = %s WHERE user_id = %s",
            (
                data["nama"],
                data["username"],
                data["password"],
                data["level_akses"],
                user_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menghapus user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM User WHERE user_id = %s", (user_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menambahkan pelanggan
@app.route("/pelanggan", methods=["POST"])
def add_pelanggan():
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Pelanggan (nama, alamat, nomor_telepon, email) VALUES (%s, %s, %s, %s)",
            (data["nama"], data["alamat"], data["nomor_telepon"], data["email"]),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Pelanggan added successfully"}), 201
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk mendapatkan semua pelanggan
@app.route("/pelanggan", methods=["GET"])
def get_pelanggan():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Pelanggan")
        pelanggan = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(pelanggan), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk memperbarui data pelanggan
@app.route("/pelanggan/<int:pelanggan_id>", methods=["PUT"])
def update_pelanggan(pelanggan_id):
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Pelanggan SET nama = %s, alamat = %s, nomor_telepon = %s, email = %s WHERE pelanggan_id = %s",
            (
                data["nama"],
                data["alamat"],
                data["nomor_telepon"],
                data["email"],
                pelanggan_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Pelanggan updated successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

# Method untuk menghapus data pelanggan
@app.route("/pelanggan/<int:pelanggan_id>", methods=["DELETE"])
def delete_pelanggan(pelanggan_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Pelanggan WHERE pelanggan_id = %s", (pelanggan_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Pelanggan deleted successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menambahkan pesanan
@app.route("/pesanan", methods=["POST"])
def add_pesanan():
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO PesananLaundry (tanggal_pemesanan, nama_pelanggan, jenis_layanan, jumlah_cucian, harga_total, status_pesanan) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                data["tanggal_pemesanan"],
                data["nama_pelanggan"],
                data["jenis_layanan"],
                data["jumlah_cucian"],
                data["harga_total"],
                data["status_pesanan"],
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Pesanan added successfully"}), 201
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk mendapatkan semua pesanan
@app.route("/pesanan", methods=["GET"])
def get_pesanan():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PesananLaundry")
        pesanan = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(pesanan), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk memperbarui data pesanan
@app.route("/pesanan/<int:pesanan_id>", methods=["PUT"])
def update_pesanan(pesanan_id):
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE PesananLaundry SET tanggal_pemesanan = %s, nama_pelanggan = %s, jenis_layanan = %s, jumlah_cucian = %s, harga_total = %s, status_pesanan = %s WHERE pesanan_id = %s",
            (
                data["tanggal_pemesanan"],
                data["nama_pelanggan"],
                data["jenis_layanan"],
                data["jumlah_cucian"],
                data["harga_total"],
                data["status_pesanan"],
                pesanan_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Pesanan laundry updated successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menghapus pesanan
@app.route("/pesanan/<int:pesanan_id>", methods=["DELETE"])
def delete_pesanan(pesanan_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM PesananLaundry WHERE pesanan_id = %s", (pesanan_id,)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Pesanan laundry deleted successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menambahkan inventaris
@app.route("/inventaris", methods=["POST"])
def add_inventaris():
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO InventarisBahanBaku (nama_bahan_baku, jumlah_stok, harga_beli) VALUES (%s, %s, %s)",
            (data["nama_bahan_baku"], data["jumlah_stok"], data["harga_beli"]),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Inventaris added successfully"}), 201
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk mendapatkan semua inventaris
@app.route("/inventaris", methods=["GET"])
def get_inventaris():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM InventarisBahanBaku")
        inventaris = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(inventaris), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk memperbarui data inventaris
@app.route("/inventaris/<int:bahan_baku_id>", methods=["PUT"])
def update_inventaris_bahan_baku(bahan_baku_id):
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE InventarisBahanBaku SET nama_bahan_baku = %s, jumlah_stok = %s, harga_beli = %s WHERE bahan_baku_id = %s",
            (
                data["nama_bahan_baku"],
                data["jumlah_stok"],
                data["harga_beli"],
                bahan_baku_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Inventaris bahan baku updated successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menghapus inventaris
@app.route("/inventaris/<int:bahan_baku_id>", methods=["DELETE"])
def delete_inventaris_bahan_baku(bahan_baku_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM InventarisBahanBaku WHERE bahan_baku_id = %s", (bahan_baku_id,)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Inventaris bahan baku deleted successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menambahkan laporan
@app.route("/laporan", methods=["POST"])
def add_laporan():
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Laporan (jenis_laporan, tanggal_laporan, data_laporan) VALUES (%s, %s, %s)",
            (data["jenis_laporan"], data["tanggal_laporan"], data["data_laporan"]),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Laporan added successfully"}), 201
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk mendapatkan semua laporan
@app.route("/laporan", methods=["GET"])
def get_laporan():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Laporan")
        laporan = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(laporan), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk memperbarui data laporan
@app.route("/laporan/<int:laporan_id>", methods=["PUT"])
def update_laporan(laporan_id):
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Laporan SET jenis_laporan = %s, tanggal_laporan = %s, data_laporan = %s WHERE laporan_id = %s",
            (
                data["jenis_laporan"],
                data["tanggal_laporan"],
                data["data_laporan"],
                laporan_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Laporan updated successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

#endpoints untuk menghapus laporan
@app.route("/laporan/<int:laporan_id>", methods=["DELETE"])
def delete_laporan(laporan_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Laporan WHERE laporan_id = %s", (laporan_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Laporan deleted successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

# Endpoint untuk menambah karyawan
@app.route("/karyawan", methods=["POST"])
def add_karyawan():
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Karyawan (nama_karyawan, username, email) VALUES (%s, %s, %s)",
            (data["nama_karyawan"], data["username"], data["email"]),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Karyawan added successfully"}), 201
    return jsonify({"message": "Error connecting to database"}), 500

# Endpoint untuk mendapatkan semua karyawan
@app.route("/karyawan", methods=["GET"])
def get_karyawan():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Karyawan")
        karyawan = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(karyawan), 200
    return jsonify({"message": "Error connecting to database"}), 500

# Endpoint untuk memperbarui data karyawan
@app.route("/karyawan/<int:karyawan_id>", methods=["PUT"])
def update_karyawan(karyawan_id):
    data = request.json
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Karyawan SET nama_karyawan = %s, username = %s, email = %s WHERE karyawan_id = %s",
            (
                data["nama_karyawan"],
                data["username"],
                data["email"],
                karyawan_id,
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Karyawan updated successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

# Endpoint untuk menghapus karyawan
@app.route("/karyawan/<int:karyawan_id>", methods=["DELETE"])
def delete_karyawan(karyawan_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Karyawan WHERE karyawan_id = %s", (karyawan_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Karyawan deleted successfully"}), 200
    return jsonify({"message": "Error connecting to database"}), 500

# Konfigurasi untuk Flask-Session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "supersecretkey"
Session(app)

# Endpoint untuk login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM User WHERE username = %s AND password = %s",
            (username, password),
        )
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            # Simpan informasi pengguna di sesi
            session["user_id"] = user[0]  # Asumsikan user_id ada di kolom pertama
            session["username"] = user[1]  # Asumsikan username ada di kolom kedua
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    return jsonify({"message": "Error connecting to database"}), 500

# Endpoint untuk logout
@app.route("/logout", methods=["POST"])
def logout():
    # Hapus informasi pengguna dari sesi
    session.pop("user_id", None)
    session.pop("username", None)
    return jsonify({"message": "Logout successful"}), 200

# Endpoint untuk mendapatkan profil pengguna
@app.route("/profile", methods=["GET"])
def profile():
    if "user_id" in session:
        return jsonify({
            "user_id": session["user_id"],
            "username": session["username"]
        }), 200
    return jsonify({"message": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(debug=True)
