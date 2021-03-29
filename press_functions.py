from functions import *
import pandas as pd

def init_df():
    df = get_DF(url)
    df["Short Name"] = get_short_name(df.index)
    return df

def press1(df):
    pe_col = df["P/E"].tolist()
    while "—" in pe_col:
        pe_col.remove("—")
    max_pe_d = {}
    for i in range(0, len(pe_col)):
        if pe_col[i] not in max_pe_d:
            max_pe_d[pe_col[i]] = [i]
        else:
            max_pe_d[pe_col[i]].append(i)
    best_pe_index_lst = max_pe_d[max(max_pe_d)]
    df_return_list = []
    for i in range(0, len(best_pe_index_lst)):
        df_return_list.append(df[df["P/E"] == max(max_pe_d)].index[0])
    return (df_return_list, max(max_pe_d))


def press2(df, chosen_num, sigma_val):
    high_bound = chosen_num + sigma_val
    low_bound = chosen_num - sigma_val
    new_df = df[df["P/E"] <= high_bound]
    new_df = new_df[new_df["P/E"] >= low_bound]
    return (new_df["P/E"], len(new_df["P/E"]))

def press3(df):
    return df["P/E"].mean()

def press4(df):
    lst = list(df["CHG%"])
    max_value = max(lst)
    lst.remove(max_value)
    max_tuples_lst = [(df.index[lst.index(max(lst))], max(lst))]
    while max_value in lst:
        max_tuples_lst.append((df.index[lst.index(max(lst))], max_value))
    return max_tuples_lst
def press5(df, filename):
    df.to_csv(filename + ".csv")
    print("Excel file has been saved with the name " + filename + ".csv")
def press8(top_gainers_df):
    lst = top_gainers_df.index
    d = {}
    d["Name"] = []
    d["CHG%"] = []
    d["Repeat"] = []
    csv = read_csv("first.csv")
    if csv.empty:
        for i in range(0, len(lst)):
            d["Name"].append(lst[i])
            d["CHG%"].append(str(top_gainers_df["CHG%"][i]) + "%")
            d["Repeat"].append(1)
            df = pd.DataFrame(d)
            df.to_csv("first.csv")
    else:
        name_lst = csv["Name"].tolist()
        chg_lst = csv["CHG%"].tolist()
        repeat_lst = csv["Repeat"].tolist()
        for i in range(0, len(lst)):
            if lst[i] in name_lst:
                index = name_lst.index(lst[i])
                repeat_lst[index] += 1
                chg_lst[index] += (" " + str(top_gainers_df["CHG%"]) + "%")
            else:
                name_lst.append(lst[i])
                chg_lst.append(str(top_gainers_df["CHG%"]) + "%")
                repeat_lst.append(1)
        df = pd.DataFrame({"Name":name_lst, "CHG%":chg_lst, "Repeat":repeat_lst})
        df.to_csv("first.csv")
    print("Finished")
def read_csv(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except:
        return None
def print1(tuple_press_2, best_pe_list):
    print("Max P/E value is: " + str(tuple_press_2[1]))
    for i in range(0, len(best_pe_list)):
        print("Stock: " + best_pe_list[i] + "\n")
def print2(returned_df, df_length):
    print("We found " + str(df_length) + " relevant stocks:\n")
    print(returned_df)
    print("\n")
def print3(input):
    print("Average P/E value is: " + str(input))
def print4(max_tuples_lst):
    print("The stocks with maximum %CHG we found are:")
    for i in range(0, len(max_tuples_lst)):
        print(max_tuples_lst[i][0] + ": " + str(max_tuples_lst[i][1]) + "%.")
def init_specific_market_df(url):
    df = get_DF(url)
    df["Short Name"] = get_short_name(df.index)
    return df