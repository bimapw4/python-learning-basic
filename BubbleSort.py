def bubble(data, banyak_data): 
  count_x = 0
  count_y = 0
  for x in range(banyak_data):
    count_x = count_x + 1
    for i in range(banyak_data-x-1):
        count_y = count_y + 1
        if data[i+1] < data[i]:
          temp = data[i+1]
          data[i+1] = data[i]
          data[i] = temp
  print("count x", count_x)
  print("count y", count_y)


data = []
banyak_data = input('Banyak data:')
banyak_data = int(banyak_data)
for x in range(banyak_data):
  data.append(input('Data ke-'+ str(x + 1) +' :'))

bubble(data, banyak_data)

print("") 
print("Data Array Terurut")
for j in range(banyak_data):
    print(str(data[j])+ " ", end="")