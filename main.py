#Tasya Ramadhinta | 19231513 | 19.1A.11
#import file
from view.txtWelcome import welcome_txt
from view.numFormat import formatrupiah
from view.divider import divider

#function main
def main():
    welcome_txt()
if __name__ == "__main__":
    main()

#form input
namaKaryawan       = str(input("Masukan Nama Karyawan       : "))
golJabatan         = int(input("Masukan Golongan Jabatan    : "))
pendidikan         = str(input("Masukan Jenjang Pendidikan  : "))
jamKerja           = int(input("Masukan Jumlah Jam Kerja    : "))

#define gaji
gajiPokok          = 4000000
divider("=")

#kondisi golongan
if( golJabatan == 1 ):
    tunjanganJabatan = 0.05 * gajiPokok
elif( golJabatan == 2 ):
    tunjanganJabatan = 0.10 * gajiPokok
elif( golJabatan == 3 ):
    tunjanganJabatan = 0.15 * gajiPokok
else:
    tunjanganJabatan = 0 

#kondisi pendidikan
if( pendidikan == "SMA" or pendidikan == "sma" ):
    tunjanganPendidikan = 0.025 * gajiPokok
elif( pendidikan == "D1" or pendidikan == "d1" ):
    tunjanganPendidikan = 0.05 * gajiPokok
elif( pendidikan == "D3" or pendidikan == "d3" ):
    tunjanganPendidikan = 0.2 * gajiPokok
elif( pendidikan == "S1" or pendidikan == "s1" ):
    tunjanganPendidikan = 0.3 * gajiPokok
else:
    tunjanganPendidikan = 0

# Proses Percabangan Honor Lembur
jamNormal = 8

if ( jamKerja > 8 ):
    prosesHonorLembur = jamKerja -  jamNormal
    jumlahHonorLembur = prosesHonorLembur * 3500
else:
    jumlahHonorLembur = 0

# Total Gaji
tunjangan = tunjanganJabatan + tunjanganPendidikan
totalGaji = gajiPokok + tunjangan + jumlahHonorLembur
 
#output
print("Karyawan Yang Bernama " +str(namaKaryawan))
print("")
print("Honor yang diterima : ")
print("Gaji Pokok            ", formatrupiah(gajiPokok))
print("Tunjangan Jabatan     ", formatrupiah(str(tunjanganJabatan).rstrip('0').rstrip('.')))
print("Tunjangan Pendidikan  ", formatrupiah(str(tunjanganPendidikan).rstrip('0').rstrip('.')))
print("Honor Lembur          ", formatrupiah(jumlahHonorLembur))
divider("=")
print("Total Gaji Karyawan          ", formatrupiah(str(totalGaji).rstrip('0').rstrip('.')))
divider("=")