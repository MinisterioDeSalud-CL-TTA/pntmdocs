---
layout: default
title: Laboratorio
nav_order: 6
parent: Reportes
has_children: true
has_toc: true
---
# Reportes laboratorios
{: .no_toc }

## Tabla de contenido
{: .no_toc .text-delta }
1. TOC
{:toc}

La siguiente tabla  proporciona información sobre los diferentes reportes que se pueden generar en la Plataforma Nacional de Toma de Muestra (PNTM) y los campos asociados a cada uno de ellos. Los reportes se generan a partir de los datos recopilados en la PNTM y permiten obtener información relevante sobre las muestras de prueba procesadas y sus respectivos resultados.


| Reporte                                          | Campo                              | Descripción                                                                                                          |
|--------------------------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Global de solicitudes                            | Fecha toma de muestra              | Muestra todas las muestras en el rango de fechas seleccionado                                                        |
| Por fecha de resultado                           | Fecha de resultado                 | Muestra solo las muestras con resultados en el estado 4 dentro del rango de fechas seleccionado                      |
| Reporte ministerial                              | Fecha reportada por el laboratorio | Muestra las muestras en el estado 4 reportadas por el laboratorio dentro del rango de fechas seleccionado            |
| Reporte Mutación por fecha de derivación         | Fecha de derivación                | Muestra las muestras en estado 7, es decir, las que fueron enviadas a mutaciones, en el rango de fechas seleccionado |
| Reporte Mutación por fecha de carga de resultado | Fecha carga de resultado           | Muestra las muestras en estado 8, es decir, las que tienen resultado de mutación, en el rango de fechas seleccionado |

Cada reporte se puede generar para un rango de fechas específico y se enfoca en diferentes aspectos de las muestras de prueba. Por ejemplo, el reporte global de solicitudes muestra todas las muestras en un rango de fechas determinado, mientras que el reporte por fecha de resultado solo incluye las muestras con resultados en el estado 4 dentro del mismo rango de fechas. Los otros reportes incluyen información sobre las muestras en estado 7 y 8, las que fueron enviadas a mutaciones y las que tienen resultados de mutación, respectivamente.

Cada reporte incluye diferentes campos de información, como la fecha de toma de muestra, la fecha de resultado, la fecha reportada por el laboratorio, entre otros, lo que permite obtener una visión detallada de las muestras procesadas y sus resultados.

# Reporte Glogal de soliciudes

La Plataforma Nacional de Toma de Muestra (PNTM) es un sistema diseñado para recopilar información sobre muestras de pruebas de diagnóstico, como las pruebas PCR y de antígenos, realizadas en establecimientos de salud pública en todo el país.

El reporte global de solicitudes es una herramienta que permite a los usuarios obtener información sobre las muestras de prueba realizadas en la PNTM. Para generar este informe, los usuarios deben asignar una fecha de inicio (DESDE) y una fecha de finalización (HASTA) que correspondan a la fecha de toma de muestra.

Es importante destacar que si el usuario no asigna ninguna fecha, el sistema tomará automáticamente la fecha y hora actual como el punto de partida y finalización para la generación del reporte.

El reporte global de solicitudes proporciona información detallada sobre el número total de muestras de prueba realizadas en la PNTM durante el período de tiempo especificado. Esto permite a los usuarios obtener información más específica sobre la distribución de muestras.

El reporte generado por la Plataforma Nacional de Toma de Muestra (PNTM) contiene información detallada sobre las muestras de prueba de diagnóstico, como las pruebas PCR y de antígenos, realizadas en establecimientos de salud pública en todo el país. A continuación se describen los campos que se incluyen en el reporte:

-   `id_muestra`: un número único que identifica a cada muestra de prueba.
-   `estado_muestra`: el estado actual de la muestra de prueba (ej. si se encuentra en proceso de análisis o ya se tiene un resultado disponible).
-   `estado_muestra_significado`: una descripción del significado del estado de la muestra de prueba.

