# lexical obfuscation

import json; import tkinter as tk; from tkinter import messagebox
import requests; from constants import USERS_PATH, API_KEY
class O0O0O0O0O0OOO00OO( tk.Entry):
    def __init__ (I1I1I1, I1II1I1111= None,B6B6B6B6B6B6B66BB6 =True, U_UUUU___   =10, **kwargs) :
        super().__init__ ( I1II1I1111, **kwargs)
        I1I1I1.Y8Y8Y8Y8Y8 = [''] * U_UUUU___ ;    I1I1I1.WWWWWWWWWWWW = U_UUUU___ ;   I1I1I1.O0O0OO0O00O0O = B6B6B6B6B6B6B66BB6
        I1I1I1.bind('<KeyRelease>',  I1I1I1.Y7YYYY77)
    def Y7YYYY77 (E3E3E3EE33E, Q1Q1Q1) :
        O0OO0O000000 = E3E3E3EE33E.get()
        if(E3E3E3EE33E.O0O0OO0O00O0O and len(O0OO0O000000) > E3E3E3EE33E.WWWWWWWWWWWW) :
            E3E3E3EE33E.delete(E3E3E3EE33E.WWWWWWWWWWWW, tk.END)
            E3E3E3EE33E.Y7YYYY77(Q1Q1Q1);  return
        O0OO0O000000 = list(O0OO0O000000);    E3E3E3EE33E.Y8Y8Y8Y8Y8 = [''] * E3E3E3EE33E.WWWWWWWWWWWW
        for R5R5RR5 in range(len(O0OO0O000000)) :
            E3E3E3EE33E.Y8Y8Y8Y8Y8[R5R5RR5] = O0OO0O000000[R5R5RR5]
    def I1I1I1I11I1I1(DdDDDDDDddvvv):
        return ''.join(DdDDDDDDddvvv.Y8Y8Y8Y8Y8)
def                 juJYJYJYYJHGHC():
    try:
        with open(USERS_PATH, 'r') as tttttititiiti:
            return json.load(tttttititiiti)
    except FileNotFoundError:
        return {}
def e3e3e3eDDDDDD(     TYTYY, O00000000QQQQQQQQOO00OO0)     :
    FHHHHHHHHHHHHHHH = juJYJYJYYJHGHC()
    if TYTYY in FHHHHHHHHHHHHHHH and FHHHHHHHHHHHHHHH[TYTYY]['password'] == O00000000QQQQQQQQOO00OO0:
        return FHHHHHHHHHHHHHHH[TYTYY]
    return None
def RRRORORORORO (I1I1I1II1I1II1I1I1I1II1, IIII1II1IIII1, IIIQIQIIIII1II1, I1I1II1II1II1III1) :
    IIIII1I111II1I1I1I = I1I1I1II1I1II1I1I1I1II1.I1I1I1I11I1I1(); I1I1I1I1II1II1I = IIII1II1IIII1.I1I1I1I11I1I1()
    II1II1I1III1IQII = e3e3e3eDDDDDD(IIIII1I111II1I1I1I, I1I1I1I1II1II1I)
    if(II1II1I1III1IQII ):
        if(I1I1II1II1II1III1) :
            if II1II1I1III1IQII['role'] == 'admin':
                OOOIIOO000(IIIII1I111II1I1I1I, IIIQIQIIIII1II1, I1I1II1II1II1III1)
            else:
                O0O0OO000O0O0O0O(IIIII1I111II1I1I1I, IIIQIQIIIII1II1, I1I1II1II1II1III1)
        else:
            OOOIIOO000(IIIII1I111II1I1I1I, IIIQIQIIIII1II1, I1I1II1II1II1III1) ;  O0O0OO000O0O0O0O(IIIII1I111II1I1I1I, IIIQIQIIIII1II1, I1I1II1II1II1III1)
        IIIQIQIIIII1II1.withdraw()
    else:
        messagebox.showerror('Error', 'Invalid username or password!!!')
def OO0O0O00OO00O0O(O000O0O0O0, O0O00O00O0OO0):
    O000O0O0O0.destroy()
    OOOOO0O0O0O0O0O0(O0O00O00O0OO0)
