import pandas as pd

path = r"C:\Users\avogu\Desktop\DA Portfolio\Stackoverflow"

df_data = pd.read_csv(f"{path}\survey_results_public.csv")
df_schema = pd.read_csv(f"{path}\survey_results_schema.csv")

#creating main data group SUMMARY
df_main = df_data.loc[:, ['ResponseId', 'DevType', 'RemoteWork', 'Industry', 'Country', 'Age', 'EdLevel', 'YearsCode',
                          'LearnCode', 'JobSat']]

#creating 2nd data group CODE LEARNING
df_learn_code_from = df_data.loc[:, ['ResponseId', 'LearnCode']]

#creating 3nd data group TECH CHOICE
df_language = df_data.loc[:, ['ResponseId', 'LanguageAdmired']]
df_database = df_data.loc[:, ['ResponseId', 'DatabaseAdmired']]
df_platform = df_data.loc[:, ['ResponseId', 'PlatformAdmired']]
df_webframe = df_data.loc[:, ['ResponseId', 'WebframeAdmired']]
df_opsys = df_data.loc[:, ['ResponseId', 'OpSysPersonal use']]
df_AIsearch = df_data.loc[:, ['ResponseId', 'AISearchDevAdmired']]

#creating 4rd data group AI
df_ai = df_data.loc[:, ['ResponseId', 'AISelect', 'AISent', 'AIAcc', 'AIComplex', 'AIThreat','AIBen',
                        'AIToolCurrently Using']]



df_main.to_csv(f'{path}\df_main.csv', index=False)

df_learn_code_from.to_csv(f'{path}\df_learn_code_from.csv', index=False)

df_language.to_csv(f'{path}\df_language.csv', index=False)
df_database.to_csv(f'{path}\df_database.csv', index=False)
df_platform.to_csv(f'{path}\df_platform.csv', index=False)
df_opsys.to_csv(f'{path}\df_opsys.csv', index=False)
df_AIsearch.to_csv(f'{path}\df_AIsearch.csv', index=False)

df_ai.to_csv(f'{path}\df_ai.csv', index=False)