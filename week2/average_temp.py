
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
x = week_temps_f.split(",")
n = len(x)
avg_temp = 0

for i in range(n):
    x[i] = float(x[i])
    avg_temp += x[i]
avg_temp /= n
print(avg_temp)
