import pandas as pd

# Select the needed cols


# def filter(fileName):
#    file = pd.ExcelFile(fileName)
#    sheet2 = file.parse(1)
#    new_sheet = sheet2[['First Name', 'Person Linkedin Url']
#                       ].dropna().values.tolist()
#    return new_sheet

def filter(fileName):
    df = pd.read_csv(fileName)
    data = df[['First Name', 'Person Linkedin Url']].dropna().values.tolist()
    return data
