from tkinter import * # imports all tkinter commands


root = Tk() # create canvas
root.geometry('500x300') # canvas dimensions
root.title("Website Blocker") # title of window


Label(root, text='Website Blocker', font='arial 20 bold').pack() # title of program


host_path = r'C:\Windows\System32\drivers\etc\hosts' # open host file
ip_address = '127.0.0.1' # host ip address
Label(root, text='Enter Website :' , font ='arial 13 bold').place(x=5 ,y=60) # instruction for user
Websites = Text(root,font = 'arial 10',height='2', width= 40, wrap = WORD, padx=5, pady=5) # entry
Websites.place(x= 140,y = 60) # entry coordinate


def blocker(): # make function
    website_lists = Websites.get(1.0,END) # make list with every entered website
    Website = list(website_lists.split(",")) # add commas to list
    with open (host_path , 'r+') as host_file: # open host file
        file_content = host_file.read() # define file_content list
        for website in Website: # entered content in entry
            if website in file_content: # website is already blocked
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200) # tell user website already blocked
                pass # user can enter a website again
            else: # entered content NOT in entry
                host_file.write(ip_address + " " + website + '\n') # add to file
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200) # tell user website blocked


block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command=blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue') # run function
block.place(x = 230, y = 150) # button coordinates
root.mainloop() # shows window / canvas
