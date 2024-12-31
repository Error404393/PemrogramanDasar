import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector 

# -- CONNECTOR DATABASE --#
db_config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "motorcustom2"
}
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor() 

    if conn.is_connected():
            print('Connected to MySQL database')
except mysql.connector.Error as e:
    print(f"Error Connecting to MySQL: {e}")
    
# -- END LINE -- #


# -- login & register -- #

def login():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan Password: ")

        # Check if the username and password match in the database
        query = f"SELECT id_akun, username, password, role FROM akun WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            id_akun, username, password, role = result
            print()
            print(f"Login berhasil! Selamat datang, {username}!")

            if role == "admin":
                admin()
            elif role == "user":
                user(username)
        else:
            print("Username atau password salah.")

def register():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")

        # Set role to 'user' automatically
        role = 'user'

        # Validate password using regex
        password_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        if not password_regex.match(password):
            print("Password harus terdiri dari setidaknya 8 karakter, minimal satu huruf, satu angka, dan satu simbol (@$!%*?&).")
            continue

        # Check if the username already exists
        check_query = f"SELECT * FROM akun WHERE username = '{username}'"
        cursor.execute(check_query)
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username sudah digunakan. Silakan pilih username lain.")
        else:
            # Insert new user into the database with nama, alamat, role, and validated password
            insert_query = f"INSERT INTO akun (username, password, nama, alamat, role) VALUES ('{username}', '{password}', '{nama}', '{alamat}', '{role}')"
            cursor.execute(insert_query)
            conn.commit()
            print()
            print("Registrasi berhasil!")
        
        comm_regist = input("Ingin Login (y) atau kembali (n)? (y/n) ")
        
        if comm_regist.lower() == 'y':
            login()
        else:
            break
            
# -- END LINE --#

# -- Fitur Program --#
def tambah():
    while True:
        print("""
||============================================||
||                                            ||
||              ADD NEW PRODUCT               ||
||                ----------                  ||
||                                            ||
||============================================||
        """)
        print("""

Opsi Menu :
1. Add
2. Back to Menu

            """)
        
        comm_add = int(input("Silahkan Pilih Menu (1/2):"))
            
        if comm_add == 1:
            print("\033c", end="", flush=True)
            cursor = conn.cursor()
            insert_query = "INSERT INTO item (jenis_motor, harga, deskripsi) VALUES (%s, %s, %s)"
            
            print(""""
||================||
||ADD NEW PRODUCT ||
||================||
""")
            jenis_motor = input ("Masukkan nama atau jenis motor yang akan ditambahkan: ")
            harga = int(input ("Masukkan harga produk: "))
            deskripsi = input ("Masukkan deskripsi tentang produk : ")
            
            values =(jenis_motor, harga, deskripsi)
            
            cursor.execute(insert_query, values) 
            
            conn.commit()
            print()
            print(f"Data berhasil dimasukkan dengan ID: {cursor.lastrowid}")
            print()

        elif comm_add == 2:
            break
        else:
            print("Pilih Opsi yang sesuai! Coba lagi!")


def show():
    while True:
        print("\033c", end="", flush=True)
        cursor = conn.cursor()
        select_query = "SELECT jenis_motor, harga, deskripsi FROM item"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        kolom = ['Jenis Motor', 'Harga', 'Deskripsi']

        print()
        print("DAFTAR JENIS MOTOR CUSTOMCLUB.ID")
        print()
        
        row = pd.DataFrame(rows, columns=kolom)
        row['NO'] = row.index + 1   
        kolom_urutkan = ['NO'] + kolom
        row = row[kolom_urutkan]
        
        print(row.to_string(index=False).center(150))
        
        print("""
||============================================||
||                 Silahkan                   ||
||             Pilih Fitur Berikut            ||
||                                            ||
||    1. Tambah Produk           2. Menu      ||
||                                            ||
||============================================||
            """)
        
        comm_show = int(input("Silahkan Pilih Menu :"))
        
        if comm_show == 1:
            tambah()
        elif comm_show == 2:
            break

