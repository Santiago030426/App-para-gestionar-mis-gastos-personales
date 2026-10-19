
# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo: Santiago Zapata Montoya
# Mi app se llama: App para gastos personales/admin. Finanzas
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí:
nombre = "Santiago"

edad = 20

estatura = 1.59

print(f"Hola, soy {nombre}, tengo {edad} y mido {estatura}")


# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:

a = "100"
b = 100
c = 100.0
d = "cien"

# Por mas que estas variables parezcan iguales, ya que se estan refiriendo a un mismo valor, para la 
# programacion son totalmente diferentes, esto se debe a algo llamado, "tipos de datos", entonces, dentro 
# de esta logica, "100", con comillas es declarado un dato string, o sea texto, 100 sin comillas, es un dato numero
# 100.0 es un dato decimal y "cien", nuevamente es un dato tipo texto/string.

# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:


valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
personas = int(input("Ingrese la cantidad de personas: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))


propina = valor_cuenta * (porcentaje_propina / 100)
total = valor_cuenta + propina
pago_por_persona = total / personas


print(f"Propina:          ${propina:,.0f}")
print(f"Total:            ${total:,.0f}")
print(f"Cada uno paga:    ${pago_por_persona:,.0f}")

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

# Tu código corregido aquí:

precio = float(input("Precio del producto: "))
unidades = int(input("Unidades: "))
print(f"Total a pagar: ${precio * unidades:,.2f}")


# Error 1: El primer error es de tipos de datos, ya que en el codigo erroneo, no se especifica si el tipo 
# de dato es float o int/numero entero, por ende a la hora de hacer la multiplicacion no saldra bien.

# Error 2: el segundo error es de concatenacion ya que en vez de usar "{}" para concatenar de una buena manera
# en el codigo original usa "+", pero python lee esto como si quisiera sumar un string con un int.


# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:

producto = input("Nombre del producto: ")
unidades = int(input("Cantidad de unidades: "))
precio = float(input("Precio por unidad: "))


valor_total = unidades * precio


print("\n===== INVENTARIO =====")
print(f"Producto:    {producto}")
print(f"Unidades:    {unidades}")
print(f"Precio:      ${precio:,.0f}")
print(f"Valor total: ${valor_total:,.0f}")
print("======================")


# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================
