# -*- coding: utf-8 -*-
import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('921078543:AAHx2ySXQli5xUc9HmvdDjFO4rT2NDiaYRY')

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

@bot.message_handler(content_types=['text'])
def send_echo(message):
    if message.text == 'World':
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"

        headers = {
            'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
            'x-rapidapi-key': "c41ce9c4dbmsh911cfeb5c4d2a99p1ca1bejsn89396f8553f6"
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            country_name = 'World'  # страна
            total_cases = data['total_cases']  # всего больных
            new_cases = data['new_cases']  # больных за сутки
            total_deaths = data['total_deaths']  # всего умерло
            new_deaths = data['new_deaths']  # умерло за сутки
            total_recovered = data['total_recovered']  # всего выздоровело
            record_date = data['statistic_taken_at']  # дата и время актуальности данных
            text_for_print = u'Страна = ' + country_name + '\n' + u'Всего больных = ' + total_cases + '\n' \
                             + u'Новых больных за сутки = ' + new_cases + '\n' + u'Всего умерло = ' + total_deaths + '\n' \
                             + u'Умерло за сутки = ' + new_deaths + '\n' + u'Всего выздоровело = ' + total_recovered + '\n' \
                             + u'Дата и время актуальности данных = ' + record_date + '\n\n'
            bot.send_message(message.chat.id, text_for_print)
        else:
            text_for_print = u"Ошибка соединения с сервером"
            bot.send_message(message.chat.id, text_for_print)
    else:
        if message.text not in countries:
            text_for_print = u'Некорректный ввод, будет выведена информация о России' + '\n\n'
            bot.send_message(message.chat.id, text_for_print)
            message.text = 'Russia'
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"
        querystring = {"country": message.text}
        headers = {'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
                   'x-rapidapi-key': "c41ce9c4dbmsh911cfeb5c4d2a99p1ca1bejsn89396f8553f6"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            country_name = data['latest_stat_by_country'][0]['country_name']
            total_cases = data['latest_stat_by_country'][0]['total_cases']
            new_cases = data['latest_stat_by_country'][0]['new_cases']
            total_deaths = data['latest_stat_by_country'][0]['total_deaths']
            new_deaths = data['latest_stat_by_country'][0]['new_deaths']
            total_recovered = data['latest_stat_by_country'][0]['total_recovered']
            record_date = data['latest_stat_by_country'][0]['record_date']
            text_for_print = u'Страна = ' + country_name + '\n' + u'Всего больных = ' + total_cases + '\n' \
                             + u'Новых больных за сутки = ' + new_cases + '\n' + u'Всего умерло = ' + total_deaths + '\n'\
                             + u'Умерло за сутки = ' + new_deaths + '\n' + u'Всего выздоровело = ' + total_recovered + '\n'\
                             + u'Дата и время актуальности данных = ' + record_date + '\n\n'
            bot.send_message(message.chat.id, text_for_print)
        else:
            text_for_print = u"Ошибка соединения с сервером"
            bot.send_message(message.chat.id, text_for_print)
        if message.text == 'Russia':
            URL = 'https://ncov.blog/countries/ru/'
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                'accept': '*/*'}
            response = requests.request("GET", URL, headers=HEADERS)
            if response.status_code == 200:
                html_data = BeautifulSoup(response.text, 'html.parser')
                quotes = html_data.find_all(class_='text-dark')
                quotes1 = html_data.find_all(class_='badge badge p-2 badge-info')
                new_list = [t.text for t in quotes]
                new_list1 = [t.text for t in quotes1]
                text_for_print = u'Всего зарегистрированных случаев заражения' + '\n' +'\n'
                for i in range(0, len(new_list)):
                    text_for_print += str(i + 1) + '.' + new_list[i] + ' - ' + new_list1[i] + '\n'
                bot.send_message(message.chat.id, text_for_print)
            else:
                text_for_print = u"Ошибка соединения с сервером"
                bot.send_message(message.chat.id, text_for_print)
        elif message.text == 'Kazakhstan':
            URL = 'https://www.coronavirus2020.kz/'
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
                'accept': '*/*'}
            response = requests.request("GET", URL, headers=HEADERS)
            if response.status_code == 200:
                html_data = BeautifulSoup(response.text, 'html.parser')
                quotes = html_data.find_all(class_='city_cov')
                new_list = [t.text for t in quotes]
                text_for_print = u'Всего зарегистрированных случаев заражения \n'
                text_for_print += new_list[0]
                bot.send_message(message.chat.id, text_for_print)
            else:
                text_for_print = u"Ошибка соединения с сервером"
                bot.send_message(message.chat.id, text_for_print)


bot.polling(none_stop=True, interval=0)
