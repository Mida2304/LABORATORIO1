<h1 align="center"> ANÁLISIS ESTADÍSTICO DE LA SEÑAL </h1>

# Introducción

El análisis estadístico de una señal biológica tiene varios propósitos de gran importancia, estos dependen del contexto en el cual se esté presentando, o incluso el tipo de señal que se quiera evaluar; sin importar esto, su finalidad es ayudar al especialista a determinar si existe alguna patología que ponga en riesgo la calidad humana, o saber de qué  forma se debe proceder con el análisis realizado, en este caso, estadísticamente.

Gracias a lo anteriormente mencionado, en esta práctica de laboratorio de la materia Procesamiento digital de señales, se pretende caracterizar y analizar una señal biomédica EMG (electromiografía) de forma estadística para poder divisar de forma clara y concisa su comportamiento. Para ello, en primera instancia se seleccionó una señal de la plataforma PhysioNet, en este caso una señal EMG correspondiente a una Miopatía, obtenida de ciertos músculos del cuerpo humano. 

Posteriormente, una vez seleccionada la señal a analizar, se importaron los datos correspondientes del paciente a la plataforma escogida, la cual fue Python 3.9, en la cual se ilustró de forma gráfica y numérica su comportamiento de forma estadística haciendo uso de los estadísticos descriptivos como la media, la desviación estándar, el coeficiente de variación, un histograma y la función de probabilidad. Estos nos permitirán entender de forma más clara la condición de la señal y su aspecto de forma más clara.

Así mismo, se requiere contaminar la señal con ruido Gaussiano y de Impulso, y con ello realizar el cálculo del SNR (Signal-to-Noise Ratio) de cada uno, esto con el propósito de saber la calidad de la señal.

Para la realización de este código de programación, se requirió la implementación de las siguientes librerías:
##### •	sys: Módulo que permite el acceso a ciertas variables y funciones específicas que permiten interactuar con el ambiente Python.

##### •	wfdb: Herramienta diseñada que permite trabajar con señales fisiológicas como señales biomédicas, en este caso como una señal EMG.

##### •	numpy: Proporciona una estructura de datos rápida y eficiente para poder trabajar con gran cantidad de funciones.

##### •	matplotlib.pyplot: Utilizada para crear gráficos y visualizaciones de datos.

##### •	scipy.stats: Parte del paquete SciPy, proporciona una amplia variedad de funciones y herramientas para realizar análisis estadísticos en Python.

# Análisis

## Cálculo de estadísticos descriptivos


## Contaminación de la señal EMG y cálculo de SNR

## Gráficas obtenidas

# Instrucciones

# Requisitos

# Usar

# Información de contacto
