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
Teniendo en cuenta lo anteriormente mencionado, se procedió a realizar un cálculo y análisis estadístico descriptivo de dos formas distintas, pero las cuáles nos proporcionan los mismos resultados, puesto que se quiere ver la comparación de ello y, así mismo, familiarizarse con las herramientas que nos brinda Python para el desarrollo de distintos programas como este. La primera forma consiste en hacer uso de los comandos y librerías que proporciona este lenguaje de programación, como lo fueron Matplotlib, numpy, etc; la segunda parte consiste en el cálculo de estos estadísticos realizando la programación manual de cada una de las fórmulas que las conforman. 

[^1^] A continuación se puede observar cuáles fueron los estadísticos descriptivos que se calcularon con base a la base de datos que modelan la señal EMG escogida:
[^1^]: Ortega, C. (2024, September 23). Estadística descriptiva: Qué Es, Objetivo, Tipos y ejemplos. QuestionPro. https://www.questionpro.com/blog/es/estadistica-descriptiva/ 

##### •	Media: Medida que se utiliza para resumir un conjunto de datos numéricos, en este caso, los datos recopilados de una señal EMG. Se calcula sumando todos los valores y dividiéndolos entre el número total de valores.

##### •	Mediana: Medida que se utiliza para indicar el valor que divide un conjunto de datos ordenados en partes iguales. Se calcula ordenando los datos de menor a mayor, su cálculo va a depender si el número de datos es par o impar. Si es impar, este valor se encuentra en el medio de la lista ordenada; si es par, la mediana se calcula como el promedio de los dos valores centrales.

##### •	Moda: Medida que se refiere al valor que más se repite en un conjunto de datos numéricos, es decir, indica el número o valor que aparece con mayor frecuencia.

##### •	Rango: Medida de dispersión que se utiliza para indicar la diferencia entre el valor máximo o mínimo de un conjunto de datos numéricos. Esto nos permite saber de forma concisa y sencilla la amplitud o extensión de los datos proporcionados. Se calcula haciendo una resta entre el valor máximo y el valor mínimo.

##### •	Desviación estándar: Medida que indica que tan dispersos se encuentran los datos de un conjunto respecto a su media. Esto quiere decir, nos permite divisar y saber cuánto se desvían los valores individuales del conjunto de datos en promedio con respecto a la media.

##### •	Coeficiente de variación: Medida que se utiliza para comparar la variabilidad o dispersión que tienen dos o más conjuntos de datos, sin embargo, su plus es que no depende de las unidades de medida ni del tamaño de los números que la conforman. Se calcula dividiendo el dato de la desviación estándar y la media, y multiplicando por 100.

##### •	Histograma: Es un tipo de gráfico que se usa en estadística para representar la distribución de un conjunto de datos. Nos muestra, mediante un diagrama de barras, la representación de la cantidad de datos que caen dentro de un intervalo específico o rango.

##### •	Función de probabilidad: Es una función que describe la probabilidad de que ocurra un evento específico en un espacio muestral determinado. 

## Contaminación de la señal EMG y cálculo de SNR
[^2^]“In science and engineering, the signal-to-noise ratio (SNR) is a measure that compares the level of a desired signal to the level of background noise”. 
[^2^]: Welvaert M, Rosseel Y (2013) On the Definition of Signal-To-Noise Ratio and Contrast-To-Noise Ratio for fMRI Data. PLoS ONE 8(11): e77089. https://doi.org/10.1371/journal.pone.0077089

## Gráficas obtenidas

# Instrucciones

# Requisitos

# Usar

# Información de contacto
