
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10216944
#    Student name: Jonty Graver
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'xhtml'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the invoice file. To simplify marking, your program should
# generate its invoice using this file name.
invoice_file = 'invoice.html'

add_check = 0 # Create a variable for reading which window is open, used for the add to cart button
item_check = 0 # Create a variable for checking whether an item has been added or not, used for the print invoice section
prices = [] # Create an empty list for prices
items = [] # Create an empty list for item names
image_links = [] # Create an empty list for image links
item_cart = [] # Create an empty list for item names in the cart
image_cart = [] # Create an empty list for image links in the cart
price_cart = [] # Create an empty list for prices in the cart

# Define the multiple shopping category windows and all their elements + the code for searching the pages

def shopping_1():
    # Modify add_check, define globals used and clear the display lists if they are full
    global add_check
    add_check = 1
    global items
    global prices
    global image_links
    del items[:]
    del prices[:]
    del image_links[:]

    # Create the window
    bgcolour='#33FF70'
    shopping_win = Tk()
    shopping_win.title('ShopExpress')
    shopping_win.resizable(width=False, height=False)
    shopping_win.configure(background=bgcolour)

    # Disable main window buttons while category page is open
    category_button_1['state'] = 'disabled'
    category_button_2['state'] = 'disabled'
    category_button_3['state'] = 'disabled'
    category_button_4['state'] = 'disabled'

    # Open the downloaded file and use regular expressions to find the relevant pieces of information
    download_file = open("Archived Web Docs\hats.xhtml", encoding = 'UTF-8')
    file_contents = download_file.read()
    item_names = findall('<title><!\[CDATA\[(.*?)]]></title>', file_contents)
    item_prices = re.compile('<description>.*?<strong>Price:(.*?)<\/strong>', re.DOTALL)
    item_prices_match = item_prices.findall(file_contents)
    item_images = findall('<isc:image><!\[CDATA\[(.*?)]]></isc:image>', file_contents)
    

    # Add the found items to the global lists
   
    items.extend(item_names)
    prices.extend(item_prices_match)
    image_links.extend(item_images)
    
    
    # Add the page elements and display the information
    shopping_title = Label(shopping_win, text = 'Western Hats', bg = bgcolour, font = (None, 22))
    shopping_title.grid(row=0, column=0)

    shopping_frame = Frame(shopping_win, bd=3,  relief = SUNKEN, bg = bgcolour)
    shopping_frame.grid(row=1, column=0, padx= 15)

    shopping_numbers1 = Label(shopping_frame, text = '#1: ' + items[1] + ' (' + prices[0] + ' )', bg = bgcolour)
    shopping_numbers2 = Label(shopping_frame, text = '#2: ' + items[2] + ' (' + prices[1] + ' )', bg = bgcolour)
    shopping_numbers3 = Label(shopping_frame, text = '#3: ' + items[3] + ' (' + prices[2] + ' )', bg = bgcolour)
    shopping_numbers4 = Label(shopping_frame, text = '#4: ' + items[4] + ' (' + prices[3] + ' )', bg = bgcolour)
    shopping_numbers5 = Label(shopping_frame, text = '#5: ' + items[5] + ' (' + prices[4] + ' )', bg = bgcolour)
    shopping_numbers6 = Label(shopping_frame, text = '#6: ' + items[6] + ' (' + prices[5] + ' )', bg = bgcolour)
    shopping_numbers7 = Label(shopping_frame, text = '#7: ' + items[7] + ' (' + prices[6] + ' )', bg = bgcolour)
    shopping_numbers8 = Label(shopping_frame, text = '#8: ' + items[8] + ' (' + prices[7] + ' )', bg = bgcolour)
    shopping_numbers9 = Label(shopping_frame, text = '#9: ' + items[9] + ' (' + prices[8] + ' )', bg = bgcolour)
    shopping_numbers10 = Label(shopping_frame, text = '#10: ' + items[10] + ' (' + prices[9] + ' )', bg = bgcolour)

    shopping_numbers1.grid(row=1, column=0)
    shopping_numbers2.grid(row=2, column=0)
    shopping_numbers3.grid(row=3, column=0)
    shopping_numbers4.grid(row=4, column=0)
    shopping_numbers5.grid(row=5, column=0)
    shopping_numbers6.grid(row=6, column=0)
    shopping_numbers7.grid(row=7, column=0)
    shopping_numbers8.grid(row=8, column=0)
    shopping_numbers9.grid(row=9, column=0)
    shopping_numbers10.grid(row=10, column=0)

    link = Label(shopping_win, text = 'http://www.westernhatstore.com/rss.php?type=rss', bg = bgcolour)
    link.grid(row=2, column=0)

    # Definition used for re-enabling the buttons on main window and clearing the lists
    def on_closing():
        shopping_win.destroy()
        category_button_1['state'] = 'normal'
        category_button_2['state'] = 'normal'
        category_button_3['state'] = 'normal'
        category_button_4['state'] = 'normal'
        
                                                        
    shopping_win.protocol("WM_DELETE_WINDOW", on_closing)

    

    
    

