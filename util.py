import pandas as pd
PATH="LargestCompanies.csv"

def get_data(PATH):
    df=pd.read_csv(PATH)
    # Get top 5 countries by market cap using Trillions
    # and return them as a dataFrane
    df["Trill"] = df ["marketcap"]/1000000000000
    mygroup=df.groupby("country")[["Trill"]].sum()
    mygroup.sort_values("Trill", ascending=False, inplace=True)
    mygroup.reset_index(inplace=True)
    top=mygroup.iloc[:5]
    print(top)
    return top



