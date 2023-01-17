from matplotlib import pyplot as plt


file1 = open("times-8-840.txt")
times1 = [int(line) for line in file1]

file2 = open("times-8-1680.txt")
times2 = [int(line) for line in file2]

file3 = open("times-8-2520.txt")
times3 = [int(line) for line in file3]

speeds1 = [times1[0] / t for t in times1]
speeds2 = [times2[0] / t for t in times2]
speeds3 = [times3[0] / t for t in times3]

effectiveness1 = [speeds1[i] / (i + 1) for i in range(len(speeds1))]
effectiveness2 = [speeds2[i] / (i + 1) for i in range(len(speeds2))]
effectiveness3 = [speeds3[i] / (i + 1) for i in range(len(speeds3))]

x_axis = [i + 1 for i in range(len(times1))]

plt.figure()
plt.title("Czas wykonania dla trzech problemów w zależności od liczby procesorów")
plt.plot(x_axis, times1, label="N = 840")
plt.plot(x_axis, times2, label="N = 1680")
plt.plot(x_axis, times3, label="N = 2520")
plt.xlabel("Liczba procesorów")
plt.ylabel("Czas")
plt.legend()


plt.figure()
plt.title("Przyspieszenie dla trzech problemów w zależności od liczby procesorów")
plt.plot(x_axis, speeds1, label="N = 840")
plt.plot(x_axis, speeds2, label="N = 1680")
plt.plot(x_axis, speeds3, label="N = 2520")
plt.plot(x_axis, x_axis, label="Wzorcowe")
plt.xlabel("Liczba procesorów")
plt.ylabel("Przyspieszenie")
plt.legend()


plt.figure()
plt.title("Efektywność dla trzech problemów w zależności od liczby procesorów")
plt.plot(x_axis, effectiveness1, label="N = 840")
plt.plot(x_axis, effectiveness2, label="N = 1680")
plt.plot(x_axis, effectiveness3, label="N = 2520")
plt.plot(x_axis, [1 for i in range(len(times1))], label="Wzorcowe")
plt.xlabel("Liczba procesorów")
plt.ylabel("Efektywność")
plt.legend()
plt.show()
