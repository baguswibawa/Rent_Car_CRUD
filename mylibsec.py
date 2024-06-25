from tabulate import tabulate
#
# Validasi 1
# String Validasi untuk filter bahwa user input dipastikan adalah Huruf Alphabet, tidak disertakan karakter Numeric/ Bilangan
def str_valid(title):
    """Fungsi untuk validasi tipe data string

    Args:
        title (String): Pesan yang akan ditampilkan pada layar

    Returns:
        String: Nilai yang diinputkan
    """
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Silahkan inputkan alfabet!')
    return teks.capitalize()
#
# Validasi 2
# Integer Validasi untuk filter bahwa user input mengikuti minimal & maksimal sesuai deafult dari setting mesin
def int_valid(title, minval=0, maxval=999999):
    """Fungsi untuk validasi bilangan bulat

    Args:
        title (String): Pesan yang akan ditampilkan pada layar
        minval (int, optional): Nilai minimal. Defaults to 0.
        maxval (int, optional): Nilai maksimal. Defaults to 999999

    Returns:
        Int: Nilai yang diinputkan
    """
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print(f'Silahkan inputkan angka diantara {minval} dan {maxval}')
        except:
            print('Silahkan inputkan angka!')
    return num
#
# sub 1.1
# Function to show Database
def show(database, header=['id', 'Merek', 'Nama', 'Tipe', 'Tahun', 'Stock', 'Harga 12 Jam', 'Harga 24 Jam']):
    """Fungsi untuk menampilkan data dalam format tabel

    Args:
        database (list): Data persediaan mobil
        header (list, optional): Nama kolom akan di setting ['id', 'Merek', 'Nama', 'Tipe', 'Tahun', 'Stock', 'Harga 12 Jam', 'Harga 24 Jam'].
    """
    # Menampilkan data dalam format tabulasi
    print(tabulate(database.values(), headers=header, tablefmt='rounded_grid'))
#
# sub 1.2
# Function to filter Databse
def filter_by_type(database, header=['id', 'Merek', 'Nama', 'Tipe', 'Tahun', 'Stock', 'Harga 12 Jam', 'Harga 24 Jam']):
    """Filter Brand mobil di OmBil

    Args:
        database (dict): data list harga dll Rental OmBil
    """
    brand = str_valid(title='Masukan Merek Mobil yang akan OmBil filter: ')
    filtered_cars = []

    for key, value in database.items():
        if value[1].lower() == brand.lower():
            filtered_cars.append(value)
    
    if filtered_cars:
        print(tabulate(filtered_cars, headers=header, tablefmt='rounded_grid'))
    else:
        print(f"OmBil tidak mempunyai merek {brand}!")
#
#sub 2.1
# Function to add Database
def add_car(database, header=['id', 'Merek', 'Nama', 'Tipe', 'Tahun', 'Stock', 'Harga 12 Jam', 'Harga 24 Jam']):
    """Fungsi untuk menambahkan list Rental ke dalam database

    Args:
        database (list): data list harga dll Rental OmBil
    """
    while True:
            car_id = int_valid(title="Masukan 'id' baru: ", minval=0, maxval=500)
            # Cek valid jika id OmBil sudah ada
            if any(car_id == i[0] for i in database.values()):
                print(f"id {car_id} sudah tersedia di OmBil, mohon masukan varian id baru Om.")
            else:
                break  

    brand = str_valid(title='Enter Merek: ')

    while True:
        model = str_valid(title='Masukan Nama Mobil: ')
        year = int(input('Masukan Tahun Mobil: '))
        
        # Cek valid duplikat data rental OmBil
        if any(i[4] == year and i[2].lower() == model.lower() for i in database.values()):
            print(f"Mobil {model} {year} sudah ada di OmBil, silahkan masukkan mobil {model} yang baru dengan tahun selain {year}")
        else:
            break  

    car_type = str_valid(title='Masukan Tipe: ')
    stock = int_valid(title='Masukan Stock: ',minval=0, maxval=5)
    price_short = int_valid(title='Masukan Harga 12 Jam: ',minval=0, maxval=1000000)
    price_long = int_valid(title='Masukan Harga 24 Jam: ',minval=0, maxval=10000000)
    
    #variabel penyimpan sementara
    new_car = [car_id, brand, model, car_type, year, stock, price_short, price_long]

    #disp database rental OmBil
    print()
    print()    
    print(tabulate([new_car], headers=header, tablefmt='rounded_grid'))  

    #user req validation    
    while True:
        cek_tambah_mobil = str_valid(title='Apakah Om ingin menyimpan data tersebut? [ya/tidak] : ')
        if cek_tambah_mobil.lower() == 'tidak':
            # Jiksa user tidak ingin save data maka
            print('Mobil tidak jadi OmBil simpan')
            break
        elif cek_tambah_mobil.lower() == 'ya':
            database[car_id] = new_car
            print(f'Selamat Om! Mobil {brand} {model}, Tipe {car_type} berhasil ditambahkan ke Rental OmBil.')
            break
        else:
            print('Input tidak tersedia Om')
            continue

    show(database)
