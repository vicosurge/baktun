import argparse

parser = argparse.ArgumentParser(description="This script can upload documents to our blogspot blog, refer to the flags below for more information")
parser.add_argument("-d","--debug", help="Debug application, set to 1 for debugging, default 0", 
    default=0, type=int, dest="debug")
flags = parser.parse_args()

def cuenta_larga():  
    print("""
    Este script calcula la cuenta larga Maya y la convierte al Gregoriano.  
    Es un aproximado que da únicamente el año, no da mes ni día. 
    Dentro del código se contiene el comentario de cómo funciona el código. 
    """)
    
    # Get Mayan Long Count components
    try:
        baktun = int(input("Baktun: "))
        baktun_days = baktun * 144000
        if flags.debug == 1:
            print(f"Baktun days: {baktun_days}")
            input("Wait...")
        
        katun = int(input("Katun: "))
        katun_days = katun * 7200
        if flags.debug == 1:
            print(f"Katun days: {katun_days}")
            input("Wait...")
        
        tun = int(input("Tun: "))
        tun_days = tun * 360
        if flags.debug == 1:
            print(f"Tun days: {tun_days}")
            input("Wait...")
        
        uinal = int(input("Uinal: "))
        uinal_days = uinal * 20
        if flags.debug == 1:
            print(f"Uinal days: {uinal_days}")
            input("Wait...")
        
        kin = int(input("Kin: "))
        if flags.debug == 1:
            print(f"Kin days: {kin}")
            input("Wait...")
            
    except ValueError:
        print("Error: Please enter valid integers for all values.")
        return
    
    # Las cantidades manejadas son días, un baktun es 144000 días, un katun es 7200,  
    # un tun 360, un uinal es 20 y los kin son unidades individuales. Todas estas se  
    # suman bajo la variable de gTotal para después usar la correlación GMT (Goodman-Martinez-Thompson)
    # que es la más aceptada para convertir fechas mayas al calendario gregoriano.
    
    gTotal = baktun_days + katun_days + tun_days + uinal_days + kin
    print(f"Total Maya (días): {gTotal}")
    
    # GMT correlation constant: 584283 days
    # This represents the Julian Day Number for Maya epoch 0.0.0.0.0 (4 Ahau 8 Cumku)
    # which corresponds to August 11, 3114 BCE in the proleptic Gregorian calendar
    GMT_CORRELATION = 584283
    
    # Calculate Julian Day Number for this Maya date
    julian_day = gTotal + GMT_CORRELATION
    
    # Convert Julian Day to Gregorian date using standard algorithm
    # This is the accepted method for JD to Gregorian conversion
    
    a = julian_day + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    gregorian_year = 100 * b + d - 4800 + m // 10
    
    if flags.debug == 1:
        print(f"Julian Day: {julian_day}")
        print(f"Calculated date: {month}/{day}/{gregorian_year}")
        print(f"Calculated year: {gregorian_year}")
    
    # Determine if it's BCE or CE
    if gregorian_year <= 0:
        final_year = abs(gregorian_year) + 1  # Adjust for no year 0
        era = "a.C."
    else:
        final_year = gregorian_year
        era = "d.C."
    
    print(f"Año aproximado: {final_year} {era}")
    
    # Show the calculation breakdown
    print("\nDesglose del cálculo:")
    print(f"Baktun: {baktun} × 144,000 = {baktun_days:,} días")
    print(f"Katun: {katun} × 7,200 = {katun_days:,} días")
    print(f"Tun: {tun} × 360 = {tun_days:,} días")
    print(f"Uinal: {uinal} × 20 = {uinal_days:,} días")
    print(f"Kin: {kin} = {kin} días")
    print(f"Total: {gTotal:,} días")
    print(f"Correlación GMT: {GMT_CORRELATION:,} días")
    print(f"Día Juliano: {julian_day:,}")
    print(f"Resultado: {final_year} {era}")
    
    input("Presiona cualquier tecla para terminar...")

if __name__ == "__main__":
    cuenta_larga()