---
layout: default
title: Últimas noticias - Desarrollos
nav_order: 3
---

<- [Desarrollos PNTM](#desarrollos-pntm)
  - [2022-09-08](#2022-09-08)

## Desarrollos PNTM

- - - 
### 2022-09-08

  -	Se realizan arreglos menores en el acceso a la plataforma. Se habilita acceso a dos módulos, uno para COVID 19 y otro para MonkeyPox
<br>
<p align="center">
  <img src="assets/img/2022-09-08-monkey-covid.png" alt="PNTM-MonkeyPox" width="300">
</p>
<br>
  - Estos perfiles están disponibles para todos los tomadores de muestra, pero solo laboratorios autorizados a procesar muestras de PCR Monkeypox, por el ISP, podrán hacer uso del módulo y recibir muestras a través de PNTM.
  -	Tipos de muestras presentes en MonkeyPox son `Tórula de Lesión` y `Contenido Vesicular` 
  -	El modulo MonkeyPox se encuentra presente con funcionalidades de carga vía interfaz, carga Masiva y vía API solo para el endpoint `/crearmuestrasmp` documentación presente en [APIDOCS](https://tomademuestras.apidocs.openagora.org/)
-	Endpoints de `/recepcionarMuestra` y `/entregaResultado` para MonkeyPox se encuentran en proceso de desarrollo

- *Respecto a módulo COVID 19:*

Con motivo de solucionar carga incorrecta de tomadores de muestra, profesionales responsables y médicos. Se han diferenciado los campos de *Tomador de Muestra*, *Profesional Responsable* y *Medico Solicitante*.

En el caso de ser búsqueda activa, se deberá agregar el Rut del Tomador de muestra, y el RUT de un profesional responsable (debe ser profesional)

<br>
<p align="center">
  <img src="assets/img/2022-09-08-profesional-responsable.png" alt="PNTM-MonkeyPox" width="300">
</p>
<br>
 
*__Datos presentes en la imagen de manera referencial, no corresponden a datos reales__

-	De ser un caso de *Atención Médica*, aparecerá el campo de *Médico Solicitante*, donde deberá usarse el RUT de un médico registrado en PNTM. De esta forma desde NC podremos rastrear quienes reportan muestras de diagnóstico utilizando perfiles técnicos y no profesionales. El Profesional responsable hace referencia al profesional tomador de la muestra o a algún profesional responsable de validar el resultado. __Esto se encuentra aún en desarrollo y será implementado en Interfaz y Carga Masiva la próxima semana.__

-	El desarrollo vía API de esta funcionalidad será implementado en el nuevo endpoint `/crearMuestras_v3` el cual también posee la funcionalidad de procesar todas las muestras de manera individual, cargando las muestras correctas y devolviendo las erróneas. Lo anterior viene a solucionar la caída de la carga completa cuando hay solo algunas muestras erróneas. Una vez realizados los desarrollos vía API, se bajará la información vía ordinario y tendrán un mes para migrar al nuevo endpoint `/crearMuestras_v3` y `/recepcionarMuestraV3`.

-	Se está trabajando en una modernización de la documentación de PNTM (`pntmdocs`), permitiendo búsqueda por temas, conteniendo preguntas frecuentes e incluyendo capsulas de ejemplo para cada tipo de proceso que se realiza (entre otras opciones). Además, se utilizarácomo medio oficial para bajar de forma rápida y oportuna los desarrollos realizados, junto a códigos ejemplo de integraciones vía API de los WS.

Estos desarrollos son los planificados a implementarse durante el mes de Septiembre 2022

- - - 

