class Estadistica:
    def __init__(self, valores):
        self.valores = valores
    def promedio(self):
        return sum(self.valores) / len(self.valores)
    def desviacion(self):
        prom = self.promedio()
        suma_cuadrados = sum((x - prom) ** 2 for x in self.valores)
        return (suma_cuadrados / (len(self.valores) - 1)) ** 0.5
def main():
    print("Ingrese 10 números separados por espacios:")
    entrada = input().split()
    valores = [float(x) for x in entrada]
    est = Estadistica(valores)
    prom = est.promedio()
    desv = est.desviacion()
    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.5f}")
if __name__ == "__main__":
    main()