'''
Construa uma função que ordene os alunos por nota.
Se houver empate em nota o nome deverá definir a ordem.
'''

alunos=[('Renzo', 9), ('Luciano', 10), ('Ada', 10), ('Andre', 10), ('Eduarda', 7), ('Elana', 7)]

def ordenar():
    ord_notas = []
    nova_lista = []
    # ordena por nota primeiro
    alunos.sort(key=lambda aluno: aluno[1])
    # guarda as difererentes notas
    for _, nota in alunos:
        if nota not in ord_notas:
            ord_notas.append(nota)
    # gera nova lista ordenando agora por nome
    for _nota in ord_notas:
        _lista = [(nome, nota) for nome, nota in alunos if nota == _nota]
        _lista.sort(key=lambda aluno: aluno[0])
        nova_lista += _lista

    return nova_lista

print(ordenar())