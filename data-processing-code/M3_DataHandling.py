import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'M3_Data3.csv'
M3DataRaw =    pd.read_csv(filename)

relativeFluxesM3 = M3DataRaw.loc[:, "rel_flux_T3": "rel_flux_T101"]
relativeFluxesB_BandM3 = relativeFluxesM3.loc[1:3]
relativeFluxesV_BandM3 = relativeFluxesM3.loc[4:6]

relativeFluxesM3Error = M3DataRaw.loc[:, "rel_flux_err_T3": "rel_flux_err_T101"]
relativeFluxesB_BandM3Error = relativeFluxesM3Error.loc[1:3]
relativeFluxesV_BandM3Error = relativeFluxesM3Error.loc[4:6]

appartentMagB_Band = 12.857 + 2.5 * np.log10(relativeFluxesB_BandM3)
appartentMagB_BandAve = appartentMagB_Band.sum() / 3
appartentMagV_Band = 12.772 + 2.5 * np.log10(relativeFluxesV_BandM3)
appartentMagV_BandAve = appartentMagV_Band.sum() / 3

appartentMagB_BandError = relativeFluxesB_BandM3 * np.log(10)
appartentMagB_BandError = relativeFluxesB_BandM3Error.div(np.array(appartentMagB_BandError))

appartentMagV_BandError = relativeFluxesV_BandM3 * np.log(10)
appartentMagV_BandError = relativeFluxesV_BandM3Error.div(np.array(appartentMagV_BandError))
appartentMagV_BandAveError = appartentMagV_BandError.sum() / 3
appartentMagV_BandAveErrorAve = appartentMagV_BandAveError.sum() / 99

ObservedColour = appartentMagB_Band - np.array(appartentMagV_Band)
intrinsicColour = ObservedColour - 0.01
intrinsicColourAve = intrinsicColour.sum() / 3

ObservedColourError = appartentMagB_BandError - np.array(appartentMagV_BandError)
intrinsicColourAveError = ObservedColourError.sum() / 3

A0_Star_col = []
for i in range(len(np.array(intrinsicColourAve))):
    if np.array(intrinsicColourAve)[i] < 0.02 and np.array(intrinsicColourAve)[i] > -0.02:
        A0_Star_col += [i]


A0_ave = (appartentMagV_BandAve)[A0_Star_col].sum() / 3
A0_ave_Error = (appartentMagV_BandAveError)[A0_Star_col].sum() / 3

Av = 3 * 0.01
distance = (10 ** ((A0_ave - 0.7 + 5 - Av) / 5))



distanceError = A0_ave_Error / 5
distanceError = distance * np.log(10) * distanceError
print(distance)
print(distanceError)

plt.title("Colour-Magnitude Diagram for Globular Cluster M3")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()

plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="red") 
#plt.scatter(np.array(intrinsicColourAve)[A0_Star_col] , np.array(appartentMagV_BandAve)[A0_Star_col], color = "blue")
plt.show() 

'''iso_1plus6 =  pd.read_csv("Iso_1.00+06.csv")
AMViso_1plus6 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus6.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00 + 06")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_1plus6.loc[:, "(B-V)_0"]) , AMViso_1plus6, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green") 
plt.show() 

iso_1plus7 =  pd.read_csv("Iso_1.00+07.csv")
AMViso_1plus7 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus7.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+07")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_1plus7.loc[:, "(B-V)_0"]) , AMViso_1plus7, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green") 
plt.show() 

iso_1plus8 =  pd.read_csv("Iso_1.00+08.csv")
AMViso_1plus8 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus8.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+08")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_1plus8.loc[:, "(B-V)_0"]) , AMViso_1plus8, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green") 
plt.show() 

iso_1plus9 =  pd.read_csv("Iso_1.00+09.csv")
AMViso_1plus9 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus9.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+09")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_1plus9.loc[:, "(B-V)_0"]) , AMViso_1plus9, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() 

iso_1plus10 =  pd.read_csv("Iso_1.00+10.csv")
AMViso_1plus10 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1plus10.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.00+10")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_1plus10.loc[:, "(B-V)_0"]) , AMViso_1plus10, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() 

iso_1_3plus10 =  pd.read_csv("Iso_1.30+10.csv")
AMViso_1_3plus10 = 5 * np.log10(distance) - 5 + Av + np.array(iso_1_3plus10.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 1.30+10")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_1_3plus10.loc[:, "(B-V)_0"]) , AMViso_1_3plus10, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() 

iso_3_16plus06 =  pd.read_csv("Iso_3.16+06.csv")
AMiso_3_16plus06 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus06.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+06")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_3_16plus06.loc[:, "(B-V)_0"]) , AMiso_3_16plus06, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() 

iso_3_16plus07 =  pd.read_csv("Iso_3.16+07.csv")
AMiso_3_16plus07 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus07.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+07")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_3_16plus07.loc[:, "(B-V)_0"]) , AMiso_3_16plus07, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() 

iso_3_16plus08 =  pd.read_csv("Iso_3.16+08.csv")
AMiso_3_16plus08 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus08.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+08")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_3_16plus08.loc[:, "(B-V)_0"]) , AMiso_3_16plus08, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() 

iso_3_16plus09 =  pd.read_csv("Iso_3.16+09.csv")
AMiso_3_16plus09 = 5 * np.log10(distance) - 5 + Av + np.array(iso_3_16plus09.loc[:, "M_V"])
plt.title("Colour-Magnitude Diagram for iso 3.16+09")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(iso_3_16plus09.loc[:, "(B-V)_0"]) , AMiso_3_16plus09, color="pink")
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="green")
plt.show() '''