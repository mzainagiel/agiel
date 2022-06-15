print ("________PROGRAM JUAL BELI_______")

print ("=======MENU PILIHAN=======")
print ("1. ROTI         : Rp 10,000")
print ("2. SAMBALADO    : Rp 15,000")
print ("3. TAHU GEPREK  :Rp 20,000")

pilih = int(input("====pilih menu==== :"))

if pilih == 1:
    print("roti seharga seharga Rp. 10,000")
    jumlah = int(input("jumlah pesanan ="))
    print("")
    total = jumlah*10000
    print("total harga",total)
    print("====thank you Mas=====")
elif pilih == 2:
    print("sambalado seharga seharga Rp. 15,000")
    jumlah = int(input("jumlah pesanan ="))
    print("")
    total = jumlah*15000
    print("total harga",total)
    print("====thank you Mas=====")
elif pilih == 3:
    print("tahu geprek  seharga Rp. 20,000")
    jumlah = int(input("jumlah pesanan ="))
    print("")
    total = jumlah*20000
    print("total harga",total)
    print("====thank you Mas=====")
else:
    print(",,,,,,,Maaf Anda Goblok,,,,,,,")
    print("hhhhhhhhhhh canda goblok")

class pilihan:
	def __init__(self, pilihan):
		self.pillihan = pilihan

class pilihan:
	pass 
	('pilihan')
print('pilihan anda telah di akses')