import mylibsec as myl

dictMobil = {
101: [101, 'Toyota', 'Innova Reborn', 'MPV', 2019, 3, 400000, 700000],
102: [102, 'Honda', 'Jazz', 'City Car', 2020, 3, 300000, 500000],
103: [103, 'Toyota', 'Fortuner', 'SUV', 2020, 2, 450000, 800000],
104: [104, 'Toyota', 'HiAce', 'Mini Bus', 2018, 2, 800000, 1100000],
105: [105, 'Honda', 'Brio', 'City Car', 2017, 1, 250000, 450000],
206: [206, 'Mitsubishi', 'Pajero Sport', 'SUV', 2019, 1, 400000, 750000],
207: [207,'Wuling', 'Air', 'Electric', 2023, 4, 400000, 800000],
208: [208, 'Daihatsu', 'Xenia', 'MPV', 2023, 3, 250000, 500000],
209: [209, 'Wuling', 'Cloud', 'Electric', 2024, 3, 400000, 750000],
210: [210, 'Mitsubishi', 'XPander', 'MPV', 2021, 2, 300000, 550000],
311: [311, 'Daihatsu', 'Ayla', 'City Car', 2022, 2, 200000, 350000],
312: [312, 'Isuzu', 'Elf', 'Mini Bus', 2019, 3, 900000, 1400000]
}

#######################+ Sub Menu Program Rental Mobil +#######################

#SubMenu 1
def sub_menu_showCar():
    pilihan_menu_1 = '''
List Menu Show Car

1. Show Stock Mobil Rental
2. Filter berdasarkan Merek
3. Kembali Ke Menu Utama

'''
    while True:
        print(pilihan_menu_1)
        user_menu_input_1 = input('Masukan Angka yang ingin dijalankan: ')   

        if user_menu_input_1 == '1':
            myl.show(dictMobil)
        elif user_menu_input_1 == '2':
            myl.filter_by_type(dictMobil)
        elif user_menu_input_1 == '3':
            break
        else:
            print('Pilihan menu tidak tersedia')

#SubMenu 2
def sub_menu_addCar():
    pilihan_menu_2 = '''
List Menu 2

1. Tambah Mobil Rental
2. Kembali ke menu utama

'''
    myl.show(dictMobil)
    while True:
        print(pilihan_menu_2)
        user_menu_input_2 = input('Masukan Angka yang ingin dijalankan: ')

        if user_menu_input_2 == '1':
            myl.add_car(dictMobil)
        elif user_menu_input_2 == '2':
            break
        else:
            print('Pilihan menu tidak tersedia')

#SubMenu 4
def sub_menu_updateStock():
    pilihan_menu_4 = '''
List Menu 4

1. Update Data Mobil
2. Kembali ke menu utama

'''
    myl.show(dictMobil)
    while True:
        print(pilihan_menu_4)
        user_menu_input_4 = input('Masukan Angka yang ingin dijalankan: ')    
        if user_menu_input_4 == '1':
            myl.update_stock(dictMobil)
        elif user_menu_input_4 == '2':
            break
        else:
            print('Pilihan menu tidak tersedia')

#SubMenu 3
def sub_menu_deleteStock():
    pilihan_menu_3 = '''
List Menu 3

1. Hapus Stock Mobil
2. Kembali ke menu utama

'''
    myl.show(dictMobil)
    while True:
        print(pilihan_menu_3) 
        user_menu_input_3 = input('Masukan Angka yang ingin dijalankan: ')   
        if user_menu_input_3 == '1':
            myl.delete_stock(dictMobil)
        elif user_menu_input_3 == '2':
            break
        else:
            print('Pilihan menu tidak tersedia')

#######################+ Menu Utama Program Rental Mobil +#######################

# Main Control Rental Mobil
def main():
    pilihan_menu = '''
Selamat Datang Rental OmBil.
   
List Menu :
1. Menampilkan Daftar
2. Menambahkan Data
3. Menghapus Data
4. Update Stock
5. Keluar
      
'''
    while True:
        print(pilihan_menu)
        user_menu_input = input('Masukan Angka yang ingin dijalankan: ')

        if user_menu_input == '1':
              sub_menu_showCar()
        elif user_menu_input == '2':
              sub_menu_addCar()
        elif user_menu_input == '3':
               sub_menu_deleteStock()
        elif user_menu_input == '4':
              sub_menu_updateStock()  
        elif user_menu_input == '5':
                  print('Terimakasih sudah menggunakan jasa OmBil Om Om sekalian!')
                  break
        else:
            print ('Anfka yang anda masukan tidak valid!')

main()