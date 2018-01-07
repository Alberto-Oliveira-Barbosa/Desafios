# -*- coding: utf-8 -*-
notas = raw_input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

msg=""

n1*=2.0
n2*=3.0
n3*=4.0
exame = False


media = (n1+n2+n3+n4)/10.0

if media>=7.0:
    msg = "Aluno aprovado."
elif media < 5.0:
    msg ="Aluno reprovado."
else:
    msg = "Aluno em exame."
    exame = True
print("Media: %.1f\n%s" % (media, msg))
if exame:
    ex = float(input())
    media = (media+ex)/2.0
    msg = "Aluno reprovado." if media < 5 else "Aluno aprovado."

    print("Nota do exame: %.1f\n%s\nMedia final: %.1f" % (ex,msg,media))
    
