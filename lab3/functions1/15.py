a = [0.86, 1.04, 1.45, 1.31, 1.22, 1.09, 0.73, 1.11, 0.95, 0.84, 0.96, 0.78, 1.23, 1.13, 1.04, 1.44, 1.32, 1.29, 0.68, 0.86, 1.33, 1.08, 0.87, 0.67, 1.28, 0.97, 1.14, 0.83, 1.33, 1.40, 1.24, 1.43, 0.98, 1.34, 0.81, 0.88, 1.10, 0.70, 1.15, 1.23, 1.34, 1.09, 0.80, 1.16, 1.24, 0.75, 0.99, 1.41, 0.88, 0.79, 1.36, 1.25, 0.89, 1.26, 1.42, 1.35, 0.80, 1.17, 0.90, 1.00, 1.11, 0.69, 1.18, 0.82, 1.01, 0.90, 1.36, 1.25, 0.67, 0.91, 1.37, 1.02, 0.92, 1.27, 1.19, 1.38, 1.46, 0.93, 1.27, 0.83, 1.04, 1.11, 1.47, 1.07, 0.72, 0.93, 1.26, 0.77, 1.20, 1.28, 0.77, 1.10, 0.95, 1.05, 1.08, 1.11, 1.10, 1.48, 1.07, 0.92]
a.sort()
for i in range(len(a)):
    print(f'{i + 1} - {a[i]}')
sum = 0
for i in range(len(a)) :
    sum += pow(a[i], 2)

print(sum)