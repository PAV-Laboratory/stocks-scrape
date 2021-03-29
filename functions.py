import requests
from bs4 import BeautifulSoup
import pandas as pd


def init_df():
    df = get_DF(url)
    df["Short Name"] = get_short_name(df.index)
    return df

def cleanString(string, clean):
    new_string = ""
    for i in range(0, len(string)):
        if string[i] == clean:
            continue
        if string[i] == "\t" and string[i + 1] != "\t":
            new_string += " "
        else:
            new_string += string[i]
    return new_string

def get_DF(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    lst = soup.findAll("td")
    d = {}
    for i in range(0, len(lst)):
        new_elem = lst[i].text
        if i % 11 == 0:
            new_elem = cleanString(new_elem, "\n")
            new_elem = cleanString(new_elem, "\t")
            d[new_elem] = []
            title = new_elem
            flag = True
        else:
            flag = False
        if i in range(1, len(lst), 11):
            new_elem = float(new_elem)
        if i in range(2, len(lst), 11):
            new_elem = float(new_elem[:-1])
        if i in range(7, len(lst), 11) or i in range(8, len(lst), 11):
            if new_elem != '—':
                new_elem = float(new_elem)
            else:
                new_elem = 0.0
        if not flag:
            d[title].append(new_elem)
    df = pd.DataFrame(d).T
    df.columns = ["Last", "CHG%", "CHG", "Rating", "VOL", "MKT CAP", "P/E", "EPS(TTM)", "Employees", "Sector"]
    return df

def get_Url(tag):
    count = 0
    return_str = ""
    for i in range(0, len(tag)):
        if tag[i] == "=":
            count += 1
        if count == 2:
            if tag[i] == " ":
                break
            return_str += tag[i]
    return return_str

def get_Stock_url(url, name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    lst = soup.findAll("a")
    for i in range(0, len(lst)):
        if name in str(lst[i].text):
            return "https://www.tradingview.com" + get_Url(str(lst[i]))[2:-1]

def get_short_name(lst):
    new_lst = []
    str = ""
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            if lst[i][j] == " ":
                new_lst.append(str)
                str = ""
                break
            str += lst[i][j]
    return new_lst

def check_refresh_input(str):
    new_lst = []
    for i in range(0, len(str)):
        new_lst.append(int(str[i]))
    poss_comb = []
    get_all_comb_rec([2, 4, 5], len(new_lst), poss_comb, [])
    if new_lst in poss_comb or new_lst[::-1] in poss_comb:
        return True
    else:
        return False

def get_all_comb_rec(lst, leni, all_comb_lst, temp_lst):
    if len(temp_lst) == leni:
        all_comb_lst.append(temp_lst)
        return
    if len(lst) == 0:
        return
    t_lst = temp_lst.copy()
    temp_lst.append(lst[-1])
    return get_all_comb_rec(lst[:-1], leni, all_comb_lst, temp_lst) or get_all_comb_rec(lst[:-1], leni, all_comb_lst, t_lst)
url = "https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/"