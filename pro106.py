import csv
import plotly.express as px
import numpy as np

def plotGraph(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        graph=px.scatter(df, x="Marks In Percentage", y="Days Present")
        graph.show()

def getDataSource(data_path):
    RN=[]
    MIP=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            RN.append(float(row["Marks In Percentage"]))
            MIP.append(float(row["Days Present"]))
        
    return {"x":RN, "y":MIP}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between marks vs days present: \n", correlation[0,1])

def setup():
    data_path="pro106.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotGraph(data_path)

setup()