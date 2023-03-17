---
layout: default
title: Creación y resultado de Muestras AG via interfaz web
parent: Registro de muestras - Profesional Tomador de Muestras 
grand_parent: Registro de muestras
nav_order: 3
---

# Creación y resultado de Muestras AG via interfaz web

Para crear muestras utilizando la interfaz de usuario, se debe seguir el siguiente proceso:

1. Acceder al módulo de __Antígeno__ en el menú de opciones
2. Seleccionar __Registro y seguimiento__ dentro del submenú
3. Hacer clic en el botón __Crear muestra__

De esta manera, podrás continuar con el proceso de creación de muestras.

![Alt text](img/ag_1.png)

_Figura 1: creación de muestras de Antígeno en la plataforma toma de muestras_

![Alt text](img/Pasted%20image%2020230214125252.png)

_Figura 2: botón "Crear registro"_

Después de hacer clic en el botón "Crear registro", se creará un id de muestra, el cual si se hace click se abrirá un formulario donde se debe rellenar los campos solicitados con la información correspondiente de cada muestra que deseas crear.

## Campos del formulario: Creación de muestra

Es importante asegurarse de que se llenen todos los campos obligatorios, que están identificados con un asterisco (\*).

## Datos de registro

![Alt text](img/datos_registro_ag.png)

_Figura 3: Sección datos de registro_

__Profesional Tomador de muestra__ Completar los datos del profesional que está registrando la solicitud, como su nombre, establecimiento de trabajo. Si el profesional que está registrando la solicitud de toma de muestra trabaja en más de un establecimiento, debe indicar desde cuál de estos está realizando el procedimiento.

__Profesional responsable__ Ingresar los datos del profesional que solicita la toma de la muestra, como su RUN (sin punto y con guión) y cualquier otra información necesaria.

## Datos del paciente

![Alt text](img/datos_paciente_ag.png)

_Figura 4: Sección datos del Paciente_

__N° Epivigila__: En caso de que se trate de un caso notificado, se debe ingresar el número de epivigila

__Tipo de documento__: Actualmente PNTM cuenta con los siguientes métodos de registro asociados al tipo de documento del paciente registrado en Antígenos:
- Run
- Pasaporte
- Sin Documentación
- DNI
- Ficha Clínica
- Recién Nacido

Para ello, se detallan los posibles tipos de registro del tipo de documento y la jerarquía a utilizar en caso de no contar con algún tipo de documento.



| Paciente             | Identificador estándar | Alternativo                                                                                                      |
|:--------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------|
| Chilenos             | RUN definitivo         | Pasaporte: número; Ficha clínica: FC. + número; NO USAR RUN PROVISORIO                                            |
| Extranjeros          | RUN definitivo         | Pasaporte: número; DNI: DNI. + número (argentinos, peruanos, otros); Ficha clínica: FC. + número; NO USAR RUN PROVISORIO |
| Recién nacidos       | RUN definitivo         | Comprobante de parto: CP. + número; Ficha clínica: FC. + número; NO USAR RUN PROVISORIO                              |
| Otro tipo de paciente| Dinámico               | Fichas clínicas: FC. + número; DNI: DNI. + número (argentinos, peruanos, otros); NO USAR RUN PROVISORIO               |


*   Ciudadanos chilenos: Utilizar siempre como primera opción el __RUN__, independiente que sean viajeros que vienen del extranjero.
*   Extranjeros: Utilizar como primera opción el __RUN definitivo__ (si lo posee). En segundo lugar, el número de pasaporte y como última opción la Identificación local del sujeto.
*   Recién nacidos: Para realizar el registro de pacientes __recién nacidos__ la regla corresponde a registrar como primera instancia el RUN, luego si el recién nacido no cuenta con este registro se procede a registrar el número de parto o ficha de recién nacido.
*   Casos excepcionales: En que un caso no tenga ningún tipo de identificación y no entregue información al respecto, se podría utilizar, por ejemplo, el número del dato de atención de urgencia o ficha clínica, utilizando tipo documento = “__Ficha Clínica__”.

__Información del paciente__ Registrar los datos del paciente, su nombre completo, fecha de nacimiento, número de RUN o pasaporte y otros datos relevantes.

En caso de ingresar un RUN en la sección de datos del paciente, éste debe ser ingresado sin puntos y con dígito verificador. 

