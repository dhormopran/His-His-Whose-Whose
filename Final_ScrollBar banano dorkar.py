#almost everything ok except the populating system scrollbar


from tkinter import *

# global variables
##for 1st page

HMI_var = 0

HMIn_var = 0
# Item names and price dictionary

FoodItemsDict = {}
# Take all the inputs in a list then assign it to a tuple

FoodKeys = []
# list of Entry Widgets

list_Items_Entry = []
# list of items in string

items = []
# list of item's per price in integer

item_prices = []
# list of another entry widgets for per price

list_Items_Price_Entry = []
# tuple for the purpose of making key

tuple_key_item = ()
# need another tuple to make value of dictionary ( per price of the fooditems

tuple_value_perPriceOfItems = ()

# 3rd Page, list of entry widget to get the person names who ate item x
list_Items_who_Entry = []

# 4th page list of individuals, yes it is a set
set_of_individuals = []

# list of participant names systemized contains only names
# list_of_participants

# entry variable of 3rd page
# enter_nameOftheParticipants

# list of intvar() for checkbox values
check_intvars = []

# list of checkboxes
check_boxes = []
# values of intvars
list_valuesOfIntVars = []
# list of frames not so important
list_ofFrames = []
list_ofFrames2 = []
# list of entry widget fifth page
list_Entry_quantity = []
# list of quantities
list_float_quantity = []
# final sum of participants
list_float_bill = []


# function for sixth page
def sixthpage(root5):
    global tuple_key_item, tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items, item_prices, check_boxes, list_Entry_quantity, list_ofFrames2
    global list_Items_who_Entry, list_of_participants, enter_nameOftheParticipants, check_intvars
    global list_float_quantity, list_float_bill, list_ofFrames, list_ofFrames2

    list_float_bill = [0.0] * len(list_of_participants)

    for i in range(0, len(list_Entry_quantity)):
        list_float_quantity.append(float(list_Entry_quantity[i].get()))

    root5.destroy()
    root6 = Tk()
    root6.geometry("")

    for i in range(0, len(list_of_participants)):
        print(i)
        list_ofFrames.append(LabelFrame(root6, text="{}, you ate following items".format(list_of_participants[i])))
        list_ofFrames[-1].pack()

        person = 0
        loop_w = 0
        while ((i + person) < ((len(list_of_participants)) * HMI_var)):
            # ekhane input nite hobe
            # list_valuesofintvar[i+person]
            list_ofFrames2.append(LabelFrame(list_ofFrames[-1]))
            list_ofFrames2[-1].pack()
            if (list_valuesOfIntVars[i + person] > 0):
                Label(list_ofFrames2[-1],
                      text="Item name={}, Price={}, quantity:{}  ".format(items[loop_w], item_prices[loop_w],
                                                                          list_float_quantity[loop_w])).pack(side=LEFT)
                list_float_bill[i] = list_float_bill[i] + (item_prices[loop_w] * list_float_quantity[loop_w])

            person += len(list_of_participants)
            loop_w += 1

    for i in range(0, len(list_of_participants)):
        Label(root6, text="Total bill of {}, is {}".format(list_of_participants[i], list_float_bill[i])).pack()

    root6.mainloop()


# function for fifthpage
def fifthpage(root4):
    global tuple_key_item, tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items, item_prices, check_boxes, list_Entry_quantity, list_ofFrames2
    global list_Items_who_Entry, list_of_participants, enter_nameOftheParticipants, check_intvars

    for i in range(0, len(check_intvars)):
        list_valuesOfIntVars.append(check_intvars[i].get())

    print(list_valuesOfIntVars)
    root4.destroy()
    root5 = Tk()
    root5.geometry("")

    # person=0
    # need a looping variable

    for i in range(0, len(list_of_participants)):
        print(i)
        list_ofFrames.append(LabelFrame(root5,
                                        text="{}, please respond, enter the quantity of the items which u ate, ignore if the quantity is 1".format(
                                            list_of_participants[i])))
        list_ofFrames[-1].pack()

        person = 0
        loop_w = 0
        while ((i + person) < ((len(list_of_participants)) * HMI_var)):
            # ekhane input nite hobe
            # list_valuesofintvar[i+person]
            list_ofFrames2.append(LabelFrame(list_ofFrames[-1]))
            list_ofFrames2[-1].pack()
            if (list_valuesOfIntVars[i + person] > 0):
                Label(list_ofFrames2[-1],
                      text="Item name={}, Price={}, quantity:  ".format(items[loop_w], item_prices[loop_w])).pack(
                    side=LEFT)
                list_Entry_quantity.append(Entry(list_ofFrames2[-1], width="5"))
                list_Entry_quantity[-1].insert(END, "1")
                list_Entry_quantity[-1].pack(side=LEFT)
            else:
                Label(list_ofFrames2[-1],
                      text="Item name={}, Price={}, quantity:  ".format(items[loop_w], item_prices[loop_w])).pack(
                    side=LEFT)
                list_Entry_quantity.append(Entry(list_ofFrames2[-1], width="5"))
                list_Entry_quantity[-1].insert(END, "0")
                list_Entry_quantity[-1].pack(side=LEFT)

            person += len(list_of_participants)
            loop_w += 1

    # button of page 5
    button_5thpage = Button(root5, text="Next", command=lambda: sixthpage(root5))
    button_5thpage.pack()

    root5.mainloop()


