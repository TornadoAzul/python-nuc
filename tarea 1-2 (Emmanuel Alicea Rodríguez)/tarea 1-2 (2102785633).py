# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 2 de septiembre de 2023.
# Tarea 1.2.

# Explicación:
# Este programa imprimirá usando format 3 fíguras horizontal
# y verticalmente.

# ↕️ Vertical
# Triángulo
print('{0:^5}'.format('*'))
print('{0:^5}'.format('***'))
print('{0:^5}'.format('*****'))
print('{0:^5}'.format(''))
print('{0:^5}'.format(''))

# Diamante
print('{0:^7}'.format('*'))
print('{0:^7}'.format('***'))
print('{0:^7}'.format('*****'))
print('{0:^7}'.format('***'))
print('{0:^7}'.format('*'))
print('{0:^5}'.format(''))
print('{0:^5}'.format(''))

# Flecha
print('{0:^7}'.format('*'))
print('{0:^7}'.format('*******'))
print('{0:^7}'.format('*'))
print('{0:^7}'.format('*'))
print('{0:^7}'.format('*'))
print('{0:^5}'.format(''))
print('{0:^5}'.format(''))

# ↔️ Horizontal

# Línea 1
print('{0:^10} {1:^10} {2:^10}'.format('Triángulo', 'Diamante', 'Flecha'))

# Línea 2
print('{0:1} {1:^6} {2:^15} {3:^6} {4:^15} {5:^6} {6:^15}'.format('*', '*', '*', '*', '*', '*', '*'))

# Línea 3
print('{0:1} {1:^6} {2:^14} {3:^6} {4:^14} {5:^6} {6:^14}'.format('*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'))

# Línea 4
print('{0:1} {1:^6} {2:^14} {3:^6} {4:^14} {5:^6} {6:^14}'.format('*', '* *', '* * *', '*', '* * *', '*', '* * *'))

# Línea 5
print('{0:1} {1:^6} {2:^14} {3:^6} {4:^14} {5:^6} {6:^14}'.format('*', '* * *', '* * * *', '*', '* * * *', '*', '* * * *'))

# Línea 6
print('{0:1} {1:^6} {2:^14} {3:^6} {4:^14} {5:^6}'.format('*', '* * * *', '* * * * *', '*', '* * * * *', '*'))

# Línea 7
print('{0:1} {1:^6} {2:^14}'.format('*', '* * *', '* * *'))

# Línea 8
print('{0:1} {1:^6} {2:^14}'.format('*', '* *', '* *'))

# Línea 9
print('{0:1} {1:^6} {2:^14}'.format('*', '*', '*'))

# Línea 10 (Espacio)
print('{0:^34}'.format('*'))

