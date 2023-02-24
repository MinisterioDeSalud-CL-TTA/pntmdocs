#%%
import os
import markdown

def split_markdown_file_by_headers(input_file):
    # Leer el archivo markdown
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Convertir el contenido en HTML
    html = markdown.markdown(content)

    # Dividir el HTML en secciones basadas en las etiquetas de encabezado
    sections = html.split("<h1>")

    # Inicializar el contador de archivos de salida
    output_counter = 1

    # Recorrer las secciones y escribir cada una en su propio archivo
    for i, section in enumerate(sections):
        # Ignorar la primera sección ya que no tiene un encabezado
        if i == 0:
            continue

        # Obtener el título de la sección
        title = section.split("</h1>")[0]

        # Eliminar cualquier carácter no válido en el título del archivo
        filename = "".join(c if c.isalnum() or c.isspace() else "_" for c in title)

        # Crear el nombre del archivo de salida con el número correspondiente
        output_filename = f"{output_counter:02d}-{filename}.md"

        # Escribir la sección en el archivo de salida
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(markdown.markdown(f"<h1>{section}"))

        # Incrementar el contador de archivos de salida
        output_counter += 1

    print(f"Se han creado {len(sections) - 1} archivos Markdown.")


# %%
split_markdown_file_by_headers('doc/reportes_lab.md')
# %%