# function checkbox maker
def checkbox_maker(root4, ii):
    global tuple_key_item, tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items, item_prices, check_boxes
    global list_Items_who_Entry, list_of_participants, enter_nameOftheParticipants, check_intvars

    '''for i in range(0,len(list_of_participants),1):
        check_intvars.append(IntVar())
        print(row_temp+1+i)
        check_boxes.append(Checkbutton(root4,variable =check_intvars[i] , text = list_of_participants[i], onvalue= item_prices[ii]))
        check_boxes[i].grid(row=row_temp+1+i, column=i)
        print(i)
    '''
    temp1 = LabelFrame(root4, text="Check the individuals name who ate the above Item")
    temp1.pack()

    for i in range(0, len(list_of_participants)):
        check_intvars.append(IntVar())

        check_boxes.append(
            Checkbutton(temp1, text=list_of_participants[i], variable=check_intvars[-1], onvalue=item_prices[ii]))
        # I want to print the last checkbox that was made by this loop thats why -1
        check_boxes[-1].pack(side=LEFT)


# function def for 4thpage

def fourthpage(root3):
    global tuple_key_item, tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items, item_prices, check_boxes
    global list_Items_who_Entry, list_of_participants, enter_nameOftheParticipants, check_intvars

    temp1 = (enter_nameOftheParticipants.get()).replace(" ", "")
    list_of_participants = (temp1.split(","))
    print(list_of_participants)

    root3.destroy()
    root4 = Tk()
    root4.geometry("")

    '''row_temp=0
    for i in range(0,len(items)):
        temp_p4L1=Label(root4, text= "Item Name is {}".format(items[i]))
        temp_p4L1.grid(row = row_temp, column =0)

        temp_p4L2=Label(root4, text="Price of the item is {}".format(item_prices[i]) )
        temp_p4L2.grid(row=row_temp, column=1)



        checkbox_maker(root4,i,row_temp)
        row_temp += 2
    '''

    for i in range(0, len(items), 1):
        # creating a labelFrame to insert Label of Item Price and
        temp1 = LabelFrame(root4)
        temp1.pack()
        Label(temp1, text="Item Name: {}".format(items[i])).pack(side=LEFT)
        Label(temp1, text=" Price:{}".format(item_prices[i])).pack(side=LEFT)

        checkbox_maker(root4, i)

    # fourth page button
    temp2 = LabelFrame(root4)
    temp2.pack()
    print("I am at temp2")
    button_4thpage = Button(temp2, text="Next", command=lambda: fifthpage(root4))
    button_4thpage.pack()

    root4.mainloop()


# function def for 3rd page
def thirdpage(root2):
    global tuple_key_item, tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items, item_prices, enter_nameOftheParticipants
    global list_Items_who_Entry

    for i in range(0, HMI_var, 1):
        ##print(len(list_Items_Entry))
        ##print(HMI_var)
        items.append(list_Items_Entry[i].get())
        ##print(int(list_Items_Price_Entry[i].get()))
        item_prices.append(int(list_Items_Price_Entry[i].get()))
    tuple_key_item = tuple(items)
    tuple_value_perPriceOfItems = tuple(item_prices)

    FoodKeys = dict(zip(tuple_key_item, tuple_value_perPriceOfItems))

    ##print(FoodKeys)  ##to see the dictionary values
    root2.destroy()
    root3 = Tk()
    root3.geometry("")

    # now we have to enter the participants name
    label_enterNameOfParticipants = Label(root3, text="Please enter the name of the participants, Comma seperated")
    label_enterNameOfParticipants.grid(row=0, column=0)
    enter_nameOftheParticipants = Entry(root3, width="100")
    enter_nameOftheParticipants.grid(row=1, column=0, rowspan=2)

    # define button for page 3
    button3 = Button(root3, text=" Next ", padx=100, command=lambda: fourthpage(root3))
    button3.grid(row=3, column=0, columnspan=10)

    root3.mainloop()


# function definition.... second page
def secondpage():
    global HMIn_var, HMI_var
    global list_Items_Entry, list_Items_Price_Entry
    HMI_var = int(HMI_entry.get())
    HMIn_var = int(HMIn_Entry.get())
    root.destroy()

    root2 = Tk()
    root2.geometry("")
    root2.title("Food Items and Values")

    for i in range(0, HMI_var, 1):
        Label(root2, text=str(i + 1) + "th Item").grid(row=i, column=0, columnspan=1)
        list_Items_Entry.append(Entry(root2, width="10"))
        list_Items_Entry[i].grid(row=i, column=1, columnspan=2)
        Label(root2, text=str(i + 1) + "th Item Per Price").grid(row=i, column=3, columnspan=1)
        list_Items_Price_Entry.append(Entry(root2, width="10"))
        list_Items_Price_Entry[i].grid(row=i, column=4, columnspan=2)
    # this button will take u to 3rd window
    ##print(HMI_var)
    Button_2ndPage = Button(root2, text="Next", command=lambda: thirdpage(root2))
    Button_2ndPage.grid(row=HMI_var + 1, column=0, columnspan=6)
    root2.mainloop()


# Program starts here
root = Tk()
root.title("HisHisWhoseWhose")
root.geometry("")
# How many Items
HMI = Label(root, text="How many Items").grid(row=0, column=0, columnspan=2)
HMI_entry = Entry(root, width="5")
HMI_entry.grid(row=0, column=3, columnspan=1)
# How many individuals
HMIn = Label(root, text="How many Individuals").grid(row=1, column=0, columnspan=2)
HMIn_Entry = Entry(root, width="5")
HMIn_Entry.grid(row=1, column=3, columnspan=1)
# submit
submit1 = Button(root, text="Submit", command=secondpage).grid(row=2, column=2, columnspan=1)

root.mainloop()