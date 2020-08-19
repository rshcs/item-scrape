import tkinter 
from tkinter import messagebox
import datetime
import aex, ebay
import csv

#-----sizes settings-----------------
init_h = 15 #y1
entr_box_h = 30 #y2
lbl_h = 2
h2 = 30   #30

init_w = 2 # x1
big_w = 500 
seller_bx_w = 380 #x2
price_bx_w = 70
mx_lbl_w = 48

btn_w = 80
btn_dst = 60

window_w = 2 * init_w + mx_lbl_w + big_w + 10

#-----window settings----------------
window = tkinter.Tk()
window.title('Items scraper')
def set_window_geo(w, h):
    out_val = str(w) + 'x' + str(h)
    return out_val

window.geometry(set_window_geo(window_w, init_h + 5 * entr_box_h + 12))

#------icon--------------------------
window.iconphoto(False, tkinter.PhotoImage(file='E:\Documents\Python\item scrape\icon.png'))

#------Labels-----------------------
url_lbl = tkinter.Label(text = "URL :")
item_lbl = tkinter.Label(text = "Item :")
seller_lbl = tkinter.Label(text = "Seller :")
price_lbl = tkinter.Label(text = "Price :")
#status_lbl = tkinter.Label(text = "Status ")

#-------Entries----------------------
url_entr = tkinter.Entry()
item_entr = tkinter.Entry()
seller_entr = tkinter.Entry()
price_entr = tkinter.Entry()

#------Button functions------------------

def read_fnc():
    '''
    clip_text = window.clipboard_get()
    url_entr.insert(0, clip_text)
    #url = url_entr.get()
    '''
    url_in = url_entr.get()

    if url_in[:24] == 'https://www.ebay.com/itm':
        itm = ebay.Ebay(url_in)
        get_info(itm)
    elif url_in[:31] == 'https://www.aliexpress.com/item':
        itm = aex.Aex(url_in)
        get_info(itm)
    else:
        messagebox.showerror('Error', 'url not support !')
    
def get_info(in_val): # read values from web page and insert them into entries
    item_entr.delete(0, tkinter.END)
    seller_entr.delete(0, tkinter.END)
    price_entr.delete(0, tkinter.END)
    
    item_entr.insert(0, in_val.get_title())
    seller_entr.insert(0, in_val.get_seller())
    price_entr.insert(0, in_val.get_price()) 
           
def save_fnc():
    print('saved to the file')
    csv_write()

def clear_fnc():
    for i in [url_entr, item_entr, seller_entr, price_entr]:
        i.delete(0, "end")

#----------Other functions----------------------------

def csv_write():
    title = item_entr.get()
    seller = seller_entr.get()
    price = price_entr.get()

    file_name = 'E:\Documents\Python\item scrape\items.csv'
    
    with open(file_name, 'a', newline='') as csv_file:
        my_writer = csv.writer(csv_file)
        time_now = datetime.datetime.now()
        my_writer.writerow([time_now.strftime('%d/%m/%Y'),time_now.strftime('%H:%M'), title, seller, price])

last_clip_txt = ""
def clip_board_fnc():
    global clip_txt, last_clip_txt
    clip_txt = window.clipboard_get()
    #print(clip_txt)
    if clip_txt != last_clip_txt:
        last_clip_txt = clip_txt
        url_entr.delete(0, 'end')
        url_entr.insert(0, last_clip_txt)

    window.after(1000, clip_board_fnc)
     
def close_fnc():
    msgbx = messagebox.askyesnocancel("Item Scrape", "Do you want to save changes?")
    if msgbx == True:
        print('saved to the file')
        window.destroy()
    elif msgbx == False:
        window.destroy()
    else:
        pass


window.protocol('WM_DELETE_WINDOW', close_fnc)
clip_board_fnc()

#------Buttons---------------------------
read_btn = tkinter.Button(text = 'Read', command = read_fnc)
save_btn = tkinter.Button(text = 'Save', command = save_fnc)
clear_btn = tkinter.Button(text = 'Clear', command = clear_fnc)

#------Placing---------------------------
url_lbl.place(x = init_w + 7, y = init_h - lbl_h)
url_entr.place(x = mx_lbl_w + init_w, y = init_h, width = big_w)

item_lbl.place(x = init_w + 4, y = init_h - lbl_h + entr_box_h)
item_entr.place(x = mx_lbl_w + init_w, y = init_h + entr_box_h, width = big_w)

seller_lbl.place(x = init_w, y = init_h - lbl_h + 2 * entr_box_h)
seller_entr.place(x = mx_lbl_w + init_w, y = init_h + 2 * entr_box_h, width = seller_bx_w)

price_lbl.place(x = mx_lbl_w + init_w + seller_bx_w + 5, y = init_h - lbl_h + 2 * entr_box_h)
price_entr.place(x = mx_lbl_w + init_w + seller_bx_w + 50, y = init_h + 2 * entr_box_h, width = price_bx_w)

read_btn.place(x = 3*window_w / 11 - btn_w, y = 4 * entr_box_h, width = btn_w)
save_btn.place(x = window_w / 2 - btn_w / 2 , y = 4 * entr_box_h, width = btn_w)
clear_btn.place(x = 8 * window_w / 11, y = 4 * entr_box_h, width = btn_w)
#status_lbl.place(x = 3 * btn_dst + 2 * btn_w, y = 4 * entr_box_h + 2 * lbl_h)


window.mainloop()

