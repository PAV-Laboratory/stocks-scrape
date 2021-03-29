from press_functions import *
url = "https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/"
top_gainers_url = "https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"
top_losers_url = "https://www.tradingview.com/markets/stocks-usa/market-movers-losers/"
most_active_url = "https://www.tradingview.com/markets/stocks-usa/market-movers-active/"

df = None
answer = None
memory = []
run = 0

while answer != "0":

    print("Hello, inorder to make an action, press the appropriate number.")
    print("\t0. exit.")
    print("\t1. Get stocks with max P/E.")
    print("\t2. Get Stocks with P/E around chosen value.")
    print("\t3. Get mean P/E value.")
    print("\t4. Get stock with maximum %change.")
    print("\t5. Save data to excel file.")
    print("\t6. Refresh data.")
    print("\t7. Daily top gainers stocks.")
    print("\t8. Daily top losers stocks.")
    print("\t9. Daily top most active stocks.")
    print("\t10. Default stocks.")

    answer = input()
    memory.append(answer)

    if answer == "1":
        if len(memory) == 1:
            df = init_df()
        tuple_press_1 = press1(df)
        best_pe_list = tuple_press_1[0]
        print1(tuple_press_1, best_pe_list)

    if answer == "2":
        try:
            if len(memory) == 1:
                df = init_df()
            else:
                chosen_num = int(input("What P/E value are you looking for?\n"))
                sigma_val = int(input("How far values do you accept to get from " + str(chosen_num) + "?\n"))
                returned_tuple = press2(df, chosen_num, sigma_val)
                returned_df = returned_tuple[0]
                df_length = returned_tuple[1]
                print2(returned_df, df_length)

        except:
            print("Something wrong happened, please try again.\n")

    if answer == "3":
        if len(memory) == 1:
            df = init_df()
        else:
            res_press_4 = press3(df)
            print3(res_press_4)

    if answer == "4":
        if len(memory) == 1:
            df = init_df()
        print4(press4(df))

    if answer == "5":
        if len(memory) == 1:
            df = init_df()
        filename = input("Write a name for the new file.\n")
        press5(df, filename)
    if answer == "6":
        df = init_df()

    if answer == "7":
        df = init_specific_market_df(top_gainers_url)
        print("Finished!")

    if answer == "8":
        df = init_specific_market_df(top_losers_url)
        print("Finished!")

    if answer == "9":
        df = init_specific_market_df(most_active_url)
        print("Finished!")

    if answer == "10":
        df = init_specific_market_df(url)
        print("Finished!")
