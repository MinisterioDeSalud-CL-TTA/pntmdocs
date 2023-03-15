---
layout: default
title: Carga Masiva de Resultados en la Plataforma
parent: Registro de muestras - Laboratorio 
grand_parent: Registro de muestras
nav_order: 7
---

# Carga Masiva de Resultados en la Plataforma

Con el objetivo de apoyar la operatividad y eficacia del sistema, se ha dispuesto un banner llamado "Carga Masiva de Resultados" para aquellos laboratorios que no tienen la capacidad de generar integración informática con los Web Services dispuestos para ello. Esta carga masiva permite la carga automática de resultados por interconexión de sistemas.

### Acceder a la opción de carga masiva

Para acceder a la carga masiva, debes seguir los siguientes pasos:

1. Ingresa a tu perfil de laboratorio.
2. Busca la opción "Carga masiva" en el menú y haz clic en ella.
3. Selecciona la sección "Resultados" en la pantalla de carga masiva.

![Imagen de referencia: Cargas masivas](img/lab_carga_masiva_1.png)
*Figura 1: Imagen de referencia para la carga masiva*

### Cargar resultados

A continuación, se detallan los pasos que se debe seguir para realizar la carga masiva:

1. Descargar datos recepcionados en planilla Excel: Para descargar los datos, debe hacer clic en "Descargar Data Actual", lo que descargará automáticamente una planilla Excel que contiene tres columnas:
   - ID Muestra: identificador asociado al RUT del paciente.
   - ID Paciente (RUT): RUT del paciente asociado al ID.
   - Resultados: columna para completar con el resultado de la muestra (Positivo, Negativo, Indeterminado, No apta).
2. Colocar resultado en la planilla: Una vez desplegada la planilla "data actual", se debe colocar el resultado asociándolo con el sistema de registro propio del establecimiento, ya sea mediante planillas configuradas de forma manual o descargadas del sistema LIS propio. Para optimizar el tiempo de carga masiva, se recomienda utilizar la función BUSCARV asociando la búsqueda a los RUT (considerar que los RUT deben poseer el mismo formato) y aplicar la carga automática de todos los resultados obtenidos y requeridos en la planilla "data actual".
3. Cargar la planilla en la plataforma: Una vez que los resultados se hayan colocado en la planilla "data actual", se debe cargar en la plataforma, lo que automáticamente cargará los resultados en cada una de las muestras.

![Proceso de carga masiva de resultados para las muestras](img/lab_carga_masiva_2.png)
*Figura 2: Proceso de carga masiva de resultados para las muestras*
