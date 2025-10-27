import math

def calcular_raiz_cuadrada():
    print("=== Cálculo de la raíz cuadrada de un número ===")
    
    try:
        numero = float(input("Ingrese un número: "))
        
        if numero < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
            return
        
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado:.4f}")
    
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido.")

if __name__ == "__main__":
    calcular_raiz_cuadrada()