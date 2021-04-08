import json

def showing(data):
  sorting = [];
  index = 0
  choose = input('Kategori Sorting: ')
  value = input('Value Sorting: ')

  if choose == 'Nama Mahasiswa:':
    for i in range(len(data)):
      if data[i][1].find(value) >= 0:
        sorting.append(data[i])

  elif  choose == 'Tahun Lahir':
    for i in range(len(data)):
      if data[i][2] == int(value):
        sorting.append(data[i])

  elif choose == 'Program Studi':
    for i in range(len(data)):
      if data[i][3].find(value) >= 0:
        sorting.append(data[i])

  else:
    print("Tidak ada kecocokan jenis kategori")

  return sorting, len(sorting);

data = []
selesai = 0

while selesai <= 0:
  Nrp = int(input('Nrp :'))
  Nama = input('Nama Mahasiswa:')
  while len(Nama) >= 15:
    print("Max Panjang Nama 15 char")
    Nama = input('Nama Mahasiswa:')

  tahun = int(input('Tahun Lahir :'))
  studi = input('Program Studi :')

  value = []
  value.append(Nrp)
  value.append(Nama)
  value.append(tahun)
  value.append(studi)
  data.append(value)

  selesai = int(input('Selesai(1/0) :'))
  print("\n")

sorting, lenData = showing(data)
toJson = []
for i in range(lenData):
  toJson.append({
      "Nrp" : sorting[i][0],
      "Nama Mahasiswa" : sorting[i][1],
      "Tahun Lahir" : sorting[i][2],
      "Program Studi" : sorting[i][3],
  })

print("\n")
print("Data Sorting :")
print(json.dumps(toJson))
print("\n")
print("Jumlah Data Sorting :", lenData)