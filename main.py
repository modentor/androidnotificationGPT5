# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests
import time
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn1 = MDFlatButton(text='Run Persistent Check', pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.show_data)
        btn = MDFloatingActionButton
        screen.add_widget(btn1)
        return screen

    def show_data(self, obj):
        # URL of the webpage to scrape
        url = "https://www.bing.com/news/search?q=gpt+5+releaed&qft=sortbydate%3d%221%22&form=YFNR"
        found = False
        # Send an HTTP GET request to the webpage
        response = requests.get(url)
        while found == False:
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the webpage using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Search for the phrase "GPT-5 released" in the webpage content
                search_phrase = "GPT-5 Released"
                search_phrase2 = "GPT-5 has been released"
                search_phrase3 = "GPT 5 Released"
                search_phrase4 = "GPT-5: Released"
                search_phrase5 = "GPT-5: has been released"
                search_phrase6 = "GPT 5: Released"

                if search_phrase in soup.get_text():
                    print(f"The phrase '{search_phrase}' was found on the webpage.")
                    found = True

                if search_phrase2 in soup.get_text():
                    print(f"The phrase '{search_phrase2}' was found on the webpage.")
                    found = True

                if search_phrase3 in soup.get_text():
                    print(f"The phrase '{search_phrase3}' was found on the webpage.")
                    found = True

                if search_phrase4 in soup.get_text():
                    print(f"The phrase '{search_phrase4}' was found on the webpage.")
                    found = True

                if search_phrase5 in soup.get_text():
                    print(f"The phrase '{search_phrase5}' was found on the webpage.")
                    found = True

                if search_phrase6 in soup.get_text():
                    print(f"The phrase '{search_phrase6}' was found on the webpage.")
                    found = True
                else:

                    time.sleep(60)
            else:
                print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

            if found == True:
                ifttt_webhook_url = "https://maker.ifttt.com/trigger/news_alert/with/key/hGro0-FS3uJdqmDdc_j_HKi_dPnj9xUmWaswmIo7nH"

                # Trigger the alarm
                response = requests.post(ifttt_webhook_url)

                # Check the response
                if response.status_code == 200:
                    print("Alarm set successfully!")
                else:
                    print("Failed to set the alarm.")

DemoApp().run()