| Estado de muestra | Descripción                                                                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                 | La muestra de prueba se encuentra en proceso de creación y aún no se ha enviado al laboratorio.                                                                                                                                                             |
| 2                 | La muestra de prueba ha sido enviada al laboratorio para su procesamiento.                                                                                                                                                                                  |
| 3                 | La muestra de prueba ha sido recepcionada por el laboratorio y se encuentra en proceso de análisis.                                                                                                                                                         |
| 4                 | La muestra de prueba ha sido procesada y se dispone de un resultado.                                                                                                                                                                                        |
| 5                 | La muestra de prueba se encuentra en proceso de modificación, es decir, se está realizando alguna corrección o actualización de la información asociada a la muestra.                                                                                       |
| 6                 | La muestra de prueba ha sido rechazada y no es apta para su procesamiento.                                                                                                                                                                                  |
| 7                 | La muestra de prueba ha sido enviada a mutaciones para su análisis y seguimiento.                                                                                                                                                                           |
| 8                 | La muestra de prueba ha sido procesada en mutaciones y se dispone de un resultado de la mutación.                                                                                                                                                           |
| 9                 | La muestra de prueba se encuentra en un estado de edición autorizada, es decir, se ha dado permiso a un usuario específico para realizar modificaciones en la información asociada a la muestra. Este estado se utiliza para evitar cambios no autorizados. |

-   `nombre_profesional`, `rut_profesional`, `titulo_profesional`, `especialidad_profesional`: información sobre el profesional de salud que tomó la muestra de prueba.
-   `profesional_solicitante`, `rut_profesional_solicitante`: información sobre el profesional de salud que solicitó la toma de muestra.
-   `tipo_documento_paciente`, `id_paciente`: información sobre el paciente al que se le realizó la prueba.
-   `pais_origen_paciente`, `nombre_paciente`, `apellido_paterno_paciente`, `apellido_materno_paciente`, `fecha_nacimiento_paciente`, `edad_paciente`, `comuna_paciente`, `dirección_paciente`, `telefono_paciente`, `paciente_email`, `sexo_paciente`, `prevision_paciente`: información personal y médica del paciente al que se le realizó la prueba.
-   `laboratorio`, `tipo_laboratorio`, `codigo_servicio_salud_laboratorio`, `servicio_salud_laboratorio`: información sobre el laboratorio que procesó la muestra de prueba.
-   `establecimiento`, `fecha_toma_muestra`, `hora_muestra`, `tecnica_muestra`, `resultado`, `tipo_muestra`, `codigo_servicio_salud_establecimiento`, `servicio_salud_establecimiento`: información sobre el establecimiento de salud donde se realizó la toma de muestra, así como detalles sobre la técnica utilizada para la prueba y los resultados obtenidos.
-   `epivigila`: información sobre el sistema de vigilancia epidemiológica utilizado para el seguimiento de los casos.
-   `fecha_recepcion_muestra`, `hora_recepcion`, `fecha_resultado_muestra`, `hora_resultado`: información sobre la fecha y hora de recepción de la muestra y la fecha y hora de los resultados obtenidos.
-   `busqueda_activa` es un campo que indica si la muestra de prueba se realizó como parte de una búsqueda activa de casos (BAC). Si el valor de este campo es "VERDADERO", significa que la muestra se tomó como parte de un operativo BAC, mientras que si es "FALSO", significa que la muestra se tomó por otra razón.
- `tiposolicitud`, `codigo_muestra_cliente`, `fecha_informada_recepcion_laboratorio`, `hora_informada_recepcion_laboratorio`, `fecha_informada_resultado_laboratorio`, `hora_informada_resultado_laboratorio`, `fecha_creacion`, `tipo_establecimiento`, `estrategia`, `subestrategia`: información adicional sobre la muestra de prueba, como el tipo de búsqueda utilizada para la detección de casos y la estrategia de atención médica utilizada.

En resumen, el reporte global de solicitudes de la PNTM es una herramienta importante para obtener información sobre las muestras de prueba realizadas en establecimientos de salud pública en todo el país. Los usuarios pueden utilizar este informe para analizar la distribución de muestras de prueba en diferentes áreas geográficas y tipos de establecimientos de salud, lo que puede ayudar a informar la toma de decisiones en materia de salud pública.


