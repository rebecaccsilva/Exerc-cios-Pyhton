from rich import print, inspect
from des23poli import Quadrado, Circulo


def main():
    q = Quadrado(20)
    #inspect(q, methods=True)
    print(f"Um quadrado de lado {q.lado} tem perímetro de {q.perimetro()}cm")
    print(f'Um quadrado de lado {q.lado} tem área de {q.area()}cm2')

    c= Circulo(25)
    #inspect(c, methods=True)
    print(f'Um circulo de raio {c.raio} tem perímetro de {c.perimetro():.2f}cm')
    print(f'Um circulo de raio {c.raio} tem area de {c.area():.1f}cm2')


if __name__ == "__main__":
    main()
