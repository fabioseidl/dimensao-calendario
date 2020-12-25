# Dimensão Calendário
Script em Python que cria uma dimensão calendário, que pode ser utilizado em aplicações Business Intelligence.

## Colunas

Nome        | Descrição
------------|----------
data        | Data no formato yyyy-mm-dd
cod_data    | Código da data no formato yyyymmdd
ano         | Ano
mes         | Número do mês
dia         | Dia do mês
nome_mes    | Nome do mês
mes_ano     | Mês e Ano no formato mm-yyyy
num_semana  | Número da semana
dia_semana  | Nome do dia da semana
estacao     | Estação do ano (Primavera, Verão, Outono, Inverno)

## Como usar

_Obs.: Certifique-se de ter a biblioteca pandas instalada._

Execute os seguintes comandos:

~~~bash
git clone https://github.com/fabioseidl/dimensao_calendario.git
cd /dimensao_calendario
python transform_dim_calendario.py
~~~~

Um arquivo dim_calendario.csv será criado na mesma pasta do script. Basta importar este arquivo em sua aplicação Business Intelligence, ou carregá-lo em seu Data Warehouse.