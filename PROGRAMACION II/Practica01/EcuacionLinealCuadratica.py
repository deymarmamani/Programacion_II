import math
class EcuacionLineal:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self) -> float:
        return self.__b ** 2 - 4 * self.__a * self.__c
    def getRaiz1(self) -> float:
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b + math.sqrt(discriminante)) / (2 * self.__a)
    def getRaiz2(self) -> float:
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b - math.sqrt(discriminante)) / (2 * self.__a)
if __name__ == "__main__":
    print("Ingrese a, b, c:", end=" ")
    a, b, c = map(float, input().split())
    ecuacion1 = EcuacionLineal(a, b, c)
    print("Ingrese a, b, c:", end=" ")
    a, b, c = map(float, input().split())
    ecuacion2 = EcuacionLineal(a, b, c)
    print("Ingrese a, b, c:", end=" ")
    a, b, c = map(float, input().split())
    ecuacion3 = EcuacionLineal(a, b, c)
    discriminante1 = ecuacion1.getDiscriminante()
    if discriminante1 > 0:
        r1 = ecuacion1.getRaiz1()
        r2 = ecuacion1.getRaiz2()
        print(f"La ecuacion tiene dos raices {r1:.6g} y {r2:.6g}")
    elif discriminante1 == 0:
        r = ecuacion1.getRaiz1()
        print(f"La ecuacion tiene una raiz {r:.6g}")
    else:
        print("La ecuacion no tiene raices reales")
    discriminante2 = ecuacion2.getDiscriminante()
    if discriminante2 > 0:
        r1 = ecuacion2.getRaiz1()
        r2 = ecuacion2.getRaiz2()
        print(f"La ecuacion tiene dos raices {r1:.6g} y {r2:.6g}")
    elif discriminante2 == 0:
        r = ecuacion2.getRaiz1()
        print(f"La ecuacion tiene una raiz {r:.6g}")
    else:
        print("La ecuacion no tiene raices reales")
    discriminante3 = ecuacion3.getDiscriminante()
    if discriminante3 > 0:
        r1 = ecuacion3.getRaiz1()
        r2 = ecuacion3.getRaiz2()
        print(f"La ecuacion tiene dos raices {r1:.6g} y {r2:.6g}")
    elif discriminante3 == 0:
        r = ecuacion3.getRaiz1()
        print(f"La ecuacion tiene una raiz {r:.6g}")
    else:
        print("La ecuacion no tiene raices reales")