import matplotlib.pyplot as plt

def one():
    data = []
    for i in range(20):
        data.append(i*i)
    plt.plot(data)
    plt.show()
    
one()

def one2():
    data = []
    plt.plot([0,1,4,9,16,25,36])
    plt.show()
one2()