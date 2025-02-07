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
# Análisis
A continuación se presenta la imagen de EMG con neuropatía, la cual, sera tomada a estudio utilizando la estadistica descriptiva para interpretarla de una forma sencilla.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/EMG_PYTHON.png?raw=true" width="60%" />

>*Señal EMG con neuropatia.*
Posteriormente se contruyo una Interfaz utilizando Pyqt6 de Python, esto para agilizar la obtencion de los datos y brindar un ambiente mas estético.

<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/Interfaz.png?raw=true" width="60%" />
>*Interfaz grafic del Laboratorio.*
## Cálculo de estadísticos descriptivos
Teniendo en cuenta lo anteriormente mencionado, se procedió a realizar un cálculo y análisis estadístico descriptivo de dos formas distintas, pero las cuáles nos proporcionan los mismos resultados, puesto que se quiere ver la comparación de ello y, así mismo, familiarizarse con las herramientas que nos brinda Python para el desarrollo de distintos programas como este. La primera forma consiste en hacer uso de los comandos y librerías que proporciona este lenguaje de programación, como lo fueron Matplotlib, numpy, etc; la segunda parte consiste en el cálculo de estos estadísticos realizando la programación manual de cada una de las fórmulas que las conforman. 

[^1^] A continuación se puede observar cuáles fueron los estadísticos descriptivos que se calcularon con base a la base de datos que modelan la señal EMG escogida:
[^1^]: Ortega, C. (2024, September 23). Estadística descriptiva: Qué Es, Objetivo, Tipos y ejemplos. QuestionPro. https://www.questionpro.com/blog/es/estadistica-descriptiva/ 

##### •	Media: Medida que se utiliza para resumir un conjunto de datos numéricos, en este caso, los datos recopilados de una señal EMG. Se calcula sumando todos los valores y dividiéndolos entre el número total de valores.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/media.png?raw=true" width="20%" />

>*Media calculada del Laboratorio.*


##### •	Mediana: Medida que se utiliza para indicar el valor que divide un conjunto de datos ordenados en partes iguales. Se calcula ordenando los datos de menor a mayor, su cálculo va a depender si el número de datos es par o impar. Si es impar, este valor se encuentra en el medio de la lista ordenada; si es par, la mediana se calcula como el promedio de los dos valores centrales.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/mediana.png?raw=true" width="40%" />

>*Mediana calculada del Laboratorio.*

##### •	Moda: Medida que se refiere al valor que más se repite en un conjunto de datos numéricos, es decir, indica el número o valor que aparece con mayor frecuencia.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/moda.png?raw=true" width="20%" />

>*Moda calculada del Laboratorio.*
##### •	Rango: Medida de dispersión que se utiliza para indicar la diferencia entre el valor máximo o mínimo de un conjunto de datos numéricos. Esto nos permite saber de forma concisa y sencilla la amplitud o extensión de los datos proporcionados. Se calcula haciendo una resta entre el valor máximo y el valor mínimo.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/rango.png?raw=true" width="20%" />

>*Rango calculado del Laboratorio.*

##### •	Desviación estándar: Medida que indica que tan dispersos se encuentran los datos de un conjunto respecto a su media. Esto quiere decir, nos permite divisar y saber cuánto se desvían los valores individuales del conjunto de datos en promedio con respecto a la media.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/desviacion%20estandar.png?raw=true" width="20%" />

>*Rango calculado del Laboratorio.*

##### •	Coeficiente de variación: Medida que se utiliza para comparar la variabilidad o dispersión que tienen dos o más conjuntos de datos, sin embargo, su plus es que no depende de las unidades de medida ni del tamaño de los números que la conforman. Se calcula dividiendo el dato de la desviación estándar y la media, y multiplicando por 100.

<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/varianza.png?raw=true" width="20%" />

>*Rango calculado del Laboratorio.*
##### •	Histograma: Es un tipo de gráfico que se usa en estadística para representar la distribución de un conjunto de datos. Nos muestra, mediante un diagrama de barras, la representación de la cantidad de datos que caen dentro de un intervalo específico o rango.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/Histograma%201.png?raw=true" width="60%" />

>*Histograma de la señal.*
##### •	Función de probabilidad: Es una función que describe la probabilidad de que ocurra un evento específico en un espacio muestral determinado. 
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/Probabilidad.png?raw=true" width="60%" />

>*Funcion de Probabilidad.*

## Contaminación de la señal EMG y cálculo de SNR
[^2^]“In science and engineering, the signal-to-noise ratio (SNR) is a measure that compares the level of a desired signal to the level of background noise”. - Welvaert M, Rosseel Y (2013)
[^2^]: Welvaert M, Rosseel Y (2013) On the Definition of Signal-To-Noise Ratio and Contrast-To-Noise Ratio for fMRI Data. PLoS ONE 8(11): e77089. https://doi.org/10.1371/journal.pone.0077089

