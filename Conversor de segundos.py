segundos_str = input('Por favor, entre com o número de segundos que deseja converter: ')
total_segs = int(segundos_str)

dias = total_segs // 86400
segundos_restdias = total_segs % 86400
horas = segundos_restdias // 3600
segundos_resthoras = segundos_restdias % 3600
minutos = segundos_resthoras // 60
segundos = segundos_resthoras % 60


print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')
