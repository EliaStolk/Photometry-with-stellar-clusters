import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'M36.csv'
M3DataRaw =    pd.read_csv(filename)

relativeFluxesM36 = M3DataRaw.loc[:, "rel_flux_T2": "rel_flux_T84"]
relativeFluxesB_BandM36 = relativeFluxesM36.loc[0:3]
relativeFluxesV_BandM36 = relativeFluxesM36.loc[4:7]

relativeFluxesM36Error = M3DataRaw.loc[:, "rel_flux_err_T2": "rel_flux_err_T84"]
relativeFluxesB_BandM36Error = relativeFluxesM36Error.loc[0:3]
relativeFluxesV_BandM36Error = relativeFluxesM36Error.loc[4:7]

appartentMagB_Band = 9.932 + 2.5 * np.log10(relativeFluxesB_BandM36)
appartentMagV_Band = 9.885 + 2.5 * np.log10(relativeFluxesV_BandM36)

appartentMagB_BandError = relativeFluxesB_BandM36 * np.log(10)
appartentMagB_BandError = 0.035 + relativeFluxesB_BandM36Error.div(np.array(appartentMagB_BandError))

appartentMagV_BandError = relativeFluxesV_BandM36 * np.log(10)
appartentMagV_BandError = 0.046 + relativeFluxesV_BandM36Error.div(np.array(appartentMagV_BandError))

ObservedColour = appartentMagB_Band - np.array(appartentMagV_Band)
intrinsicColour = ObservedColour - 0.22
intrinsicColourAve = intrinsicColour.sum() / 4

ObservedColourError = appartentMagB_BandError - np.array(appartentMagV_BandError)
intrinsicColourAveError = ObservedColourError.sum() / 4


colToRemove = []
appartentMagV_BandAve = appartentMagV_Band.sum() / 4
for i in range(len(intrinsicColourAve)):
   if intrinsicColourAve[i] < -0.35:
        colToRemove += [i]
intrinsicColourAve_Adjusted = np.array(intrinsicColourAve)
appartentMagV_BandAve_Adjusted = np.array(appartentMagV_BandAve)
intrinsicColourAve_Adjusted = np.delete(intrinsicColourAve_Adjusted, colToRemove)
appartentMagV_BandAve_Adjusted = np.delete(appartentMagV_BandAve_Adjusted, colToRemove)

idx = np.isfinite(np.array(intrinsicColourAve_Adjusted)) & np.isfinite(np.array(appartentMagV_BandAve_Adjusted))
a, b = np.polyfit(np.array(intrinsicColourAve_Adjusted)[idx] , np.array(appartentMagV_BandAve_Adjusted)[idx], 1)
A0_Star = b

Av = 3 * 0.22
distance = (10 ** ((A0_Star - 0.7 + 5 - Av) / 5))

appartentMagV_BandAveError = appartentMagV_BandError.sum() / 4
appartentMagV_BandAveErrorAve = appartentMagV_BandAveError.sum() / 83
distanceError = appartentMagV_BandAveErrorAve / 5
distanceError = distance * np.log(10) * distanceError

print(distance)
print(distanceError)

plt.title("Colour-Magnitude Diagram for Open Cluster M36")
plt.xlabel("Intrinsic Colour")
plt.ylabel("V-Band Apparent Magnitude")
plt.gca().invert_yaxis()
plt.scatter(np.array(intrinsicColourAve) , np.array(appartentMagV_BandAve), color="red") 
plt.show() 

iso_1plus6 =  pd.read_csv("Iso_1.00+06.csv")
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
plt.show() 



