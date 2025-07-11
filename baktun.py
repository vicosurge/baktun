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
    # suman bajo la variable de gTotal para después ser divididas entre 365.25, que es la  
    # cantidad promedio de días que tiene un año considerando años bisiestos, para así generar una cantidad en   
    # años gregorianos que después se resta contra 3114, que es la correlación GMT (Goodman-Martinez-Thompson)
    # que es la más aceptada para convertir fechas mayas al calendario gregoriano.
    
    gTotal = baktun_days + katun_days + tun_days + uinal_days + kin
    print(f"Total Maya (días): {gTotal}")
    
    # Convert to years using average year length (accounting for leap years)
    # The GMT correlation constant is 584283 (days from Maya epoch to Jan 1, 1 CE)
    # But for simplicity, we'll use the approximation method with 3114 BCE as base
    
    # Calculate approximate years from total days
    years_from_maya_epoch = gTotal / 365.25
    
    # Maya epoch corresponds to August 11, 3114 BCE in the proleptic Gregorian calendar
    # So we subtract from 3114 to get the year
    gregorian_year = years_from_maya_epoch - 3114
    
    if flags.debug == 1:
        print(f"Years from Maya epoch: {years_from_maya_epoch}")
        print(f"Calculated year: {gregorian_year}")
    
    # Determine if it's BCE or CE
    if gregorian_year < 0:
        final_year = abs(int(gregorian_year))
        era = "a.C."
    else:
        final_year = int(gregorian_year)
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
    print(f"Años desde época maya: {years_from_maya_epoch:.2f}")
    print(f"Resultado: {final_year} {era}")
    
    input("Presiona cualquier tecla para terminar...")

if __name__ == "__main__":
    cuenta_larga()