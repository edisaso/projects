import requests
from tkinter import Tk     
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
filename = askopenfilename() 
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(filename, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'Xz6dG9zUer2k4L4c6fuEMy19'},
)
if response.status_code == requests.codes.ok:
    with open('removedBackground.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)