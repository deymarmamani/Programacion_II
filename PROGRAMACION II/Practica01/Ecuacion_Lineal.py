class EcuacionLineal:
    def __init__(self, a: float, b: float, c: float, d: float, e: float, f: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def tieneSolucion(self) -> bool:
        determinante = self.a * self.d - self.b * self.c
        return determinante != 0
    def getX(self) -> float:
        if not self.tieneSolucion():
            return None
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)
    def getY(self) -> float:
        if not self.tieneSolucion():
            return None
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)

if __name__ == "__main__":
    valores = input("Ingrese a, b, c, d, e, f: ").split()
    a, b, c, d, e, f = map(float, valores)
    ecuacion = EcuacionLineal(a, b, c, d, e, f)
    if ecuacion.tieneSolucion():
        x = ecuacion.getX()
        y = ecuacion.getY()
        print(f"x = {x:.1f}, y = {y:.1f}")
    else:
        print("La ecuación no tiene solución")