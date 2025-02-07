import sys
import wfdb
import numpy as np
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QGridLayout, QWidget, QMessageBox, QTextEdit, QFileDialog
)
from PyQt6.QtCore import Qt
import matplotlib.pyplot as plt
from scipy.stats import mode, norm

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LABORATORIO 1 ESTADISTICA")
        self.setGeometry(200, 200, 800, 600)

        # Widget principal
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Estilo general
        self.setStyleSheet("""
            QMainWindow {
                background-color: #E3DFF3;  /* Azul claro */
            }
            QPushButton {
                background-color: #B19CD9;  /* Morado */
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FFB6C1;  /* Rosado */
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #4B0082;  /* Morado oscuro */
            }
        """)

        # Layout principal
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Botón para cargar archivos
        self.load_button = QPushButton("Cargar Archivo .hea")
        self.load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_button)

        # Layout para botones y etiquetas
        self.stats_layout = QGridLayout()

        # Botones ruido y SNR
        self.ruido_gaussiano_button = QPushButton("Agregar Ruido Gaussiano")
        self.snr_button = QPushButton("Calcular SNR")
        self.ruido_impulso_button = QPushButton("Agregar Ruido Tipo Impulso")
        self.ruido_artefacto_button = QPushButton("Agregar Ruido Artefacto")
        self.ruido_gaussiano_amplificado_button = QPushButton("Agregar Ruido Gaussiano Amplificado")
       


        # Conectar botones
        self.ruido_gaussiano_button.clicked.connect(self.agregar_ruido_gaussiano)
        self.ruido_impulso_button.clicked.connect(self.agregar_ruido_impulso)
        self.ruido_artefacto_button.clicked.connect(self.agregar_ruido_artefacto)
        self.ruido_gaussiano_amplificado_button.clicked.connect(self.agregar_ruido_gaussiano_amplificado)
        self.snr_button.clicked.connect(self.calcular_snr)

        # Botones de estadísticas
        self.media_button = QPushButton("MEDIA")
        self.mediana_button = QPushButton("MEDIANA")
        self.moda_button = QPushButton("MODA")
        self.varianza_button = QPushButton("VARIANZA")
        self.rango_button = QPushButton("RANGO")
        self.histograma_button = QPushButton("HISTOGRAMA")
        self.desviacion_button = QPushButton("DESVIACIÓN ESTÁNDAR")

        # Etiquetas para mostrar los valores
        self.media_label = QLabel("")
        self.mediana_label = QLabel("")
        self.moda_label = QLabel("")
        self.varianza_label = QLabel("")
        self.rango_label = QLabel("")
        self.desviacion_label = QLabel("")

        # Conectar botones a funciones
        self.media_button.clicked.connect(self.calcular_media)
        self.mediana_button.clicked.connect(self.calcular_mediana)
        self.moda_button.clicked.connect(self.calcular_moda)
        self.varianza_button.clicked.connect(self.calcular_varianza)
        self.rango_button.clicked.connect(self.calcular_rango)
        self.histograma_button.clicked.connect(self.mostrar_histograma)
        self.desviacion_button.clicked.connect(self.calcular_desviacion_estandar)

        # Botones de cálculo manual
        self.media_normal_button = QPushButton("MEDIA NORMAL")
        self.mediana_normal_button = QPushButton("MEDIANA NORMAL")
        self.moda_normal_button = QPushButton("MODA NORMAL")
        self.varianza_normal_button = QPushButton("VARIANZA NORMAL")
        self.rango_normal_button = QPushButton("RANGO NORMAL")
        self.desviacion_normal_button = QPushButton("DESVIACIÓN ESTÁNDAR N")

        # Etiquetas para mostrar los valores manuales
        self.media_normal_label = QLabel("")
        self.mediana_normal_label = QLabel("")
        self.moda_normal_label = QLabel("")
        self.varianza_normal_label = QLabel("")
        self.rango_normal_label = QLabel("")
        self.desviacion_normal_label = QLabel("")

        # Conectar botones a funciones manuales
        self.media_normal_button.clicked.connect(self.calcular_media_normal)
        self.mediana_normal_button.clicked.connect(self.calcular_mediana_normal)
        self.moda_normal_button.clicked.connect(self.calcular_moda_normal)
        self.varianza_normal_button.clicked.connect(self.calcular_varianza_normal)
        self.rango_normal_button.clicked.connect(self.calcular_rango_normal)
        self.desviacion_normal_button.clicked.connect(self.calcular_desviacion_estandar_normal)

        # Añadir botones y etiquetas al layout de estadísticas
        self.stats_layout.addWidget(self.media_button, 0, 0)
        self.stats_layout.addWidget(self.media_label, 0, 1)
        self.stats_layout.addWidget(self.mediana_button, 0, 2)
        self.stats_layout.addWidget(self.mediana_label, 0, 3)
        self.stats_layout.addWidget(self.moda_button, 1, 0)
        self.stats_layout.addWidget(self.moda_label, 1, 1)
        self.stats_layout.addWidget(self.varianza_button, 1, 2)
        self.stats_layout.addWidget(self.varianza_label, 1, 3)
        self.stats_layout.addWidget(self.rango_button, 2, 0)
        self.stats_layout.addWidget(self.rango_label, 2, 1)
        self.stats_layout.addWidget(self.desviacion_button, 2, 2)
        self.stats_layout.addWidget(self.desviacion_label, 2, 3)
        self.stats_layout.addWidget(self.histograma_button, 5, 0)
        self.stats_layout.addWidget(self.snr_button, 12, 0)
        self.stats_layout.addWidget(self.ruido_gaussiano_button, 13, 0)
        self.stats_layout.addWidget(self.ruido_impulso_button, 13, 1)
        self.stats_layout.addWidget(self.ruido_artefacto_button, 14, 0)
        self.stats_layout.addWidget(self.ruido_gaussiano_amplificado_button, 14, 1)

        # Botones para cálculos manuales
        self.stats_layout.addWidget(self.media_normal_button, 3, 0)
        self.stats_layout.addWidget(self.media_normal_label, 3, 1)
        self.stats_layout.addWidget(self.mediana_normal_button, 3, 2)
        self.stats_layout.addWidget(self.mediana_normal_label, 3, 3)
        self.stats_layout.addWidget(self.moda_normal_button, 4, 0)
        self.stats_layout.addWidget(self.moda_normal_label, 4, 1)
        self.stats_layout.addWidget(self.varianza_normal_button, 4, 2)
        self.stats_layout.addWidget(self.varianza_normal_label, 4, 3)
        self.stats_layout.addWidget(self.rango_normal_button, 5, 0)
        self.stats_layout.addWidget(self.rango_normal_label, 5, 1)
        self.stats_layout.addWidget(self.desviacion_normal_button, 5, 2)
        self.stats_layout.addWidget(self.desviacion_normal_label, 5, 3)

        self.layout.addLayout(self.stats_layout)

        # Botón para calcular probabilidad
        self.probabilidad_emg_button = QPushButton("Calcular Probabilidad EMG")
        self.probabilidad_emg_button.clicked.connect(self.calcular_probabilidad_emg)
        self.layout.addWidget(self.probabilidad_emg_button)

        # Área de texto para el registro
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.layout.addWidget(self.log_area)

        # Variable para almacenar la señal cargada
        self.signal = None

    def calcular_media_normal(self):
        if self.signal is not None:
            suma = sum(self.signal)
            count = len(self.signal)
            media = suma / count if count > 0 else 0
            self.media_normal_label.setText(f"{media:.6f}")

    def calcular_moda_normal(self):
        if self.signal is not None:
            frecuencia = {}
            for valor in self.signal:
                frecuencia[valor] = frecuencia.get(valor, 0) + 1
            moda = max(frecuencia, key=frecuencia.get)
            self.moda_normal_label.setText(f"{moda:.6f}")

    def calcular_varianza_normal(self):
        if self.signal is not None:
            media = sum(self.signal) / len(self.signal)
            varianza = sum((x - media) ** 2 for x in self.signal) / len(self.signal)
            self.varianza_normal_label.setText(f"{varianza:.6f}")

    def calcular_rango_normal(self):
        if self.signal is not None:
            rango = max(self.signal) - min(self.signal)
            self.rango_normal_label.setText(f"{rango:.6f}")

    def calcular_mediana_normal(self):
        if self.signal is not None:
            sorted_signal = sorted(self.signal)
            n = len(sorted_signal)
            mid = n // 2
            if n % 2 == 0:
                mediana = (sorted_signal[mid - 1] + sorted_signal[mid]) / 2
            else:
                mediana = sorted_signal[mid]
            self.mediana_normal_label.setText(f"{mediana:.6f}")

    def calcular_desviacion_estandar_normal(self):
        if self.signal is not None:
            media = sum(self.signal) / len(self.signal)
            varianza = sum((x - media) ** 2 for x in self.signal) / len(self.signal)
            desviacion_estandar = varianza ** 0.5
            self.desviacion_normal_label.setText(f"{desviacion_estandar:.6f}")


    def load_file(self):
        # Seleccionar archivo .hea
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo .hea", "", "Archivos .hea (*.hea)")

        if file_path:
            try:
                # Elimina la extensión del archivo para cargar el registro
                record_path = file_path.rsplit('.', 1)[0]
                record = wfdb.rdrecord(record_path)

                # Almacena la señal
                self.signal = record.p_signal
                self.log_area.append(f"Archivo cargado: {file_path}\nDimensiones de la señal: {self.signal.shape}")

                # Mostrar la señal EMG en una gráfica
                plt.figure(figsize=(18, 4))
                plt.plot(self.signal[:, 0], color='purple')
                plt.title("Señal EMG")
                plt.xlabel("Tiempo ")
                plt.ylabel("Amplitud (mV)")
                plt.grid()
                plt.show()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo: {e}")

    def calcular_media(self):
        if self.signal is not None:
            media = np.nanmean(self.signal[:, 0])
            self.media_label.setText(f"{media:.6f}")
            self.log_area.append(f"Media calculada: {media:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_mediana(self):
        if self.signal is not None:
            mediana = np.nanmedian(self.signal[:, 0])
            self.mediana_label.setText(f"{mediana:.6f}")
            self.log_area.append(f"Mediana calculada: {mediana:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_moda(self):
        if self.signal is not None:
            data = self.signal[:, 0]
            # Calcular el histograma
            counts, bins = np.histogram(data, bins=10)
            # Encontrar el índice del intervalo con la mayor frecuencia
            index_max = np.argmax(counts)
            # Calcular el centro del intervalo modal
            moda_continua = (bins[index_max] + bins[index_max + 1]) / 2
            self.moda_label.setText(f"{moda_continua:.6f}")
            self.log_area.append(f"Moda continua calculada: {moda_continua:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_varianza(self):
        if self.signal is not None:
            varianza = np.nanvar(self.signal[:, 0])
            self.varianza_label.setText(f"{varianza:.6f}")
            self.log_area.append(f"Varianza calculada: {varianza:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_rango(self):
        if self.signal is not None:
            rango = np.ptp(self.signal[:, 0])
            self.rango_label.setText(f"{rango:.6f}")
            self.log_area.append(f"Rango calculado: {rango:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_probabilidad_emg(self):
        if self.signal is not None:
            # Extraer los datos de la señal
            data = self.signal[:, 0]
            
            # Calcular la media y desviación estándar de la señal
            mu = np.mean(data)
            sigma = np.std(data)
            
            # Definir el rango para el cálculo de probabilidad
            rango_min, rango_max = np.percentile(data, [5, 95])  # Usamos el rango del 5% al 95% de los datos
            
            # Calcular la probabilidad de que la señal caiga en el rango dado
            probabilidad = norm.cdf(rango_max, mu, sigma) - norm.cdf(rango_min, mu, sigma)

            self.log_area.append(f"Probabilidad de la señal EMG en el rango [{rango_min:.2f}, {rango_max:.2f}]: {probabilidad:.4%}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_desviacion_estandar(self):
        if self.signal is not None:
            desviacion_estandar = np.nanstd(self.signal[:, 0])
            self.log_area.append(f"Desviación estándar calculada: {desviacion_estandar:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")


    def mostrar_histograma(self):
        
        if self.signal is not None:
            data = self.signal[:, 0]
            plt.figure(figsize=(10, 6))

            # Histograma
            counts, bins, _ = plt.hist(data, bins=20, color='#D8BFD8', edgecolor='black', density=False)

            # Ajuste de la curva de Gauss
            mu, sigma = norm.fit(data)
            x = np.linspace(np.min(data), np.max(data), 100)
            pdf = norm.pdf(x, mu, sigma)

            # Escalar la curva de Gauss para ajustarse al histograma
            pdf_scaled = pdf * (np.max(counts) / np.max(pdf))

            plt.plot(x, pdf_scaled, color='purple', lw=2, label=f'Campana de Gauss (μ={mu:.4f}, σ={sigma:.4f})')

            plt.title("Histograma de la Señal EMG con Campana de Gauss")
            plt.xlabel("Amplitud mV")
            plt.ylabel("Frecuencia")
            plt.legend()
            plt.grid(axis='y', alpha=0.75)
            plt.show()

            self.log_area.append("Histograma con campana de Gauss generado.")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

        # Funciones sin numpy
    def calcular_media_normal(self):
        if self.signal is not None:
            suma = 0
            contador = 0
            for valor in self.signal[:, 0]:
                suma += valor
                contador += 1
            media = suma / contador if contador > 0 else 0
            self.log_area.append(f"Media calculada: {media:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_mediana_normal(self):
        if self.signal is not None:
            signal_ordenada = sorted(self.signal[:, 0])
            n = len(signal_ordenada)
            if n == 0:
                mediana = 0
            elif n % 2 == 0:
                mitad = n // 2
                mediana = (signal_ordenada[mitad - 1] + signal_ordenada[mitad]) / 2
            else:
                mediana = signal_ordenada[n // 2]
            self.log_area.append(f"Mediana calculada: {mediana:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_moda_normal(self):
        if self.signal is not None:
            frecuencia = {}
            for valor in self.signal[:, 0]:
                if valor in frecuencia:
                    frecuencia[valor] += 1
                else:
                    frecuencia[valor] = 1
            moda = max(frecuencia, key=frecuencia.get)
            self.log_area.append(f"Moda  calculada: {moda:.4f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def calcular_varianza_normal(self):
        if self.signal is not None:
            # Calcular la media manualmente
            suma = 0
            contador = 0

            for valor in self.signal[:, 0]:
                suma += valor
                contador += 1

            media = suma / contador if contador > 0 else 0

            # Calcular la varianza manualmente
            suma_cuadrados = 0

            for valor in self.signal[:, 0]:
                suma_cuadrados += (valor - media) ** 2

            varianza = suma_cuadrados / contador if contador > 0 else 0
            self.log_area.append(f"Varianza calculada: {varianza:.4f}")

    def calcular_rango_normal(self):
        if self.signal is not None:
            max_valor = self.signal[0, 0]
            min_valor = self.signal[0, 0]

            for valor in self.signal[:, 0]:
                if valor > max_valor:
                    max_valor = valor
                if valor < min_valor:
                    min_valor = valor

            rango = max_valor - min_valor
            self.log_area.append(f"Rango calculado: {rango:.4f}")

    def calcular_desviacion_estandar_normal(self):
        if self.signal is not None:
            # Calcular la media
            suma = sum(self.signal[:, 0])
            n = len(self.signal[:, 0])
            media = suma / n if n > 0 else 0

            # Calcular la desviación estándar manualmente
            suma_cuadrados = sum((valor - media) ** 2 for valor in self.signal[:, 0])
            desviacion_estandar = (suma_cuadrados / n) ** 0.5 if n > 0 else 0

            self.log_area.append(f"Desviación estándar calculada: {desviacion_estandar:.6f}")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

            


        #SNR Y RUIDOS 
    def agregar_ruido_gaussiano(self):
        if self.signal is not None:
            media = 0  # Media del ruido
            desviacion = 0.1  # Desviación estándar del ruido
            ruido = np.random.normal(media, desviacion, size=self.signal[:, 0].shape)
        
            # Señal con ruido
            self.signal_con_ruido = self.signal[:, 0] + ruido

            # Mostrar gráfica
            plt.figure(figsize=(10, 6))
            plt.plot(self.signal[:, 0], label='Señal original', color='purple')
            plt.plot(self.signal_con_ruido, label='Señal con ruido gaussiano', color='skyblue', alpha=0.7)
            plt.title("Señal EMG con Ruido Gaussiano")
            plt.xlabel("Tiempo (Segundos)")
            plt.ylabel("Amplitud (mV)")
            plt.legend()
            plt.grid()
            plt.show()

            self.log_area.append("Ruido gaussiano agregado a la señal.")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def agregar_ruido_impulso(self):
        if self.signal is not None:
            probabilidad = 0.05  # Probabilidad de un impulso
            amplitud_impulso = 1.5  # Amplitud del impulso
            num_muestras = len(self.signal[:, 0])

            # Generación de ruido impulsivo
            ruido_impulso = np.zeros(num_muestras)
            indices_impulso = np.random.choice([0, 1], size=num_muestras, p=[1 - probabilidad, probabilidad])
            ruido_impulso[indices_impulso == 1] = amplitud_impulso * (2 * np.random.rand(np.sum(indices_impulso)) - 1)

            # Señal con ruido impulsivo
            self.signal_con_ruido = self.signal[:, 0] + ruido_impulso

            # Mostrar gráfica
            plt.figure(figsize=(10, 6))
            plt.plot(self.signal[:, 0], label='Señal original', color='purple')
            plt.plot(self.signal_con_ruido, label='Señal con ruido impulsivo', color='orange', alpha=0.7)
            plt.title("Señal EMG con Ruido Impulsivo")
            plt.xlabel("Tiempo (Segundos)")
            plt.ylabel("Amplitud (mV)")
            plt.legend()
            plt.grid()
            plt.show()

            self.log_area.append("Ruido impulsivo agregado a la señal.")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def agregar_ruido_artefacto(self):
        if self.signal is not None:
            num_muestras = len(self.signal[:, 0])

            # Simulación de artefacto por movimiento (picos grandes aleatorios)
            num_artefactos = int(num_muestras * 0.02)  # Artefactos en el 2% de las muestras
            amplitud_artefacto = np.max(self.signal[:, 0]) * 2  # Doble de la amplitud máxima

            # Crear artefactos en posiciones aleatorias
            artefacto_ruido = np.zeros(num_muestras)
            posiciones = np.random.choice(num_muestras, num_artefactos, replace=False)

            for pos in posiciones:
                artefacto_ruido[pos:pos + 10] = amplitud_artefacto * (np.random.rand(10) - 0.5)

            # Señal con artefacto
            self.signal_con_ruido = self.signal[:, 0] + artefacto_ruido

            # Mostrar gráfica
            plt.figure(figsize=(10, 6))
            plt.plot(self.signal[:, 0], label='Señal original', color='purple')
            plt.plot(self.signal_con_ruido, label='Señal con artefacto', color='pink', alpha=0.7)
            plt.title("Señal EMG con Artefacto por Movimiento")
            plt.xlabel("Tiempo (Segundos)")
            plt.ylabel("Amplitud (mV)")
            plt.legend()
            plt.grid()
            plt.show()

            self.log_area.append("Ruido tipo artefacto agregado a la señal.")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")

    def agregar_ruido_gaussiano_amplificado(self):
        if self.signal is not None:
            # Parámetros del ruido
            mu = 0  # Media del ruido
            sigma = 0.01 * np.ptp(self.signal[:, 0])  # Desviación estándar basada en el rango de la señal
            ruido = np.random.normal(mu, sigma, self.signal[:, 0].shape)
            
            # Factor de amplificación
            amplificacion_factor = 3  # Amplificación por un factor de 3
            ruido_amplificado = ruido * amplificacion_factor
            
            # Aplicar el ruido a la señal
            señal_ruido_amplificado = self.signal[:, 0] + ruido_amplificado

            # Mostrar la señal con ruido en el gráfico
            plt.figure(figsize=(18, 4))
            plt.plot(self.signal[:, 0], label="Señal Original", color='purple')
            plt.plot(señal_ruido_amplificado, label="Señal con Ruido Gaussiano Amplificado", color='red')
            plt.title("Señal EMG con Ruido Gaussiano Amplificado")
            plt.xlabel("Tiempo")
            plt.ylabel("Amplitud (mV)")
            plt.legend()
            plt.grid()
            plt.show()

            self.log_area.append("Ruido gaussiano amplificado agregado a la señal.")
        else:
            QMessageBox.warning(self, "Error", "No hay datos cargados.")


    def calcular_snr(self):
        if hasattr(self, 'signal_con_ruido'):
            potencia_señal = np.mean(self.signal[:, 0] ** 2)
            potencia_ruido = np.mean((self.signal_con_ruido - self.signal[:, 0]) ** 2)

            if potencia_ruido == 0:
                snr = float('inf')  # Ruido nulo
            else:
                snr = 10 * np.log10(potencia_señal / potencia_ruido)

            self.log_area.append(f"SNR calculado: {snr:.6f} dB")
        else:
            QMessageBox.warning(self, "Error", "Primero agrega ruido a la señal.")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = Principal()
    viewer.show()
    sys.exit(app.exec())
