from tkinter import *
import tkinter.scrolledtext as Tkscrolled
import os,sys
from tkinter.filedialog import askopenfilename,asksaveasfile
import random
import webbrowser
from copy import *

ftypes=[("C file","*.c")]
ttl="Choose directory"
dir1='C:\\'
root = Tk()
root.title("Lite C 1.0")

colors=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

root.configure(background="black",menu=Menu)
root.wm_attributes("-alpha",1.0)

locstore="";

def start_compile():
    output = ""
    code=input_box.get("1.0",END)
    file = open("testfile.c","w")
    file.write(code)
    file.close()
    os.system("gcc %s"%("testfile.c"))
    os.system("abc.bat")
    #os.system("a.exe > %s"%("output.txt"))
    """with open("output.txt") as f:
        for line in f:
            output += line"""
    #os.popen("start cmd /k a.exe") #uncomment this and comment from 'with open' to output+=line for scanf and CLI calls
    
    label.config(text=output)
input_box = Tkscrolled.ScrolledText(root, width=55,height=15,bg="black",fg="#15ea18",insertbackground="yellow",relief=GROOVE)
input_box.pack(side= TOP,fill="both",expand="yes")
compile_button = Button(root,text="COMPILE",command=lambda:start_compile(),background='black',foreground='#15ea18')
compile_button.pack(side=BOTTOM,fill="both",expand="yes")
label= Label(root)
label.pack(side=BOTTOM)

def newfile():
    input_box.delete('1.0',END)

def openfile():
    global locstore
    root.fileName=askopenfilename(filetypes=ftypes,initialdir=dir1,title=ttl)
    try:
        with open(root.fileName,'r') as f:
            newfile()
            input_box.insert(INSERT,f.read())
            locstore=deepcopy(root.fileName)
    except:
        print("File doesn't exist")

def savefile():
    global locstore
    if(locstore==""):
        root.fileName=asksaveasfile(filetypes=ftypes,initialdir=dir1,title=ttl)
        with open(root.fileName.name,'w') as f:
            xx=input_box.get('1.0',END)
            f.write(xx)
        locstore=deepcopy(root.fileName.name)
    else:
        with open(locstore,'w') as f:
            xx=input_box.get('1.0',END)
            f.write(xx)
        try:
            with open(locstore,'r') as f:
                newfile()
                input_box.insert(INSERT,f.read())
        except:
            print("File doesn't exist")

def savefileas():
    global locstore
    root.fileName=asksaveasfile(filetypes=ftypes,initialdir=dir1,title=ttl)
    try:
        with open(root.fileName.name,'w') as f:
            xx=input_box.get('1.0',END)
            f.write(xx)
            locstore=deepcopy(root.fileName.name)
        with open(locstore,'r') as f:
            newfile()
            input_box.insert(INSERT,f.read())
    except:
        print("File doesn't exist")

def curcol():
    selcol=random.choice(colors)
    input_box['insertbackground']=selcol

def bgcol():
    selcol=random.choice(colors)
    input_box['bg']=selcol

def fgcol():
    selcol=random.choice(colors)
    input_box['fg']=selcol

def bubgcol():
    selcol=random.choice(colors)
    compile_button['background']=selcol

def bufgcol():
    selcol=random.choice(colors)
    compile_button['foreground']=selcol

def givehelp():
    about_window=Tk()
    about_window.geometry("600x200")
    about_window.config(bg="black")
    about_label=Label(about_window,bg="black",font=(24),fg="green",text="This is a lite IDE for C/C++ programs\nJust press the compile button to run your program")
    about_label.pack(fill="both",expand="yes")
    about_window.mainloop()
    
def authors():
    webbrowser.open("https://www.linkedin.com/in/rudranil-sarkar-150744159/")
    webbrowser.open("https://www.linkedin.com/in/ankan-das-647592134/")   

def opacity(val):
    root.wm_attributes("-alpha",val)

slider=Scale(root,command=opacity,orient=HORIZONTAL,length=200,from_=0.1,to=1.0,tickinterval=0.5,resolution=0.1,background="black",foreground="white",relief=GROOVE)
slider.set(1.0)
slider.pack()

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="Save As",command=savefileas)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)
designmenu=Menu(menubar,tearoff=0)
designmenu.add_command(label="Cursor Color",command=curcol)
designmenu.add_command(label="Background Color",command=bgcol)
designmenu.add_command(label="Text Color",command=fgcol)
designmenu.add_command(label="Compile Button Background Color",command=bubgcol)
designmenu.add_command(label="Compile Button Text Color",command=bufgcol)
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=givehelp)
helpmenu.add_command(label="Authors",command=authors)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Design",menu=designmenu)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
