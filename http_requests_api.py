# import requests
#
# url = 'https://www.google.ru'
# response = requests.get(url)
# print(f'Request to {url}. Status code is {response.status_code}. ')
import requests

def contry_stat(your_country):
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

    querystring = {"country":your_country}

    headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "c41ce9c4dbmsh911cfeb5c4d2a99p1ca1bejsn89396f8553f6"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    country_name = data['latest_stat_by_country'][0]['country_name'] # страна
    total_cases = data['latest_stat_by_country'][0]['total_cases'] # всего больных
    new_cases = data['latest_stat_by_country'][0]['new_cases'] # больных за сутки
    total_deaths = data['latest_stat_by_country'][0]['total_deaths'] # всего умерло
    new_deaths = data['latest_stat_by_country'][0]['new_deaths'] # умерло за сутки
    total_recovered = data['latest_stat_by_country'][0]['total_recovered'] # всего выздоровело
    record_date = data['latest_stat_by_country'][0]['record_date'] # дата и время актуальности данных

    country_dict = {'Cтрана':country_name,'Всего больных':total_cases,'Новых больных за сутки':new_cases,
                    'Всего умерло':total_deaths,'Умерло за сутки':new_deaths,'Всего выздоровело':total_recovered,
                    'Дата и время актуальности данных':record_date}
    return country_dict


def world_stat(your_country):
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"

    headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "c41ce9c4dbmsh911cfeb5c4d2a99p1ca1bejsn89396f8553f6"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    country_name = 'World'  # страна
    total_cases = data['total_cases']  # всего больных
    new_cases = data['new_cases']  # больных за сутки
    total_deaths = data['total_deaths']  # всего умерло
    new_deaths = data['new_deaths']  # умерло за сутки
    total_recovered = data['total_recovered']  # всего выздоровело
    record_date = data['statistic_taken_at']  # дата и время актуальности данных

    country_dict = {'Cтрана': country_name, 'Всего больных': total_cases, 'Новых больных за сутки': new_cases,
                   'Всего умерло': total_deaths, 'Умерло за сутки': new_deaths, 'Всего выздоровело': total_recovered,
                   'Дата и время актуальности данных': record_date}

    return country_dict

#=================================================================================================================
def main():
    countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
                 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
                 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'CAR', 'Chad',
                 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba',
                 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
                 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland',
                 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
                 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
                 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait',
                 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
                 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
                 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua',
                 'Niger', 'Nigeria', 'N. Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine',
                 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
                 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
                 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
                 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'S. Korea',
                 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
                 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
                 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'UAE', 'UK', 'USA', 'Uruguay', 'Uzbekistan',
                 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', 'World']

    print('Эта программа позволяет получать актуальные данные \nо кол-ве заразившихся вирусом COVID-19 в мире',end='\n\n')
    print('Введите название страны на английском языке\nс заглавной буквы, например Russia ')
    print('Для получения статистики заражения во всем мире, введите World')
    while True:
        try:
            your_country = input()
            if your_country not in countries:
                raise ValueError
            if type(your_country) is not str:
                raise ValueError
        except ValueError:
            print()
            print('Не корректный ввод, повторите попытку', end='\n\n')
            continue
        else:
            break

    if your_country == 'World':
        country_dict = world_stat(your_country)
    else:
        country_dict = contry_stat(your_country)

    for dic in country_dict:
        if country_dict[dic] == '':
            country_dict[dic] = 'нет данных'
        print(dic, ' = ', country_dict[dic])

    print()
    print(chr(169) + ' 2020, HarryChpoker\'s program. All rights reserved.')
    input('Для закрытия программы Нажмите клавишу ENTER')

if __name__ == '__main__':
    main()