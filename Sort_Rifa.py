import pandas as pd

PartCSV = pd.read_csv('Lista_Participantes.csv')
NumPart = len(PartCSV)
#RandNum = rand.randint(0, NumPart)
PartDataFrame = pd.DataFrame(PartCSV) 
PartSort = PartDataFrame.sample()

print(f"\n" + str(PartCSV))
print(f"\n" + str(PartSort))
print(f"\n""Número de Participantes " + str(NumPart))

