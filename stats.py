import matplotlib.pyplot as plt


times1 = []
times2 = []
mem1 = []
mem2 = []
problem_size = []

with open('./problem_size.txt', 'r') as f:
    for line in f.readlines():
        problem_size.append(int(line))
    

for i in range(1,16):
    with open("./outputs_basic/output" + str(i) + ".txt", 'r') as f1:
        data = f1.readlines()
        times1.append(float(data[3].strip()))
        mem1.append(float(data[4].strip()))

        
for i in range(1,16):
    with open("./outputs_efficient/output" + str(i) + ".txt", 'r') as f2:
        data = f2.readlines()
        times2.append(float(data[3].strip()))
        mem2.append(float(data[4].strip()))

plt.plot(problem_size, times1, label='Basic')
plt.plot(problem_size, times2, label='Efficient')
plt.legend()
plt.show()

plt.plot(problem_size, mem1, label='Basic')
plt.plot(problem_size, mem2, label='Efficient')
plt.legend()
plt.show()