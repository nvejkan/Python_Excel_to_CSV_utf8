import pandas as pd
import csv

def excel_to_csv(excel_name,csv_name,sheetname='Sheet1'):
    data_xls = pd.read_excel(excel_name, sheetname, index_col=None)
    #data_xls = data_xls.head()
    data_xls.to_csv(csv_name
                    , encoding='utf-8'
                    ,quoting=csv.QUOTE_ALL
                    ,doublequote=True
                    ,index=False
                    ,date_format='%Y-%m-%d')

folder_name = "C:/Users/nattawut vejkanchana/Documents/work/Projects/Kubota/ascore2/"

##excel_name = folder_name+"main_good_rows.xlsx"
##csv_name = folder_name+"main_good_rows.csv"
##
##excel_to_csv(excel_name,csv_name)

##excel_name = folder_name+"main_fix_type3.xlsx"
##csv_name = folder_name+"main_fix_type3.csv"
##
##excel_to_csv(excel_name,csv_name)

#l_name = ["main_fix_type.xlsx","main_fix_type2.xlsx","main_fix_type3.xlsx","main_fix_type4.xlsx"]
l_name = ["a_scorce_acc_level.xlsx"]
for excel_name in l_name:
    excel_name = folder_name+excel_name
    csv_name = excel_name[ 0 : excel_name.find(".") ] + ".csv"
    excel_to_csv(excel_name,csv_name,'Sheet1')
    #print(excel_name,csv_name)