def O0O0OO000O0O0O0O(IOIOOOIOIOII0I0I0, O0O0O0OO00OO0R0ORO0, O0O00O0OF0OF0OF0O):
    I1I1III1II2I2I21II2I12 = tk.Toplevel(O0O0O0OO00OO0R0ORO0)
    I1I1III1II2I2I21II2I12.title(f'Welcome, {IOIOOOIOIOII0I0I0}!')
    I1I1I1I12I21I12II12(I1I1III1II2I2I21II2I12)
    O00OO99OO9O00O99O9899O9O = tk.Label(I1I1III1II2I2I21II2I12, text='Latitude:')
    O00OO99OO9O00O99O9899O9O.pack();    O0O0O0O04O0O040O40O = O0O0O0O0O0OOO00OO(I1I1III1II2I2I21II2I12, O0O00O0OF0OF0OF0O)
    O0O0O0O04O0O040O40O.pack() ;   OOPPPO998I88O88O = tk.Label(I1I1III1II2I2I21II2I12, text='Longitude:')
    OOPPPO998I88O88O.pack();
    O1O1O1O1O1O1OO1O1OO1O1 = O0O0O0O0O0OOO00OO(I1I1III1II2I2I21II2I12, O0O00O0OF0OF0OF0O)
    O1O1O1O1O1O1OO1O1OO1O1.pack()
    O1OOO1OO1O1O1O1O = tk.Button(I1I1III1II2I2I21II2I12, text='Show weather',
command=lambda: O1O1O1O1(O0O0O0O04O0O040O40O, 
                                                             O1O1O1O1O1O1OO1O1OO1O1, 
                                                             I1I1III1II2I2I21II2I12, O0O00O0OF0OF0OF0O))
    O1OOO1OO1O1O1O1O.pack() ;    I1I1III1II2I2I21II2I12.protocol("WM_DELETE_WINDOW", lambda: 
OO0O0O00OO00O0O(O0O0O0OO00OO0R0ORO0, O0O00O0OF0OF0OF0O))
def  O1O1O1O1            (U7UU7U7U77U7U, HH1H1H1HH1WJJ1, O1O1OO1OOO1OO1, OO1OO1OOO1):
    if (OO1OO1OOO1):
        hhfgfgfgfgf = O1O1OO1OOO1OO1.children['!button'];        hhfgfgfgfgf.config(state=tk.DISABLED)
        O1O1OO1OOO1OO1.after(5000,                  lambda: hhfgfgfgfgf.config(state=tk.NORMAL))
    IO1IO1IOI1 = U7UU7U7U77U7U.I1I1I1I11I1I1();    O11111111111O1O1OO1O1O1 = HH1H1H1HH1WJJ1.I1I1I1I11I1I1()
    if OO1OO1OOO1:
        if not IIII1I1I1I1O1O1OO1O1(IO1IO1IOI1, O11111111111O1O1OO1O1O1):
            messagebox.showerror('Error', 'Invalid latitude or longitude!')
            return
    OO1O1OO1O1OO1O1O1O = POPOPOPPOOPOPPPOOP(IO1IO1IOI1, O11111111111O1O1OO1O1O1);    UUUIUI1IU1UI1UIUI1(OO1O1OO1O1OO1O1O1O, O1O1OO1OOO1OO1)
def IIII1I1I1I1O1O1OO1O1    (O0O0OO0O00OO00OO0, OO0O00O00O0OO0O0):
    try:
        O0O0OO0O00OO00OO0 = float(O0O0OO0O00OO00OO0); OO0O00O00O0OO0O0 = float(OO0O00O00O0OO0O0)
        if -90 <= O0O0OO0O00OO00OO0 <= 90 and -180 <= OO0O00O00O0OO0O0 <= 180:
            return True
        else:
            return False
    except ValueError:
        return False