def shopping_2():
    
    # Modify add_check, define globals used and clear the display lists if they are full
    global add_check
    add_check = 2
    global items
    global prices
    global image_links
    del items[:]
    del prices[:]
    del image_links[:]

    # Create the window
    bgcolour='#33FF70'
    shopping_win = Tk()
    shopping_win.title('ShopExpress')
    shopping_win.resizable(width=False, height=False)
    shopping_win.configure(background=bgcolour)

    # Disable main window buttons while category page is open
    category_button_1['state'] = 'disabled'
    category_button_2['state'] = 'disabled'
    category_button_3['state'] = 'disabled'
    category_button_4['state'] = 'disabled'

    # Open the downloaded file and use regular expressions to find the relevant pieces of information
    download_file = open("Archived Web Docs\zombie.xhtml", encoding = 'UTF-8')
    global file_contents
    file_contents = download_file.read()
    item_names = findall('<title><!\[CDATA\[(.*?)]]></title>', file_contents)
    item_prices = re.compile('<description>.*?<strong>Price:(.*?)<\/strong>', re.DOTALL)
    item_prices_match = item_prices.findall(file_contents)
    item_images = findall('<isc:image><!\[CDATA\[(.*?)]]></isc:image>', file_contents)

    # Add the found items to the global lists
    items.extend(item_names)
    prices.extend(item_prices_match)
    image_links.extend(item_images)

    # Add the page elements and display the information
    shopping_title = Label(shopping_win, text = 'Zombie Unlimited', bg = bgcolour, font = (None, 22))
    shopping_title.grid(row=0, column=0)

    shopping_frame = Frame(shopping_win, bd=3,  relief = SUNKEN, bg = bgcolour)
    shopping_frame.grid(row=1, column=0)

    shopping_numbers1 = Label(shopping_frame, text = '#1: ' + items[1] + ' (' + prices[0] + ' )', bg = bgcolour)
    shopping_numbers2 = Label(shopping_frame, text = '#2: ' + items[2] + ' (' + prices[1] + ' )', bg = bgcolour)
    shopping_numbers3 = Label(shopping_frame, text = '#3: ' + items[3] + ' (' + prices[2] + ' )', bg = bgcolour)
    shopping_numbers4 = Label(shopping_frame, text = '#4: ' + items[4] + ' (' + prices[3] + ' )', bg = bgcolour)
    shopping_numbers5 = Label(shopping_frame, text = '#5: ' + items[5] + ' (' + prices[4] + ' )', bg = bgcolour)
    shopping_numbers6 = Label(shopping_frame, text = '#6: ' + items[6] + ' (' + prices[5] + ' )', bg = bgcolour)
    shopping_numbers7 = Label(shopping_frame, text = '#7: ' + items[7] + ' (' + prices[6] + ' )', bg = bgcolour)
    shopping_numbers8 = Label(shopping_frame, text = '#8: ' + items[8] + ' (' + prices[7] + ' )', bg = bgcolour)
    shopping_numbers9 = Label(shopping_frame, text = '#9: ' + items[9] + ' (' + prices[8] + ' )', bg = bgcolour)
    shopping_numbers10 = Label(shopping_frame, text = '#10: ' + items[10] + ' (' + prices[9] + ' )', bg = bgcolour)


    shopping_numbers1.grid(row=1, column=0)
    shopping_numbers2.grid(row=2, column=0)
    shopping_numbers3.grid(row=3, column=0)
    shopping_numbers4.grid(row=4, column=0)
    shopping_numbers5.grid(row=5, column=0)
    shopping_numbers6.grid(row=6, column=0)
    shopping_numbers7.grid(row=7, column=0)
    shopping_numbers8.grid(row=8, column=0)
    shopping_numbers9.grid(row=9, column=0)
    shopping_numbers10.grid(row=10, column=0)

    link = Label(shopping_win, text = 'http://zombieunlimited.com/rss.php?action=popularproducts&type=rss', bg = bgcolour)
    link.grid(row=2, column=0)
    
    # Definition used for re-enabling the buttons on main window and clearing the lists
    def on_closing():
        shopping_win.destroy()
        category_button_1['state'] = 'normal'
        category_button_2['state'] = 'normal'
        category_button_3['state'] = 'normal'
        category_button_4['state'] = 'normal'

                                                        
    shopping_win.protocol("WM_DELETE_WINDOW", on_closing)



    
