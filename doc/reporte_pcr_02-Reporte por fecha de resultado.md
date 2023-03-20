---
layout: default
title: Reporte por Fecha de Resultado
nav_order: 2
grand_parent: Reportes
parent: Reportes - PCR
has_children: false
has_toc: true
---

# Reporte por Fecha de Resultado

El Reporte por Fecha de Resultado es una herramienta que permite obtener información sobre las muestras de prueba que han sido procesadas y que disponen de un resultado entregado. Este reporte solo entrega datos de las muestras que se encuentran en `estado_muestra` 4, es decir, aquellas que han sido procesadas y disponen de un resultado, considerando que las fechas corresponden a la fecha de resultado de la muestra.

## Acceso al reporte por fecha de resultado

Para acceder al reporte por fecha de resultado, siga estos pasos:

1. Ingrese a la interfaz de usuario del sistema.
2. Haga clic en la opción de "Reportes".
3. Seleccione el submenú de "PCR".
4. Seleccione la opción de "Por fecha de resultado".
5. Establezca las fechas "DESDE" y "HASTA" para definir el rango de tiempo que desea incluir en el reporte, correspondiente a la fecha en que se obtuvo el resultado de la muestra. Si no asigna fechas, el sistema tomará automáticamente la fecha y hora actual como punto de partida y finalización.
6. Si el período de tiempo que selecciona es mayor a 7 días (fecha desde y fecha hasta), el sistema no descargará datos.
7. Una vez que ingrese las fechas requeridas, el reporte por fecha de resultado se generará automáticamente y se descargará en formato Excel.

![Alt text](img/Reporte-PCR-Resultado.jpg)
_Figura 1: Reporte por Fecha de Resultado_