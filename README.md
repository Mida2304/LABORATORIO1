<h1 align="center"> LABORATORIO 1. ANÁLISIS ESTADÍSTICO DE LA SEÑAL </h1>

# Introducción

El análisis estadístico de una señal biológica tiene varios propósitos de gran importancia, estos dependen del contexto en el cual se esté presentando, o incluso el tipo de señal que se quiera evaluar; sin importar esto, su finalidad es ayudar al especialista a determinar si existe alguna patología que ponga en riesgo la calidad humana, o saber de qué  forma se debe proceder con el análisis realizado, en este caso, estadísticamente.

Gracias a lo anteriormente mencionado, en esta práctica de laboratorio de la materia Procesamiento digital de señales, se pretende caracterizar y analizar una señal biomédica EMG (electromiografía) de forma estadística para poder divisar de forma clara y concisa su comportamiento. Para ello, en primera instancia se seleccionó una señal de la plataforma PhysioNet, en este caso una señal EMG correspondiente a una Miopatía, obtenida de ciertos músculos del cuerpo humano. 

Posteriormente, una vez seleccionada la señal a analizar, se importaron los datos correspondientes del paciente a la plataforma escogida, la cual fue Python 3.9, en la cual se ilustró de forma gráfica y numérica su comportamiento de forma estadística haciendo uso de los estadísticos descriptivos como la media, la desviación estándar, el coeficiente de variación, un histograma y la función de probabilidad. Estos nos permitirán entender de forma más clara la condición de la señal y su aspecto de forma más clara.

Así mismo, se requiere contaminar la señal con ruido Gaussiano y de Impulso, y con ello realizar el cálculo del SNR (Signal-to-Noise Ratio) de cada uno, esto con el propósito de saber la calidad de la señal.

Para la realización de este código de programación, se requirió la implementación de las siguientes librerías:

##### •	sys: Módulo que permite el acceso a ciertas variables y funciones específicas que permiten interactuar con el ambiente Python.

##### •	wfdb: Herramienta diseñada que permite trabajar con señales fisiológicas como señales biomédicas, en este caso como una señal EMG.

##### •	numpy: Proporciona una estrcutura de datos rápida y eficiente para poder trabajar con gran cantidad de funciones.

##### •	matplotlib.pyplot: Utilizada para crear gráficos y visualizaciones de datos.

##### •	scipy.stats: Parte del paquete SciPy, proporciona una amplia variedad de funciones y herramientas para realizar análisis estadísticos en Python.

# Análisis

## Cálculo de estadísticos descriptivos

## Contaminación de la señal EMG y cálculo de SNR

## Gráficas obtenidas

# Instrucciones
**1.Creación del entorno Python:**
- Utilizando las librerias enunciadas en la introducción se inicializa el entorno.
- Se crea una interfaz utilizando Pyqt6 para el diseño de la misma.
- Se establecen los botones y se definen cada uno de los estadisticos, tanto utilizando la libreria numpy como haciendolo de formal larga.
- Se crean las variables de los ruidos  gaussiano, pulso y ruido tipo artefacto.
**2. Extracción de datos:**

- Se descargan los datos desde Physionet que es un repositorio de datos de investigación médica de libre acceso.
- Se se seleccionan los archivos .dat y .hea de la señal EMG en este caso.


**3. Proceso de análisis:**

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
