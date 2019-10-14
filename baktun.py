def cuenta_larga():  
    print """ 
    Este script calcula la cuenta larga Maya y la convierte al Gregoriano.  
    Es un aproximado que da unicamente el anyo, no da mes ni dia. 
    Dentro del codigo se contiene el comentario de como funciona el codigo. 
    """  
    baktun = input("Baktun: ")  
    katun = input("Katun: ")  
    tun = input("Tun: ")  
    uinal = input("Uinal: ")  
    kin = input("Kin: ")  
    baktun = baktun*144000  
    katun = katun*7200  
    tun = tun*360  
    uinal = uinal*20  
    kin = kin  
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
    print gTotal  
    gregoriano = gTotal / 365  
    print gregoriano  
    maya = gregoriano - 3115  
    if "-" in str(maya):  
        a = str(maya)  
        final = a.replace("-","")  
        print final, "a.C."  
    else:  
        print maya, "d.C."  
        stop = raw_input("Presiona cualquier tecla para terminar...")  
  
cuenta_larga()