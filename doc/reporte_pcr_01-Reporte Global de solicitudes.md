---
layout: default
title: Reporte Global de Solicitudes
nav_order: 1
grand_parent: Reportes
parent: Reportes - PCR
has_children: false
has_toc: true
---

# Reporte Global de Solicitudes

El reporte global de solicitudes proporciona información detallada acerca de las muestras de pruebas realizadas en la PNTM durante un período de tiempo específico, considerando las fechas correspondientes a la fecha de toma de la muestra.

El reporte contiene las muestras con los siguientes estados:

| Estado de muestra | Descripción                                                                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2                 | La muestra de prueba ha sido **enviada al laboratorio** para su procesamiento.                                                                                                                                                                                  |
| 3                 | La muestra de prueba ha sido **recepcionada por el laboratorio** y se encuentra en proceso de análisis.                                                                                                                                                         |
| 4                 | La muestra de prueba ha sido procesada y se dispone de un **resultado**.                                                                                                                                                                                        |
| 5                 | La muestra de prueba se encuentra en **proceso de modificación**, es decir, se está realizando alguna corrección o actualización de la información asociada a la muestra.                                                                                       |
| 6                 | La muestra de prueba ha sido **rechazada** y no es apta para su procesamiento.                                                                                                                                                                                  |
| 7                 | La muestra de prueba ha sido **enviada a mutaciones para su análisis** y seguimiento.                                                                                                                                                                           |
| 8                 | La muestra de prueba ha sido procesada en mutaciones y se **dispone de un resultado de la mutación**.                                                                                                                                                           |
| 9                 | La muestra de prueba se encuentra en un estado de **edición autorizada**, es decir, se ha dado permiso a un usuario específico para realizar modificaciones en la información asociada a la muestra. Este estado se utiliza para evitar cambios no autorizados. |

## Acceso al reporte global de solicitudes de PCR

Para acceder al reporte global de solicitudes de PCR, siga estos pasos:

1. Ingrese al menú de reportes en la interfaz de usuario.
2. Seleccione el submenú de PCR en la lista de opciones disponibles.
3. Haga clic en el botón para generar el reporte global de solicitudes.
4. Establezca las fechas "DESDE" y "HASTA" para definir el rango de tiempo que desea incluir en el reporte, correspondiente a la fecha de toma de muestra. Si no asigna fechas, el sistema tomará automáticamente la fecha y hora actual como punto de partida y finalización.
5. El reporte global de solicitudes de PCR se generará automáticamente y se descargará en formato Excel.

![Alt text](img/Reporte-PCR.jpg)
_Figura 1: Reporte global de solicitudes_

![Alt text](img/Reportes-PCR-Global.png)
_Figura 2: Reporte global de solicitudes_
