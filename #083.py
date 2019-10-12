"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressao = input('Digite uma expressão matemática: ').upper().strip()
parenteses = []
for i in expressao:
    if i == '(':
        parenteses.append('(')
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
if len(parenteses) == 0:
    print('A expressão está correta!', len(parenteses))
else:
    print('A expressão está incorreta!')