"""
Script for turning the ppm values from Iolite 4 into molar ratios
"""

import re
import pandas as pd
from tqdm import tqdm  # Loading bar
import tkinter.filedialog

# Create the dialog window for choosing the file.
file_path = tkinter.filedialog.askopenfilename()

if file_path[-3:] == "csv":
    df = pd.read_csv(file_path)
elif file_path[-4:] == "xlsx":
    df = pd.read_excel(file_path, sheet_name="Data", engine="openpyxl")
    
# Hard coding all the RAM values
ramdict = {"H":"1.008", "He":"4.003","Li":"6.941","Be":"9.012","B":"10.811",
"C":"12.011","N":"14.007","O":"15.999","F":"18.998","Ne":"20.18","Na":"22.99",
"Mg":"24.305","Al":"26.982","Si":"28.086","P":"30.974","S":"32.065","Cl":"35.453",
"Ar":"39.948","K":"39.098","Ca":"40.078","Sc":"44.956","Ti":"47.867","V":"50.942",
"Cr":"51.996","Mn":"54.938","Fe":"55.845","Co":"58.933","Ni":"58.693",
"Cu":"63.546","Zn":"65.39","Ga":"69.723","Ge":"72.64","As":"74.922","Se":"78.96",
"Br":"79.904","Kr":"83.8","Rb":"85.468","Sr":"87.62","Y":"88.906","Zr":"91.224",
"Nb":"92.906","Mo":"95.94","Tc":"98","Ru":"101.07","Rh":"102.906","Pd":"106.42",
"Ag":"107.868","Cd":"112.411","In":"114.818","Sn":"118.71","Sb":"121.76",
"Te":"127.6","I":"126.905","Xe":"131.293","Cs":"132.906","Ba":"137.327",
"La":"138.906","Ce":"140.116","Pr":"140.908","Nd":"144.24","Pm":"145",
"Sm":"150.36","Eu":"151.964","Gd":"157.25","Tb":"158.925","Dy":"162.5",
"Ho":"164.93","Er":"167.259","Tm":"168.934","Yb":"173.04","Lu":"174.967",
"Hf":"178.49","Ta":"180.948","W":"183.84","Re":"186.207","Os":"190.23",
"Ir":"192.217","Pt":"195.078","Au":"196.967","Hg":"200.59","Tl":"204.383",
"Pb":"207.2","Bi":"208.98","Po":"209","At":"210","Rn":"222","Fr":"223",
"Ra":"226","Ac":"227","Th":"232.038","Pa":"231.036","U":"238.029","Np":"237",
"Pu":"244","Am":"243","Cm":"247","Bk":"247","Cf":"251","Es":"252","Fm":"257",
"Md":"258","No":"259","Lr":"262","Rf":"261","Db":"262","Sg":"266","Bh":"264",
"Hs":"277","Mt":"268","Ds":"281.164","Rg":"280.165","Cn":"285.117",
"Nh":"284.178","Fl":"289.19","Mc":"288.192","Lv":"293.204","Ts":"292.207","Og":"294.213"}

# Main loop
for i in tqdm(range(len(df.iloc[0,:]))):  # Loop through columns
    # Get the element of the column and the associated RAM value.
    element = re.search("([A-z]{1,2})", df.columns[i]).group()
    for k in ramdict:
        if k == element:
            ramval = float(ramdict[k])
    #Now looping through each row and change all the values in molar ratio
    for j in range(len(df)):
        if not pd.isna(df.iloc[j, i]):
            try:
                x = float(df.iloc[j, i])
                df.iloc[j, i] = (x/ramval) * (40.078/400400) * 1000
            except ValueError:
                pass

if file_path[-3:] == "csv":
    fname = file_path[:-4] + "_molar.csv"
    df.to_csv(file_path[:-4] + "_molar.csv", index=None)
elif file_path[-4:] == "xlsx":
    fname = file_path[:-5] + "_molar.csv"
    df.to_csv(fname, index=None)
   
print("All done! File saved at {}".format(fname))