def POPOPOPPOOPOPPPOOP(O0O0OO0O00OO0O0, O0O0OOO00OO0O0OO0O0)   : 
    I1I1II1I1I1II1 = f'https://api.openweathermap.org/data/2.5/weather?lat={O0O0OO0O00OO0O0}&lon={O0O0OOO00OO0O0OO0O0}&appid={API_KEY}'
    I1II1II1I1II1I1II1I1I1 = requests.get(I1I1II1I1I1II1)
    OOO1OO1O1OO1OO1OO = I1II1II1I1II1I1II1I1I1.json()
    if I1II1II1I1II1I1II1I1I1.status_code == 200:
        IIIIII1I1II1IEI1EI1IE1IE = OOO1OO1O1OO1OO1OO['weather'][0]['description'] ;        I1I1II1I1I711I171I = OOO1OO1O1OO1OO1OO['main']['temp'] 
        HHHHH8H8H8H8H8H8 = I1I1II1I1I711I171I - 273.15 ;
        OIOIO1IO1OIO1IO1OI = OOO1OO1O1OO1OO1OO['name'] ;UUUUUUU0U0U0U00UU0U0 = OOO1OO1O1OO1OO1OO['sys'].get('country', 'N/A')
        return f'{OIOIO1IO1OIO1IO1OI}, {UUUUUUU0U0U0U00UU0U0}\n{IIIIII1I1II1IEI1EI1IE1IE.capitalize()}, {HHHHH8H8H8H8H8H8:.1f}°C'
    raise Exception('Error while getting weather!!!')
def UUUIUI1IU1UI1UIUI1(O0O00OO0O00O0O, O000O0O00OO0O00O)        :
    O0O00O0OO00000000000000000000000000 = O000O0O00OO0O00O.winfo_children()
    if O0O00O0OO00000000000000000000000000:
        O0000O0O0O0O00000000000 = O0O00O0OO00000000000000000000000000[-1]
        if isinstance(O0000O0O0O0O00000000000, tk.Label):
            O0000O0O0O0O00000000000.destroy()
    IOOIIOIODFIOIODFIODFIODFIODF = tk.Label(O000O0O00OO0O00O, text=O0O00OO0O00O0O);    IOOIIOIODFIOIODFIODFIODFIODF.pack()
def OOOIIOO000  (UIUIIUUIUIIUIUIIUIUIUIU, HEGRHGH4HRH4GHG     ,    IJEIFHUEUIRUIERUHERHUEU):
    KJDFJFDJDFSJJLDSFLJDFSDSF8 = tk.Toplevel(HEGRHGH4HRH4GHG);    KJDFJFDJDFSJJLDSFLJDFSDSF8.title(f'Welcome, {UIUIIUUIUIIUIUIIUIUIUIU}!')
    I1I1I1I12I21I12II12(KJDFJFDJDFSJJLDSFLJDFSDSF8)
    O11O1OO1111111O1O1O1O1O11O1O1OO1O1 = tk.Label(KJDFJFDJDFSJJLDSFLJDFSDSF8, text='Username:')
    O11O1OO1111111O1O1O1O1O11O1O1OO1O1.pack();
    O0O0OO0O00OO00O0O0O0OO0O0O0O0 = O0O0O0O0O0OOO00OO(KJDFJFDJDFSJJLDSFLJDFSDSF8, IJEIFHUEUIRUIERUHERHUEU)
    O0O0OO0O00OO00O0O0O0OO0O0O0O0.pack();    O0O0O00O0O0O0O00O0O0O0O0OO00OO0O00O = tk.Label(KJDFJFDJDFSJJLDSFLJDFSDSF8, text='Password:')
    O0O0O00O0O0O0O00O0O0O0O0OO00OO0O00O.pack();
    O00O00000O0O0O00O0O0OO0 = O0O0O0O0O0OOO00OO(KJDFJFDJDFSJJLDSFLJDFSDSF8, IJEIFHUEUIRUIERUHERHUEU, show='*')
    O00O00000O0O0O00O0O0OO0.pack();    O0O00OO00OO0O00O01O1O01O0O010O1 = tk.Button(KJDFJFDJDFSJJLDSFLJDFSDSF8, text='Add User', 
                                 command=lambda: 
OIOIOIIOIOIOIOIOIO(O0O0OO0O00OO00O0O0O0OO0O0O0O0.I1I1I1I11I1I1(), O00O00000O0O0O00O0O0OO0.I1I1I1I11I1I1(), IJEIFHUEUIRUIERUHERHUEU))
    O0O00OO00OO0O00O01O1O01O0O010O1.pack();    KJDFJFDJDFSJJLDSFLJDFSDSF8.protocol("WM_DELETE_WINDOW", 
                    lambda: OO0O0O00OO00O0O(HEGRHGH4HRH4GHG, IJEIFHUEUIRUIERUHERHUEU))