El botón __Obtener datos del paciente__ permite que el sistema autocomplete la información disponible en las bases de datos. Sin embargo, es importante que el profesional verifique todos estos datos directamente con el paciente.

A continuación, se detallan cada uno de los datos que deben ser ingresados en la sección de datos de paciente

| Columna          | Tipo de dato | Descripción                                               | Restricciones                                                                                            |
|:-----------------|:------------|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| N Epivigila      | Número      | Id Epivigila                                              | Opcional                                                                                                  |
| RUN o Pasaporte  | Texto       | Número de identificación del paciente                     | Obligatorio y válido en caso de ser RUN                                                                   |
| Tipo documento   | Texto       | RUN; PASAPORTE; DNI PAIS DE ORIGEN; SIN DOCUMENTACION; N° FICHA CLINICA | Obligatorio                                                                                     |
| Nombres          | Texto       | Nombres del paciente                                      | Obligatorio                                                                                     |
| Apellido paterno | Texto       | Apellido paterno del paciente                             | Obligatorio                                                                                     |
| Apellido materno | Texto       | Apellido Materno del paciente                             | Obligatorio, en caso de no poseer indicar: "."                                                         |
| Sexo             | Texto       | Sexo del paciente                                         | Obligatorio y solo podrá ser M, F, Intersex o Desconocido                                                |
| Dirección        | Texto       | Dirección del paciente                                     | Obligatorio, Ejemplo: Avenida El Bosque.                                                                 |
| Teléfono         | Número      | Número de teléfono del paciente                           | Obligatorio                                                                                              |
| Edad             | Número      | Edad del paciente                                         | Obligatorio                                                                                              |
| Comuna           | Texto       | Comuna del paciente                                        | Obligatorio, Debe ser una comuna valida del listado                                                      |
| N Residencia     | Texto       | Numero de identificador de la calle/avenida                | Obligatorio, Ejemplo: 130                                                                                |
| Dpto. Residencia | Texto       | Numero de identificador del dpto. casa del paciente        | Opcional, Ejemplo: 22A                                                                                    |
| Población, Villa | Texto       | Población de residencia del paciente                       | Opcional, Ejemplo: Villa Magisterio                                                                       |
| Vía Residencia   | Texto       | Tipo de vía residencia del paciente                        | Obligatorio, Debe ser una vía valida del listado                                                          |
| Paciente mail    | Texto       | Dirección de correo electrónico                           | Obligatorio                                                                                              |


## Datos de la muestra y resultado

![datos_muestra_resultado_ag](img/datos_muestra_resultado_ag.png)

_Figura 5: Datos de la muestra y resultado_

El profesional deberá ingresar de forma obligatoria todos los campos indicados en asterisco, debiendo completar la información indicada en la siguiente tabla.

| Tipo de muestra | Texto | Descripción                                             | Restricciones                                                                                      |
|:----------------|:------|:--------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| Tipo de muestra  | Texto | Tórula nasofaríngea; Tórula Nasal                       | Obligatorio                                                                                         |
| Búsqueda activa  | Bool  | 0 = No; 1 = Sí                                          | Obligatorio                                                                                         |
| Resultado        | Texto | Positivo; Negativo; No concluyente                      | Obligatorio                                                                                         |
| Marca Test       | Texto | Marca de la prueba                                      | Obligatorio, debe ser una marca disponible en el listado de PNTM                                  |
| Fecha muestra    | Fecha | Fecha en que se crea la solicitud                       | Obligatorio                                                                                         |
| No ingresa al país | Bool  | 0 = Sí ingresa al país; 1 = No ingresa al país           | Obligatorio                                                                                         |


## Finalizar la creación del registro

![Alt text](img/botones_2_ag.png)

_Figura 6: botones Eliminar registro y Finalizar_

Se recomienda verificar los datos luego de haber realizado la lectura e interpretación de los resultados, para así completar el registro haciendo click en __Finalizar__

## Informe de resultado para test antígeno

Una vez finalizado, deberán subir en la plataforma y pinchar __“INFORME DE RESULTADO PARA TEST ANTIGENO”__ para descargar informe. 

Una vez pinchado se desplegará informe para que pueda ser impreso y firmado a mano alzada por profesional responsable del análisis de la muestra.