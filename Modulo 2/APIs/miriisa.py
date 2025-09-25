import requests

url = "https://classroom.google.com/c/Nzc3NzQxOTU5NDA4/m/NzgwNjk1ODgwNjY4/details"


informação = requests.get(url)

if 200<= informação.status_code <=299:
    print ("Requisição bem-sucedida!",informação.status_code)
elif 400<= informação.status_code <=499:
    print ("Erro na requisição",informação.status_code)


else:
    print("numero fora de range")