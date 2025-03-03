    import cv2
    import paho.mqtt.client as mqtt

    area_minima = 100
    area_maxima = 1000

    canal_ID = "2722477" 
    mqtt_host = "mqtt3.thingspeak.com"
    mqtt_port = 1883
    mqtt_usuario = "LgETHBkWMy4CKh4qMSIgHSk"  
    mqtt_clave = "SzBgqGPqNaU73HbXzkNQNMsJ"  
    mqtt_tema = "channels/" + canal_ID + "/publish"

    cliente = mqtt.Client(protocol=mqtt.MQTTv5)  
    cliente.username_pw_set(mqtt_usuario, mqtt_clave)

    #CALLBACK
    def on_log(client, userdata, level, buf):
        print("Log MQTT:", buf)

    #Detectarlas 
    def detectar_etiquetas_defectuosas(imagen):
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        _, imagen_binaria = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        defectos_detectados = 0

        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area > area_maxima or area < area_minima:
                defectos_detectados += 1
                x, y, w, h = cv2.boundingRect(contorno)
                etiqueta = imagen[y:y+h, x:x+w]

                cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Publicar el número de defectos detectados en ThingSpeak
        if defectos_detectados > 0:
            payload = "field1=" + str(defectos_detectados)
            cliente.publish(mqtt_tema, payload)

        return imagen

    # Iniciar camara
    camara = cv2.VideoCapture(0)

    while True:
        ret, frame = camara.read()
        if not ret:
            break

        imagen_procesada = detectar_etiquetas_defectuosas(frame)
        cv2.imshow('Deteccion de etiquetas defectuosas', imagen_procesada)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camara.release()
    cv2.destroyAllWindows()