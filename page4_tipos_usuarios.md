---
layout: home
title: Usuarios
description: Documentación para Plataforma Nacional de Toma de muestras
nav_order: 4
---
- [Tipos de usuarios](#tipos-de-usuarios)
  - [Profesional Tomador de Muestras](#profesional-tomador-de-muestras)
  - [Establecimiento](#establecimiento)
  - [Comuna](#comuna)
  - [SEREMI](#seremi)
  - [Servicio de Salud](#servicio-de-salud)
  - [Laboratorio](#laboratorio)
- [Solicitud de Creación: Profesional Tomador de Muestra](#solicitud-de-creación-profesional-tomador-de-muestra)
- [Solicitud de Creación: Establecimientos o Unidades Tomadoras de Muestras (UTM) para qRT-PCR y Antígeno en PNTM](#solicitud-de-creación-establecimientos-o-unidades-tomadoras-de-muestras-utm-para-qrt-pcr-y-antígeno-en-pntm)
  - [Establecimientos o Unidades Tomadoras de Muestras (UTM) para qRT-PCR](#establecimientos-o-unidades-tomadoras-de-muestras-utm-para-qrt-pcr)
    - [Formulario de Datos Mínimos Requeridos](#formulario-de-datos-mínimos-requeridos)
  - [Establecimientos Tomadores de Test de Antígeno](#establecimientos-tomadores-de-test-de-antígeno)
    - [Formulario de Datos Mínimos Requeridos](#formulario-de-datos-mínimos-requeridos-1)
- [Solicitud de Creación: Laboratorios qRT-PCR para SARS-CoV-2 en PNTM](#solicitud-de-creación-laboratorios-qrt-pcr-para-sars-cov-2-en-pntm)
- [Proceso de creación de usuarios](#proceso-de-creación-de-usuarios)

# Tipos de usuarios
La plataforma de toma de muestra tiene como objetivo implementar un sistema de registro y trazabilidad de las muestras biológicas recolectadas en establecimientos de salud, para su procesamiento en laboratorios y la emisión de informes de diagnóstico para los pacientes. Para lograr esto, la plataforma cuenta con perfiles de usuario que permiten el registro y seguimiento de las muestras a lo largo del proceso de diagnóstico.

Los perfiles de usuario en la plataforma de toma de muestra se diferencian en tres áreas principales: búsqueda de muestras, descarga de reportes y alcance y visualización.

## Profesional Tomador de Muestras
Usuario encargado de recolectar la muestra biológica en el establecimiento de salud.
-   **Antígenos**
    -   El alcance de la información se restringe a las muestras que registró el profesional.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 11 días.
    -   Puede editar el resultado de una muestra de antígenos, siempre y cuando no hayan pasado más de 3 días.
    -   Si el profesional o el laboratorio necesitan realizar una modificación a una muestra, deben enviar una solicitud a la mesa de ayuda.
    -   No tiene acceso para descargar reportes.
-   **PCR**
    -   El alcance de la información se restringe a las muestras asociadas al profesional que las registró.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 14 días.
    -   Puede editar el registro siempre y cuando no haya enviado la muestra al laboratorio y no hayan pasado más de 12 días.
    -   Si el profesional o el laboratorio necesitan realizar una modificación a una muestra, deben enviar una solicitud a la mesa de ayuda.
    -   No tiene acceso para descargar reportes.

## Establecimiento
Lugar donde se realiza la toma de muestra y se gestionan las solicitudes de exámenes de los pacientes.
-   **Antígenos**
    -   El alcance de la información se restringe a las muestras que el profesional registró.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 11 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.
-   **PCR**
    -   El alcance de la información se restringe a las muestras asociadas al establecimiento.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 14 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.

## Comuna
Unidad administrativa local encargada de brindar servicios de salud a la comunidad.
-   **Antígenos**
    -   El alcance de la información se restringe a las muestras de la comuna.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 11 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.
-   **PCR**
    -   El alcance de la información se restringe a las muestras de la comuna.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 14 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.
## SEREMI
Secretaría Regional Ministerial de Salud encargada de coordinar y supervisar las acciones de salud en una región.
-   **Antígenos**
    -   El alcance de la información se restringe a las muestras de la región.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 11 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.
-   **PCR**
    -   El alcance de la información se restringe a las muestras asociadas a la región.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 14 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.

## Servicio de Salud
Organismo público encargado de coordinar y supervisar las acciones de salud en una región.
-   **Antígenos**
    -   El alcance de la información se restringe a las muestras del servicio.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 11 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.
-   **PCR**
    -   El alcance de la información se restringe a las muestras del servicio.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 14 días.
    -   No tiene permiso para modificar las muestras.
    -   Tiene acceso para descargar reportes de los últimos 120 días.

## Laboratorio
Lugar donde se procesan las muestras biológicas para realizar el diagnóstico de una enfermedad.
-   **PCR**
    -   El alcance de la información se restringe a las muestras asociadas al laboratorio.
    -   El usuario tiene acceso para visualizar las muestras registradas de los últimos 7 días.
    -   Puede aceptar, rechazar, devolver la muestra para cambio de laboratorio o devolverla al profesional.
    -   Puede editar el resultado hasta 7 días.
    -   Si se quiere editar una muestra, tiene que ser aprobada por la mesa de ayuda de PNTM y el laboratorio es el responsable de editar la información.
    -   Tiene acceso para descargar reportes de los últimos 120 días.

# Solicitud de Creación: Profesional Tomador de Muestra

Para registrarse como Profesional Tomador de Muestra en la Plataforma Nacional de Toma de Muestras (PNTM), es necesario completar el Formulario para Registro de Profesionales. El formulario se encuentra en el siguiente enlace: [https://docs.google.com/forms/d/e/1FAIpQLSePoFBV-LGbo8rSpjL4fozsjOkwEyv8xxCNAx7fjytnA-UVTQ/viewform](https://docs.google.com/forms/d/e/1FAIpQLSePoFBV-LGbo8rSpjL4fozsjOkwEyv8xxCNAx7fjytnA-UVTQ/viewform).

El formulario cuenta con los siguientes campos obligatorios para completar:

| Campo                        | Descripción                                                                                                                               |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Primer y segundo nombre      | Nombres del profesional que solicita acceso                                                                                               |
| Apellido paterno             | Apellido paterno del profesional que solicita acceso                                                                                      |
| Apellido materno             | Apellido materno del profesional que solicita acceso                                                                                      |
| Rut                          | Número de RUT del profesional sin puntos, guión y dígito verificador (Ejemplo: 11222333)                                                  |
| Dígito verificador           | Dígito verificador del RUT del profesional solicitante                                                                                    |
| Profesión                    | Profesión del profesional según lo indicado por la Superintendencia de Salud                                                              |
| Especialidad                 | Especialidad del profesional, ingresar información solo si cuenta con alguna                                                              |
| Registro SIS                 | Número de registro en la Superintendencia de Salud (SIS) válido. Si no se tiene, debe solicitarse información a mesadeayudapntm@minsal.cl |
| Fecha de obtención del grado | Fecha en que se obtuvo el grado del profesional solicitante según registro en el SIS                                                      |
| Correo electrónico           | Correo electrónico del profesional que solicita acceso, a través del cual se enviarán las instrucciones de acceso                         |
| Región                       | Región en la que se encuentra el centro de salud donde el profesional solicitante está desempeñándose.                                    |


Una vez completado el formulario, se debe esperar un máximo de 48 horas hábiles para que el acceso del usuario quede activado. Si pasado este tiempo, el usuario no puede ingresar a la plataforma, debe comunicarse con [mesadeayudapntm@minsal.cl](mailto:mesadeayudapntm@minsal.cl) o llamar al teléfono +56 9 99424751.

Es importante mencionar que solo se permitirá el acceso a la plataforma a aquellos profesionales que hayan completado y enviado el formulario de registro.

# Solicitud de Creación: Establecimientos o Unidades Tomadoras de Muestras (UTM) para qRT-PCR y Antígeno en PNTM

Los establecimientos tomadores de muestras para PCR o designados por Seremi de Salud para la toma de Test de Antígeno deben registrar en PNTM las muestras tomadas y, en el caso de Test Antígeno, el resultado una vez conocido.

## Establecimientos o Unidades Tomadoras de Muestras (UTM) para qRT-PCR

Para la creación de una unidad tomadora de muestras en PNTM, se debe seguir el siguiente proceso:

1.  Solicitud a Referente Macroregional correspondiente de Testeo - MINSAL, vía correo electrónico.
2.  Completar el [formulario de datos mínimos requeridos](/page5_creacion_usuarios_utm.md#formulario-de-datos-mínimos-requeridos) para la creación de Establecimiento/UTM .
3.  Toda la información requerida debe estar contenida en el formulario para evitar atrasos en el proceso.

Una vez recibida la información, el Referente Territorial de Testeo - MINSAL la validará y se creará el establecimiento/UTM de toma de qRT-PCR en un plazo de 24 horas. La respuesta será informada al correo electrónico del (la) profesional responsable de la solicitud, que debe ser indicado en el formulario.

### Formulario de Datos Mínimos Requeridos

| Campo                                                                   | Descripción                                                                                                                    |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Nombre Unidad Tomadora de Muestras                                      | Nombre completo del establecimiento en base a DEIS. En caso de no tener un código DEIS, indicar nombre específico.             |
| Código DEIS                                                             | Código designado por DEIS para registro de producción. Si no cuenta con código DEIS, indicar que "no cuenta con cod deis".     |
| Publico/Privado                                                         | Descripción del tipo de establecimiento, indicando si es "Público" o "Privado".                                                |
| Servicio de Salud                                                       | Descripción del servicio de salud a que corresponde por asignación territorial de la comuna en donde se encuentra establecido. |
| N° de Resolución Sanitaria y adjunto de Res.                            | Resolución sanitaria que acredita al establecimiento como tomador de muestras autorizado.                                      |
| Fecha de Resolución Sanitaria Región                                    | Fecha de la resolución indicada previamente.                                                                                   |
| Región  | Región donde se encuentra ubicada la unidad tomadora de muestras.                                                              |
| Comuna  | Comuna donde se encuentra ubicada la unidad tomadora de muestras.                                                              |
| Dirección                                                               | Dirección física de la unidad tomadora de muestras.                                                                            |
| Correo electrónico                                                      | Correo electrónico del encargado de la solicitud de creación para informar la posterior creación efectiva.                     |
| Celular Institucional o Anexo MINSAL                                    | Teléfono de contacto para abordar dudas o datos faltantes.                                                                     |

## Establecimientos Tomadores de Test de Antígeno

Para la creación de una unidad tomadora de test de antigeno en PNTM, se debe seguir el siguiente proceso:

1.  Solicitud a Referente Macroregional correspondiente de Testeo - MINSAL, vía correo electrónico.
2.  Completar el formulario de datos mínimos requeridos para la creación de Establecimiento/UTM .
3.  Toda la información requerida debe estar contenida en el formulario para evitar atrasos en el proceso.

Una vez recibida la información, el Referente Territorial de Testeo - MINSAL la validará y se creará el establecimiento/UTM de toma de qRT-PCR o Test de Antígeno en un plazo de 24 horas. La respuesta será informada al correo electrónico del (la) profesional responsable de la solicitud, que debe ser indicado en el formulario.

### Formulario de Datos Mínimos Requeridos

| Dato requerido                                             | Descripción                                                                                                                      |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Nombre Unidad Tomadora de Muestras                         | Nombre completo del establecimiento en base a DEIS. Si no está disponible, indicar nombre específico según resolución sanitaria. |
| Código DEIS                                                | Código designado por DEIS para registro de producción. Si no tiene código DEIS, especificar en el campo correspondiente.         |
| Público/Privado                                            | Descripción del tipo de establecimiento, indicando si es "Público" o "Privado".                                                  |
| Servicio de Salud                                          | Descripción del servicio de salud al que corresponde según asignación territorial de la comuna donde se encuentra establecido.   |
| N° de resolución de Designación SEREMI de Salud - adjuntar | Resolución sanitaria que acredita al establecimiento como tomador de muestras autorizado para realizar test de antígenos.        |
| Fecha de Resolución de Designación SEREMI de Salud         | Fecha de la resolución indicada previamente.                                                                                     |
| Región                                                     | Región en donde se encuentra establecida la unidad tomadora de muestras.                                                         |
| Comuna                                                     | Comuna en donde se encuentra establecida la unidad tomadora de muestras.                                                         |
| Dirección                                                  | Dirección física de la unidad tomadora de muestras.                                                                              |
| Correo electrónico                                         | Correo electrónico del encargado de la solicitud de creación, para informar la posterior creación efectiva.                      |
| Celular Institucional o Anexo MINSAL                       | Teléfono de contacto para abordar dudas o datos faltantes.                                                                       |

Una vez recibida la información, el Referente Territorial de Testeo - MINSAL la validará y se creará el establecimiento/UTM de toma de Test de Antígeno en un plazo de 24 horas. La respuesta será informada al correo electrónico del (la) profesional responsable de la solicitud, que debe ser indicado en el formulario.

# Solicitud de Creación: Laboratorios qRT-PCR para SARS-CoV-2 en PNTM

Es importante registrar en PNTM la fase analítica y el resultado obtenido a través de técnicas de biología molecular. Por esta razón, todo laboratorio que cuente con Resolución Sanitaria emitida por SEREMI de Salud y con el Certificado de Capacidad Diagnóstica correspondiente para realizar técnicas de Biología Molecular por la técnica PCR, otorgado por el ISP, debe estar habilitado para registrar sus resultados en el sistema.

Para habilitar el registro de resultados, los laboratorios debe realizar una solicitud por correo electrónico al Referente Macroregional de Testeo del MINSAL correspondiente, para la creación del Laboratorio en PNTM. Para ello, se debe completar el siguiente formulario con los datos mínimos requeridos:

| Campo                                             | Descripción                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre del Laboratorio                            | Nombre del laboratorio, indicando el mismo nombre descrito en la Resolución Sanitaria.                                                            |
| Tipo de Laboratorio                               | Descripción del tipo de laboratorio, indicando si es "Público", "Privado" o "Universitario".                                                      |
| Servicio de Salud                                 | Descripción del servicio de salud al que corresponde el laboratorio, según la asignación territorial de la comuna donde se encuentra establecido. |
| N° de Resolución Sanitaria SEREMI de Salud        | Resolución sanitaria que acredita al laboratorio para procesamiento de muestras de PCR, adjuntar una copia.                                       |
| Fecha de Resolución Sanitaria SEREMI de Salud     | Fecha de la resolución indicada previamente.                                                                                                      |
| N° de Certificado de Capacidad Diagnóstica ISP    | Certificado de capacidad diagnóstica otorgado por el Instituto de Salud Pública, adjuntar una copia.                                              |
| Fecha de Certificado de Capacidad Diagnóstica ISP | Fecha de la resolución indicada previamente.                                                                                                      |
| Región                                            | Región donde se encuentra establecido el laboratorio.                                                                                             |
| Comuna                                            | Comuna donde se encuentra establecido el laboratorio.                                                                                             |
| Dirección                                         | Dirección física del laboratorio.                                                                                                                 |
| Correo electrónico                                | Correo electrónico del encargado de la solicitud de creación, para informar sobre la posterior creación efectiva.                                 |
| Celular Institucional o Anexo MINSAL              | Teléfono de contacto para abordar dudas o datos faltantes.                                                                                        |

Toda la información requerida en el formulario será validada por el Referente Territorial de Testeo del MINSAL. Para evitar retrasos en el proceso, es importante que el formulario esté completo y que contenga toda la información necesaria.

Una vez recibida la información, el Referente Territorial de Testeo - MINSAL la validará y se creará el establecimiento/UTM de toma de Test de Antígeno en un plazo de 24 horas. La respuesta será informada al correo electrónico del (la) profesional responsable de la solicitud, que debe ser indicado en el formulario.

# Proceso de creación de usuarios

El proceso de creación de muestras por parte del equipo del MINSAL se realiza de la siguiente manera:

1.  Recepción de la solicitud de creación por parte del equipo del MINSAL.
2.  Canalización de la solicitud con el referente territorial de testeo asignado según la macrozona correspondiente.
3.  Validación de los datos mínimos requeridos para la creación del establecimiento o laboratorio.
4.  Información vía correo electrónico al solicitante por el referente de testeo correspondiente en caso de faltar datos o si la solicitud es impertinente.
5.  Aprobación de la solicitud si cumple con todos los requisitos.
6.  Envío de la solicitud a la mesa de ayuda, la cual tiene un plazo de 24 horas para crear la solicitud correspondiente.
7.  Información vía correo electrónico al solicitante, con copia al referente de testeo correspondiente, sobre la inclusión del establecimiento o laboratorio.