# Reporte por fecha de resultado

El Reporte por Resultado es una herramienta que permite obtener información sobre las muestras de prueba que han sido procesadas y que disponen de un resultado entregado. Este reporte solo entrega datos de las muestras que se encuentran en estado_muestra 4, es decir, aquellas que han sido procesadas y disponen de un resultado. Para acceder a este reporte, se deben seguir las siguientes instrucciones:

1.  Asignar una fecha desde y una fecha hasta: Se debe indicar un rango de fechas que determine el periodo para el cual se desea obtener el reporte. Las fechas corresponden a la fecha de toma de la muestra. Si no se asigna ninguna fecha, el sistema tomará por defecto el día y la hora actuales.
2.  Verificar el periodo de fechas: Es importante tener en cuenta que si el periodo de fechas es mayor a 7 días, no se descargarán datos. Para obtener información sobre un periodo más amplio, se pueden generar varios reportes con diferentes periodos de fechas.

El reporte generado por la Plataforma Nacional de Toma de Muestra (PNTM) contiene información detallada sobre las muestras de prueba de diagnóstico, como las pruebas PCR y de antígenos, realizadas en establecimientos de salud pública en todo el país. A continuación se describen los campos que se incluyen en el reporte:

-   `id_muestra`: un número único que identifica a cada muestra de prueba.
-   `estado_muestra`: el estado actual de la muestra de prueba (ej. si se encuentra en proceso de análisis o ya se tiene un resultado disponible).
-   `estado_muestra_significado`: una descripción del significado del estado de la muestra de prueba.

| Estado de muestra | Descripción                                                                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4                 | La muestra de prueba ha sido procesada y se dispone de un resultado.                                                                                                                                                                                        |

-   `nombre_profesional`, `rut_profesional`, `titulo_profesional`, `especialidad_profesional`: información sobre el profesional de salud que tomó la muestra de prueba.
-   `profesional_solicitante`, `rut_profesional_solicitante`: información sobre el profesional de salud que solicitó la toma de muestra.
-   `tipo_documento_paciente`, `id_paciente`: información sobre el paciente al que se le realizó la prueba.
-   `pais_origen_paciente`, `nombre_paciente`, `apellido_paterno_paciente`, `apellido_materno_paciente`, `fecha_nacimiento_paciente`, `edad_paciente`, `comuna_paciente`, `dirección_paciente`, `telefono_paciente`, `paciente_email`, `sexo_paciente`, `prevision_paciente`: información personal y médica del paciente al que se le realizó la prueba.
-   `laboratorio`, `tipo_laboratorio`, `codigo_servicio_salud_laboratorio`, `servicio_salud_laboratorio`: información sobre el laboratorio que procesó la muestra de prueba.
-   `establecimiento`, `fecha_toma_muestra`, `hora_muestra`, `tecnica_muestra`, `resultado`, `tipo_muestra`, `codigo_servicio_salud_establecimiento`, `servicio_salud_establecimiento`: información sobre el establecimiento de salud donde se realizó la toma de muestra, así como detalles sobre la técnica utilizada para la prueba y los resultados obtenidos.
-   `epivigila`: información sobre el sistema de vigilancia epidemiológica utilizado para el seguimiento de los casos.
-   `fecha_recepcion_muestra`, `hora_recepcion`, `fecha_resultado_muestra`, `hora_resultado`: información sobre la fecha y hora de recepción de la muestra y la fecha y hora de los resultados obtenidos.
-   `busqueda_activa` es un campo que indica si la muestra de prueba se realizó como parte de una búsqueda activa de casos (BAC). Si el valor de este campo es "VERDADERO", significa que la muestra se tomó como parte de un operativo BAC, mientras que si es "FALSO", significa que la muestra se tomó por otra razón.
- `tiposolicitud`, `codigo_muestra_cliente`, `fecha_informada_recepcion_laboratorio`, `hora_informada_recepcion_laboratorio`, `fecha_informada_resultado_laboratorio`, `hora_informada_resultado_laboratorio`, `fecha_creacion`, `tipo_establecimiento`, `estrategia`, `subestrategia`: información adicional sobre la muestra de prueba, como el tipo de búsqueda utilizada para la detección de casos y la estrategia de atención médica utilizada.

