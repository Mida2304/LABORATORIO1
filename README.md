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
[^2^]“In science and engineering, the signal-to-noise ratio (SNR) is a measure that compares the level of a desired signal to the level of background noise”. - Welvaert M, Rosseel Y (2013)
[^2^]: Welvaert M, Rosseel Y (2013) On the Definition of Signal-To-Noise Ratio and Contrast-To-Noise Ratio for fMRI Data. PLoS ONE 8(11): e77089. https://doi.org/10.1371/journal.pone.0077089

El SNR, o mejor conocido por sus siglas en inglés Signal-to-Noise Ratio, o Relación Señal-Ruido, es una medida que se usa en el campo del procesamiento de señales para describir la proporción entre la potencia de la señal útil (lo que se quiere medir o transmitir), y la potencia del ruido, o como la conocemos, las interferencias o distorsiones no deseadas.

Siguiendo este concepto, al fórmula utilizada para su cálculo es la siguiente, y se tiene que se mide en decibelios (dB):

De igual forma, se puede tener en cuenta lo siguiente: 
##### •	SNR Alto: Cuando un SNR es alto significa que la señal es mucho más fuerte que el ruido, lo cuál nos puede indicar que esta es buena. En otras palabras, al ser el SNR alto implica que la calidad de la señal es alta y más fácil de procesar sin interferencias.

##### •	SNR Bajo: Cuando un SNR es bajo, significa que la señal es muy débil comparada con el ruido, o cuál es algo no adecuado. Esto provoca que la señal se pierda o sea difícil de interpretar puesto que el ruido interfiere mucho con la señal.

Para saber si la calidad de nuestra señal es buena, se procedió a contaminarla con dos tipos de ruidos distintos, uno conocido como el Ruido Gaussiano, y el otro como Ruido de pulso:

##### •	[^3^]Ruido Gaussiano: Es un tipo de ruido o interferencia que sigue una distribución normal o gaussiana, es una distribución de probabilidad que tiene la forma de una curva de campana. El ruido Gaussiano es una señal aleatoria cuyo valor sigue una distribución normal (Gaussiana), en otras palabras, tiene una distribución que se ajusta de forma correcta a la famosa curva de campana.

[^3^]: Ortiz Rangel, Estela, Mejía-Lavalle, Manuel, & Sossa, Humberto. (2017). Filtrado de ruido Gaussiano mediante redes neuronales pulso-acopladas. Computación y Sistemas, 21(2), 381-395. https://doi.org/10.13053/cys-21-2-2742

Su fórmula matemática es la siguiente:

##### •	[^4^]Ruido de impulso: Es un tipo de interferencia de gran amplitud que afecta señales en intervalos impredecibles. Se caracteriza por picos de energía breves y de gran amplitud que generalmente son mucho más altos que el nivel de la señal o el ruido de fondo, y pueden distorsionar significativamente una señal si no se maneja adecuadamente.

[^4^]: Ruido de Impulso. SVANTEK. (2023, September 27). https://svantek.com/es/servicios/ruido-de-impulso/#:~:text=El%20ruido%20de%20impulso%20se,inferior%20a%201%20segundo)%C2%BB. 

## Gráficas obtenidas

# Instrucciones

# Requisitos

# Usar

# Información de contacto
