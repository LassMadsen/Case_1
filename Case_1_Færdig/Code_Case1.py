from turtle import title
from flask import Flask, render_template
from matplotlib import pyplot as plt
import pandas as pd 
import csv
import excelReader

app = Flask(__name__)

@app.route('/')

def Co2():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("1Case/Data.csv")
        del dataframe[0]
      
        return( '<center><h1>Kategori</h1></center> '
                '<br /><br /><a href="/Titler"><button>Se CO2 Udledning</button></a>'
                ' <a href="/"><button>Se Kategori</button></a>'
                ' <a href="/Grafer"><button>Se Grafer</button></a>'
                '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
                '<br /><br />' + render_template('htmlTable.html', data = dataframe ))



# Definere class
class Co2:
    # Definere attributer for vores kategorier
    def __init__(self, Co2Title, Co2Kate, Co2Udl, Co2TotalEnhÅ):
        self.Co2Title = Co2Title
        self.Co2Kate = Co2Kate
        self.Co2Udl = Co2Udl
        self.Co2TotalEn = Co2TotalEnhÅ
        
        #Data for 
        Data=["Indkøb", "transport", "Overnatninger", "Mad_og_drikkevare", "Hjemmeside", "Medarbejdergoder", "Flyrejser", "Ambassadørpakke_og_Merch"]
              
     

# Decorator for en route så den får adressen http://127.0.0.1:5000/Odense
@app.route('/')
def Kategori():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("Case1/DataLatrefori.csv")
        del dataframe[0]

      
        return( '<center><h1></h1></center> '
                '<br /><br /><a href="/Aalborg"><button>Se Aalborg</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
                ' <a href="/Grafer"><button>Se Grafer</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe ))          



# Decorator for en route så den får adressen
@app.route('/')
def Aalborg():
        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataAalborg.csv")
        del dataframe[0]

        return( '<center><h1>Aalborg</h1></center> '
                '<br /><br /><a href="/Odense"><button>Se Odense</button></a>'
                ' <a href="/København"><button>Se København</button></a>'
                ' <a href="/Grafer"><button>Se Grafer</button></a>'
             '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
             '<br /><br />' + render_template('htmlTable.html', data = dataframe )) 



# Decorator for en route så den får adressen http://127.0.0.1:5000/Grafer
@app.route('/Grafer')
def Grafer():

        return( '<center><h1>Grafer</h1></center> '
                '<br /><br /><a href="/Odense"><button>Se </button></a>'
                ' <a href="/København"><button>Se København</button></a>'
                ' <a href="/Aalborg"><button>Aalborg</button></a>'
                '<br /><br /><a href="/"><button>Tilbage til forsiden</button></a>'
                '<br /><br /><h2>Grafer for København</h2>'
                '<br /><br />' + render_template('plotKBH.html') +
                '<br /><br /><h2>Grafer for Odense</h2>'
                '<br /><br />' + render_template('plotOD.html') +
                '<br /><br /><h2>Grafer for Aalborg</h2>'
                '<br /><br />' + render_template('plotAA.html')) 





# til at køre koden direkte
if __name__== '__main__':
    app.run()