En resumen, el reporte por resultado de solicitudes de la PNTM es una herramienta importante para obtener información sobre las muestras de prueba realizadas en establecimientos de salud pública en todo el país. Los usuarios pueden utilizar este informe para analizar la distribución de muestras de prueba en diferentes áreas geográficas y tipos de establecimientos de salud, lo que puede ayudar a informar la toma de decisiones en materia de salud pública.

# Reporte ministerial

# Reporte Mutación por fecha de derivación

El Reporte Mutación por fecha de derivación es un informe generado por la Plataforma Nacional de Toma de Muestra (PNTM) que proporciona información detallada sobre las muestras de prueba que fueron enviadas a mutaciones. Este informe se enfoca en las muestras en estado 7, es decir, aquellas que fueron enviadas a mutaciones para su análisis.

Para generar este informe, es necesario especificar un rango de fechas que corresponda al período en el que se derivaron las muestras. El informe incluirá todas las muestras que se encuentren en el estado 7 dentro del rango de fechas especificado.

El Reporte Mutación por fecha de derivación permite obtener información detallada sobre las muestras de prueba que fueron enviadas a mutaciones, lo que puede ser útil para el monitoreo de la propagación de variantes del virus.

# Reporte Mutación por fecha de carga de resultado

El Reporte Mutación por fecha de carga de resultado es un informe generado por la Plataforma Nacional de Toma de Muestra (PNTM) que proporciona información detallada sobre las muestras de prueba que tienen resultados de mutación. Este informe se enfoca en las muestras en estado 8, es decir, aquellas que tienen resultados de mutación.

Para generar este informe, es necesario especificar un rango de fechas que corresponda al período de fecha de resultado. El informe incluirá todas las muestras que se encuentren en el estado 8 dentro del rango de fechas especificado.

El Reporte Mutación por fecha de carga de resultado permite obtener información detallada sobre las muestras de prueba que tienen resultados de mutación, lo que puede ser útil para el monitoreo de la propagación de variantes del virus.

# Documentación del Reporte de Resultados Acumulados RT

Este reporte presenta información sobre el número de muestras acumuladas, muestras acumuladas positivas y alerta de cuello de botella. A continuación se detallan las instrucciones para su uso:
- Se deben asignar la fecha, y el sistema mostrará los resultados acumulados para ese dia.

## Contenido del reporte

El reporte se divide en cuatro secciones:

1.  **Resultados Acumulados:** Esta sección muestra el número total de muestras acumuladas y el número de muestras positivas hasta la fecha indicada en el reporte. Además, se indica si hay una alerta de cuello de botella en el proceso.

2.  **Resultados obtenidos del sistema:** Esta sección muestra información sobre el stock en espera, el número de muestras recibidas y procesadas en el día, el stock final, la capacidad máxima y la tasa de ocupación del día. También se muestra el número de muestras positivas obtenidas en el día.

3.  **Resultados tributados por laboratorio:** En esta sección se presenta información similar a la sección anterior, pero se detalla por laboratorio.

4.  **Diferencias:** Esta sección muestra las diferencias entre los resultados obtenidos del sistema y los resultados tributados por laboratorio.

# Documentación de Tributación Manual del Reporte RT

El siguiente es un informe de tributación manual del Reporte RT, el cual presenta información correspondiente a la fecha de tributo del laboratorio y el stock de muestras en espera, recibidas, procesadas y final, junto con la capacidad máxima y la tasa de ocupación diaria. También se incluyen las muestras positivas del día y las muestras acumuladas y acumuladas positivas.

-   La fecha de tributo del laboratorio se debe ingresar manualmente en formato dd-mm-yyyy.
-   Se deben ingresar manualmente los valores correspondientes a stock espera, muestras recibidas día, muestras procesadas día, stock final, capacidad máxima y muestras positivas día.
-   El valor de tasa de ocupación día se calcula automáticamente al ingresar los valores de capacidad máxima y muestras procesadas día.
-   Los valores de muestras acumuladas y muestras acumuladas positivas se obtienen de forma automática desde el reporte RT.
-   Se puede incluir información adicional según sea necesario.