def edit():
    while True:
        cursor = conn.cursor()
        select_query = "SELECT * FROM item"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        kolom = ['ID', 'Jenis Motor', 'Harga', 'Deskripsi']

        print()
        print("DAFTAR JENIS MOTOR CUSTOMCLUB.ID")
        print()
        
        row = pd.DataFrame(rows, columns=kolom)
        row['NO'] = row.index + 1   
        kolom_urutkan = ['NO'] + kolom
        row = row[kolom_urutkan]
        
        print(row.to_string(index=False).center(150))
    
        cursor = conn.cursor()

        update_query = "UPDATE item SET jenis_motor = %s, harga = %s, deskripsi = %s WHERE id_item = %s"
        id_item = int(input("Masukkan id data yang akan diubah: "))
        jenis_motor = input ("Masukkan nama jenis motor yang baru :")
        harga = int(input("Masukkan Harga motor yang baru: "))
        deskripsi = input("Masukkan deskripsi produk yang baru: ")

        values = (jenis_motor, harga, deskripsi, id_item)

        cursor.execute(update_query, values)

        conn.commit()
        print()
        print (f"Data berhasil diubah untuk ID: {id_item}")
        print()
        
        com_edit = input("Mau Edit Lagi? (y/n): ")
        
        if com_edit == 'n':
            break
        else:
            continue

def show2(id_akun):
    while True:
        print("\033c", end="", flush=True)
        cursor = conn.cursor()
        select_query = "SELECT jenis_motor, harga, deskripsi FROM item"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        kolom = ['Jenis Motor', 'Harga', 'Deskripsi']

        print()
        print("DAFTAR JENIS MOTOR CUSTOMCLUB.ID")
        print()

        row = pd.DataFrame(rows, columns=kolom)
        row['NO'] = row.index + 1
        kolom_urutkan = ['NO'] + kolom
        row = row[kolom_urutkan]

        print(row.to_string(index=False).center(150))

        print("""
||============================================||
||                 Silahkan                   ||
||             Pilih Fitur Berikut            ||
||                                            ||
||    1. Pemesanan            2. Menu         ||
||                                            ||
||============================================||
            """)

        comm_show = int(input("Silahkan Pilih Menu :"))

        if comm_show == 1:
            pemesanan(id_akun)
        elif comm_show == 2:
            break

