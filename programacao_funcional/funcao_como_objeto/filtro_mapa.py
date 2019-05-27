import operator
alunos=[('Renzo', 0), ('Luciano', 10), ('Ada', 9)]

print ('filter com list comprehension')
print([(nome, nota) for nome, nota in alunos if nota > 5])
print ('map com list comprehension')
print([nome for nome, nota in alunos if nota > 5])


def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5
print('filter')
print(list(filter(possui_nota_maior_que_5, alunos)))


def extrair_nome(aluno):
    nome, nota = aluno
    return nome

print('map')
print(list(map(extrair_nome, filter(possui_nota_maior_que_5, alunos))))

# utilizando o operator para, fazer a mesma coisa que a funcao, extrair_nome
print('')
print('operator')
print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))