def shopping_3():
    
    # Modify add_check, define globals used and clear the display lists if they are full
    global add_check
    add_check = 3
    global items
    global prices
    global image_links
    del items[:]
    del prices[:]
    del image_links[:]

    # Create the window
    bgcolour='#33FF70'
    shopping_win = Tk()
    shopping_win.title('ShopExpress')
    shopping_win.resizable(width=False, height=False)
    shopping_win.configure(background=bgcolour)
    
    # Disable main window buttons while category page is open
    category_button_1['state'] = 'disabled'
    category_button_2['state'] = 'disabled'
    category_button_3['state'] = 'disabled'
    category_button_4['state'] = 'disabled'

    # Access the Webpage and display the text using Regex
    download(url = "https://www.shoeever.com/rss.php?type=rss")
    download_file = open("download.xhtml", encoding = 'UTF-8')
    file_contents = download_file.read()
    item_names = findall('<title><!\[CDATA\[(.*?)]]></title>', file_contents)
    item_prices = re.compile('<description>.*?<strong>Price:(.*?)<\/strong>', re.DOTALL)
    item_prices_match = item_prices.findall(file_contents)
    item_images = findall('<isc:image><!\[CDATA\[(.*?)]]></isc:image>', file_contents)

    # Add the found items to the global lists
    items.extend(item_names)
    prices.extend(item_prices_match)
    image_links.extend(item_images)

    # Add the page elements and display the information
    shopping_title = Label(shopping_win, text = 'ShoeEver', bg = bgcolour, font = (None, 22))
    shopping_title.grid(row=0, column=0)

    shopping_frame = Frame(shopping_win, bd=3,  relief = SUNKEN, bg = bgcolour)
    shopping_frame.grid(row=1, column=0, padx= 15)

    shopping_numbers1 = Label(shopping_frame, text = '#1: ' + items[1] + ' (' + prices[0] + ' )', bg = bgcolour)
    shopping_numbers2 = Label(shopping_frame, text = '#2: ' + items[2] + ' (' + prices[1] + ' )', bg = bgcolour)
    shopping_numbers3 = Label(shopping_frame, text = '#3: ' + items[3] + ' (' + prices[2] + ' )', bg = bgcolour)
    shopping_numbers4 = Label(shopping_frame, text = '#4: ' + items[4] + ' (' + prices[3] + ' )', bg = bgcolour)
    shopping_numbers5 = Label(shopping_frame, text = '#5: ' + items[5] + ' (' + prices[4] + ' )', bg = bgcolour)
    shopping_numbers6 = Label(shopping_frame, text = '#6: ' + items[6] + ' (' + prices[5] + ' )', bg = bgcolour)
    shopping_numbers7 = Label(shopping_frame, text = '#7: ' + items[7] + ' (' + prices[6] + ' )', bg = bgcolour)
    shopping_numbers8 = Label(shopping_frame, text = '#8: ' + items[8] + ' (' + prices[7] + ' )', bg = bgcolour)
    shopping_numbers9 = Label(shopping_frame, text = '#9: ' + items[9] + ' (' + prices[8] + ' )', bg = bgcolour)
    shopping_numbers10 = Label(shopping_frame, text = '#10: ' + items[10] + ' (' + prices[9] + ' )', bg = bgcolour)


    shopping_numbers1.grid(row=1, column=0)
    shopping_numbers2.grid(row=2, column=0)
    shopping_numbers3.grid(row=3, column=0)
    shopping_numbers4.grid(row=4, column=0)
    shopping_numbers5.grid(row=5, column=0)
    shopping_numbers6.grid(row=6, column=0)
    shopping_numbers7.grid(row=7, column=0)
    shopping_numbers8.grid(row=8, column=0)
    shopping_numbers9.grid(row=9, column=0)
    shopping_numbers10.grid(row=10, column=0)

    link = Label(shopping_win, text = 'https://www.shoeever.com/rss.php?type=rss', bg = bgcolour)
    link.grid(row=2, column=0)

    # Definition used for re-enabling the buttons on main window and clearing the lists
    def on_closing():
        shopping_win.destroy()
        category_button_1['state'] = 'normal'
        category_button_2['state'] = 'normal'
        category_button_3['state'] = 'normal'
        category_button_4['state'] = 'normal'
                                  
    shopping_win.protocol("WM_DELETE_WINDOW", on_closing)
    
   
    
    



