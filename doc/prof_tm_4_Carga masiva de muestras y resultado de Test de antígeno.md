---
layout: default
title: Carga masiva de muestras y resultado de Test de antígeno
parent: Registro de muestras - Profesional Tomador de Muestras 
grand_parent: Registro de muestras
nav_order: 4
---

# Carga masiva de muestras y resultado de Test de antígeno
El siguiente instructivo explica los pasos necesarios para realizar cargas masivas de resultados de antígeno. Los usuarios podrán acceder a la sección de cargas masivas, descargar una planilla base con los campos solicitados, ingresar los datos requeridos y cargar el archivo de forma satisfactoria.

## Instrucciones de la carga masiva

![Alt text](img/carga_masiva_ag.png)
_Figura 1: Cargas masivas por la interfaz_
1.   Acceder al módulo de "Cargas Masivas" dentro de la plataforma y seleccionar "Antígeno".
2.   En el botón desplegable "Estructura del archivo a cargar" se pueden visualizar los campos solicitados en la Planilla Base de toma de muestras, incluyendo el nombre de la columna, el tipo de dato, la descripción y las restricciones correspondientes.
3.   La Planilla Base se encuentra disponible para su descarga en formato Excel, a través del botón "Descargar base" ubicado debajo de la descripción de los campos.
4.   Para ingresar los datos correspondientes a cada muestra, es necesario incluir al menos todos los datos obligatorios del archivo Excel, y guardar el archivo una vez completado.
5.   En la plataforma, se debe hacer clic en el botón "Seleccionar archivo" y elegir el archivo deseado para luego hacer clic en "Subir archivo" y completar la carga de forma satisfactoria.

## Estructura del archivo a cargar
La tabla que se presenta a continuación muestra la estructura de los datos que se deben rellenar en el archivo Excel. Cada columna representa un tipo de dato y la descripción que indica su función dentro del formulario. Además, se especifican las restricciones que se deben cumplir en cada columna para asegurar que la carga masiva sea procesada correctamente. Los usuarios deben incluir al menos todos los datos obligatorios descritos en la sección "Campos Solicitados".

| Columna                     | Tipo de dato | Descripción                                                                                                                                  | Restricciones                                                                                                                                                                                                                                                                               |
|:----------------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| run_pasaporte_              | Varchar      | Número de identificación del paciente                                                                                                       | Obligatorio. En caso de ser RUN, debe ser válido.                                                                                                                                                                                                                                           |
| paciente_tipodoc_           | Varchar      | Tipo de documento de identificación del paciente. Ejemplo: RUN, PASAPORTE, DNI PAIS DE ORIGEN, SIN DOCUMENTACION, N° FICHA CLINICA           | Obligatorio. Debe estar dentro de los valores aceptados: 1. RUN: run_pasaporte 2. PASAPORTE: run_pasaporte y paciente_ext_paisorigen 3. DNI PAIS DE ORIGEN: run_pasaporte y paciente_ext_paisorigen 4. SIN DOCUMENTACION: No se debe asignar valor a run_pasaporte y paciente_ext_paisorigen 5. N° FICHA CLINICA: run_pasaporte y paciente_ext_paisorigen |
| paciente_nombres_           | Varchar      | Nombres del paciente                                                                                                                        | Obligatorio.                                                                                                                                                                                                                                                                               |
| paciente_ap_pat_            | Varchar      | Apellido paterno del paciente                                                                                                               | Obligatorio.                                                                                                                                                                                                                                                                               |
| paciente_ap_mat_            | Varchar      | Apellido Materno del paciente                                                                                                               | Obligatorio. En caso de no poseer, indicar ".".                                                                                                                                                                                                                                             |
| paciente_direccion_         | Varchar      | Dirección del paciente                                                                                                                      | Obligatorio. Ejemplo: Avenida El Bosque.                                                                                                                                                                                                                                                    |
| paciente_telefono_          | Numero       | Número de teléfono del paciente                                                                                                             | Obligatorio.                                                                                                                                                                                                                                                                               |
| paciente_edad_              | Date         | Edad del paciente                                                                                                                            | Obligatorio.                                                                                                                                                                                                                                                                               |
| paciente_comuna_            | Numero       | Código de la comuna del paciente                                                                                                             | Obligatorio. Debe ser una comuna válida del maestro.                                                                                                                                                                                                                                        |
| paciente_numero_direccion_  | Varchar      | Número de identificador de la calle/avenida                                                                                                  | Obligatorio. Ejemplo: 130.                                                                                                                                                                                                                                                                  |
| paciente_depto_direccion_   | Varchar      | Número de identificador del departamento o casa del paciente                                                                                  | No obligatorio. Ejemplo: 22A.                                                                                                                                                                                                                                                               |
| paciente_poblacion_villa_   | Varchar      | Población de residencia del paciente                                                                                                         | Obligatorio. Ejemplo: Talca.                                                                                                                                                                                                                                                                 |
| paciente_via_direccion_     | Varchar      | Tipo de vía de la residencia del paciente                                                                                                     | Obligatorio. Debe estar dentro del maestro via_dirección. Ejemplo: 1.                                                                                                                                                                                                                        |
| paciente_mail_              | Varchar      | Dirección de correo electrónico del paciente                                                                                                 | Obligatorio.                                                                                                                                                                                                                                                                               |
| paciente_ext_paisorigen_    | Numero       | Código del país de origen del paciente                                                                                                       | Obligatorio si paciente_tipodoc es igual a "PASAPORTE", "DNI PAIS DE ORIGEN", "N° FICHA CLINICA" o "SIN DOCUMENTACION". Debe ser un código válido del maestro paises.                                                                                                                                                                                    |

