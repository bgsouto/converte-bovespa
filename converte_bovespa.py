# -*- coding: utf-8 -*-
"""
Converte arquivos de historico de cotação da bovespa para um padrão .CSV
que permite a abertura e tratamento no EXCEL.

Para entender o layout do arquivo:
http://www.bmfbovespa.com.br/lumis/portal/file/fileDownload.jsp?fileId=8A828D294E9C618F014EB7924B803F8B

Para pegar cotações históricas:
http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/cotacoes-historicas/

Created on Fri Aug 17 15:54:43 2018

@author: Bruno Guedes Souto
"""

arquivo_formatado=open("C:/Users/c122802/Documents/Estudos/ARQUIVO_FORMATADO.csv", "w+")
#local que deseja que seja salvo o arquivo .csv

arquivo_formatado.write ("TIP REG;DATA PREGAO;CODBDI;CODNEG;TPMERC;EMPRESA;ESPECI;ESPECI 2;PRAZOT;MOEDA;ABERTURA;MAX;MIN;MEDIO;:ULTIMO;MELHOR OFERTA COMPRA;MELHOR OFERTA VENDA;TOTAL NEGOCIOS; TITULOS NEGOCIADOS;VOLUME TIT NEGOCIADOS;PRECO EXERCICIO OPCOES;INDOPC;DATA VENC OP;FATOR DE COT;PTOEXE;COD ISIN;DISMES;\n")
#escreve o cabeçalho com os campos no arquivo .csv
with open("C:/Users/c122802/Documents/Estudos/COTAHIST_A2017.TXT") as arquivo_bovespa:

    for line in arquivo_bovespa:

        TIP_REG                 = line[0:2]
        #testa pra saber a linha é HEADER ou TRAILER, só processas as linhas que são de cotações.
        if TIP_REG == "01":

            DATA_PREGAO             = line[2:10]
            COD_BDI                 = line[10:12]
            COD_NEG                 = line[12:24].strip(' ')
            TP_MERC                 = line[24:27].strip(' ')
            EMPRESA                 = line[27:39].strip(' ')
            ESPECI                  = line[39:42].strip(' ')
            ESPECI2                 = line[42:49].strip(' ')
            PRAZO_T                 = line[49:52].strip(' ')
            MOEDA                   = line[52:56].strip(' ')
            #arruma os valores fornecedidos pela bovespa que vem em milhar e sem casa decimal de separação
            ABERTURA                = float(line[56:69])/100
            MAX                     = float(line[69:82])/100
            MIN                     = float(line[82:95])/100
            MEDIO                   = float(line[95:108])/100
            ULTIMO                  = float(line[108:121])/100
            MELHOR_OFERTA_COMPRA    = float(line[121:134])/100
            MELHOR_OFERTA_VENDA     = float(line[134:147])/100
            PRE_EX_OP               = float(lineline[188:201])/100
            #fim
            TOTAL_NEGOCIOS          = line[147:152]
            TITULOS_NEGOCIADOS      = line[152:170]
            VOLUME_TIT_NEGOCIADOS   = line[170:188]
            IND_OPC                 = line[201:202]
            DATA_VENC_OP            = line[202:210]
            FATOR_DE_COT            = line[210:217]
            PTO_EXE                 = line[217:230]
            COD_ISIN                = line[230:242]
            DISMES                  = line[242:245]

#Delimita o layout do arquivo linha a linha;
            arquivo_formatado.write (TIP_REG+";"+DATA_PREGAO+";"+COD_BDI+";"+COD_NEG+";"
                +TP_MERC+";"+EMPRESA+";"+ESPECI+";"+ESPECI2+";"+PRAZO_T+";"+MOEDA+";"
                #retorna os valores como strings trocando . por , como separador decimal
                +str(ABERTURA).replace(".",",")+";"+str(MAX).replace(".",",")+";"+str(MIN).replace(".",",")+";"+str(MEDIO).replace(".",",")+";"
                +str(ULTIMO).replace(".",",")+";"+str(MELHOR_OFERTA_COMPRA).replace(".",",")+";"+str(MELHOR_OFERTA_VENDA).replace(".",",")+";"
                #fim
                +TOTAL_NEGOCIOS+";"+TITULOS_NEGOCIADOS+";"
                +VOLUME_TIT_NEGOCIADOS+";"+str(PRE_EX_OP).replace(".",",")+";"
                +IND_OPC+";"+DATA_VENC_OP+";"+FATOR_DE_COT+";"
                +PTO_EXE+";"+COD_ISIN+";"+DISMES+";\n")
#escreve no novo arquivo já no formato .csv ignorando headers e trailers

arquivo_formatado.close()
arquivo_bovespa.close()
#fecha os arquivos abertos
