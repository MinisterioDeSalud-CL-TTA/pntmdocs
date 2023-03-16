---
layout: default
title: Reporte por fecha de resultado
nav_order: 2
grand_parent: Reportes
parent: Reportes - SEREMI, Servicio de salud y perfil visualizador
has_children: false
has_toc: true
---


# Reporte por fecha de resultado

El Reporte por Resultado es una herramienta que permite obtener información sobre las muestras de prueba que han sido procesadas y que disponen de un resultado entregado. Este reporte solo entrega datos de las muestras que se encuentran en estado_muestra 4, es decir, aquellas que han sido procesadas y disponen de un resultado. Para acceder a este reporte, se deben seguir las siguientes instrucciones:

Para generar el reporte de solicitudes de PCR, sigue estas instrucciones:

- Ingresa a la interfaz de usuario del sistema.
- Haz clic en la opción de "Reportes".
- Selecciona el submenú de "PCR".
- Selecciona la opción de "Por fecha de resultado".
- Se te pedirá que especifiques un rango de fechas para el reporte. Asegúrate de seleccionar una "fecha desde" y una "fecha hasta". Estas fechas corresponden a la fecha en que se tomó la muestra.
- Si no asignas ninguna fecha, el sistema tomará por defecto el día y la hora actual.
- Si el periodo de tiempo que seleccionas es mayor a 7 días (fecha desde y fecha hasta), el sistema no descargará datos.
- Una vez que ingreses las fechas requeridas, el reporte global de solicitudes de PCR se generará automáticamente y se descargará en formato excel


![Alt text](img/Reporte-PCR.jpg)

_Reporte Por fecha de resultado_

El reporte generado por la Plataforma Nacional de Toma de Muestra (PNTM) contiene información detallada sobre las muestras de prueba de diagnóstico, como las pruebas PCR y de antígenos, realizadas en establecimientos de salud pública en todo el país. A continuación se describen los campos que se incluyen en el reporte:

- `id_muestra`: un número único que identifica a cada muestra de prueba.
- `estado_muestra`: el estado actual de la muestra de prueba (ej. si se encuentra en proceso de análisis o ya se tiene un resultado disponible).
- `estado_muestra_significado`: una descripción del significado del estado de la muestra de prueba.

- `nombre_profesional`, `rut_profesional`, `titulo_profesional`, `especialidad_profesional`: información sobre el profesional de salud que tomó la muestra de prueba.
- `profesional_solicitante`, `rut_profesional_solicitante`: información sobre el profesional de salud que solicitó la toma de muestra.
- `tipo_documento_paciente`, `id_paciente`: información sobre el paciente al que se le realizó la prueba.
- `pais_origen_paciente`, `nombre_paciente`, `apellido_paterno_paciente`, `apellido_materno_paciente`, `fecha_nacimiento_paciente`, `edad_paciente`, `comuna_paciente`, `dirección_paciente`, `telefono_paciente`, `paciente_email`, `sexo_paciente`, `prevision_paciente`: información personal y médica del paciente al que se le realizó la prueba.
- `laboratorio`, `tipo_laboratorio`, `codigo_servicio_salud_laboratorio`, `servicio_salud_laboratorio`: información sobre el laboratorio que procesó la muestra de prueba.
- `establecimiento`, `fecha_toma_muestra`, `hora_muestra`, `tecnica_muestra`, `resultado`, `tipo_muestra`, `codigo_servicio_salud_establecimiento`, `servicio_salud_establecimiento`: información sobre el establecimiento de salud donde se realizó la toma de muestra, así como detalles sobre la técnica utilizada para la prueba y los resultados obtenidos.
- `epivigila`: información sobre el sistema de vigilancia epidemiológica utilizado para el seguimiento de los casos.
- `fecha_recepcion_muestra`, `hora_recepcion`, `fecha_resultado_muestra`, `hora_resultado`: información sobre la fecha y hora de recepción de la muestra y la fecha y hora de los resultados obtenidos.
- `busqueda_activa` es un campo que indica si la muestra de prueba se realizó como parte de una búsqueda activa de casos (BAC). Si el valor de este campo es "VERDADERO", significa que la muestra se tomó como parte de un operativo BAC, mientras que si es "FALSO", significa que la muestra se tomó por otra razón.
- `tiposolicitud`, `codigo_muestra_cliente`, `fecha_informada_recepcion_laboratorio`, `hora_informada_recepcion_laboratorio`, `fecha_informada_resultado_laboratorio`, `hora_informada_resultado_laboratorio`, `fecha_creacion`, `tipo_establecimiento`, `estrategia`, `subestrategia`: información adicional sobre la muestra de prueba, como el tipo de búsqueda utilizada para la detección de casos y la estrategia de atención médica utilizada.

En resumen, el reporte por resultado de solicitudes de la PNTM es una herramienta importante para obtener información sobre las muestras de prueba realizadas en establecimientos de salud pública en todo el país. Los usuarios pueden utilizar este informe para analizar la distribución de muestras de prueba en diferentes áreas geográficas y tipos de establecimientos de salud, lo que puede ayudar a informar la toma de decisiones en materia de salud pública.