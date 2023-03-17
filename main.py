import yaml

with open('example.yaml', 'r') as file:
    dados = yaml.load(file, Loader=yaml.FullLoader)

print(dados)