def shopping_4():
    
    # Modify add_check, define globals used and clear the display lists if they are full
    global add_check
    add_check = 4
    global items
    global prices
    global image_links
    del items[:]
    del prices[:]
    del image_links[:]

    # Create the window
    bgcolour='#33FF70'
    shopping_win = Tk()
    shopping_win.title('ShopExpress')
    shopping_win.resizable(width=False, height=False)
    shopping_win.configure(background=bgcolour)

    # Disable main window buttons while category page is open
    category_button_1['state'] = 'disabled'
    category_button_2['state'] = 'disabled'
    category_button_3['state'] = 'disabled'
    category_button_4['state'] = 'disabled'

    # Access the Webpage and display the text using Regex
    download(url = "https://frankiesautoelectrics.com.au/rss.php?type=rss")
    download_file = open("download.xhtml", encoding = 'UTF-8')
    file_contents = download_file.read()
    item_names = findall('<title><!\[CDATA\[(.*?)]]></title>', file_contents)
    item_prices = re.compile('<description>.*?<strong>Price:(.*?)<\/strong>', re.DOTALL)
    item_prices_match = item_prices.findall(file_contents)
    item_images = findall('<isc:image><!\[CDATA\[(.*?)]]></isc:image>', file_contents)

    # Add the found items to the global lists
    items.extend(item_names)
    prices.extend(item_prices_match)
    image_links.extend(item_images)

    # Add the page elements and display the information  
    shopping_title = Label(shopping_win, text = 'Auto Electrics', bg = bgcolour, font = (None, 22))
    shopping_title.grid(row=0, column=0)

    shopping_frame = Frame(shopping_win, bd=3,  relief = SUNKEN, bg = bgcolour)
    shopping_frame.grid(row=1, column=0, padx= 15)

    shopping_numbers1 = Label(shopping_frame, text = '#1: ' + items[1] + ' (' + prices[0] + ' )', bg = bgcolour)
    shopping_numbers2 = Label(shopping_frame, text = '#2: ' + items[2] + ' (' + prices[1] + ' )', bg = bgcolour)
    shopping_numbers3 = Label(shopping_frame, text = '#3: ' + items[3] + ' (' + prices[2] + ' )', bg = bgcolour)
    shopping_numbers4 = Label(shopping_frame, text = '#4: ' + items[4] + ' (' + prices[3] + ' )', bg = bgcolour)
    shopping_numbers5 = Label(shopping_frame, text = '#5: ' + items[5] + ' (' + prices[4] + ' )', bg = bgcolour)
    shopping_numbers6 = Label(shopping_frame, text = '#6: ' + items[6] + ' (' + prices[5] + ' )', bg = bgcolour)
    shopping_numbers7 = Label(shopping_frame, text = '#7: ' + items[7] + ' (' + prices[6] + ' )', bg = bgcolour)
    shopping_numbers8 = Label(shopping_frame, text = '#8: ' + items[8] + ' (' + prices[7] + ' )', bg = bgcolour)
    shopping_numbers9 = Label(shopping_frame, text = '#9: ' + items[9] + ' (' + prices[8] + ' )', bg = bgcolour)
    shopping_numbers10 = Label(shopping_frame, text = '#10: ' + items[10] + ' (' + prices[9] + ' )', bg = bgcolour)


    shopping_numbers1.grid(row=1, column=0)
    shopping_numbers2.grid(row=2, column=0)
    shopping_numbers3.grid(row=3, column=0)
    shopping_numbers4.grid(row=4, column=0)
    shopping_numbers5.grid(row=5, column=0)
    shopping_numbers6.grid(row=6, column=0)
    shopping_numbers7.grid(row=7, column=0)
    shopping_numbers8.grid(row=8, column=0)
    shopping_numbers9.grid(row=9, column=0)
    shopping_numbers10.grid(row=10, column=0)

    link = Label(shopping_win, text = 'https://frankiesautoelectrics.com.au/rss.php?type=rss', bg = bgcolour)
    link.grid(row=2, column=0)

    # Definition used for re-enabling the buttons on main window and clearing the lists
    def on_closing():
        shopping_win.destroy()
        category_button_1['state'] = 'normal'
        category_button_2['state'] = 'normal'
        category_button_3['state'] = 'normal'
        category_button_4['state'] = 'normal'
      
                                                        
    shopping_win.protocol("WM_DELETE_WINDOW", on_closing)
    


