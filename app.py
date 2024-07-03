# app.py
from flask import Flask, request, jsonify, session
from models import create_connection
from flask_session import Session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# User Controller
@app.route("/users", methods=["GET"])
def get_users():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)


@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO User (nama, username, password, level_akses) VALUES (%s, %s, %s, %s)",
        (data["nama"], data["username"], data["password"], data["level_akses"]),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User created successfully"})


@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE User SET nama=%s, username=%s, password=%s, level_akses=%s WHERE user_id=%s",
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
    return jsonify({"message": "User updated successfully"})


@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM User WHERE user_id=%s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User deleted successfully"})


@app.route("/dashboard", methods=["GET"])
def dashboard():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    # Query to count records in karyawan table
    cursor.execute("SELECT COUNT(*) as count FROM karyawan")
    karyawan_count = cursor.fetchone()["count"]

    # Query to count records in PesananLaundry table
    cursor.execute("SELECT COUNT(*) as count FROM PesananLaundry")
    pesananlaundry_count = cursor.fetchone()["count"]

    cursor.close()
    connection.close()

    return jsonify(
        {"karyawan_count": karyawan_count, "pesananlaundry_count": pesananlaundry_count}
    )


# Karyawan Controller
@app.route("/karyawan", methods=["GET"])
def get_karyawan():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Karyawan")
    karyawans = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(karyawans)


@app.route("/karyawan", methods=["POST"])
def create_karyawan():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Karyawan (nama, nomor_telepon, email) VALUES (%s, %s, %s)",
        (data["nama"], data["nomor_telepon"], data["email"]),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Karyawan created successfully"})


@app.route("/karyawan/<int:id>", methods=["PUT"])
def update_karyawan(id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Karyawan SET nama=%s, nomor_telepon=%s, email=%s WHERE id=%s",
        (data["nama"], data["nomor_telepon"], data["email"], id),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Karyawan updated successfully"})


@app.route("/karyawan/<int:id>", methods=["DELETE"])
def delete_karyawan(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Karyawan WHERE id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Karyawan deleted successfully"})


# PesananLaundry Controller
@app.route("/pesananlaundry", methods=["GET"])
def get_pesanan_laundry():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PesananLaundry")
    pesanan_laundries = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(pesanan_laundries)


@app.route("/pesananlaundry/<int:id>", methods=["GET"])
def get_pesanan_laundry_detail(id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PesananLaundry where pesanan_id=%s", (id,))
    pesanan_laundries = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(pesanan_laundries)


@app.route("/pesananlaundry", methods=["POST"])
def create_pesanan_laundry():
    data = request.get_json()
    data = data["data"]
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO PesananLaundry (nama, nomor_telepon, alamat, tanggal_pemesanan, tanggal_pengambilan, berat_kg, total_harga, status, keterangan, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["status"],
            data["keterangan"],
            data["type_id"],
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry created successfully"})


@app.route("/pesananlaundry/<int:id>", methods=["PUT"])
def update_pesanan_laundry(id):
    data = request.get_json()
    data = data["data"]
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE PesananLaundry SET nama=%s, nomor_telepon=%s, alamat=%s, tanggal_pemesanan=%s, tanggal_pengambilan=%s, berat_kg=%s, total_harga=%s, uang_bayar=%s, kembalian=%s, status=%s, keterangan=%s, type_id=%s WHERE pesanan_id=%s",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
            data["type_id"],
            id,
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry updated successfully"})


@app.route("/pesananlaundry/<int:id>", methods=["DELETE"])
def delete_pesanan_laundry(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM PesananLaundry WHERE pesanan_id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry deleted successfully"})


# Type Controller
@app.route("/type", methods=["GET"])
def get_types():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Type")
    types = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(types)


@app.route("/type", methods=["POST"])
def create_type():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Type (nama) VALUES (%s)", (data["nama"],))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Type created successfully"})


@app.route("/type/<int:id>", methods=["PUT"])
def update_type(id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Type SET nama=%s WHERE id=%s", (data["nama"], id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Type updated successfully"})


# PesananLaundry cuci komplit Controller
@app.route("/pesananlaundry/cucikomplit", methods=["GET"])
def get_pesanan_laundry_cucikomplit():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PesananLaundry WHERE type_id=1")
    pesanan_laundries = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(pesanan_laundries)


@app.route("/pesananlaundry/cucikomplit", methods=["POST"])
def create_pesanan_laundry_cucikomplit():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO PesananLaundry (nama, nomor_telepon, alamat, tanggal_pemesanan, tanggal_pengambilan, berat_kg, total_harga, uang_bayar, kembalian, status, keterangan, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 1)",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry cuci komplit created successfully"})


