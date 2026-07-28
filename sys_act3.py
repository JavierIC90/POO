import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz

# ==========================================================
# ACTIVIDAD FORMATIVA 3
# Implementación y evaluación de filtros digitales
# Autor: Francisco Javier Iracheta Carrion
# Matricula: 70217
# ==========================================================

# ----------------------------------------------------------
# 1. Definición de la señal de entrada
# ----------------------------------------------------------

# Frecuencia de muestreo
fs = 500  # Hz

# Tiempo de la señal (2 segundos)
t = np.linspace(0, 2, 2 * fs, endpoint=False)

# Señal compuesta
senal_baja = np.sin(2 * np.pi * 5 * t)      # 5 Hz
senal_alta = 0.5 * np.sin(2 * np.pi * 50 * t)  # 50 Hz

senal = senal_baja + senal_alta

# Agregar ruido blanco
ruido = 0.4 * np.random.randn(len(t))

senal_ruidosa = senal + ruido

# ----------------------------------------------------------
# 2. Diseño de filtros Butterworth (IIR)
# ----------------------------------------------------------

orden = 4

# Frecuencia de Nyquist
nyquist = fs / 2

# ----- Pasa Bajos -----
fc_baja = 10
b_low, a_low = butter(
    orden,
    fc_baja / nyquist,
    btype='low'
)

# ----- Pasa Altos -----
fc_alta = 20
b_high, a_high = butter(
    orden,
    fc_alta / nyquist,
    btype='high'
)

# ----- Pasa Bandas -----
fc1 = 40
fc2 = 60

b_band, a_band = butter(
    orden,
    [fc1 / nyquist, fc2 / nyquist],
    btype='band'
)

# ----------------------------------------------------------
# 3. Aplicación de los filtros
# ----------------------------------------------------------

senal_low = filtfilt(b_low, a_low, senal_ruidosa)

senal_high = filtfilt(b_high, a_high, senal_ruidosa)

senal_band = filtfilt(b_band, a_band, senal_ruidosa)

# ----------------------------------------------------------
# 4. Visualización de señales
# ----------------------------------------------------------

plt.figure(figsize=(14,10))

plt.subplot(4,1,1)
plt.plot(t, senal_ruidosa)
plt.title("Señal con ruido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(4,1,2)
plt.plot(t, senal_low,color='green')
plt.title("Filtro Pasa Bajos")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(4,1,3)
plt.plot(t, senal_high,color='red')
plt.title("Filtro Pasa Altos")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(4,1,4)
plt.plot(t, senal_band,color='purple')
plt.title("Filtro Pasa Bandas")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()

# ----------------------------------------------------------
# 5. Respuesta en frecuencia
# ----------------------------------------------------------

plt.figure(figsize=(12,8))

w, h = freqz(b_low, a_low)

plt.plot(
    w * fs / (2 * np.pi),
    20 * np.log10(abs(h)),
    label="Pasa Bajos"
)

w, h = freqz(b_high, a_high)

plt.plot(
    w * fs / (2 * np.pi),
    20 * np.log10(abs(h)),
    label="Pasa Altos"
)

w, h = freqz(b_band, a_band)

plt.plot(
    w * fs / (2 * np.pi),
    20 * np.log10(abs(h)),
    label="Pasa Bandas"
)

plt.title("Respuesta en frecuencia de los filtros")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.grid()
plt.legend()

# ----------------------------------------------------------
# 6. Comparación entre señal original y filtrada
# ----------------------------------------------------------

plt.figure(figsize=(14,8))

plt.plot(
    t,
    senal_ruidosa,
    label="Señal con ruido",
    alpha=0.5
)

plt.plot(
    t,
    senal_low,
    label="Pasa Bajos"
)

plt.plot(
    t,
    senal_high,
    label="Pasa Altos"
)

plt.plot(
    t,
    senal_band,
    label="Pasa Bandas"
)

plt.title("Comparación de señales")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.show()