# Reporte RT - Descarga detalle 7 dias

Este reporte presenta información relevante sobre el procesamiento y resultados de muestras en el laboratorio en los últimos 7 días, permitiendo una mejor gestión y monitoreo de la capacidad y efectividad del laboratorio en la detección del virus.

| Columna                            | Descripción                                                                                                                                                                      |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fecha_x_1                          | Día anterior a la fecha de resultado informado en reporte RT.                                                                                                                    |
| fecha_x                            | Fecha de resultado informado en reporte RT.                                                                                                                                      |
| stock_espera_inf_pntm              | Muestras recepcionadas, pero sin procesar pendientes del día anterior a la fecha de resultado informado, considerando la fecha de recepción indicada por el laboratorio en PNTM. |
| muestras_recibidas_dia_inf_pntm    | Muestras recibidas el día de la fecha de resultado informado, considerando la fecha de recepción indicada por el laboratorio en PNTM.                                            |
| stock_espera_sist_pntm             | Muestras recepcionadas, pero sin procesar pendientes del día anterior a la fecha de resultado informado, considerando la fecha de recepción indicada por el sistema en PNTM.     |
| muestras_recibidas_dia_sist_pntm   | Muestras recibidas el día de la fecha de resultado informado, considerando la fecha de recepción indicada por el sistema en PNTM.                                                |
| muestras_procesadas_dia_pntm       | Muestras procesadas por el laboratorio el día de la fecha de resultado informado en PNTM.                                                                                        |
| stock_final_inf_pntm               | Stock final de muestras en espera o no procesadas el día de la fecha de resultado informado, considerando la fecha de recepción indicada por el laboratorio en PNTM.             |
| stock_final_sist_pntm              | Stock final de muestras en espera o no procesadas el día de la fecha de resultado informado, considerando la fecha de recepción indicada por el sistema en PNTM.                 |
| tasa_ocupacion_dia_pntm            | Stock Final informado en PNTM / Capacidad máxima de procesamiento informada por el laboratorio en PNTM.                                                                          |
| muestras_positivas_dia_pntm        | Muestras procesadas con resultado positivo el día de la fecha de resultado informado en PNTM.                                                                                    |
| stock_espera_trib                  | Muestras efectivamente recepcionadas en RT, pero sin procesar pendientes del día anterior a la fecha de resultado informado, considerando información del LIS del laboratorio.   |
| muestras_recibidas_dia_trib        | Muestras efectivamente recibidas en RT el día de la fecha de resultado informado, considerando información del LIS del laboratorio.                                              |
| muestras_procesadas_dia_trib       | Muestras efectivamente procesadas por el laboratorio el día de la fecha de resultado informado en RT, considerando información del LIS del laboratorio.                          |
| stock_final_trib                   | Stock final de muestras efectivamente en espera o no procesadas el día de la fecha de resultado informado en RT, considerando información del LIS del laboratorio.               |
| capacidad_max_trib                 | Capacidad máxima de procesamiento informada por el laboratorio en RT.                                                                                                            |
| tasa_ocupacion_dia_trib            | Stock Final informado en RT/ Capacidad máxima de procesamiento informada por el laboratorio en RT.                                                                               |
| muestras_positivas_dia_trib        | Muestras procesadas con resultado positivo el día de la fecha de resultado informado en RT, considerando información del LIS del laboratorio.                                    |
| muestras_acumuladas_trib           | Muestras acumuladas históricas informadas por el laboratorio en RT.                                                                                                              |
| muestras_acumuladas_positivas_trib | Muestras positivas acumuladas históricas informadas por el laboratorio en RT.                                                                                                    |
| alerta_cuello_botella_trib         | Información de insumos críticos o potenciales quiebres de stock informados por el laboratorio en RT.                                                                             |

Este reporte permite una mejor comprensión y seguimiento del trabajo del laboratorio en los últimos 7 días, lo que es vital para tomar decisiones en cuanto a la gestión y planificación de recursos para la detección del virus.
