import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ----------------- CONFIGURAÇÃO DO GOOGLE FORMS -----------------
# ATENÇÃO: Mude o final da URL de 'viewform' para 'formResponse'
URL_FORMULARIO = "https://docs.google.com/forms/d/e/1FAIpQLSeqCqewT71tPiBlODxyaNGoPnpTvcE2fyyHn3_AYMX45XJ6lw/formResponse"

# Substitua os números abaixo pelos IDs reais que você inspecionou no seu formulário:
ID_CAMPO_ENDERECO = "entry.245485707"
ID_CAMPO_VALOR    = "entry.1487527207"
ID_CAMPO_LINK     = "entry.823921287"
# ----------------------------------------------------------------

# 1. URL estruturada do Imovelweb com os filtros: Casas, Aluguel, Curitiba, até R$3000, ordenado por menor preço
url = "https://www.imovelweb.com.br/casas-aluguel-curitiba-pr-ordem-precio-menor-precio-0-3000.html"

# Configurações do Selenium para evitar detecção básica
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
# Se quiser rodar sem abrir a janela do navegador em segundo plano, descomente a linha abaixo:
# chrome_options.add_argument("--headless") 

# Inicia o navegador automatizado
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

print("Acessando o Imovelweb...")
driver.get(url)

# Aguarda 6 segundos para garantir o carregamento do conteúdo dinâmico e passar por verificações de bot
time.sleep(6)

# passa o HTML renderizado pelo navegador para o BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()  # Fecha o navegador, pois já temos o HTML necessário

# 2. Localiza os cards de propriedades através do atributo "data-to-posting"
cards = soup.find_all(attrs={"data-to-posting": True})

# 2. ENVIANDO OS DADOS PARA O GOOGLE FORMS
for i, card in enumerate(cards, 1):
    # Extração dos dados
    link_relativo = card.get("data-to-posting")
    link_completo = f"https://www.imovelweb.com.br{link_relativo}"

    preco_element = card.find(attrs={"data-qa": "POSTING_CARD_PRICE"})
    valor_mes = preco_element.text.strip() if preco_element else "Valor não informado"

    loc_element = card.find(attrs={"data-qa": "POSTING_CARD_LOCATION"})
    endereco = loc_element.text.strip() if loc_element else "Endereço indisponível"

    # Organiza os dados no formato que o Google Forms espera receber
    dados_formulario = {
        ID_CAMPO_ENDERECO: endereco,
        ID_CAMPO_VALOR: valor_mes,
        ID_CAMPO_LINK: link_completo
    }

    # Envia os dados via requisição POST (simula o clique no botão 'Enviar')
    resposta = requests.post(URL_FORMULARIO, data=dados_formulario)

    if resposta.status_code == 200:
        print(f"[{i}/{len(cards)}] Sucesso! Imóvel enviado: {endereco[:30]}...")
    else:
        print(f"[{i}/{len(cards)}] Erro ao enviar imóvel. Status: {resposta.status_code}")

    # Uma pequena pausa de 1 segundo para evitar que o Google bloqueie por excesso de requisições rápidas
    time.sleep(1)

print("\nProcesso concluído! Verifique a planilha de respostas do seu Google Forms.")







# lista_propriedades = []
#
# print(f"\nForam encontrados {len(cards)} imóveis nesta página.\n")
#
# for card in cards:
#     # Extrai o link (O atributo data-to-posting traz o caminho relativo)
#     link_relativo = card.get("data-to-posting")
#     link_completo = f"https://www.imovelweb.com.br{link_relativo}"
#
#     # Extrai o valor do aluguel mensal usando a tag de QA do Imovelweb
#     preco_element = card.find(attrs={"data-qa": "POSTING_CARD_PRICE"})
#     valor_mes = preco_element.text.strip() if preco_element else "Valor não informado"
#
#     # Extrai a localização/endereço (Geralmente fica na tag de localização de QA do card)
#     # Caso a tag mude, buscamos pelo componente que descreve a localização no topo/corpo do card
#     loc_element = card.find(attrs={"data-qa": "POSTING_CARD_LOCATION"})
#     if not loc_element:
#         # Fallback caso mudem o padrão da tag de localização
#         loc_element = card.find(class_=lambda x: x and 'Location' in x)
#
#     endereco = loc_element.text.strip() if loc_element else "Endereço indisponível no card"
#
#     # Adiciona o dicionário estruturado à lista
#     lista_propriedades.append({
#         "endereco": endereco,
#         "valor": valor_mes,
#         "link": link_completo
#     })
#
# # 3. Exibe o resultado formatado na tela
# for i, prop in enumerate(lista_propriedades, 1):
#     print(f"Propriedade #{i}")
#     print(f"📍 Endereço: {prop['endereco']}")
#     print(f"💰 Valor/Mês: {prop['valor']}")
#     print(f"🔗 Link: {prop['link']}")
#     print("-" * 60)