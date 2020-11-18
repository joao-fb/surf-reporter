from reporter import Reporter
import requests
import os


url = 'https://www.surfguru.com.br/previsao/brasil/sao-paulo/ubatuba/praia-grande'
x_arg = '//label[@class="resumo_energia_en"]'

slack_api = os.environ["SLACK_API"]


reporter = Reporter(url, x_arg)
raw_energies = reporter.find_energies()
p_energies = reporter.process_energies(raw_energies)
del reporter

for energy_key in p_energies.keys():
    energy = p_energies[energy_key]
    if energy > 300:
        msg = f"Previsão das ondas para os próximos dias tem pelo menos {energy} J na PG!\n"

        format_forecast = [f'{k}: {p_energies[k]}J' for k in p_energies.keys()]
        forecast = "\n".join(format_forecast)

        msg += forecast

        requests.post(slack_api, json={'text': msg})
        print("Forecast enviado!")
        break