def pemesanan(id_akun):
    while True:
        cursor = conn.cursor()
        select_query = "SELECT * FROM item"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        kolom = ['ID', 'Jenis Motor', 'Harga', 'Deskripsi']

        print()
        print("DAFTAR JENIS MOTOR CUSTOMCLUB.ID")
        print()

        row = pd.DataFrame(rows, columns=kolom)
        row['NO'] = row.index + 1
        kolom_urutkan = ['NO'] + kolom
        row = row[kolom_urutkan]

        print(row.to_string(index=False).center(150))

        id_item = int(input("Masukkan ID produk yang akan dipesan: "))
        jumlah_pesanan = int(input("Masukkan jumlah produk yang akan dipesan: "))
        tanggal_pemesanan = pd.to_datetime('today').strftime('%Y-%m-%d')
        total_pembayaran = 0

        # Menghitung total pembayaran
        cursor.execute(f"SELECT harga FROM item WHERE id_item = {id_item}")
        harga_produk = cursor.fetchone()[0]
        total_pembayaran = jumlah_pesanan * harga_produk

        # Menambahkan data ke tabel transaksi
        insert_query = "INSERT INTO transaksi (id_item, id_akun, jumlah_pesanan, tanggal_pemesanan, total_pembayaran) VALUES (%s, %s, %s, %s, %s)"
        values = (id_item, id_akun, jumlah_pesanan, tanggal_pemesanan, total_pembayaran)
        cursor.execute(insert_query, values)
        conn.commit()

        print()
        print("Pemesanan berhasil!")
        print(f"Total pembayaran: {total_pembayaran}")
        print()

        lanjut = input("Ingin memesan lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break

def hapus():
    while True:
        print("""
||================||
||Delete Product  ||
||================||
""")
        
        cursor = conn.cursor()
        select_query = "SELECT * FROM item"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        kolom = ['ID', 'Jenis Motor', 'Harga', 'Deskripsi']

        print()
        print("DAFTAR JENIS MOTOR CUSTOMCLUB.ID")
        print()
        
        row = pd.DataFrame(rows, columns=kolom)
        row['NO'] = row.index + 1   
        kolom_urutkan = ['NO'] + kolom
        row = row[kolom_urutkan]
        
        print(row.to_string(index=False).center(150))
        
        print("_______________________")
        print()
        
        cursor = conn.cursor()
        delete_query = "DELETE FROM item WHERE id_item = %s"
        delete_item = input("Masukkan id untuk data yang akan dihapus: (tekan y untuk kembali)")
        values =(delete_item,)

        cursor.execute(delete_query, values)

        conn.commit()
        print()
        print (f"Data berhasil dihapus untuk ID: {delete_item}")
        print()
        
        if delete_item == 'y':
            break
        
        print("\033c", end="", flush=True)

def statistik():
    cursor = conn.cursor()
    query = "SELECT tanggal_pemesanan, COUNT(*) as jumlah_pesanan FROM transaksi GROUP BY tanggal_pemesanan"
    df = pd.read_sql_query(query, conn)

    # Konversi kolom tanggal ke tipe datetime
    df['tanggal'] = pd.to_datetime(df['tanggal_pemesanan'])

    # Mengurutkan data berdasarkan tanggal
    df.sort_values('tanggal', inplace=True)

    # Membuat grafik kurva
    plt.figure(figsize=(10, 6))
    plt.plot(df['tanggal'], df['jumlah_pesanan'], marker='o', linestyle='-')
    plt.title('Grafik Jumlah Item Dibeli per Tanggal')
    plt.xlabel('Tanggal Pemesanan')
    plt.ylabel('Jumlah Item')
    plt.grid(True)
    plt.show()

# -- User & Admin Program --#
def user(username):
    cursor = conn.cursor()
    query = f"SELECT id_akun FROM akun WHERE username = '{username}'"
    cursor.execute(query)
    id_akun = cursor.fetchone()[0]

    while True:
        print("\033c", end="", flush=True)
        print("""
        ________________________________________________    
        |                                              |
        |                Welcome User                  |
        |             Happy Shopping                   |
        |               CUSTOMCLUB.id                  |
        |______________________________________________|
        """)
        print("""
    Menu:
    1. Lihat Produk Tersedia
    2. Pemesanan
    3. Log Out
    4. Exit
        """)

        com_user = int(input("Silahkan pilih menu (1/2/3/4): "))

        if com_user == 1:
            show2(id_akun)
        elif com_user == 2:
            pemesanan(id_akun)
        elif com_user == 3:
            break
        elif com_user == 4:
            exit()
        else:
            print("Masukkan perintah yang benar! Coba Lagi")

def admin():
    while True:
        print("\033c", end="", flush=True)
        print("""
________________________________________________
|                                              |
|               Welcome Admin                  |
|          let's do the work happily           |
|               CUSTOMCLUB.id                  |
|______________________________________________|
        """)
        print("""
    Menu:
    1. Tambah Produk
    2. Edit Produk
    3. Hapus Produk
    4. Statistik Penjualan
    5. Tampilkan Produk Tersedia
    6. Log Out
    7. Exit
        """)
            
        com_admin =int(input("Silahkan pilih menu (1/2/3/4/5/6/7) : "))

        if com_admin == 1:
            tambah()
        elif com_admin == 2:
            edit()
        elif com_admin == 3:
            hapus()
        elif com_admin == 4:
            statistik()
        elif com_admin == 5:
            show()
        elif com_admin == 6:
            print("\033c", end="", flush=True)
            break
        elif com_admin == 7:
            exit()
        else:
            print("Masukkan perintah yang benar! Coba Lagi")

# -- END LINE --#
    
    

#-- In First Running Condition --#

while True:
    print("\033c", end="", flush=True)
    print ("""
___________________________________________________________
|                                                         |
|             Selamat Datang Di Aplikasi                  |
|                   CUSTOMCLUB.id                         |
|_________________________________________________________|
""")
    print("""
    Menu:
    1. Login
    2. Register
    3. Exit
        """)
    com_menu =int(input("Silahkan pilih menu (1/2/3) : "))

    if com_menu == 1:
        login()
    elif com_menu == 2:
        register()
    elif com_menu == 3:
        print ("GOODBYE !")
        break
    else:
        print("Masukkan perintah yang benar! Coba Lagi")