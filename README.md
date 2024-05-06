# guide_Python

## Installazione di Python
https://www.python.org/downloads/
Installa Python su Windows.

### VS Code Plugins
- Python (estensione ufficiale di Microsoft)
- Kivy (estensione per il framework Kivy)

## Sintassi

### Variabili e Classi

# numeri
`numInt = 10`
`numFloat = 5.4`

stringa
`nome = "Alice"`

boolean
`value = True`

lista
`lista = [1, 2, 3, 4, 5]`

dizionario
`dizionario = {"nome": "Bob", "età": 25}`

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


### Operazioni