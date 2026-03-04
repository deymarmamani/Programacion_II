import time
import random
from typing import List

class Cronometro:
    def __init__(self) -> None:
        self.__inicia: float = time.time()
        self.__finaliza: float = 0.0

    def iniciar(self) -> None:
        self.__inicia = time.time()

    def detener(self) -> None:
        self.__finaliza = time.time()

    def lapsoDeTiempo(self) -> float:
        return (self.__finaliza - self.__inicia) * 1000.0

    def get_inicia(self) -> float:
        return self.__inicia

    def get_finaliza(self) -> float:
        return self.__finaliza

if __name__ == "__main__":
    numeros = [random.randint(0, 1_000_000) for _ in range(100_000)]
    cron = Cronometro()
    cron.iniciar()
    numeros.sort()
    cron.detener()
    print(f"Tiempo de ordenación eficiente: {cron.lapsoDeTiempo():.3f} milisegundos")