# SHOPPING WINDOWS END #


# Define the add to cart commands using if statement to determine which window is selected and which items are to be added

def add_to_cart():
    # Retrieve global variables
    global add_check
    global item_check
    global image_links
    global prices
    global items
    global item_cart
    global price_cart
    global image_cart
    if add_check == 0: # If no category has been selected, do nothing
        pass
    elif add_check == 1: # If first has been selected, use if statements to determine the item being selected
        if item_number_select.get() == '1':
            item_check = 1
            price_cart.append(prices[0])
            image_cart.append(image_links[0])
            item_cart.append(items[1])
        elif item_number_select.get() == '2':
            item_check = 1
            price_cart.append(prices[1])
            image_cart.append(image_links[1])
            item_cart.append(items[2])
        elif item_number_select.get() == '3':
            item_check = 1
            price_cart.append(prices[2])
            image_cart.append(image_links[2])
            item_cart.append(items[3])
        elif item_number_select.get() == '4':
            item_check = 1
            price_cart.append(prices[3])
            image_cart.append(image_links[3])
            item_cart.append(items[4])
        elif item_number_select.get() == '5':
            item_check = 1
            price_cart.append(prices[4])
            image_cart.append(image_links[4])
            item_cart.append(items[5])
        elif item_number_select.get() == '6':
            item_check = 1
            price_cart.append(prices[5])
            image_cart.append(image_links[5])
            item_cart.append(items[6])
        elif item_number_select.get() == '7':
            item_check = 1
            price_cart.append(prices[6])
            image_cart.append(image_links[6])
            item_cart.append(items[7])
        elif item_number_select.get() == '8':
            item_check = 1
            price_cart.append(prices[7])
            image_cart.append(image_links[7])
            item_cart.append(items[8])
        elif item_number_select.get() == '9':
            item_check = 1
            price_cart.append(prices[8])
            image_cart.append(image_links[8])
            item_cart.append(items[9])
        elif item_number_select.get() == '10':
            item_check = 1
            price_cart.append(prices[9])
            image_cart.append(image_links[9])
            item_cart.append(items[10])
        
    elif add_check == 2: # If second has been selected, use if statements to determine the item being selected
        if item_number_select.get() == '1':
            item_check = 1
            price_cart.append(prices[0])
            image_cart.append(image_links[0])
            item_cart.append(items[1])
        elif item_number_select.get() == '2':
            item_check = 1
            price_cart.append(prices[1])
            image_cart.append(image_links[1])
            item_cart.append(items[2])
        elif item_number_select.get() == '3':
            item_check = 1
            price_cart.append(prices[2])
            image_cart.append(image_links[2])
            item_cart.append(items[3])
        elif item_number_select.get() == '4':
            item_check = 1
            price_cart.append(prices[3])
            image_cart.append(image_links[3])
            item_cart.append(items[4])
        elif item_number_select.get() == '5':
            item_check = 1
            price_cart.append(prices[4])
            image_cart.append(image_links[4])
            item_cart.append(items[5])
        elif item_number_select.get() == '6':
            item_check = 1
            price_cart.append(prices[5])
            image_cart.append(image_links[5])
            item_cart.append(items[6])
        elif item_number_select.get() == '7':
            item_check = 1
            price_cart.append(prices[6])
            image_cart.append(image_links[6])
            item_cart.append(items[7])
        elif item_number_select.get() == '8':
            item_check = 1
            price_cart.append(prices[7])
            image_cart.append(image_links[7])
            item_cart.append(items[8])
        elif item_number_select.get() == '9':
            item_check = 1
            price_cart.append(prices[8])
            image_cart.append(image_links[8])
            item_cart.append(items[9])
        elif item_number_select.get() == '10':
            item_check = 1
            price_cart.append(prices[9])
            image_cart.append(image_links[9])
            item_cart.append(items[10])
            
    elif add_check == 3: # If third has been selected, use if statements to determine the item being selected
        if item_number_select.get() == '1':
            item_check = 1
            price_cart.append(prices[0])
            image_cart.append(image_links[0])
            item_cart.append(items[1])
        elif item_number_select.get() == '2':
            item_check = 1
            price_cart.append(prices[1])
            image_cart.append(image_links[1])
            item_cart.append(items[2])
        elif item_number_select.get() == '3':
            item_check = 1
            price_cart.append(prices[2])
            image_cart.append(image_links[2])
            item_cart.append(items[3])
        elif item_number_select.get() == '4':
            item_check = 1
            price_cart.append(prices[3])
            image_cart.append(image_links[3])
            item_cart.append(items[4])
        elif item_number_select.get() == '5':
            item_check = 1
            price_cart.append(prices[4])
            image_cart.append(image_links[4])
            item_cart.append(items[5])
        elif item_number_select.get() == '6':
            item_check = 1
            price_cart.append(prices[5])
            image_cart.append(image_links[5])
            item_cart.append(items[6])
        elif item_number_select.get() == '7':
            item_check = 1
            price_cart.append(prices[6])
            image_cart.append(image_links[6])
            item_cart.append(items[7])
        elif item_number_select.get() == '8':
            item_check = 1
            price_cart.append(prices[7])
            image_cart.append(image_links[7])
            item_cart.append(items[8])
        elif item_number_select.get() == '9':
            item_check = 1
            price_cart.append(prices[8])
            image_cart.append(image_links[8])
            item_cart.append(items[9])
        elif item_number_select.get() == '10':
            item_check = 1
            price_cart.append(prices[9])
            image_cart.append(image_links[9])
            item_cart.append(items[10])
        
    elif add_check == 4: # If fourth has been selected, use if statements to determine the item being selected
        if item_number_select.get() == '1':
            item_check = 1
            price_cart.append(prices[0])
            image_cart.append(image_links[0])
            item_cart.append(items[1])
        elif item_number_select.get() == '2':
            item_check = 1
            price_cart.append(prices[1])
            image_cart.append(image_links[1])
            item_cart.append(items[2])
        elif item_number_select.get() == '3':
            item_check = 1
            price_cart.append(prices[2])
            image_cart.append(image_links[2])
            item_cart.append(items[3])
        elif item_number_select.get() == '4':
            item_check = 1
            price_cart.append(prices[3])
            image_cart.append(image_links[3])
            item_cart.append(items[4])
        elif item_number_select.get() == '5':
            item_check = 1
            price_cart.append(prices[4])
            image_cart.append(image_links[4])
            item_cart.append(items[5])
        elif item_number_select.get() == '6':
            item_check = 1
            price_cart.append(prices[5])
            image_cart.append(image_links[5])
            item_cart.append(items[6])
        elif item_number_select.get() == '7':
            item_check = 1
            price_cart.append(prices[6])
            image_cart.append(image_links[6])
            item_cart.append(items[7])
        elif item_number_select.get() == '8':
            item_check = 1
            price_cart.append(prices[7])
            image_cart.append(image_links[7])
            item_cart.append(items[8])
        elif item_number_select.get() == '9':
            item_check = 1
            price_cart.append(prices[8])
            image_cart.append(image_links[8])
            item_cart.append(items[9])
        elif item_number_select.get() == '10':
            item_check = 1
            price_cart.append(prices[9])
            image_cart.append(image_links[9])
            item_cart.append(items[10])

