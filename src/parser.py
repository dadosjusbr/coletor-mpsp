# coding: utf8
import sys
import os
from coleta import coleta_pb2 as Coleta

CONTRACHEQUE_2018 = "contracheque"
CONTRACHEQUE_2019_JAN = "contracheque_2019_jan"
CONTRACHEQUE_2019_FEV_FORWARD = "contracheque_2019_fev_forward"
CONTRACHEQUE_2019_JUN = "contracheque_2019_jul"
CONTRACHEQUE_2019_JUL_FORWARD = "contracheque_2019_jul_forward"
INDENIZACOES_2019_JUL = "indenizações_2019_jul"
INDENIZACOES_2021_BACKWARD = "indenizações_2021_backward"
INDENIZACOES_2021_JAN = "indenizações_2021_jan"
INDENIZACOES_2021_FEV_2020_DEZ = "indenizações_2021_fev"
INDENIZACOES_2021_MAR_FORWARD = "indenizações_2021_mar_forward"
INDENIZACOES_2021_JUN_FORWARD = "indenizações_2021_jun_forward"
INDENIZACOES_2020_OUT = "indenizações_2020_out"

HEADERS = {
    CONTRACHEQUE_2018: {
        "Remuneração do Cargo Efetivo": 4,
        "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        "Função de Confiança ou Cargo em Comissão": 6,
        "Gratificação Natalina (13º  sal.)": 7,
        "Férias (1/3 constitucional)": 8,
        "Abono de Permanência": 9,
        "Contribuição Previdenciária": 11,
        "Imposto de Renda": 12,
        "Retenção por Teto Constitucional": 13,
        "Auxílio alimentação": 16,
        "Auxílio Moradia": 17,
        "Férias em Pecúnia": 18,
        "Outras Remunerações Temporárias": 19
    },
    CONTRACHEQUE_2019_JAN: {
        "Remuneração do Cargo Efetivo": 4,
        "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        "Função de Confiança ou Cargo em Comissão": 6,
        "Gratificação Natalina (13º  sal.)": 7,
        "Férias (1/3 constitucional)": 8,
        "Abono de Permanência": 9,
        "Contribuição Previdenciária": 11,
        "Imposto de Renda": 12,
        "Retenção por Teto Constitucional": 13,
        "Auxílio alimentação": 16,
        "Auxílio Moradia": 17,
        "Outras Remunerações Temporárias": 18
    },
    CONTRACHEQUE_2019_FEV_FORWARD: {
        "Remuneração do Cargo Efetivo": 4,
        "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        "Função de Confiança ou Cargo em Comissão": 6,
        "Gratificação Natalina (13º  sal.)": 7,
        "Férias (1/3 constitucional)": 8,
        "Abono de Permanência": 9,
        "Contribuição Previdenciária": 11,
        "Imposto de Renda": 12,
        "Retenção por Teto Constitucional": 13,
        "Auxílio alimentação": 16,
        "Férias em Pecúnia": 17,
        "Outras Remunerações Temporárias": 18
    },
    CONTRACHEQUE_2019_JUN: {
        "Remuneração do Cargo Efetivo": 4,
        "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        "Função de Confiança ou Cargo em Comissão": 6,
        "Gratificação Natalina (13º  sal.)": 7,
        "Férias (1/3 constitucional)": 8,
        "Abono de Permanência": 9,
        "Contribuição Previdenciária": 11,
        "Imposto de Renda": 12,
        "Auxílio alimentação": 15,
        "Férias em Pecúnia": 16,
        "Licença Prêmio em Pecúnia": 17,
        "Outras Remunerações Temporárias": 18
    },
    CONTRACHEQUE_2019_JUL_FORWARD: {
        "Remuneração do Cargo Efetivo": 4,
        "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        "Função de Confiança ou Cargo em Comissão": 6,
        "Gratificação Natalina (13º  sal.)": 7,
        "Férias (1/3 constitucional)": 8,
        "Abono de Permanência": 9,
        "Contribuição Previdenciária": 13,
        "Imposto de Renda": 14,
        "Retenção por Teto Constitucional": 15,
    },
    INDENIZACOES_2019_JUL: {
        "Auxílio Alimentação": 4,
        "Férias em pecúnia": 5,
        "Gratificação Cumulativa": 6,
        "Gratificação de Natureza Especial": 7,
    },
    INDENIZACOES_2021_BACKWARD: {
        "Aux Alimentação": 4,
        "Férias em pecúnia": 5,
        "LP em pecúnia": 6,
        "Gratificação Cumulativa": 7,
        "Gratificação de Natureza Especial": 8,
        "Gratificação de Grupo de Atuação Especial": 9,
    },
    INDENIZACOES_2021_JAN: {
        "Auxílio Alimentação": 4,
        "Gratificação Cumulativa": 5,
        "Gratificação de Natureza Especial": 6,
        "Gratificação de Grupo de Atuação Especial": 7,
    },
    INDENIZACOES_2021_FEV_2020_DEZ: {
        "Auxílio Alimentação": 4,
        "Férias em pecúnia": 5,
        "Gratificação Cumulativa": 6,
        "Gratificação de Natureza Especial": 7,
        "Gratificação de Grupo de Atuação Especial": 8,
    },
    INDENIZACOES_2021_MAR_FORWARD: {
        "Auxílio Alimentação": 4,
        "Férias em pecúnia": 5,
        "Assistencia Saúde": 6,
        "Gratificação Cumulativa": 7,
        "Gratificação de Natureza Especial": 8,
        "Gratificação de Grupo de Atuação Especial": 9,
    },
    INDENIZACOES_2021_JUN_FORWARD: {
        "Auxílio Alimentação": 4,
        "Férias em pecúnia": 5,
        "Licença Prêmio em Pecúnia": 6,
        "Assistncia Saúde": 7,
        "Gratificação Cumulativa": 8,
        "Gratificação de Natureza Especial": 9,
        "Gratificação de Grupo de Atuação Especial": 10,
    },
    INDENIZACOES_2020_OUT: {
        "Férias em pecúnia": 4,
        "Gratificação Cumulativa": 5,
        "Gratificação de Natureza Especial": 6,
        "Gratificação de Grupo de Atuação Especial": 7,
    },
}


