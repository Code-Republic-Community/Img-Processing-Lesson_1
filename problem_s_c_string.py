key = 'var'
value = 1.234
correct = '%-10s = %.2f' % (key, value)
print(correct)
incorrect = '%-10s = %.2f' % (value, key)
print(incorrect)

