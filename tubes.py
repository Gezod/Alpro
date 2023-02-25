''' PEMBUATAN GUI '''
import csv
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Layout =======================================================================================
# Angga Jobdesk
root = Tk()
root.configure(background='black')
root.geometry('700x600')
root.title('Gudang Serba Bisa By Kelompok 3 SI 05-01')


# Frame Inti
display = Frame(root, background='grey')
display.pack(padx=30, pady=10, expand=True, fill='both')

# Bagian Layout ================================================================================
# Frame Judul Atas
layoutAtas = Frame(display, background='lightgrey')
layoutAtas.pack()

# Frame Scroll
frameScroll = Frame(display, background='white')
frameScroll.pack()

# Frame Sort
frameSort = Frame(display, background='white')
frameSort.pack(fill="both")

# Frame Input Data
inputData = Frame(display, background='white', border=15, highlightcolor='black', highlightthickness=2)
inputData.pack(fill='both')

# Frame Tombol CRUD
tombolCrud = Frame(display, background='white')
tombolCrud.pack(fill='both')

# Variable Data ================================================================================
#All
NAMA = StringVar()
KODE = StringVar()
QTY = StringVar()
JABATAN = StringVar()
DELETEDATA = StringVar()
UPDATEDATA = StringVar ()

# Daftar Function ==============================================================================
# Baca File CSV
def readCsv(): # Steffi
    ''' READ + UPDATE CSV '''
    with open('data_1.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        csvtoList = []
        for data_list in reader:
            csvtoList.append(data_list)
        return csvtoList

# Create Csv
def createCsv(createData): # Nessa
    ''' UPDATE '''
    with open('data_1.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in createData:
            write_file.writerow(i)

# Delete Csv
def deleteCsv(remove_data): #Hendri
    ''' DELETE '''
    # Open File CSV nya
    openCsv = readCsv()

    ''' Remove Data '''
    del openCsv[int(remove_data) - 1]
    # for dataList in openCsv:
    #     if remove_data in dataList[0]: # jika ingin menghapus index ke berapa
    #         openCsv.remove(dataList)

    with open('data_1.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in openCsv:
            write_file.writerow(i)

# Update Data List Box
def update_data(data = list): # Steffi
    for i in tree.get_children():
        tree.delete(i)
    count = 0

#Ia menggunakan perulangan for untuk mengiterasi anak-anak dari pohon variabel, yang tidak ditentukan dalam cuplikan ini. Ini kemudian memanggil metode delete() pada setiap anak dari variabel pohon. Setelah for loop selesai, ia membuat variabel count dan memberinya nilai 0.
#Sepertinya fungsi ini dimaksudkan untuk menghapus konten widget tampilan pohon dan mengatur ulang penghitung.

    # Urutkan berdasarkan jabatan
    data.sort(key=lambda x: x[1])
    # Baris kode ini menggunakan fungsi sort() bawaan untuk mengurutkan daftar dataKosong berdasarkan elemen kedua dari setiap sub-daftar (ditunjukkan dengan x[1] dalam argumen kunci). 
    # Fungsi lambda digunakan sebagai cara untuk menentukan fungsi pengurutan khusus, dalam hal ini, pengurutan berdasarkan elemen kedua dari setiap sub-daftar. 
    # Daftar yang dihasilkan akan diurutkan dalam urutan menaik berdasarkan elemen kedua dari setiap sub-daftar.
    for item in data:
        count += 1
        tree.insert("", "end", text=count, values=(item[0], item[1], item[2], item[3]))


# Function Search
def functionSearch(e): # Hendri Jobdesk
    # Mengambil data dengan .get()
    search = searchBox.get()
    if search == '':
        data = readCsv()
    else:
        data = []
        for item in readCsv():
            if search in item[0]:
                data.append(item)
    # Perbarui data
    update_data(data)

# Function Sort
def sortBy(e): #Sikki
    # file Csv
    data = readCsv()
    sort_by = menuSort.get()
    dataBaru =[]

    # Kondisi Opsi
    if sort_by == 'Staff':
        for item in data:
            if item[3] == 'Staff':
                dataBaru.append(item)
        update_data(dataBaru)

    elif sort_by == 'Admin':
        for item in data:
            if item[3] == 'Admin':
                dataBaru.append(item)
        update_data(dataBaru)

    else:
        update_data(data)

# Function Memilih Jabatan
def pilihanJabatan(): # Sikki JobDesk
    dataJab = entriJabatan.get()
    data = ''
    if dataJab == 'Staff':
        data = ('Staff')
    elif dataJab == 'Admin':
        data = ('Admin')
    return data
# Menambahkan data ke list CSV
def create_Data_Csv(): # Sikki JobDesk
    ambil_nama = NAMA.get()
    ambil_kode = KODE.get()
    ambil_qty = QTY.get()
    # ambil_jabatan = JABATAN.get()
    # Memasukan data yang diambil ke dalam list
    listTOCsv = [ambil_nama, ambil_kode, ambil_qty, pilihanJabatan()]
    
    # Baca file CSV dulu
    bacaCsv = readCsv()
    # Menaruh semua data ke dataKosong
    dataKosong = []
    for i in bacaCsv:
        dataKosong.append(i)
    dataKosong.append(listTOCsv)

    # Sorting data menurut jabatan
    dataKosong.sort(key=lambda x: x[1])
    # Baris kode ini menggunakan fungsi sort() bawaan untuk mengurutkan daftar dataKosong berdasarkan elemen kedua dari setiap sub-daftar (ditunjukkan dengan x[1] dalam argumen kunci). 
    # Fungsi lambda digunakan sebagai cara untuk menentukan fungsi pengurutan khusus, dalam hal ini, pengurutan berdasarkan elemen kedua dari setiap sub-daftar. 
    # Daftar yang dihasilkan akan diurutkan dalam urutan menaik berdasarkan elemen kedua dari setiap sub-daftar.

    # Masukkan semua data ke CSV dengan menimpa data sebelumnya
    messagebox.showinfo("",'Berhasil Dibuat! Silahkan Klik (Ok)')
    createCsv(dataKosong)
    # Auto Update Bosskuuu
    update_data(readCsv())

# Menghapus data CSV dan menampilkan data nya
def delete_Data_Csv(): #Hendri
    ambil_delete_name = DELETEDATA.get()
    deleteCsv(ambil_delete_name)
    messagebox.showinfo("",'Berhasil Dihapus! Silahkan Klik (Ok)')  
    update_data(readCsv())

def edit_Data_Csv():
    openCsv = readCsv() 
    openCsv.reverse()  ## we normalize data
    data = UPDATEDATA.get()
    nama_temp = NAMA.get()
    kode_temp = KODE.get()
    qty_temp =QTY.get()
    entriJabatan_temp = entriJabatan.get()
    # print(openCsv)
    # print(data)
    openCsv[int(data) - 1] = [nama_temp, kode_temp, qty_temp, entriJabatan_temp]
    # print(openCsv)
    with open('data_1.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in openCsv:
            write_file.writerow(i)

    messagebox.showinfo("",'Berhasil Diedit! Silahkan Klik (Ok)')  
    update_data(readCsv())
    
def logout():
    root.destroy()
    import login_gudang
    # print(openCsv)
    # for datalist in openCsv:
    #     if data.lower() == datalist[0].lower():
    #         nama_temp = datalist[0]
    #         kode_temp = datalist[1]
    #         qty_temp =  datalist[2]
    #         entriJabatan_temp = 0 if datalist[3] == "Admin" else 1
        

    # NAMA.set(nama_temp) #edit nama barang
    # KODE.set(kode_temp)
    # QTY.set(qty_temp)
    # entriJabatan.current(entriJabatan_temp) # 2 items 


# Isi Layout Atas ==============================================================================
# Judul
judul = Label(layoutAtas, text='Inventory Gudang',font=('Times New Roman', 20), background='light grey')
judul.pack(fill='y', pady=15)

# garis lurus
canvas = Canvas(layoutAtas, width=600, height=2, background='white')
canvas.pack(fill='y')

# Garis Bagian Judul
line = canvas.create_line(0, 3, 580, 3, fill="black", width=2)

# Search 
# searchBox = Label(tombolCrud, text='GUI Kelompok 3', background='white', font=('inter', 9))
searchBox = ttk.Entry(layoutAtas)
searchBox.pack(ipadx=15, padx=20, pady=15, anchor=E)
# searchBoxLabel = Label(tombolCrud, text='GUI Kelompok 3', background='black', font=('inter', 9))


# Autosearch
searchBox.bind("<KeyRelease>", functionSearch,)


# Tree View and Frame Scroll ===================================================================
# Melakukan scroll
scrollData = Scrollbar(frameScroll)
scrollData.pack(side=RIGHT, fill=Y)

# Buat Treeview
tree = ttk.Treeview(frameScroll, yscrollcommand=scrollData.set)

# Format panggilan & keluaran
tree["columns"] = ("nama", "kode", "qty", "jabatan")

# Column
tree.column("#0", width=50, minwidth=50, stretch=tk.NO)
tree.column("nama", width=100, minwidth=100, stretch=tk.NO)
tree.column("kode", width=100, minwidth=100)
tree.column("qty", width=140, minwidth=140)
tree.column("jabatan", width=100, minwidth=100)

# Heading
tree.heading("#0", text="No.", anchor=tk.W)
tree.heading("nama", text="Nama Barang", anchor=tk.W)
tree.heading("kode", text="Kode", anchor=tk.W)
tree.heading("qty", text="QTY", anchor=tk.W)
tree.heading("jabatan", text="Jabatan", anchor=tk.W)

# Menampailkan Data Tree
update_data(readCsv())
tree.pack()

# Menampilkan scroll
scrollData.config(command=tree.yview)

# Isi Frame Sort ===============================================================================
# Sorting Data list
menuSort = ttk.Combobox(frameSort, values=[
                        'All', 'Staff', 'Admin'], state='readonly')
menuSort.current(0)
menuSort.config(width=15)
menuSort.pack(padx=15, pady=15, fill='y', side=LEFT)

# Menjalankan fungsi pengurutan data
menuSort.bind("<<ComboboxSelected>>",sortBy)

# Frame Input ==================================================================================
# Input Nama
nama = ttk.Label(inputData, background='white', text='Nama Barang', font=('inter', 10))
nama.grid(row=0, column=0, padx=25, pady=7)

entriNama = ttk.Entry(inputData, textvariable=NAMA)
entriNama.grid(row=0, column=1)

# Input Jenis Kelamin
jabatan = ttk.Label(inputData, background='white',text='Jabatan', font=('inter', 10))
jabatan.grid(row=0, column=2, padx=25)

entriJabatan = ttk.Combobox(inputData, values=['Staff', 'Admin'], state='readonly')
entriJabatan.grid(row=0, column=3)
entriJabatan.config(width=17)


# Input Jabatan
kode = ttk.Label(inputData, background='white',text='Kode', font=('inter', 10))
kode.grid(row=1, column=0, pady=7)

entrikode = ttk.Entry(inputData, textvariable=KODE)
entrikode.grid(row=1, column=1)

# Input Kedahiran
harga = Label(inputData, background='white', text='QTY', font=('inter', 10))
harga.grid(row=1, column=2)

entriharga = ttk.Entry(inputData, textvariable=QTY)
entriharga.grid(row=1, column=3)

# Tombol CRUD 
# Button Logout
button_Logout = Button(tombolCrud, text='Logout', font=('inter', 9), foreground='white', background='red', activebackground='white',
                       activeforeground='black', borderwidth=1, command=logout)
button_Logout.grid(row=0, column=0, ipadx=15, ipady=3,pady=20, padx=10)

# Button Create
button_Create = Button(tombolCrud, text='Create', font=('inter', 9), foreground='white', background='green', activebackground='white',
                       activeforeground='black', borderwidth=1, command=create_Data_Csv)
button_Create.grid(row=0, column=1, ipadx=15, ipady=3, pady=20, padx=10, )

#Edit Button
button_Delete = Button(tombolCrud, text='Delete', font=('inter', 9), foreground='white', background='orange', activebackground='white',
                       activeforeground='black', borderwidth=1, command=delete_Data_Csv)
button_Delete.grid(row=0, column=2, ipadx=15, ipady=3, pady=20, padx=10, )


# Label Delete
# deleteLabel = Label(tombolCrud,textvariable=DELETEDATA, text=' Nomor = ', background='white', font=('inter', 9))
# deleteLabel.grid(row=0, column=5)

# # Entri Delete
entriDeleteLabel = ttk.Entry(tombolCrud, textvariable=DELETEDATA)
entriDeleteLabel.grid(row=0, column=6)

#Entri Edit
deleteLabel = Label(tombolCrud,textvariable=UPDATEDATA, text=' Nomor = ', background='white', font=('inter', 9))
deleteLabel.grid(row=0, column=7)

# # Entri Edit data
entriDeleteLabel = ttk.Entry(tombolCrud, textvariable=UPDATEDATA)
entriDeleteLabel.grid(row=0, column=8)

# Button Logout
button_Edit = Button(tombolCrud, text='Edit', font=('inter', 9), foreground='white', background='blue', activebackground='white',
                       activeforeground='black', borderwidth=1, command=edit_Data_Csv)
button_Edit.grid(row=0, column=7, ipadx=15, ipady=3, pady=20, padx=10, )



root.mainloop()