def parse_employees(fn, chave_coleta, mes, ano):
    employees = {}
    counter = 1
    for row in fn:
        matricula = str(row[0])
        name = row[1]
        funcao = row[2]
        local_trabalho = row[3]
        if not is_nan(name) and name != "0":
            membro = Coleta.ContraCheque()
            membro.id_contra_cheque = chave_coleta + "/" + str(counter)
            membro.chave_coleta = chave_coleta
            membro.nome = name
            membro.matricula = matricula
            membro.funcao = funcao
            membro.local_trabalho = local_trabalho
            membro.tipo = Coleta.ContraCheque.Tipo.Value("MEMBRO")
            membro.ativo = True
            if int(ano) == 2018:
                membro.remuneracoes.CopyFrom(
                    cria_remuneracao(row, CONTRACHEQUE_2018)
                )
            elif int(ano) == 2019 and int(mes) == 1:
                membro.remuneracoes.CopyFrom(
                    cria_remuneracao(row, CONTRACHEQUE_2019_JAN)
                )
            elif int(ano) == 2019 and (int(mes) in [2, 3, 4, 5]):
                membro.remuneracoes.CopyFrom(
                    cria_remuneracao(row, CONTRACHEQUE_2019_FEV_FORWARD)
                )
            elif int(ano) == 2019 and int(mes) == 6:
                membro.remuneracoes.CopyFrom(
                    cria_remuneracao(row, CONTRACHEQUE_2019_JUN)
                )
            else:
                membro.remuneracoes.CopyFrom(
                    cria_remuneracao(row, CONTRACHEQUE_2019_JUL_FORWARD)
                )
            employees[name] = membro
            counter += 1
    return employees