@app.route("/pesananlaundry/cucikomplit", methods=["PUT"])
def update_pesanan_laundry_cucikomplit(pesanan_id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE PesananLaundry SET nama=%s, nomor_telepon=%s, alamat=%s, tanggal_pemesanan=%s, tanggal_pengambilan=%s, berat_kg=%s, total_harga=%s, uang_bayar=%s, kembalian=%s, status=%s, keterangan=%s WHERE pesanan_id=%s AND type_id=1",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
            pesanan_id,
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry cuci komplit updated successfully"})


@app.route("/pesananlaundry/cucikomplit/", methods=["DELETE"])
def delete_pesanan_laundry_cucikomplit(pesanan_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM PesananLaundry WHERE pesanan_id=%s AND type_id=1", (pesanan_id,)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry cuci komplit deleted successfully"})


# PesananLaundry dry clean Controller
@app.route("/pesananlaundry/dryclean", methods=["GET"])
def get_pesanan_laundry_dryclean():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PesananLaundry WHERE type_id=2")
    pesanan_laundries = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(pesanan_laundries)


@app.route("/pesananlaundry/dryclean", methods=["POST"])
def create_pesanan_laundry_dryclean():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO PesananLaundry (nama, nomor_telepon, alamat, tanggal_pemesanan, tanggal_pengambilan, berat_kg, total_harga, uang_bayar, kembalian, status, keterangan, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 2)",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry dry clean created successfully"})


@app.route("/pesananlaundry/dryclean", methods=["PUT"])
def update_pesanan_laundry_dryclean(pesanan_id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE PesananLaundry SET nama=%s, nomor_telepon=%s, alamat=%s, tanggal_pemesanan=%s, tanggal_pengambilan=%s, berat_kg=%s, total_harga=%s, uang_bayar=%s, kembalian=%s, status=%s, keterangan=%s WHERE pesanan_id=%s AND type_id=2",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
            pesanan_id,
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry dry clean updated successfully"})


@app.route("/pesananlaundry/dryclean", methods=["DELETE"])
def delete_pesanan_laundry_dryclean(pesanan_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM PesananLaundry WHERE pesanan_id=%s AND type_id=2", (pesanan_id,)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry dry clean deleted successfully"})


# PesananLaundry cuci satuan Controller
@app.route("/pesananlaundry/cucisatuan", methods=["GET"])
def get_pesanan_laundry_cucisatuan():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PesananLaundry WHERE type_id=3")
    pesanan_laundries = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(pesanan_laundries)


@app.route("/pesananlaundry/cucisatuan", methods=["POST"])
def create_pesanan_laundry_cucisatuan():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO PesananLaundry (nama, nomor_telepon, alamat, tanggal_pemesanan, tanggal_pengambilan, berat_kg, total_harga, uang_bayar, kembalian, status, keterangan, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 3)",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry cuci satuan created successfully"})


@app.route("/pesananlaundry/cucisatuan", methods=["PUT"])
def update_pesanan_laundry_cucisatuan(pesanan_id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE PesananLaundry SET nama=%s, nomor_telepon=%s, alamat=%s, tanggal_pemesanan=%s, tanggal_pengambilan=%s, berat_kg=%s, total_harga=%s, uang_bayar=%s, kembalian=%s, status=%s, keterangan=%s WHERE pesanan_id=%s AND type_id=3",
        (
            data["nama"],
            data["nomor_telepon"],
            data["alamat"],
            data["tanggal_pemesanan"],
            data["tanggal_pengambilan"],
            data["berat_kg"],
            data["total_harga"],
            data["uang_bayar"],
            data["kembalian"],
            data["status"],
            data["keterangan"],
            pesanan_id,
        ),
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry cuci satuan updated successfully"})


@app.route("/pesananlaundry/cucisatuan", methods=["DELETE"])
def delete_pesanan_laundry_cucisatuan(pesanan_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM PesananLaundry WHERE pesanan_id=%s AND type_id=2", (pesanan_id,)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Pesanan Laundry cuci satuan deleted successfully"})


@app.route("/type/<int:id>", methods=["DELETE"])
def delete_type(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Type WHERE id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Type deleted successfully"})


# Konfigurasi untuk Flask-Session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "supersecretkey"
Session(app)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM User WHERE username = %s AND password = %s",
            (username, password),
        )
        user = cursor.fetchone()
        # print(user)
        print("User from User table:", user)

        if user:
            cursor.execute("SELECT * FROM Karyawan WHERE nama = %s", (user["nama"],))
            data = cursor.fetchone()
            print("User from Karyawan table:", data)  # Debugging line
            # connection.close()
            if data:
                datas = {
                    "user": user,
                    "karyawan": data,
                }
                return jsonify(datas), 200
            else:
                return jsonify({"message": "bukan karyawan"}), 401
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    return jsonify({"message": "Error connecting to database"}), 500


@app.route("/logout", methods=["POST"])
def logout():
    # Hapus informasi pengguna dari sesi
    session.pop("user_id", None)
    session.pop("username", None)
    return jsonify({"message": "Logout successful"}), 200


@app.route("/profile", methods=["GET"])
def profile():
    if "user_id" in session:
        return (
            jsonify({"user_id": session["user_id"], "username": session["username"]}),
            200,
        )
    return jsonify({"message": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(debug=True)
