a = input("Masukkan nilai a:")
b = input("Masukkan nilai b:")
print("Variable a=", a)
print("Variable b=", b)
print("Hasil penggabungan {0}&{1}= %s".format(a, b) % (a+b))

# konversi nilai variable
a = int(a)
b = int(b)
print("Hasil penjumlahan {0}+{1}= %d".format(a, b) % (a+b))
print("Hasil pembagian {0}/{1}= %d".format(a, b) % (a/b))