def cria_remuneracao(row, categoria):
    remu_array = Coleta.Remuneracoes()
    items = list(HEADERS[categoria].items())
    for i in range(len(items)):
        key, value = items[i][0], items[i][1]
        remuneracao = Coleta.Remuneracao()
        remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("R")
        remuneracao.categoria = categoria
        remuneracao.item = key
        remuneracao.valor = format_value(row[value])
        if categoria in [CONTRACHEQUE_2018, CONTRACHEQUE_2019_JAN, CONTRACHEQUE_2019_FEV_FORWARD]:
            if value == 4:
                remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")
            elif value in [11, 12, 13]:
                remuneracao.valor = remuneracao.valor * (-1)
                remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
            elif value in [5, 6, 7, 8, 9, 16, 17, 18, 19]:
                remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")
        elif categoria == CONTRACHEQUE_2019_JUN:
            if value == 4:
                remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")
            elif value in [11, 12, ]:
                remuneracao.valor = remuneracao.valor * (-1)
                remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
            elif value in [5, 6, 7, 8, 9, 15, 16, 17, 18]:
                remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")
        elif categoria == CONTRACHEQUE_2019_JUL_FORWARD:
            if value == 4:
                remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")
            elif value in [13, 14, 15]:
                if remuneracao.valor > 0:   # Planilha de 2021 já entrega valores negativos
                    remuneracao.valor = remuneracao.valor * (-1)
                remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
            elif value in [5, 6, 7, 8, 9]:
                remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")
        else:
            remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")

        remu_array.remuneracao.append(remuneracao)
    return remu_array


def update_employees(fn, employees, categoria):
    for row in fn:
        name = row[1]
        if name in employees.keys():
            emp = employees[name]
            remu = cria_remuneracao(row, categoria)
            emp.remuneracoes.MergeFrom(remu)
            employees[name] = emp
    return employees


def is_nan(string):
    return string != string


def parse(data, chave_coleta, mes, ano):
    employees = {}
    folha = Coleta.FolhaDePagamento()
    if int(ano) == 2018 or (int(ano) == 2019 and int(mes) < 7):
        try:
            employees.update(parse_employees(data.contracheque, chave_coleta, mes, ano))

        except KeyError as e:
            sys.stderr.write(
                "Registro inválido ao processar contracheque: {}".format(e)
            )
            os._exit(1)
    else:
        try:
            employees.update(parse_employees(data.contracheque, chave_coleta, mes, ano))
            if int(ano) == 2019 and int(mes) in [7, 8]:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2019_JUL)
            elif int(ano) == 2020 and int(mes) == 10:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2020_OUT)
            elif int(ano) == 2020 and int(mes) == 12:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2021_FEV_2020_DEZ)
            elif int(ano) == 2021 and int(mes) == 1:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2021_JAN)
            elif int(ano) == 2021 and int(mes) == 2:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2021_FEV_2020_DEZ)
            elif int(ano) == 2021 and int(mes) in [3, 4, 5]:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2021_MAR_FORWARD)
            elif int(ano) == 2021 and int(mes) in [6, 7, 8]:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2021_JUN_FORWARD)
            else:
                update_employees(data.indenizatorias, employees, INDENIZACOES_2021_BACKWARD)

        except KeyError as e:
            sys.stderr.write(
                "Registro inválido ao processar contracheque ou indenizações: {}".format(e)
            )
            os._exit(1)
    for i in employees.values():
        folha.contra_cheque.append(i)
    return folha


def format_value(element):
    # A value was found with incorrect formatting. (3,045.99 instead of 3045.99)
    if is_nan(element) or element == '#N/DISP':
        return 0.0
    if type(element) == str:
        if "." in element and "," in element:
            element = element.replace(".", "").replace(",", ".")
        elif "," in element:
            element = element.replace(",", ".")
        elif "-" in element:
            element = 0.0

    return float(element)
