import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'M3_OnlineEdited.tsv'
DataRaw =    pd.read_csv(filename, sep = ';')

appartentMagB_Band = DataRaw.loc[:, "Bmag"]
appartentMagB_Band = appartentMagB_Band.iloc[2:]
appartentMagB_Band = appartentMagB_Band.astype(float)
appartentMagV_Band = DataRaw.loc[:, "Vmag"]
appartentMagV_Band = appartentMagV_Band.iloc[2:]
appartentMagV_Band = appartentMagV_Band.astype(float)

ObservedColour = appartentMagB_Band - np.array(appartentMagV_Band)
intrinsicColour = ObservedColour - 0.01
A0_Star_col = []
for i in range(len(np.array(intrinsicColour))):
    if np.array(intrinsicColour)[i] < 10**-15 and np.array(intrinsicColour)[i] > -10**-15:
       A0_Star_col += [i]

Av = 3 * 0.01
A0_ave = np.array(appartentMagV_Band)[A0_Star_col].sum() / 3
distance = (10 ** ((A0_ave - 0.7 + 5 - Av) / 5))

print(distance)

'''plt.title("Colour-Magnitude Diagram for Globular Cluster M3")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()

plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="red") 
#plt.scatter(np.array(intrinsicColour)[A0_Star_col] , np.array(appartentMagV_Band)[A0_Star_col], color = "blue")
plt.show() 

iso_1plus6 =  pd.read_csv("Iso_1.00+06.csv")
AMViso_1plus6 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus6.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00 + 06")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green") 
plt.scatter(np.array(iso_1plus6.loc[:, "(B-V)_0"]) , AMViso_1plus6, color="pink")

plt.show() 

iso_1plus7 =  pd.read_csv("Iso_1.00+07.csv")
AMViso_1plus7 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus7.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+07")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green") 
plt.scatter(np.array(iso_1plus7.loc[:, "(B-V)_0"]) , AMViso_1plus7, color="pink")

plt.show() 

iso_1plus8 =  pd.read_csv("Iso_1.00+08.csv")
AMViso_1plus8 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus8.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+08")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_1plus8.loc[:, "(B-V)_0"]) , AMViso_1plus8, color="pink")
 
plt.show() 

iso_1plus9 =  pd.read_csv("Iso_1.00+09.csv")
AMViso_1plus9 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus9.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+09")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_1plus9.loc[:, "(B-V)_0"]) , AMViso_1plus9, color="pink")

plt.show() 

iso_1plus10 =  pd.read_csv("Iso_1.00+10.csv")
AMViso_1plus10 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus10.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+10")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_1plus10.loc[:, "(B-V)_0"]) , AMViso_1plus10, color="pink")

plt.show() 

iso_1_3plus10 =  pd.read_csv("Iso_1.30+10.csv")
AMViso_1_3plus10 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1_3plus10.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.30+10")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_1_3plus10.loc[:, "(B-V)_0"]) , AMViso_1_3plus10, color="pink")

plt.show() 

iso_3_16plus06 =  pd.read_csv("Iso_3.16+06.csv")
AMiso_3_16plus06 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus06.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+06")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_3_16plus06.loc[:, "(B-V)_0"]) , AMiso_3_16plus06, color="pink")

plt.show() 

iso_3_16plus07 =  pd.read_csv("Iso_3.16+07.csv")
AMiso_3_16plus07 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus07.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+07")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_3_16plus07.loc[:, "(B-V)_0"]) , AMiso_3_16plus07, color="pink")

plt.show() 

iso_3_16plus08 =  pd.read_csv("Iso_3.16+08.csv")
AMiso_3_16plus08 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus08.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+08")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_3_16plus08.loc[:, "(B-V)_0"]) , AMiso_3_16plus08, color="pink")

plt.show() 

iso_3_16plus09 =  pd.read_csv("Iso_3.16+09.csv")
AMiso_3_16plus09 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus09.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+09")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_3_16plus09.loc[:, "(B-V)_0"]) , AMiso_3_16plus09, color="pink")'''

iso_3_16plus10 =  pd.read_csv("Iso_3.16+10.csv")
AMiso_3_16plus10 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus10.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+10")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColour) , np.array(appartentMagV_Band), color="green")
plt.scatter(np.array(iso_3_16plus10.loc[:, "(B-V)_0"]) , AMiso_3_16plus10, color="pink")

plt.show()