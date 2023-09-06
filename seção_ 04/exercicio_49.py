
hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite o minuto de início: "))
segundo_inicio = int(input("Digite o segundo de início: "))


duracao_segundos = int(input("Digite a duração da experiência em segundos: "))


segundo_total_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
segundo_total_termino = segundo_total_inicio + duracao_segundos

hora_termino = segundo_total_termino // 3600
segundo_total_termino %= 3600
minuto_termino = segundo_total_termino // 60
segundo_termino = segundo_total_termino % 60


print(f"O horário de término da experiência é: {hora_termino}:{minuto_termino}:{segundo_termino}")
