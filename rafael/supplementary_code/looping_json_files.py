import datetime
import json
import pandas as pd


poop = True

start_date = datetime.datetime.strptime('2007-06-18', '%Y-%m-%d')

end_date = datetime.datetime.strptime('2017-08-30', '%Y-%m-%d')

print(end_date.strftime('%Y-%m-%d'))


df_top = []
df_bot = []


while start_date.strftime('%Y-%m-%d') < end_date.strftime('%Y-%m-%d'):
#     print(f"Resources/weekly_json/{start_date.strftime('%Y-%m-%d')}_factbook.json")
    

    JsonFile = f"Resources/weekly_json/{start_date.strftime('%Y-%m-%d')}_factbook.json"

    dic = {}
    dic2 = {}

    with open(JsonFile, 'r') as f:
        objects = json.loads(f.read())
    #     country = list(objects['countries'].keys())
        try:
            for top, bot in zip(top_country_names,bot_country_names):
                dic[top] = objects['countries'][top]['data']['economy']['industries']['industries']
                dic2[bot] = objects['countries'][bot]['data']['economy']['industries']['industries']
            print(f'appending dataframes from {start_date} to lists...')

        except:
            poop = False
            
        df_top.append(pd.DataFrame.from_dict(dic, orient = 'index').transpose())
        df_bot.append(pd.DataFrame.from_dict(dic2, orient = 'index').transpose())
    
    start_date += datetime.timedelta(days=7)

print(len(df_top))
