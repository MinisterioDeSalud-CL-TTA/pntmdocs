#%%
import html2markdown

def convert_html_to_markdown(input_file, output_file):
    # Leemos el archivo HTML
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Convertimos el contenido HTML a Markdown
    markdown_content = html2markdown.convert(html_content)

    # Escribimos el contenido Markdown en el archivo de salida
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Se ha convertido el archivo {input_file} a Markdown y se ha guardado en {output_file}.")
#%%
convert_html_to_markdown("reporte_lab_08-Reporte RT _ Descarga detalle 7 días.md", "reporte_lab_08-Reporte RT _ Descarga detalle 7 días.md")

# %%
