import requests
import pathlib
import sys
import os
import urllib3

base_url = "http://www.mpsp.mp.br/portal/page/portal/Portal_da_Transparencia/Contracheque/Membros_ativos/"
base_url_indenizatorias = "http://www.mpsp.mp.br/portal/page/portal/Portal_da_Transparencia/Contracheque/verbas_indeniz/verb_ind_mem/verb_ind_mem_ativos/"


def links_remuneration(month, year):
    links_type = {}
    link = ''
    month_int = int(month)
    if year == 2018:
        if month_int == 12:
            link = base_url + "Tabela I membros ativos ref122018.ods"
        else:
            link = base_url + "Tabela I membros ativos ref" + month + ".ods"
        links_type["Membros ativos"] = link
    elif year == 2019:
        if month_int < 6:
            link = base_url + "Tabela I membros ativos ref" + month + "19.ods"
        elif month_int == 6:
            link = base_url + "Tabela I Membros Ativos ref" + month + "19.ods"
        elif month_int in [7, 8]:
            link = base_url + "Membros Ativos - Tabela I ref " + month + "2019.ods"
        elif month_int == 9:
            link = base_url + "Tabela I memb092019.ods"
        elif month_int == 10:
            link = base_url + "Tabela I memb092019_1.ods"
        elif month_int == 11:
            link = base_url + "Tabela I memb112019A.ods"
        else:
            link = base_url + "Tabela I memb122019.ods"
        links_type["Membros ativos"] = link
    elif year == 2020:
        if month_int < 8:
            link = base_url + "Tabela I memb" + month + "2020.ods"
        elif month_int in [8, 9, 12]:
            link = base_url + "Tabela 1 Membros Ativos ref " + month + "-2020.ods"
        elif month_int == 10:
            link = base_url + "Membros Ativos tabela 1 ref 10-2020.ods"
        elif month_int == 11:
            link = base_url + "Membros Ativos Tabela 1 ref 11-2020.ods"
        links_type["Membros ativos"] = link
    else:
        if month_int in [1, 2]:
            link = base_url + "Tabela 1 Membros Ativos ref " + month + "-2021.ods"
        else:
            link = base_url + "membros-ativos-remuneracao-" + month + "-2021.ods"
        links_type["Membros ativos"] = link
    return links_type


def links_perks_temporary_funds(month, year):
    links_type = {}
    link = ''
    month_int = int(month)
    if year == 2019:
        if month_int in [7, 8]:
            link = base_url_indenizatorias + "Membros Ativos - Tabela III ref " + month + "2019.ods"
        elif month_int in [9, 12]:
            link = base_url_indenizatorias + "Tabela III memb" + month + "2019.ods"
        elif month_int == 10:
            link = base_url_indenizatorias + "Tabela III memb092019_1.ods"
        elif month_int == 11:
            link = base_url_indenizatorias + "Tabela III memb112019A.ods"
        links_type["Membros ativos"] = link
    elif year == 2020:
        if month_int < 8:
            link = base_url_indenizatorias + "Tabela III memb" + month + "2020.ods"
        elif month_int in [8, 9, 12]:
            link = base_url_indenizatorias + "Tabela 3 Membros Ativos ref " + month + "-2020.ods"
        elif month_int == 10:
            link = base_url_indenizatorias + "Membros Ativos tabela 3 ref 10-2020.ods"
        elif month_int == 11:
            link = base_url_indenizatorias + "Membros Ativos Tabela 3 ref 11-2020.ods"
        links_type["Membros ativos"] = link
    else:
        if month_int in [1, 2]:
            link = base_url_indenizatorias + "Tabela 3 Membros Ativos ref " + month + "-2021.ods"
        else:
            link = base_url_indenizatorias + "membros-ativos-verba-indenizatoria-" + month + "-2021.ods"
        links_type["Membros ativos"] = link
    return links_type


def download(url, file_path):
    # Silence InsecureRequestWarning
    requests.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        response = requests.get(url, allow_redirects=True, verify=False)
        with open(file_path, "wb") as file:
            file.write(response.content)
        file.close()
    except Exception as excep:
        sys.stderr.write(
            "Não foi possível fazer o download do arquivo: "
            + file_path
            + ". O seguinte erro foi gerado: "
            + excep
        )
        os._exit(1)


def crawl(year, month, output_path):
    urls_remuneration = links_remuneration(month, int(year))
    files = []

    for element in urls_remuneration:
        pathlib.Path(output_path).mkdir(exist_ok=True)
        file_name = "membros-ativos-contracheque-" + month + "-" + year + ".ods"
        file_path = output_path + "/" + file_name
        download(urls_remuneration[element], file_path)
        files.append(file_path)

    if int(year) == 2018 or (int(year) == 2019 and int(month) < 7):
        # Não existe dados exclusivos de verbas indenizatórias nesse período de tempo.
        pass
    else:
        urls_perks = links_perks_temporary_funds(month, int(year))
        for element in urls_perks:
            pathlib.Path(output_path).mkdir(exist_ok=True)
            file_name_indemnity = (
                "membros-ativos-verbas-indenizatorias-" + month + "-" + year + ".ods"
            )

            file_path_indemnity = output_path + "/" + file_name_indemnity
            download(urls_perks[element], file_path_indemnity)
            files.append(file_path_indemnity)

    return files
