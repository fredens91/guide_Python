# commento in python
"""
commento su
più righe
"""

print("Hello World")

## variabili

# numeri
numInt = 10
numFloat = 5.4

# stringa
nome = "Alice"

#boolean
boolean = True

# list
lista = [1, 2, 3, 4, 5]

# dizionario
dizionario = {"nome": "Bob", "età": 25}


# Classe
class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.età} anni.")

# Creazione di un nuovo oggetto Persona
persona1 = Persona("Alice", 30)

# Accesso agli attributi dell'oggetto
print(persona1.nome)  # Stampa: Alice
print(persona1.età)   # Stampa: 30

# Chiamata a un metodo dell'oggetto
persona1.saluta()     # Stampa: Ciao, mi chiamo Alice e ho 30 anni.


# Funzioni
def somma(a, b):
    return a + b







## Operazioni

# IF

if(numInt < 15):
    print("numero minore di 15")
else:
    print("numero maggiore di 15")

# Switch

# Non esiste lo Switch Case ma si può creare una funzione
def switch_case(argument):
    switcher = {
        1: "Primo caso",
        2: "Secondo caso",
        3: "Terzo caso"
        # Aggiungere altri casi se necessario
    }
    
    # Ottenere il valore corrispondente all'argomento
    risultato = switcher.get(argument, "Caso predefinito")
    
    # Restituire il risultato
    return risultato

print(switch_case(1))  # Stampa: Primo caso
print(switch_case(2))  # Stampa: Secondo caso
print(switch_case(4))  # Stampa: Caso predefinito


# for (non esiste il foreach)

# Iterazione attraverso una lista
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)

# Iterazione attraverso una stringa
stringa = "Python"
for carattere in stringa:
    print(carattere)

# Iterazione attraverso un dizionario
dizionario = {"chiave1": 1, "chiave2": 2, "chiave3": 3}
for chiave, valore in dizionario.items():
    print(chiave, valore)

# While
contatore = 1
while contatore <= 5:
    print(contatore)
    contatore += 1
