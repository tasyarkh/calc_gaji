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
gajiPokok          = 300000
divider("=")

#kondisi golongan
if( golJabatan == 1 ):
    tunjanganJabatan = 0.05 * gajiPokok #jika jabatan gol 1 maka tunjangan =  5% * 300.000
elif( golJabatan == 2 ):
    tunjanganJabatan = 0.10 * gajiPokok #jika jabatan gol 2 maka tunjangan =  10% * 300.000
elif( golJabatan == 3 ):
    tunjanganJabatan = 0.15 * gajiPokok #jika jabatan gol 2 maka tunjangan =  15% * 300.000
else:
    tunjanganJabatan = 0 

#kondisi tunj pendidikan
if( pendidikan == "SMA" or pendidikan == "sma" ): #jika pend sma tunjangan = 2.5% * 300.000
    tunjanganPendidikan = 0.025 * gajiPokok
elif( pendidikan == "D1" or pendidikan == "d1" ): #jika pend d1 tunjangan = 5% * 300.000
    tunjanganPendidikan = 0.05 * gajiPokok
elif( pendidikan == "D3" or pendidikan == "d3" ): #jika pend d3 tunjangan = 20% * 300.000
    tunjanganPendidikan = 0.20 * gajiPokok
elif( pendidikan == "S1" or pendidikan == "s1" ): #jika pend s1 tunjangan = 30% * 300.000
    tunjanganPendidikan = 0.30 * gajiPokok
else:
    tunjanganPendidikan = 0

#define jam kerja tetap
jamNormal = 8

#kondisi jika jam kerja lebih / lembur
if ( jamKerja > 8 ):
    prosesHonorLembur = jamKerja -  jamNormal #jika jam kerja lebih dari 8 jam, jumlah jam kerja - 8
    jumlahHonorLembur = prosesHonorLembur * 3500 # jumlah honor * 3.500
else:
    jumlahHonorLembur = 0

#Total
tunjangan = tunjanganJabatan + tunjanganPendidikan
totalGaji = gajiPokok + tunjangan + jumlahHonorLembur
 
#output
print("Karyawan Yang Bernama " +str(namaKaryawan))
print("")
print("Honor yang diterima : ")
#print("Gaji Pokok            ", formatrupiah(gajiPokok))
print("Tunjangan Jabatan     ", formatrupiah(str(tunjanganJabatan).rstrip('0').rstrip('.')))
print("Tunjangan Pendidikan  ", formatrupiah(str(tunjanganPendidikan).rstrip('0').rstrip('.')))
print("Honor Lembur          ", formatrupiah(jumlahHonorLembur))
divider("=")
print("Total Gaji Karyawan          ", formatrupiah(str(totalGaji).rstrip('0').rstrip('.')))
divider("=")