# CART END #


# Define the print invoice command
def print_invoice():
    global item_check
    if item_check == 0: # Check if item has been added to cart, if not, print no sale invoice
        invoice = open(invoice_file, 'w')
        no_sale = """<!DOCTYPE html>
<html>

<head>
    <title>ShopExpress Invoice</title>
</head>
<header>
    <div align="center">
        <h1>Your ShopExpress Invoice!</h1>
        <img src="logo.gif">
        <h1>No items were found when checking out!</h1>
    </div>
</header>

</html>
        """
        invoice.write(no_sale)
        invoice.close()

    
    elif item_check == 1:
        # Define globals, some useful tags, convert the prices list to AUD and add them all up for the total sum
        global prices
        global items
        global image_links
        global descriptions
        table_tag_op = '<tr>'
        table_tag_en = '</tr>'
        table_data_op = '<td align="center">'
        table_data_en = '</td>'
        image_op = '<img src ='
        image_en = '</img>'
        test = '<p>HOWDY</p>'
        new_price_list1 = [i.strip(' $') for i in price_cart] # Strip the whitespace and $ from the list
        new_price_list2 = [i.replace(' $', '') for i in new_price_list1] # Replace the stripped items with an empty character
        amount_US = list(map(float, new_price_list2)) # Convert the strings in the list into floats
        amount_AUD = [item * 1.32 for item in amount_US] # Convert each price into AUD
        final_amount = sum(amount_AUD) # Add all prices together for the total amount
        final_amount_round = str(round(final_amount,2))
        invoice = open(invoice_file, 'w')

        # Define the content header to write to the page
        
        content_header = """<!DOCTYPE html>
<html>

<head>
    <title>ShopExpress Invoice</title>
</head>
<header>
    <div align="center">
        <h1>Your ShopExpress Invoice!</h1>
        <img src="logo.gif">
        <h1>Total Amount(AUD): $***AMOUNT***</h1>
    </div>
</header>

<body>
"""

        content_header_new = content_header.replace('***AMOUNT***', final_amount_round) # Replace the tagged amount with the final amount
        invoice.write(content_header_new)
        # Write the contents of the cart to the invoice
        cycle = 0
        for each in range(len(item_cart)):
            invoice.write('\n' + '<table align="center", border="1">')
            invoice.write('\n' + table_tag_op + '\n' + table_data_op + item_cart[cycle] + table_data_en + '\n' + table_tag_en)
            invoice.write('\n' + table_tag_op + '\n' + table_data_op + image_op + '"' + image_cart[cycle] + '"' + '>' + image_en + table_data_en + '\n' + table_tag_en)
            invoice.write('\n' + table_tag_op + '\n' + table_data_op + 'Our Price: ' + price_cart[cycle] + ' USD' + table_data_en + '\n' + table_tag_en)
            invoice.write('\n' + '</table>')
            cycle = cycle + 1

        
        # Define the content footer to write to the page
        content_footer = """
</body>
<footer>
    <p>Old Stock from:</p>
    <ul>
        <li>http://www.westernhatstore.com/rss.php?type=rss</li>
        <li>http://zombieunlimited.com/rss.php?action=popularproducts&type=rss</li>
    </ul>
    <p>New Stock from:</p>
    <ul>
        <li>https://www.shoeever.com/rss.php?type=rss</li>
        <li>https://frankiesautoelectrics.com.au/rss.php?type=rss</li>
    </ul>
</footer>
    </html>
"""
    

        invoice.write(content_footer)
        invoice.close()

        # PART B: DATABASE

        shopping_connect = connect('shopping_cart.db')
        shopping_view = shopping_connect.cursor()
        shopping_view.execute("""DELETE FROM ShoppingCart""") # Clear all current items in the database
        # Insert each item in the cart and their prices into the table
        for each in range(len(item_cart)):
            item = item_cart[each]
            price = price_cart[each]
            shopping_view.execute("""INSERT INTO ShoppingCart(Item, Price)
                                  VALUES(?,?)""", (item, price ))    
        
        shopping_connect.commit()
        shopping_view.close()
        shopping_connect.close()

        

