import requests
import tkinter
from apikey import key


# http call to openai api
def send_message(message):
    url = "https://open-ai21.p.rapidapi.com/conversationgpt"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "web_access": False,
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    #print(response.json()["result"])
    output_box.config(state=tkinter.NORMAL)
    # add response to output box
    output_box.insert(tkinter.END, "You: " + message + "\n")
    # add response to output box
    output_box.insert(tkinter.END, "Chatbot: " + response.json()["result"] + "\n")
    # clear input box
    input_box.delete(0, tkinter.END)
    
# set up window
window = tkinter.Tk()
# set title
window.title("Chatbot")
# set window size
window.geometry("600x500")
# make window not resizable
window.resizable(False, False)


# create input box
input_box = tkinter.Entry(window)
# place input box in window
input_box.place(x=6, y=6, width=500, height=30)
# submit button
submit_button = tkinter.Button(window, text="Submit", command=lambda: send_message(input_box.get()))
# place submit button in window
submit_button.place(x=506, y=6, width=90, height=30)
# create output box
output_box = tkinter.Text(window)
# place output box in window
output_box.place(x=6, y=42, width=590, height=450)
#make output box not editable
output_box.config(state=tkinter.DISABLED)







#start tkinter loop
window.mainloop()