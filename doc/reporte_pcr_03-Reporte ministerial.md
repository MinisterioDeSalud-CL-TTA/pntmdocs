---
layout: default
title: Reporte Ministerial
nav_order: 3
grand_parent: Reportes
parent: Reportes - PCR
has_children: false
has_toc: true
---

# Reporte Ministerial

El Reporte Ministerial es una herramienta que permite obtener información sobre las muestras de prueba que han sido procesadas y que disponen de un resultado entregado. Este reporte solo entrega datos de las muestras que se encuentran en `estado_muestra` 4, es decir, aquellas que han sido procesadas y disponen de un resultado, considerando que las fechas corresponden a la fecha de toma de la muestra.

## Acceso al reporte ministerial

Para generar el Reporte Ministerial, siga estos pasos:

1. Ingrese a la interfaz de usuario del sistema.
2. Haga clic en la opción de "Reportes".
3. Seleccione el submenú de "PCR".
4. Seleccione la opción de "Reporte Ministerial".
5. Establezca las fechas "DESDE" y "HASTA" para definir el rango de tiempo que desea incluir en el reporte, correspondiente a la fecha en que se tomó la muestra. Si no asigna fechas, el sistema tomará automáticamente la fecha y hora actual como punto de partida y finalización.
6. Si el período de tiempo que selecciona es mayor a 7 días (fecha desde y fecha hasta), el sistema no descargará datos.
7. Una vez que ingrese las fechas requeridas, el Reporte Ministerial de PCR se generará automáticamente y se descargará en formato Excel.

![Alt text](img/Reporte-Ministerial.jpg)
_Figura 1: Reporte Ministerial_
