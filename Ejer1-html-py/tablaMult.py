from jinja2 import Template


def tabla_multiplicar(numero):
    resultado = f"# Tabla del {numero} #\n"

    for i in range(11):
        multiplicacion = i * numero
        resultado += f"{i} x {numero} = {multiplicacion}\n"

    return resultado
# Cargar el código Python
codigo_python = open('tablaMult.py').read()

# Cargar la plantilla HTML
plantilla = Template(open('codigo_python.html').read())

# Renderizar la plantilla con el código Python
resultado_html = plantilla.render(codigo_python=codigo_python)

# Mostrar el resultado HTML
print(resultado_html)
