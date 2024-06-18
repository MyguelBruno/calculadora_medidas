from classes import Medidas, Info
from dataclasses import dataclass
from pathlib import Path
import PySimpleGUI as sg

    
#INTERFACE
layout = [
    [sg.Text("CALCULADORA DE MEDIDAS")],
    
    [sg.Text("Largura:"), sg.InputText(key="largura")],
    [sg.Text("Altura:"), sg.InputText(key="altura")],
    [sg.Text("Valor do Metro Quadrado:"), sg.InputText(key="valor_metro_quadrado")],

    [sg.Text("Descrição do Serviço:"), sg.InputText(key="descricao")],
    [sg.Text("Data de Entrega:"), sg.InputText(key="data_entrega")],

    [sg.Text("Nome do Cliente:"), sg.InputText(key="nome_cliente")],
    [sg.Text("Telefone do Cliente:"), sg.InputText(key="tel_cliente")],

    [sg.Button("ENVIAR"), sg.Text("", key="confirmacao")],
]


janela = sg.Window("Calculadora de medidas", layout)



while True:
    evento, valores = janela.read()


    largura = float(valores["largura"])
    altura = float(valores["altura"])
    valor_metro_quadrado = float(valores["valor_metro_quadrado"])

    descricao = valores["descricao"]
    data_entrega = valores["data_entrega"]

    nome_cliente = valores["nome_cliente"]
    tel_cliente = valores["tel_cliente"]

    if valores["descricao"] == "":
        descricao = "_Não informado_"
    
    if valores["data_entrega"] == "":
        data_entrega = "_Não informado_"
        
    if valores["nome_cliente"] == "":
        nome_cliente = "_Não informado_"

    if valores["tel_cliente"] == "":
        tel_cliente = "_Não informado_"

    
    if evento == "ENVIAR":

         
        #CALCULO MEDIDA E VALOR
        informacoes_medidas = Medidas(largura=largura, altura=altura, valor_por_metro=valor_metro_quadrado)
        metros_quadrados = informacoes_medidas.calcular_metro_quadrado()
        valor_total = informacoes_medidas.calcular_valor_total()


        #VARIAVEL QUE ENVIA E RECEBE INFORMAÇÕES DO CLIENTE 
        informacoes_cliente = Info(desc_trabalho=descricao, tel_cliente=tel_cliente)
        telefone_cliente = informacoes_cliente.info_exibir()
        descricao_trabalho = informacoes_cliente.info_exibir()

        

        #GERADOR DE PASTAS
        dir_path = Path(f"./projetos/calculadora_medidas/{nome_cliente}")
        dir_path.mkdir(parents=True, exist_ok=True)

        #GERADOR DE ARQUIVO TXT
        
        arquivo_path = dir_path / f"{nome_cliente}.txt"
        with open(arquivo_path, "w") as arquivo_infos:

            arquivo_infos.write(f"METROS QUADRADOS: {metros_quadrados:.2f}m² | VALOR TOTAL: R${valor_total:.2f}\n")
            arquivo_infos.write(f"VALOR DO METRO QUADRADO: R${valor_metro_quadrado:.2f}\n")
            arquivo_infos.write(f"LARGURA: {largura}m | ALTURA: {altura}m\n\n")

            arquivo_infos.write(f"DESCRIÇÃO DO TRABALHO: {descricao}\n")
            arquivo_infos.write(f"DATA DE ENTREGA: {data_entrega}\n\n")

            arquivo_infos.write(f"NOME DO CLIENTE: {nome_cliente}\n")
            arquivo_infos.write(f"CONTATO DO CLIENTE: {tel_cliente}\n\n-------")

            janela["confirmacao"].update("PASTA CRIADA COM SUCESSO!")


    if evento == sg.WIN_CLOSED:
        break

janela.close()