# INVOICE END #
    
# Create the shopping app window and add all components

shopping_window = Tk()
shopping_window.title('ShopExpress')
shopping_window.resizable(width=False, height=False)
shopping_window.configure(background= '#A3D3F8')


# Create the title name and place it

title_label = Label(shopping_window, text = 'Welcome to ShopExpress!', bg = '#A3D3F8', font = (None, 22), width = 25, height = 2)
title_label.grid(row=0, column = 0, pady = 10, padx = 120)


# Create the image and place it

logo_img = PhotoImage(file="logo.gif")
logo = logo_img.subsample(4, 4)
logo_label = Label(image = logo, bg = '#A3D3F8')
logo_label.grid(row = 2, column = 0)


# Create the category title and place it

category_label = Label(shopping_window, bg = '#A3D3F8', text = 'Select a category:', font = (None, 18), width = 25, height = 2)
category_label.grid(row=3, column = 0, pady = 5, ipadx= 120 )


# Create the different buttons (in a frame) for selecting category and place them

category_frame_labels = Frame(shopping_window,  height = 10, width = 10,  relief = SUNKEN, bg='#A3D3F8')
category_frame_labels.grid(row=4, column=0, pady=5)

category_label_1 = Label(category_frame_labels, text='Old Stock', bg = '#A3D3F8')
category_label_2 = Label(category_frame_labels, text='New Stock', bg = '#A3D3F8') 


