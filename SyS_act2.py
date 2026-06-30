# ============================================================
# Actividad: Transformada de Fourier
# Autor: Francisco Javier Iracheta Carrion
# ============================================================

# Importar librerías
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Definición del dominio del tiempo
# ------------------------------------------------------------

# Tiempo desde -2 hasta 2 segundos
t = np.linspace(-2, 2, 1000)

# ------------------------------------------------------------
# Creación de señales
# ------------------------------------------------------------

# Señal senoidal (5 Hz)
senal_seno = np.sin(2 * np.pi * 5 * t)

# Función escalón
senal_escalon = np.where(t >= 0, 1, 0)

# Pulso rectangular
senal_pulso = np.where(np.abs(t) <= 0.5, 1, 0)

# ------------------------------------------------------------
# Graficar las señales
# ------------------------------------------------------------

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(t, senal_seno)
plt.title("Señal senoidal")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t, senal_escalon)
plt.title("Función escalón")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t, senal_pulso)
plt.title("Pulso rectangular")
plt.grid()

plt.tight_layout()
plt.show()