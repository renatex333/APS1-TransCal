from math import cosh, sinh, sqrt, tanh
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# T_Kelvin = T_Celsius + 273.15

# Parâmetros para o nosso grupo: Seção transversal retangular
L = 0.175 # Comprimento da aleta em m
t = 0.02 # Espessura da aleta
w = 0.24 # Largura da aleta
P = 0.52 # Perímetro da seção transversal em m
A = 0.0048 # Área da seção transversal em m^2
h = 20 # Coeficiente de convecção em W/ m^2 * K
As = (2 * L * t) + (w * t) + (2 * L * w) # Área da superfície
Ab = (w * t) # Área da base

# Parâmetros gerais
k_Al = 240 # Condutividade do material em W/m*K
T = 25 + 273.15 # T_infinito é a temepratura do ambiente em K
Tb = 100 + 273.15 # Tb é a temperatura da base em K
x = L # Condição de contorno na extremidade da aleta

# Exercício I

# 1. Calcular a temperatura na extremidade da aleta e plotar gráfico da 
# distribuição de temperatura ao longo da aleta.

# Temperatura na extremidade da aleta (T_L)

# Função que calcula a distribuição de temperaturas para transferência de calor por convecção
def calcula_distribuicao_de_temperaturas(h, P, k, A, L, x):

    m = sqrt((h*P)/(k*A))

    const = h / (m * k)

    numerador = cosh(m * (L - x)) + const * sinh(m * (L - x))
    denominador = cosh(m * L) + const * sinh(m * L)

    distribuicao_de_temperaturas = numerador / denominador

    return distribuicao_de_temperaturas

distribuicao_de_temperaturas = calcula_distribuicao_de_temperaturas(h, P, k_Al, A, L, x)

T_L = (distribuicao_de_temperaturas * (Tb - T)) + T

print(f"Temperatura na extremidade da aleta: {T_L} K")

# Gráfico da distribuição de temperaturas ao longo do comprimento da aleta

lista_distr_temps = []
lista_x_aleta = np.arange(0, L+0.001, 0.001)

for x in lista_x_aleta:
    distr_temp_x = calcula_distribuicao_de_temperaturas(h, P, k_Al, A, L, x)
    lista_distr_temps.append(distr_temp_x)

fig, ax = plt.subplots()
ax.plot(lista_x_aleta, lista_distr_temps, color="red")
ax.set(xlabel='Comprimento da aleta (m)', ylabel='Distribuição de temperatura',
       title='Distribuição de temperatura ao longo da aleta')
plt.grid()
fig.savefig("Atividades\APS 1\Distribuição_de_temperatura.png")
# plt.show()

# 2. Taxa de transferência de calor

# Função que calcula a distribuição de temperaturas para transferência de calor por convecção
def calcula_transferencia_de_calor(h, P, k, A, L, x, T, Tb):
    thetab = Tb - T
    M = sqrt(h*P*k*A) * thetab
    m = sqrt((h*P)/(k*A))

    const = h / (m * k)

    numerador = sinh(m * L) + const * cosh(m * L)
    denominador = cosh(m * L) + const * sinh(m * L)

    taxa_de_transferencia_de_calor = M * (numerador / denominador)

    return taxa_de_transferencia_de_calor

taxa_de_transferencia_de_calor = calcula_transferencia_de_calor(h, P, k_Al, A, L, x, T, Tb)

print(f"Taxa de transferência de calor: {taxa_de_transferencia_de_calor} W")

# 3. Eficiência da aleta

thetab = Tb - T
eficiencia = taxa_de_transferencia_de_calor/(h * As * thetab)

print(f"Eficiênica da aleta: {eficiencia}")

# 4. Efetividade da aleta

efetividade = taxa_de_transferencia_de_calor/(h * Ab * thetab)

print(f"Efetividade: {efetividade}")

# 5. Taxa de transferência de calor para aleta infinita

taxa_de_transferencia_de_calor_aleta_infinita = sqrt(h*P*k_Al*A) * thetab

print(f"Taxa de transferência de calor para aleta infinita: {taxa_de_transferencia_de_calor_aleta_infinita} W")

# 6. Comparando modelo de aleta finita e aleta infinita
print("Numericamente é diferente, porque ...")

# 7. Descobrir o comprimento mínimo para que a hipótese de aleta infinita forneça uma medida precisa para
# a taxa de transferência de calor

# Se thetab = 0, Tb = Tamb, e portanto, podemos considerar uma condição adiabática na extremidade
# M ~ M*tanh(m * L)
# tanh(m * L) >= 0.99

m = sqrt((h*P)/(k_Al*A))

L_minimo = L

while(tanh(m * L_minimo) < 0.99):
    L_minimo += 0.001

print(f"O comprimento mínimo da aleta: {L_minimo:.3f} m")

# Exercício II




