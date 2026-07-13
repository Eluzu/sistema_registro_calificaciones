# Sistema de Registro de Calificaciones

## Descripción del Proyecto
Este proyecto es una aplicación desarrollada en Python para gestionar el registro, lectura y resumen estadístico de las calificaciones de estudiantes. El sistema permite evaluar notas, calcular promedios y determinar automáticamente si un estudiante ha aprobado o reprobado según las reglas de negocio establecidas.

## Proceso de Refactorización y Código Limpio
El código original era funcional, pero ha sido sometido a un proceso de refactorización progresiva utilizando el control de versiones Git para mejorar su calidad y mantenibilidad, sin alterar su comportamiento final.

### Mejoras Implementadas:

A continuación se detallan las refactorizaciones clave aplicadas, siguiendo los principios de *Clean Code*.

#### 1. Nombres Descriptivos y Reveladores de Intención
Se reemplazaron identificadores crípticos por nombres que auto-documentan el código, haciendo su propósito evidente.
*   **Antes:** `def p(n, c1): ...`
*   **Después:** `def guardar_registro_calificacion(nombre_estudiante: str, calificacion1: float): ...`
*   **Impacto:** Mejora radical de la legibilidad y reducción de la carga cognitiva para entender el código.

#### 2. Extracción de "Números Mágicos" y Cadenas a Constantes
Los valores literales fijos en la lógica (como `7` o `"APROBADO"`) se extrajeron a constantes globales con nombres semánticos.
*   **Antes:** `if promedio >= 7: estado = "APROBADO"`
*   **Después:** `if promedio >= CALIFICACION_MINIMA_APROBATORIA: estado = ESTADO_APROBADO`
*   **Impacto:** Centraliza las reglas de negocio, facilita su modificación futura y previene errores por inconsistencias.

#### 3. Uso de Administradores de Contexto para Manejo de Archivos
Se modernizó el manejo de ficheros para garantizar que siempre se cierren correctamente, incluso si ocurren errores.
*   **Antes:** `archivo = open(...)` y un `archivo.close()` manual al final.
*   **Después:** `with open(...) as archivo:`, que gestiona el ciclo de vida del recurso automáticamente.
*   **Impacto:** Código más seguro, robusto y limpio, previniendo fugas de recursos.

#### 4. Modernización de la Manipulación de Cadenas con F-Strings
La concatenación de cadenas tradicional se sustituyó por f-strings, la forma moderna y preferida en Python.
*   **Antes:** `nombre + "," + str(c1) + "," + str(c2)`
*   **Después:** `f"{nombre},{c1},{c2}"`
*   **Impacto:** Código más legible, conciso y menos propenso a errores de tipo al concatenar.

#### 5. Documentación y Tipado Estático (Type Hints)
Se enriqueció el código con documentación formal y anotaciones de tipo para mejorar la experiencia de desarrollo.
*   **Antes:** `def generar_reporte_aprobados():`
*   **Después:**
    ```python
    def generar_reporte_aprobados() -> None:
        """
        Cuenta y muestra un resumen del total de estudiantes aprobados y reprobados.
        """
        ...
    ```
*   **Impacto:** Facilita la colaboración, habilita un análisis estático más potente por parte de los IDEs y sirve como documentación viva del código.

## Tecnologías Utilizadas
* Python 3
* Git / GitHub

## Cómo Ejecutar el Proyecto
1.  Asegúrate de tener Python 3 instalado.
2.  Clona este repositorio.
3.  Ejecuta el script principal desde tu terminal:
    ```bash
    python main.py
    ```
4.  El script creará y gestionará el archivo `notas.txt` y mostrará los resultados en la consola.