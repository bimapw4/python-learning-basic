def v_insAsc(data, banyak_data):
  k = 1
  while k <= banyak_data - 1:
    i = k
    x = data[i]
    while i >= 1 and data[i-1] > x:
      data[i] = data[i-1]
      i -= 1
    data[i] = x
    k += 1

data = []
banyak_data = int(input('Banyak data:'))
x = 0
while x < banyak_data:
  data.append(input('Data ke-'+ str(x + 1) +' :'))
  x += 1

v_insAsc(data, banyak_data)

print("\n")
print("Data Array Terurut")
j = 0
while j < banyak_data:
    print(str(data[j])+ " ", end="")
    j += 1