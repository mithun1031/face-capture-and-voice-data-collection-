import cam
import voice
import glob
import os
import csv


cam.detect('haarcascade_frontalface_alt2.xml')

list_of_files = glob.glob('cropped_face/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime)


data = voice.recognize()

try:
    name = data['name']
    contact = data['contact']


    with open('data.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([name,contact,latest_file])
        print('Successfully Saved...........')
except:
    print("Please Try Once Again")