def OIOIOIIOIOIOIOIOIO(I9I9I9I99II99I9II99I9I, II1I1I1II1I1II1I1, I1I1I1II1I1II1I1II1I)   :
    OIOIIOIO1IOIO1IO1IO = juJYJYJYYJHGHC()
    if I1I1I1II1I1II1I1II1I:
        if I9I9I9I99II99I9II99I9I not in OIOIIOIO1IOIO1IO1IO:
            OIOIIOIO1IOIO1IO1IO[I9I9I9I99II99I9II99I9I] = {'password': II1I1I1II1I1II1I1, 'role': 'user'}
            with open(USERS_PATH, 'w') as OPOPOPO1PO1POP1OPO1PO1:
                json.dump(OIOIIOIO1IOIO1IO1IO, OPOPOPO1PO1POP1OPO1PO1)
            messagebox.showinfo('Success', 'User added successfully!')
        else:
            messagebox.showerror('Error', 'User already exists!')
    else:
        OIOIIOIO1IOIO1IO1IO[I9I9I9I99II99I9II99I9I] = {'password': II1I1I1II1I1II1I1, 'role': 'user'}
        with open(USERS_PATH, 'w') as OPOPOPO1PO1POP1OPO1PO1:
            json.dump(OIOIIOIO1IOIO1IO1IO, OPOPOPO1PO1POP1OPO1PO1)
def     I1I1I1I12I21I12II12(  POPOPOPOPOPOPO1OPOP1OP1PO1):
    POPOPOPOPOPOPO1OPOP1OP1PO1.geometry('400x200');     POPOPOPOPOPOPO1OPOP1OP1PO1.update_idletasks()
    I0I00I0I0II0 = POPOPOPOPOPOPO1OPOP1OP1PO1.winfo_width();     O1O1O1O1OO1O1 = POPOPOPOPOPOPO1OPOP1OP1PO1.winfo_height()
    O0O0O0OO0O0O0O00O = (POPOPOPOPOPOPO1OPOP1OP1PO1.winfo_screenwidth() - I0I00I0I0II0) // 2;
    I1I1I1I1II1I1I1 = (POPOPOPOPOPOPO1OPOP1OP1PO1.winfo_screenheight() - O1O1O1O1OO1O1) // 2
    POPOPOPOPOPOPO1OPOP1OP1PO1.geometry(f'+{O0O0O0OO0O0O0O00O}+{I1I1I1I1II1I1I1}') ;    POPOPOPOPOPOPO1OPOP1OP1PO1.focus_set()
def  OOOOO0O0O0O0O0O0 (O0O0O0OO00O0O0O0OO0O0) :
    I1I1I1I1II1I1I1II1II1I1I1I = tk.Tk();    I1I1I1I1II1I1I1II1II1I1I1I.title('Authentication')
    I1I1I1I12I21I12II12(I1I1I1I1II1I1I1II1II1I1I1I) ;    IO1IO1IOIO1IOIO1I1OI = tk.Label(I1I1I1I1II1I1I1II1II1I1I1I, text='Username:')
    IO1IO1IOIO1IOIO1I1OI.pack(); O0O0OO0O0O0O0O0 = O0O0O0O0O0OOO00OO(I1I1I1I1II1I1I1II1II1I1I1I, O0O0O0OO00O0O0O0OO0O0)
    O0O0OO0O0O0O0O0.pack() ;
    I1II1II18I881I = tk.Label(I1I1I1I1II1I1I1II1II1I1I1I, text='Password:')
    I1II1II18I881I.pack()    ; 
    OI00I00IOO00O0O = O0O0O0O0O0OOO00OO(I1I1I1I1II1I1I1II1II1I1I1I, O0O0O0OO00O0O0O0OO0O0, show='*')
    OI00I00IOO00O0O.pack();  O0O9I99O00OO00O = tk.Button(I1I1I1I1II1I1I1II1II1I1I1I, text='Login', 
                             command=lambda: RRRORORORORO(O0O0OO0O0O0O0O0, OI00I00IOO00O0O, I1I1I1I1II1I1I1II1II1I1I1I, O0O0O0OO00O0O0O0OO0O0))
    O0O9I99O00OO00O.pack() ;  I1I1I1I1II1I1I1II1II1I1I1I.mainloop()