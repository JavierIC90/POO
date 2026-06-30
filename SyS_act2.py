# ============================================================
# Actividad: Transformada de Fourier
# Autor: Francisco Javier Iracheta Carrion
# ============================================================

# Importar librerías
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Definición del dominio del tiempo
# ============================================================

# Tiempo desde -2 hasta 2 segundos
t = np.linspace(-2, 2, 1000)

# Número de muestras
N = len(t)

# Tiempo entre muestras
dt = t[1] - t[0]

# Eje de frecuencias
frecuencia = np.fft.fftfreq(N, d=dt)

# ============================================================
# 2. Creación de señales
# ============================================================

# Señal senoidal de 5 Hz
senal_seno = np.sin(2 * np.pi * 5 * t)

# Función escalón
senal_escalon = np.where(t >= 0, 1, 0)

# Pulso rectangular
senal_pulso = np.where(np.abs(t) <= 0.5, 1, 0)

# ============================================================
# 3. Dominio del tiempo
# ============================================================

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(t, senal_seno)
plt.title("Señal senoidal")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t, senal_escalon)
plt.title("Función escalón")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t, senal_pulso)
plt.title("Pulso rectangular")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()

# ============================================================
# 4. Transformada de Fourier
# ============================================================

fft_seno = np.fft.fft(senal_seno)
fft_escalon = np.fft.fft(senal_escalon)
fft_pulso = np.fft.fft(senal_pulso)

# ============================================================
# 5. Magnitud del espectro
# ============================================================

plt.figure(figsize=(12,9))

plt.subplot(3,1,1)
plt.plot(frecuencia, np.abs(fft_seno))
plt.title("Magnitud del espectro - Señal senoidal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()

plt.subplot(3,1,2)
plt.plot(frecuencia, np.abs(fft_escalon))
plt.title("Magnitud del espectro - Función escalón")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()

plt.subplot(3,1,3)
plt.plot(frecuencia, np.abs(fft_pulso))
plt.title("Magnitud del espectro - Pulso rectangular")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()

plt.tight_layout()
plt.show()

# ============================================================
# 6. Fase del espectro
# ============================================================

plt.figure(figsize=(12,9))

plt.subplot(3,1,1)
plt.plot(frecuencia, np.angle(fft_seno))
plt.title("Fase - Señal senoidal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid()

plt.subplot(3,1,2)
plt.plot(frecuencia, np.angle(fft_escalon))
plt.title("Fase - Función escalón")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid()

plt.subplot(3,1,3)
plt.plot(frecuencia, np.angle(fft_pulso))
plt.title("Fase - Pulso rectangular")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid()

plt.tight_layout()
plt.show()

# ============================================================
# 7. Propiedad de linealidad
# ============================================================

# Crear una nueva señal sumando la senoidal y el pulso
senal_lineal = senal_seno + senal_pulso

# Transformada de la nueva señal
fft_lineal = np.fft.fft(senal_lineal)

# Suma de las transformadas individuales
fft_suma = fft_seno + fft_pulso

# Comparación gráfica
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(frecuencia, np.abs(fft_lineal))
plt.title("Transformada de la suma")
plt.xlabel("Frecuencia (Hz)")
plt.grid()

plt.subplot(1,2,2)
plt.plot(frecuencia, np.abs(fft_suma))
plt.title("Suma de las transformadas")
plt.xlabel("Frecuencia (Hz)")
plt.grid()

plt.tight_layout()
plt.show()