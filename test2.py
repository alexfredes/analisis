# Simulación de una vulnerabilidad SQL Injection en una cadena de consulta
def login(user_input):
    # Esta línea simula una consulta insegura que podría ser vulnerable a inyección SQL
    query = f"SELECT * FROM users WHERE username = '{user_input}' AND password = 'password123';"
    print("Ejecutando consulta: " + query)

# Ejemplo de entrada potencialmente maliciosa
usuario = "admin' OR '1'='1"
login(usuario)
