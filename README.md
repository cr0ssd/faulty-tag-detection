# Detección y Separación de Etiquetas Defectuosas en Línea de Producción

Este proyecto utiliza visión por computadora (OpenCV), ThingSpeak y un ESP32 con servomotor para detectar etiquetas defectuosas en frascos en una línea de producción y separarlos automáticamente.

## Componentes

* **Python (OpenCV):** Detecta etiquetas defectuosas en imágenes capturadas por una cámara, guarda las imágenes y envía una señal a ThingSpeak.
* **ThingSpeak:** Plataforma IoT que recibe la señal de la computadora e informa al ESP32 si hay etiquetas defectuosas.
* **ESP32:** Recibe la señal de ThingSpeak y activa un servomotor para separar los frascos defectuosos.
* **Servomotor:** Separa físicamente los frascos defectuosos de la línea de producción.
* **Cámara:** Captura imágenes de los frascos en la línea de producción.

## Requisitos

* **Hardware:**
    * Computadora con cámara
    * ESP32
    * Servomotor
* **Software:**
    * Python 3.x
    * OpenCV (`cv2`)
    * `paho-mqtt`
    * IDE de Arduino
    * Librería `ThingSpeak` para Arduino
    * Cuenta en ThingSpeak

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone [https://github.com/cr0ssd/faulty-tag-detection](https://github.com/cr0ssd/faulty-tag-detection)
    cd [faulty-tag-detection]
    ```

2.  **Instala las dependencias de Python:**

    ```bash
    pip install opencv-python paho-mqtt
    ```

3.  **Configura ThingSpeak:**
    * Crea una cuenta en ThingSpeak.
    * Crea un nuevo canal y anota el Channel ID.
    * Obtén las claves de acceso (Write API Key y Read API Key).
    * Obtén las credenciales MQTT.

4.  **Configura el ESP32:**
    * Abre el código del ESP32 en el IDE de Arduino.
    * Reemplaza las credenciales de WiFi y ThingSpeak con tus propios valores.
    * Completa la función `activarServo()` con la lógica para controlar tu servomotor.
    * Sube el código al ESP32.

5.  **Configura el código Python:**
    * Abre el código de Python y reemplaza las credenciales de ThingSpeak con tus propios valores.

## Uso

1.  Conecta la cámara a la computadora y el ESP32 al servomotor.
2.  Ejecuta el código de Python.
3.  Coloca los frascos en la línea de producción frente a la cámara.
4.  El sistema detectará automáticamente las etiquetas defectuosas y separará los frascos.

## Créditos

Proyecto desarrollado por \[Tu Nombre]

## Licencia

Este proyecto está bajo la Licencia MIT.
