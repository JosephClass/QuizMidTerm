#from curses import window
import CaseStudy
import os
from tkinter import filedialog as fd
from tkinter import *

AccessData = CaseStudy.StudiKasus(host="localhost" , port=3306 , user="root" , password=os.environ['PASS_MYSQL'])

print(AccessData.create_db("Tryout2"))

df = AccessData.import_csv("C:\\Users\\User-PC\\Desktop\\us-500.csv")

AccessData.create_table("Tryout2","user",df)

print(AccessData.load_data("Tryout2","user"))



window.title("Hello Python")
window.geometry("300x200+10+20")
window.mainloop()