import tkinter as tk
from tkinter import messagebox

def tampilkan_menu():
    menu_window = tk.Toplevel(app)
    menu_window.title("Menu Makanan")

    menu_label = tk.Label(menu_window, text="Menu Makanan : ")
    menu_label.pack()

    menu = {
        1: "Nasi Goreng - Rp. 25000",
        2: "Mie Goreng - Rp. 20000",
        3: "Sate Ayam - Rp. 30000",
        4: "Ayam Bakar - Rp. 35000",
        5: "Es Teh - Rp. 5000",
        6: "Es Jeruk - Rp. 7000"
    }

    for key, value in menu.items():
        menu_item = tk.Label(menu_window, text=f"{key}. {value}")
        menu_item.pack()

def hitung_total(harga, jumlah):
    return harga * jumlah

def pesan_makanan():
    nama_makanan = entry_nama_makanan.get()
    harga_makanan =float(entry_harga_makanan.get())
    jumlah_pesanan = int(entry_jumlah_pesanan.get())

    total_harga = hitung_total(harga_makanan, jumlah_pesanan)

    pesan = f"Terima kasih atas pesanan Anda!\n\n"\
            f"Nama Makanan: {nama_makanan}\n"\
            f"Harga Makanan: Rp {harga_makanan:,.2f}\n"\
            f"Jumlah Pesanan: {jumlah_pesanan}\n"\
            f"Total Harga: Rp {total_harga:,.2f}"

    messagebox.showinfo("Pesanan Diterima", pesan)

# Membuat instance Tkinter
app = tk.Tk()
app.title("Toko Makanan")

# Membuat label dan entry untuk nama makanan
label_nama_makanan = tk.Label(app, text="Nama Makanan:")
label_nama_makanan.grid(row=0, column=0, padx=10, pady=5)
entry_nama_makanan = tk.Entry(app)
entry_nama_makanan.grid(row=0, column=1, padx=10, pady=5)

# Membuat label dan entry untuk harga makanan
label_harga_makanan = tk.Label(app, text="Harga Makanan (Rp):")
label_harga_makanan.grid(row=1, column=0, padx=10, pady=5)
entry_harga_makanan = tk.Entry(app)
entry_harga_makanan.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk jumlah pesanan
label_jumlah_pesanan = tk.Label(app, text="Jumlah Pesanan:")
label_jumlah_pesanan.grid(row=2, column=0, padx=10, pady=5)
entry_jumlah_pesanan = tk.Entry(app)
entry_jumlah_pesanan.grid(row=2, column=1, padx=10, pady=5)

# Membuat tombol pesan
tombol_pesan = tk.Button(app, text="Pesan", command=pesan_makanan)
tombol_pesan.grid(row=3, column=1, columnspan=2, pady=10)

# Membuat toombol menu
menu_button = tk.Button(app, text="Lihat Menu", command=tampilkan_menu)
menu_button.grid(row=3, column=0, columnspan=2, pady=10)

# Menjalankan loop utama aplikasi
app.mainloop()
