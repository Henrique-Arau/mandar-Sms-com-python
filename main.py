import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8b5172a3ef7754bd126588068758af43"
# Your Auth Token from twilio.com/console
auth_token  = "d8061ebdb3d2ff617a6a4bbe3175ebea"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f' No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5561992324542",#coloca o numero de cadastro do twilio
            from_="+19894738556",
            body=f' No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)



#Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o nome, o mês e as vendas dele

# Caso não seja maior do que 55.000 não quero fazer nada


