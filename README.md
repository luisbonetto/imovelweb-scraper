# imovelweb-scraper

Este é um projeto desenvolvido em Python focado na automação de coleta de dados (Web Scraping) no portal Imovelweb. O script busca anúncios de imóveis utilizando critérios de filtragem específicos, extrai as principais informações de interesse e realiza o preenchimento automatizado em um formulário do Google Forms.

O projeto foi construído para simular uma rotina automatizada de monitoramento de oportunidades imobiliárias para locação.

## 🚀 Funcionalidades

* **Filtro Customizado:** Coleta automática de casas para aluguel em Curitiba/PR com teto de orçamento definido (R$ 3.000,00).
* **Extração de Dados:** Raspagem inteligente de informações cruciais diretamente da página de listagem:
  * Endereço/Localização da propriedade.
  * Valor mensal do aluguel.
  * Link direto do anúncio do imóvel.
* **Integração com Google Forms:** Envio em lote dos dados capturados diretamente para um banco de dados de respostas (planilha vinculada) via requisições HTTP (`POST`), sem a necessidade de digitação manual.

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Linguagem base)
* **Selenium WebDriver:** Utilizado para contornar proteções antibot (DataDome) e renderizar o conteúdo dinâmico (JavaScript) do site.
* **BeautifulSoup4:** Responsável por analisar o HTML renderizado e extrair as tags específicas de dados (`data-qa`).
* **Requests:** Utilizado para otimizar o envio direto dos dados para a API de recebimento do Google Forms via requisição assíncrona.
* **WebDriver Manager:** Gerenciamento automático do binário do ChromeDriver para o navegador.

## 📋 Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado:
* Python 3.x
* Google Chrome instalado no sistema

## 🔧 Como Executar o Projeto

1. Clone o repositório:
```bash
   git clone [https://github.com/SEU_USUARIO/imovelweb-scraper.git](https://github.com/SEU_USUARIO/imovelweb-scraper.git)