import argparse

parser = argparse.ArgumentParser(description="This script can upload documents to our blogspot blog, refer to the flags below for more information")
parser.add_argument("-d","--debug", help="Debug application, set to 1 for debuging, default 0", 
    default=0, type=int, dest="debug")
flags = parser.parse_args()

def cuenta_larga():  
    print("""
    Este script calcula la cuenta larga Maya y la convierte al Gregoriano.  
    Es un aproximado que da unicamente el anyo, no da mes ni dia. 
    Dentro del codigo se contiene el comentario de como funciona el codigo. 
    """)
    baktun = int(input("Baktun: "))
    baktun = baktun*144000
    if flags.debug == 1:
        print(baktun)
        input("Wait...")
    katun = int(input("Katun: "))
    katun = katun*7200
    if flags.debug == 1:
        print(katun)
        input("Wait...")
    tun = int(input("Tun: "))
    tun = tun*360
    if flags.debug == 1:
        print(tun)
        input("Wait...")
    uinal = int(input("Uinal: "))
    uinal = uinal*20
    if flags.debug == 1:
        print(uinal)
        input("Wait...")
    kin = int(input("Kin: "))
    # Las cantidades manejadas son dias, un baktun es 144000 dias, un katun es 7200,  
    # un tun 360, un uinal es 20 y los kin son unidades individuales. Todas estas se  
    # suman bajo la variable de gTotal para despues ser dividas entre 365, que es la  
    # cantidad de dias que tiene un anyo comun, para asi generar una cantidad en   
    # anyos gregorianos que despues se resta contra 3115, que es la epoca de la   
    # antiguedad Maya. En teoria una vez que sale el numero si genera un numero  
    # negativo, es decir marca -X este tendra el signo de menos removido y en lugar  
    # de marcar d.e.C. marcara a.e.C. como debe corresponder por ser previo a la   
    # epoca que nosotros demarcamos como la era Comun.  
    gTotal = baktun+katun+tun+uinal+kin
    print("Total Maya:",gTotal)
    years = 0
    total_days = int(gTotal)
    print(total_days)
    while total_days >= 0:
        for i in range(3):
            total_days -= 365
            years += 1
        total_days -= 366
        years += 1
    print(years,years-3115,total_days)
#    if "-" in str(maya):
#        a = str(maya)
#        final = a.replace("-","")
#        print(final, "a.C.")
#    else:
#        print(maya, "d.C.")
#        input("Presiona cualquier tecla para terminar...")

cuenta_larga()