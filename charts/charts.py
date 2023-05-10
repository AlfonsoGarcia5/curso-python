import matplotlib.pyplot as plt

def pie_chart ():
    labels = ['A', 'B', 'C']
    values=[150, 250, 350]

    fig, ax = plt.subplots() #Declaración standar para pie charts
    ax.pie(values, labels=labels) #declaración std
    #plt.show() #graficar, pero el programa se detiene
    plt.savefig ('pie.png') #Evitando errores
    plt.close()