## Errores en la carga masiva
La plataforma detalla los posibles errores que pueden ser indicados por el sistema al momento de subir una planilla de carga masiva a la plataforma, así como los errores que no detectará el sistema pero que pueden afectar la calidad de la información. El objetivo es verificar estas condiciones para poder subir una planilla de carga masiva de forma correcta.

### Errores indicados por el sistema
Los posibles errores que pueden ser indicados por el sistema al momento de subir una planilla de carga masiva a la plataforma son:
- __Campo obligatorio en blanco__: Este error se presenta al dejar en blanco campos que son de carácter obligatorio, como el RUN_pasaporte.
- __RUN Paciente Incorrecto__: Este error se presenta cuando la planilla posee algún RUN inválido. Cabe destacar que el RUN debe ser escrito sin puntos y con guion.
- __Rut Profesional_sis o Rut_medico no existente en base de profesionales__: Este error se presenta al ingresar un rut en el campo rut_profesional o rut_medico que no se encuentre en la base de profesionales.
- __Rut_medico en blanco__: Este error se presenta al dejar en blanco el campo rut_medico, ya que la plataforma fue diseñada en un principio para recibir muestras de antígenos de pacientes sintomáticos provenientes de alguna médica.
- __Fecha diferente a la fecha actual__: Este error se presenta al ingresar una fecha de muestra diferente a la fecha actual.
- __Campo no figura dentro del conjunto de datos__: Este error se presenta al ingresar información que no esté contenida dentro del maestro de datos. En dicho caso se indicará por pantalla el conjunto de datos aceptado.

### Errores no indicados por el sistema

Los errores no indicados por el sistema son aquellos que pueden afectar directamente el tratamiento de los datos y la calidad de la información, por lo que es importante verificar dicha información antes de ser subida. 

Algunos ejemplos de estos errores son:
- Ingreso de código DEIS de otro establecimiento.
- Ingreso erróneo de resultado.
- Ingreso de RUN de otro paciente.
- Ingreso de ID de otra comuna.
- Ingreso de código EPIVIGILA erróneo.
- Ingreso erróneo de tipo de búsqueda (activa o no activa).

### Excepciones

PNTM detalla algunas especificaciones a con
iderar en diversos campos obligatorios al momento de realizar una carga masiva en la plataforma en circunstancias excepcionales. Por ejemplo:
- Dirección o teléfono del paciente: En caso de que no se posea la dirección detallada del paciente debido a circunstancias en las cuales sea dificultoso poseer este tipo de información, se deberán considerar algunas indicaciones específicas dependiendo del resultado de la muestra.
- Pacientes menores de edad: En caso de que se trate de pacientes menores de edad, se debe ingresar el RUN del apoderado en el campo rut_medico.
- En caso de fallecimiento del paciente: Si el paciente ha fallecido, se debe indicar en el campo estado_paciente la opción "Fallecido".
- Muestras en contexto de pesquisa activa: En caso de que las muestras sean tomadas en el contexto de pesquisa