Por consiguiente, se plantea el contaminar la señal EMG con ruidos tales como el Ruido Gaussiano, Ruido Inpulso y Ruido tipo Artefacto.

El SNR, o mejor conocido por sus siglas en inglés Signal-to-Noise Ratio, o Relación Señal-Ruido, es una medida que se usa en el campo del procesamiento de señales para describir la proporción entre la potencia de la señal útil (lo que se quiere medir o transmitir), y la potencia del ruido, o como la conocemos, las interferencias o distorsiones no deseadas.

Siguiendo este concepto, al fórmula utilizada para su cálculo es la siguiente, y se tiene que se mide en decibelios (dB):
$$
SNR = 10 \times \log_{10} \left(\frac{P_{\text{señal}}}{P_{\text{ruido}}}\right)
$$
De igual forma, se puede tener en cuenta lo siguiente: 

##### •	SNR Alto: Cuando un SNR es alto significa que la señal es mucho más fuerte que el ruido, lo cuál nos puede indicar que esta es buena. En otras palabras, al ser el SNR alto implica que la calidad de la señal es alta y más fácil de procesar sin interferencias.

##### •	SNR Bajo: Cuando un SNR es bajo, significa que la señal es muy débil comparada con el ruido, o cuál es algo no adecuado. Esto provoca que la señal se pierda o sea difícil de interpretar puesto que el ruido interfiere mucho con la señal.

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


### Gráficas obtenidas y SNR
#### Ruido Gaussiano y Ruido Gaussiano Amplificado
Este es un tipo de ruido de señal que tiene una función de densidad de probabilidad  igual a la de la distribución normal.
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/ruido%20gaussiano.png?raw=true" width="60%" /
>*Ruido Gaussiano.*

<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/ruido%20gaussiano.png?raw=true" width="60%" />

>*Ruido Gaussiano.*
https://github.com/Mida2304/LABORATORIO1/blob/master/ruido%20gaussiano.png

#### Ruido impulso  y Ruido Impulso Amplificado
Es un sonido breve y agudo que se caracteriza por una presión sonora repentina y de corta duración. 
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/impulso.png?raw=true" width="60%" />

>*Ruido Impulso.*
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/impulso%20amplificado.png" width="60%" />

>*SNR Ruido Impulso.*


<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/impulso%20amplificado.png" width="60%" />

>*Ruido Impulso Amplificado.*

#### Ruido Tipo Artefacto y Ruido Tipo Artefacto Amplificado
<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/artefacto.png" width="60%" />

>*Ruido Tipo Artefacto.*

<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/snriartefacto.png" width="20%" />

>*SNR Ruido Artefacto.*

<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/ruidoatramplificado.png" width="60%" />

>*Ruido Tipo Artefacto Amplificado.*

<img src="https://github.com/Mida2304/LABORATORIO1/blob/master/snriartefacto.png" width="20%" />

>*SNR Ruido Artefacto Amplificado.*

# Instrucciones
*1.Creación del entorno Python:*
- Utilizando las librerias enunciadas en la introducción se inicializa el entorno.
- Se crea una interfaz utilizando Pyqt6 para el diseño de la misma.
- Se establecen los botones y se definen cada uno de los estadisticos, tanto utilizando la libreria numpy como haciendolo de formal larga.
- Se crean las variables de los ruidos  gaussiano, pulso y ruido tipo artefacto.
*2. Extracción de datos:*

- Se descargan los datos desde Physionet que es un repositorio de datos de investigación médica de libre acceso.
- Se se seleccionan los archivos .dat y .hea de la señal EMG en este caso.


*3. Proceso de análisis:*

• La señal se descarga y se procesa en Python.

• Todo el análisis se realiza mediante código, lo que permitió evaluar los datos de manera precisa.

###### - Se carga la señal usando wfdb.rdrecord(), y se extraen los datos de la señal en signal_data.
###### - Se creauna replica de la gráfica para observar la señal original utilizando matplotlib, esto con el fin de observar las modificaciones por agregar ruidos.
###### - Se calculan los estadisticos utilizando la librería numpy y manualmente para reforzar la comprensión de los métodos.
###### - Se calcula el histograma y función de probabilidad tanto manualmente como utilizando la función predefinida para visualizar la distribución de los valores.
###### - Se añade un ruido gaussiano, de impulso y artefcato, y se agrega a la señal original. Luego, se calcula el Signal-to-Noise Ratio (SNR).

# Requisitos
- Contar con Python 3.9.0 instalado.
- Tener acceso a los archivos .dat y .hea.
- Instalar las librerías necesarias instaladas para ejecutar el código correctamente.
- Contar con conocimiento sobre programacion en Python.
  
# Usar
Por favor, cite este articulo de la siguiente manera:

Aux, M.; Martinez, M.;  LABORATORIO 1. Análisis estadístico de la señal. 6 de febrero de 2025.

# Información de contacto

est.manuela.martin@unimilitar.edu.co y est.midalys.aux@unimilitar.edu.co
