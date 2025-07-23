#creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

def fibonacci(num):
    # Inicializamos los dos primeros números de la sucesión: 0 y 1
    a,b = 0,1
    
    # Creamos la lista donde se guardará la sucesión, comenzando con el 0
    fibonacci_lista = [0]
    
    # Creamos un bucle que se repite un número de veces igual al valor pasado como argumento
    for i in range(num):
        
        # Verificamos si el siguiente número de la sucesión excede el límite dado
        if b > num : 
            # Si el número supera el límite, terminamos la función y devolvemos la lista
            return fibonacci_lista
        else:
            # Si no lo supera, lo agregamos a la lista
            fibonacci_lista.append(b)
            
            
            # Calculamos los siguientes valores de la sucesión:
            # a toma el valor de b, y b toma el valor de a + b (el siguiente número en la serie)
            a,b = b,a+b
            
            
# Llamamos a la función con el número 98 y guardamos el resultado    
resultado = fibonacci(98)

# Imprimimos el resultado final de la sucesión de Fibonacci hasta el número dado
print(resultado)
        
        
        
        
        

#Funcion de fibonacci que genera N elementos de la sucesion de fibonacci

# Creamos una función que genera los primeros "n" números de la sucesión de Fibonacci
def fibonacci_cantidad(n):
    
    # Inicializamos los dos primeros valores de la sucesión: 0 y 1
    a, b = 0, 1
    
    # Creamos la lista donde se guardarán los números de la sucesión
    fibonacci_lista = []
    
    
    #Usamos un bucle que se repite 'n' veces
    for _ in range(n):
        
        # Agregamos el número actual (a) a la lista
        fibonacci_lista.append(a)
        
        # Actualizamos los valores:
        # - 'a' toma el valor de 'b'
        # - 'b' toma el valor de la suma de los anteriores 'a' y 'b'
        a, b = b, a+b

    # Retornamos la lista completa con los n primeros números de Fibonacci
    return fibonacci_lista
    
resultado = fibonacci_cantidad(10)
print(resultado)