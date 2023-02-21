La plataforma Nacional de Toma de Muestras detalla los posibles errores que pueden ser indicados por el sistema al momento de subir una planilla de carga masiva a la plataforma, así como los errores que no detectará el sistema pero que pueden afectar la calidad de la información. El objetivo es verificar estas condiciones para poder subir una planilla de carga masiva de forma correcta a la PNTM.

### Errores indicados por el sistema

Los posibles errores que pueden ser indicados por el sistema al momento de subir una planilla de carga masiva a la plataforma son:

-   **Campo obligatorio en blanco**: este error se presenta al dejar en blanco campos que son de carácter obligatorio, como el RUN_pasaporte.
-   **RUN Paciente Incorrecto**: este error se presenta cuando la planilla posee algún RUN inválido. Cabe destacar que el RUN debe ser escrito sin puntos y con guion.
-   **Rut Profesional_sis o Rut_medico no existente en base de profesionales**: este error se presenta al ingresar un rut en el campo rut_profesional o rut_medico que no se encuentre en la base de profesionales.
-   **Rut_medico en blanco**: este error se presenta al dejar en blanco el campo rut_medico, ya que la plataforma fue diseñada en un principio para recibir muestras de antígenos de pacientes sintomáticos provenientes de alguna médica.
-   **Fecha diferente a la fecha actual**: este error se presenta al ingresar una fecha de muestra diferente a la fecha actual.
-   **Campo no figura dentro del conjunto de datos**: este error se presenta al ingresar información que no esté contenida dentro del maestro de datos. En dicho caso se indicará por pantalla el conjunto de datos aceptado.

### Errores no indicados por el sistema

Los errores no indicados por el sistema son aquellos que pueden afectar directamente el tratamiento de los datos y la calidad de la información, por lo que es importante verificar dicha información antes de ser subida. Algunos ejemplos de estos errores son:

-   Ingreso de código DEIS de otro establecimiento.
-   Ingreso erróneo de resultado.
-   Ingreso de RUN de otro paciente.
-   Ingreso de ID de otra comuna.
-   Ingreso de código EPIVIGILA erróneo.
-   Ingreso erróneo de tipo de búsqueda (activa o no activa).

### Excepciones

PNTM detalla algunas especificaciones a considerar en diversos campos obligatorios al momento de realizar una carga masiva en la plataforma en circunstancias excepcionales. Por ejemplo:

-   Dirección o teléfono del paciente: en caso de que no se posea la dirección detallada del paciente debido a circunstancias en las cuales sea dificultoso poseer este tipo de información, se deberán considerar algunas indicaciones específicas dependiendo del resultado de la muestra.
-   Pacientes menores de edad: en caso de que se trate de pacientes menores de edad, se debe ingresar el RUN del apoderado en el campo rut_medico.
-   En caso de fallecimiento del paciente: si el paciente ha fallecido, se debe indicar en el campo estado_paciente la opción "Fallecido".
-   Muestras en contexto de pesquisa activa: en caso de que las muestras sean tomadas en el contexto de pesquisa