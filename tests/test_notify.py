import os
import requests

slack_api = os.environ["SLACK_API"]

requests.post(slack_api, json={'text': "Testing notifications..."})
requests.post(slack_api,
              json={'text': "Previsão das ondas para os próximos dias tem pelo menos 311 J na PG!\n\
Monday, 25 Jan 2021: 311J\n\
Tuesday, 26 Jan 2021: 514J\n\
Wednesday, 27 Jan 2021: 406J\n\
Thursday, 28 Jan 2021: 311J\n\
Friday, 29 Jan 2021: 228J"})