category_label_1.grid(row=0, column=0, padx=50)
category_label_2.grid(row=0, column=1, padx=50)

category_frame_buttons = Frame(shopping_window,  height = 10, width = 10, bd=3,  relief = SUNKEN, bg='#A3D3F8')
category_frame_buttons.grid(row=5, column=0)

v = IntVar()
category_button_1 = Radiobutton(category_frame_buttons, variable=v, value=1, text = "Hats", bg = '#A3D3F8', command = shopping_1,)
category_button_2 = Radiobutton(category_frame_buttons, variable=v, value=2, text = "Zombie Unlimited", bg = '#A3D3F8', command = shopping_2)
category_button_3 = Radiobutton(category_frame_buttons, variable=v, value=3, text = "ShoeEver", bg = '#A3D3F8', command = shopping_3)
category_button_4 = Radiobutton(category_frame_buttons, variable=v, value=4, text = "Auto Electrics", bg = '#A3D3F8', command = shopping_4)


category_button_1.grid(row=1, column=0, padx = 5)
category_button_2.grid(row=1, column=1, padx = 5)
category_button_3.grid(row=1, column=2, padx = 5)
category_button_4.grid(row=1, column=3, padx = 5)


# Create the item selection elements

item_frame = Frame(shopping_window, bg='#A3D3F8')
item_frame.grid(row=6, column=0)

item_number_label = Label(item_frame, bg = '#A3D3F8', text = 'Item number:', font = (None, 16), width = 12, height = 1)
item_number_select = Spinbox(item_frame, width = 10, state = 'readonly', values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


item_number_label.grid(row=0, column = 0, pady=15)
item_number_select.grid(row=0, column = 1, pady=10)


# Create the buttons for printing invoice and adding to cart

button_frame = Frame(shopping_window, bg='#A3D3F8')
button_frame.grid(row=7, column=0, pady = 15)

invoice_button = Button(button_frame, text = "Print Invoice", command = print_invoice)
invoice_button.grid(row=0, column=0, padx= 50)

add_button = Button(button_frame, text = "Add to Cart", command = add_to_cart)
add_button.grid(row=0, column=1, padx= 50)

# Run and Loop the program
shopping_window.mainloop()

# MAIN WINDOW END #
