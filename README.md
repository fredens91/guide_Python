# guide_Python

## Installazione di Python
https://www.python.org/downloads/

### VS Code Plugins
- Python (estensione ufficiale di Microsoft)
- Kivy (estensione per il framework Kivy)

## Sintassi

### Variabili e Classi

numeri
```
numInt = 10
numFloat = 5.4
```

stringa
```
nome = "Alice"
```

boolean
```
value = True
```

lista
```
list = [1, 2, 3, 4, 5]
```

dizionario
```
dictionary = {"nome": "Bob", "età": 25}
```

Classi

```
class Persona
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
```

### Funzioni
```
def somma(a, b):
    return a + b
```

### Cicli
If
```
if(numInt < 15):
    print("numero minore di 15")
else:
    print("numero maggiore di 15")
```

For (non esiste il foreach)

```
# Iterazione attraverso una lista
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)
```
```
# Iterazione attraverso una stringa
stringa = "Python"
for carattere in stringa:
    print(carattere)
```
```
# Iterazione attraverso un dizionario
dizionario = {"chiave1": 1, "chiave2": 2, "chiave3": 3}
for chiave, valore in dizionario.items():
    print(chiave, valore)
```

While
```
contatore = 1
while contatore <= 5:
    print(contatore)
    contatore += 1
```
