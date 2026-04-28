class Puesto:
    def __init__(self, codigo=0, descripcion="", areaSolicitante="", plazasRequeridas=0, sueldo=0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - {self.areaSolicitante} - {self.plazasRequeridas} plazas - S/{self.sueldo}"

    def __repr__(self):
        return f"{self.codigo} {self.descripcion}"


def buscaPuesto(lst, nuevo):
    for p in lst:
        if p.codigo == nuevo.codigo or p.descripcion == nuevo.descripcion or p.areaSolicitante == nuevo.areaSolicitante:
            return True
    return False


def ordBurbujaCodigo(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j].codigo < lst[j + 1].codigo:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def ordInsercionSueldo(lst):
    n = len(lst)
    for i in range(1, n):
        aux = lst[i]
        j = i - 1

        while j >= 0 and lst[j].sueldo < aux.sueldo:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = aux


def ordSeleccionTotal(lst):
    n = len(lst)

    for i in range(n - 1):
        mayor = i

        for j in range(i + 1, n):
            total1 = lst[j].plazasRequeridas * lst[j].sueldo
            total2 = lst[mayor].plazasRequeridas * lst[mayor].sueldo

            if total1 > total2:
                mayor = j

        lst[i], lst[mayor] = lst[mayor], lst[i]


def AgregaPuesto(lst):
    codigo = int(input("Ingrese codigo: "))
    descripcion = input("Ingrese descripcion: ")
    area = input("Ingrese area solicitante: ")
    plazas = int(input("Ingrese plazas requeridas: "))
    sueldo = float(input("Ingrese sueldo: "))

    if codigo <= 0 or plazas <= 0 or sueldo <= 0:
        print("Numeros invalidos")
        return

    if len(descripcion) < 3 or len(area) < 3:
        print("Texto invalido")
        return

    nuevo = Puesto(codigo, descripcion, area, plazas, sueldo)

    if not buscaPuesto(lst, nuevo):
        lst.append(nuevo)
        print("Registrado correctamente")
    else:
        print("Codigo, descripcion o area repetida")


def MostrarTodo(lst):
    print("\nLISTA DE PUESTOS")
    for p in lst:
        print(p)


def BorraPuesto(lst):
    ordBurbujaCodigo(lst)

    cod = int(input("Ingrese codigo a eliminar: "))

    for i, p in enumerate(lst):
        if p.codigo == cod:
            del lst[i]
            print("Eliminado")
            return

    print("No encontrado")


def BuscaSueldo(lst):
    ordInsercionSueldo(lst)

    buscar = float(input("Ingrese sueldo a buscar: "))

    izq = 0
    der = len(lst) - 1
    pos = -1

    while izq <= der:
        cen = (izq + der) // 2

        if lst[cen].sueldo == buscar:
            pos = cen
            break

        elif buscar > lst[cen].sueldo:
            der = cen - 1
        else:
            izq = cen + 1

    if pos == -1:
        print("No existe")
    else:
        i = pos

        while i >= 0 and lst[i].sueldo == buscar:
            i -= 1

        i += 1

        while i < len(lst) and lst[i].sueldo == buscar:
            print(lst[i])
            i += 1


def PuestosAContratar(lst):
    ordSeleccionTotal(lst)

    dinero = float(input("Ingrese dinero total a invertir: "))
    suma = 0

    for p in lst:
        total = p.plazasRequeridas * p.sueldo

        if suma + total <= dinero:
            print(p, " Total:", total)
            suma += total

    print("Total usado:", suma)


lista = []

lista.append(Puesto(101, "PUESTO 1", "1", 2, 2000))
lista.append(Puesto(102, "PUESTO 2", "2", 3, 4000))
lista.append(Puesto(103, "PUESTO 3", "3", 1, 800))
lista.append(Puesto(104, "PUESTO 4", "4", 2, 1000))
lista.append(Puesto(105, "PUESTO 5", "5", 4, 7700))
lista.append(Puesto(106, "PUESTO 6", "6", 1, 5200))


while True:
    print("\n1-AgregaPuesto")
    print("2-MostrarTodo")
    print("3-BorraPuesto")
    print("4-BuscaSueldo")
    print("5-PuestosAContratar")
    print("6-Salir")

    opc = int(input("Ingrese opcion: "))

    if opc == 1:
        AgregaPuesto(lista)

    elif opc == 2:
        MostrarTodo(lista)

    elif opc == 3:
        BorraPuesto(lista)

    elif opc == 4:
        BuscaSueldo(lista)

    elif opc == 5:
        PuestosAContratar(lista)

    elif opc == 6:
        print("Programa terminado")
        break

    else:
        print("Ingrese opcion valida")
