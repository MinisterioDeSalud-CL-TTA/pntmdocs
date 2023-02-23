---
layout: default
title: Tipos de usuarios
has_children: false
nav_order: 2
---

# Tipos de usuarios
{: .no_toc }

## Tabla de contenido
{: .no_toc .text-delta }
1. TOC
{:toc}

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
