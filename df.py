import pandas as pd

file_name = "100.csv"
file_name2 = "train_file.csv"

df = pd.read_csv(file_name, sep=",", error_bad_lines=False)
df = df.iloc[:,0:6]
df2 = pd.read_csv(file_name2, sep=",", error_bad_lines=False)
print(df.merge(df2, on='Project_Name'))

'''print(str(df.loc['aadsm/JavaScript-ID3-Reader','# of Vuln']))
print(str(df.loc['aadsm/JavaScript-ID3-Reader',' Vul-1']))
print(str(df.loc['aadsm/JavaScript-ID3-Reader',' Vul-2']))
print(str(df.loc['aadsm/JavaScript-ID3-Reader',' Vul-3']))'''
#print(df.iloc[0,5])
#+','+str(df.loc[json_data['svn_url'][19:],'# of Vuln'])+','+str(df.loc[json_data['svn_url'][19:],' Vul-1'])+','+str(df.loc[json_data['svn_url'][19:],' Vul-2'])+','+str(df.loc[json_data['svn_url'][19:],' Vul-3'])+','+str(df.loc[json_data['svn_url'][19:],' Vul-4'])
projects = list(df['Project_Name'])
#print(projects)
'''no_vulnerabilities= list(df['# of Vuln'])
vulner1 = list(df[' Vul-1'])
vulner2 = list(df[' Vul-2'])
vulner3 = list(df[' Vul-3'])
vulner4 = list(df[' Vul-4'])'''