#
# sub 3.1
# Function to Delete Databsae 
def delete_stock(database, header=['id', 'Merek', 'Nama', 'Tipe', 'Tahun', 'Stock', 'Harga 12 Jam', 'Harga 24 Jam']):
    while True:
        idx = int_valid(title='masukan id rental OmBil yang ingin dihapus: ',minval=0, maxval=500)
        if idx not in database:
            print('id mobil tidak ditemukan di OmBil, silakan coba lagi Om.')
            continue

        #disp Databasae rental OmBil
        print()
        print()        
        print('Data mobil yang dipilih:')
        print(tabulate([database[idx]], headers=header, tablefmt='rounded_grid'))
        print(f'OmBil akan menghapus data rental, mobil {database[idx][1]} {database[idx][2]} tahun {database[idx][4]}')

        #user req validation
        cek_hapus_mobil = input('Apakah Om yakin ingin menghapus data mobil diatas? [ya/tidak] : ').lower()
        if cek_hapus_mobil == 'tidak':
            #jika user tidak ingin menghapus data maka akan keluar dari looping / break
            print('Data mobil tidak dihapus')
            break
        elif cek_hapus_mobil == 'ya':
            del database[idx]
            #menampilkan data mobil rental setelah menghapus data
            show(database)
            print('Data mobil berhasil dihapus')
        else:
            print('Input tidak tersedia')
            continue

        # Are konfirm user
        cont_choice = input('Apakah Om ingin menghapus data lain? [ya/tidak]: ').lower()
        if cont_choice == 'ya':
            continue
        else:
            break
#
# sub 4.1
# Function to Update Databsae
def update_stock(database, header=['id', 'Merek', 'Nama', 'Tipe', 'Tahun', 'Stock', 'Harga 12 Jam', 'Harga 24 Jam']):
     """Fungsi untuk update stock list Rental ke dalam database

    Args:
        database (list): data list harga dll Rental OmBil
    """
     while True:
        idx = int_valid(title='Masukkan id yang ingin OmBil update: ', minval=0, maxval=500)
        if idx not in database:
            print('d mobil yang Om masukkan tidak ada dalam list rental OmBil.')
            continue
        
        # Disp database rental OmBil
        print()
        print()        
        print('Data mobil yang dipilih:')
        print(tabulate([database[idx]], headers=header, tablefmt='rounded_grid'))
        print(f'OmBil akan update data rental, mobil {database[idx][1]} {database[idx][2]} tahun {database[idx][4]}')
        
        updet_choice = input('Apakah Om ingin memperbarui data ini? [ya/tidak]: ').lower()
        if updet_choice == 'tidak':
            print('Data mobil tidak OmBil update')
            break
        elif updet_choice == 'ya':
            print("Kolom mana yang ingin OmBil update:")
            for i, col in enumerate(header):
                print(f"{i}: {col}")  # Akan di print secara iterasi
        
        col_idx = int_valid(title='Masukkan nomor kolom yang ingin di update: ', minval=0, maxval=len(header))
        valueBaru = input(f'Masukkan {header[col_idx]} baru untuk kolom {header[col_idx]}: ')
        
        # konfirmasi user
        confirm_updet = input(f'Apakah Om yakin ingin memperbarui {header[col_idx]} dengan"{valueBaru}" yang baru? [ya/tidak]: ').lower()
        if confirm_updet == 'ya':
            # seragamankan tipe data dengan default kolom dict di main.py
            if col_idx == 0 or col_idx == 4 or col_idx == 5: 
                valueBaru = int(valueBaru)
            elif col_idx == 6 or col_idx == 7: 
                valueBaru = float(valueBaru)
            database[idx][col_idx] = valueBaru
            print(f'Data untuk id {idx} berhasil diperbarui.')
            print(tabulate([database[idx]], headers=header, tablefmt='rounded_grid'))
        
        # re konfirm user 
        cont_choice = input('Apakah Om ingin memperbarui data lain? [ya/tidak]: ').lower()
        if cont_choice == 'ya':
            continue
        else:
            break