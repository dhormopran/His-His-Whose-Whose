#fourth page is done , except for the functionality

from tkinter import *
#global variables
##for 1st page

HMI_var=0

HMIn_var=0
# Item names and price dictionary

FoodItemsDict={}
#Take all the inputs in a list then assign it to a tuple

FoodKeys=[]
# list of Entry Widgets

list_Items_Entry = []
#list of items in string

items=[]
#list of item's per price in integer

item_prices=[]
#list of another entry widgets for per price

list_Items_Price_Entry=[]
#tuple for the purpose of making key

tuple_key_item=()
#need another tuple to make value of dictionary ( per price of the fooditems

tuple_value_perPriceOfItems=()

#3rd Page, list of entry widget to get the person names who ate item x
list_Items_who_Entry = []

#4th page list of individuals, yes it is a set
set_of_individuals = []

#list of participant names systemized contains only names
#list_of_participants

#entry variable of 3rd page
#enter_nameOftheParticipants

#list of intvar() for checkbox values
check_intvars = []

#list of checkboxes
check_boxes = []



#function checkbox maker
def checkbox_maker(root4,ii):
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


    for i in range(0,len(list_of_participants)):
        check_intvars.append(IntVar())

        check_boxes.append(Checkbutton(temp1, text= list_of_participants[i], variable= check_intvars[i], onvalue= item_prices[ii]))
        # I want to print the last checkbox that was made by this loop thats why -1
        check_boxes[-1].pack(side=LEFT)


#function def for 4thpage

def fourthpage(root3):
    global tuple_key_item, tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items, item_prices, check_boxes
    global list_Items_who_Entry, list_of_participants, enter_nameOftheParticipants, check_intvars

    temp1 = (enter_nameOftheParticipants.get()).replace(" ", "")
    list_of_participants = (temp1.split(","))
    print(list_of_participants)

    root3.destroy()
    root4 = Tk()

    '''row_temp=0
    for i in range(0,len(items)):
        temp_p4L1=Label(root4, text= "Item Name is {}".format(items[i]))
        temp_p4L1.grid(row = row_temp, column =0)

        temp_p4L2=Label(root4, text="Price of the item is {}".format(item_prices[i]) )
        temp_p4L2.grid(row=row_temp, column=1)



        checkbox_maker(root4,i,row_temp)
        row_temp += 2
    '''

    for i in range(0,len(items),1):
        #creating a labelFrame to insert Label of Item Price and
        temp1= LabelFrame(root4)
        temp1.pack()
        Label(temp1, text = "Item Name: {}".format(items[i])).pack(side=LEFT)
        Label(temp1, text= " Price:{}".format(item_prices[i])).pack(side=LEFT)

        checkbox_maker(root4,i)




    root4.mainloop()




#function def for 3rd page
def thirdpage(root2):
    global tuple_key_item,tuple_value_perPriceOfItems, HMI_var, HMIn_var
    global items,item_prices,enter_nameOftheParticipants
    global list_Items_who_Entry


    for i in range(0,HMI_var,1):
        ##print(len(list_Items_Entry))
        ##print(HMI_var)
        items.append(list_Items_Entry[i].get())
        ##print(int(list_Items_Price_Entry[i].get()))
        item_prices.append(int(list_Items_Price_Entry[i].get()))
    tuple_key_item=tuple(items)
    tuple_value_perPriceOfItems=tuple(item_prices)

    FoodKeys= dict(zip(tuple_key_item,tuple_value_perPriceOfItems))

    ##print(FoodKeys)  ##to see the dictionary values
    root2.destroy()
    root3=Tk()


    #now we have to enter the participants name
    label_enterNameOfParticipants=Label(root3, text = "Please enter the name of the participants, Comma seperated")
    label_enterNameOfParticipants.grid(row=0,column =0)
    enter_nameOftheParticipants = Entry(root3, width="100")
    enter_nameOftheParticipants.grid(row=1, column=0, rowspan=2)


    #define button for page 3
    button3 = Button(root3, text=" Next ", padx=100, command=lambda:fourthpage(root3))
    button3.grid(row=3, column=0, columnspan=10)

    root3.mainloop()



# function definition.... second page
def secondpage():
    global HMIn_var, HMI_var
    global list_Items_Entry,list_Items_Price_Entry
    HMI_var=int(HMI_entry.get())
    HMIn_var=int(HMIn_Entry.get())
    root.destroy()


    root2 = Tk()
    root2.title("Food Items and Values")


    for i in range(0,HMI_var,1):

        Label(root2, text= str(i+1)+ "th Item").grid(row=i, column=0,columnspan=1)
        list_Items_Entry.append(Entry(root2, width="10"))
        list_Items_Entry[i].grid(row=i,column=1,columnspan=2)
        Label(root2, text=str(i + 1) + "th Item Per Price").grid(row=i, column=3, columnspan=1)
        list_Items_Price_Entry.append(Entry(root2, width="10"))
        list_Items_Price_Entry[i].grid(row=i, column=4, columnspan=2)
    #this button will take u to 3rd window
    ##print(HMI_var)
    Button_2ndPage= Button(root2, text="Next", command=lambda:thirdpage(root2))
    Button_2ndPage.grid(row=HMI_var+1, column=0, columnspan= 6)
    root2.mainloop()

#Program starts here
root = Tk()
root.title("HisHisWhoseWhose")
root.config()
#How many Items
HMI = Label(root, text= "How many Items").grid(row=0,column=0, columnspan=2)
HMI_entry= Entry(root, width=  "5")
HMI_entry.grid(row=0,column=3, columnspan=1)
#How many individuals
HMIn = Label(root, text="How many Individuals").grid(row=1,column=0, columnspan=2)
HMIn_Entry = Entry(root, width="5")
HMIn_Entry.grid(row=1,column=3, columnspan=1)
#submit
submit1= Button(root, text= "Submit", command= secondpage).grid(row=2, column=2, columnspan=1)
























root.mainloop()
