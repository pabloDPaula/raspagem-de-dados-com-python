import pandas as pd
from utils import Automacao

try:
    nome_jogo = input(str('Digite o nome do jogo que quer procurar: ')).strip()

    # browser = abri_navegador()
    automacao = Automacao(nome_jogo)

    url = "https://store.steampowered.com/?l=portuguese"
    xpath_input_busca = '//*[@id="store_nav_search_term"]'
    xpath_filtro = '//*[@id="additional_search_options"]/div[1]/div[2]/div[4]/span/span/span[1]'
    steam = automacao.busca_jogo(url,xpath_input_busca,'title','discount_final_price',xpath_filtro,True)

    url = "https://www.nuuvem.com/br-pt/"
    xpath_input_busca = '//*[@id="header-search-small"]/div/input'
    nuuvem = automacao.busca_jogo(url,xpath_input_busca,'product-title','product-price--val')


    lista_final = {
        'Nome': [],
        'Preço Steam': [],
        'Preço Nuuvem': []
    }

    for i,jogo_steam in enumerate(steam):
        for i,jogo_nuuvem in enumerate(nuuvem):
            if(jogo_steam['nome'].lower() == jogo_nuuvem['nome'].lower()):
                # lista_final.append({'nome': jogo_steam['nome'], 'preco-steam': jogo_steam['preco'], 'preco-nuuvem': jogo_nuuvem['preco']})
                lista_final['Nome'].append(jogo_steam['nome'])
                lista_final['Preço Steam'].append(jogo_steam['preco'].replace('R$','').replace(',','.'))
                lista_final['Preço Nuuvem'].append(jogo_nuuvem['preco'].replace('R$ ','').replace(',','.'))

    #
    # print('\n************* Steam e Nuuvem *************')
    # for jogo in lista_final:
    #     print(f"Nome: {jogo['nome']}\n preço na STEAM: {jogo['preco-steam']}\n preço na NUUVEM: {jogo['preco-nuuvem']}\n")

    if(len(lista_final['Nome']) != 0):
        df = pd.DataFrame(lista_final)
        with pd.ExcelWriter(f'Relatorio - {nome_jogo}.xlsx') as writer:
            df.to_excel(writer,index=False)
    # else:
    #     df = pd.DataFrame('Não existem jogos iguais nas duas plataformas ( STEAM e NUUVEM ) para comparar')
    #     df.to_excel('Relatório - Steam e Nuuvem')

    automacao.fecha_navegador()
except Exception as err:
    print(err)

