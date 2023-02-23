#student name: Leon Guo
#student number: 98879711

""" Covid Simple Dashboard App

    If VScode/IDE's built in 'run' button doesn't work due to 
    "Can't connect to HTTPS URL because the SSL module is not available" error, 
    open Anaconda Promt (anaconda3) and type the following commands:
    -> conda activate lab2
    -> python Lab2.py

    *Adapted from Edward Han's discussion post*
"""
#imports
from covid import Covid

from tkinter import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CovidDataGUI:
    def __init__(self, master):
        self.master = master
        master.title("Covid Data Visualization")
        master.geometry("800x500")

        # getting data to be used by methods
        self.masterData = getMasterCovidData()
        self.confirmed = getConfirmed(self.masterData)
        self.active = getActive(self.masterData)
        self.deaths = getDeaths(self.masterData)
        self.recovered = getRecovered(self.masterData)

        # creating frames
        self.frame_buttons = Frame(master)
        self.frame_buttons.grid(row = 0, column = 0)
        self.frame_menu = Frame(master)
        self.frame_graph = Frame(master)
        self.frame_graph.place(x = 150, y = 50)

        # creating buttons (mainly for commands in task1)
        self.menu_button = Button(self.frame_buttons,  
                                    command = lambda: switch(self.frame_buttons, self.frame_menu),
                                    height = 2,
                                    width = 20,
                                    text="SELECT COUNTRY")
        self.menu_button.grid(row = 0, column = 0)

        self.plot_button_c = Button(self.frame_buttons, 
                                    command = lambda: plot(self.frame_graph, self.confirmed, "Confirmed Cases"), 
                                    height = 2, 
                                    width = 20, 
                                    text="Plot: Top 10 Confirmed")  
        self.plot_button_c.grid(row = 1, column = 0)
        
        self.plot_button_a = Button(self.frame_buttons, 
                                    command = lambda: plot(self.frame_graph, self.active, "Active Cases"), 
                                    height = 2, 
                                    width = 20, 
                                    text="Plot: Top 10 Active")
        self.plot_button_a.grid(row = 2, column = 0)

        self.plot_button_d = Button(self.frame_buttons, 
                                    command = lambda: plot(self.frame_graph, self.deaths, "Deaths"), 
                                    height = 2, 
                                    width = 20, 
                                    text="Plot: Top 10 Deaths")
        self.plot_button_d.grid(row = 3, column = 0)

        self.plot_button_r = Button(self.frame_buttons, 
                                    command = lambda: plot(self.frame_graph, self.recovered, "Recoveries"), 
                                    height = 2, 
                                    width = 20, 
                                    text="Plot: Top 10 Recovered")
        self.plot_button_r.grid(row = 4, column = 0)

        self.clear_button = Button(self.frame_buttons,  
                                    command = lambda: clear(),
                                    height = 2,
                                    width = 20,
                                    text="CLEAR")
        self.clear_button.grid(row = 5, column = 0)

        self.close_button = Button(self.frame_buttons, 
                                    command = master.quit, 
                                    height = 2,
                                    width = 20,
                                    text = "CLOSE")
        self.close_button.grid(row = 6, column = 0)
        
        # these buttons for task 2 are hidden upon boot up, but appear after the user has clicked menu_button
        self.plot_USA = Button(self.frame_menu,  
                                    command = lambda: getCountryData("USA", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: USA")
        self.plot_USA.grid(row = 9, column = 0)

        self.plot_Canada = Button(self.frame_menu,  
                                    command = lambda: getCountryData("Canada", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: Canada")
        self.plot_Canada.grid(row = 1, column = 0)

        self.plot_Australia= Button(self.frame_menu,  
                                    command = lambda: getCountryData("Australia", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: Australia")
        self.plot_Australia.grid(row = 0, column = 0)

        self.plot_Japan = Button(self.frame_menu,  
                                    command = lambda: getCountryData("Japan", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: Japan")
        self.plot_Japan.grid(row = 5, column = 0)

        self.plot_China = Button(self.frame_menu,  
                                    command = lambda: getCountryData("China", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: China")
        self.plot_China.grid(row = 2, column = 0)

        self.plot_UK = Button(self.frame_menu,  
                                    command = lambda: getCountryData("UK", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: United Kingdom")
        self.plot_UK.grid(row = 8, column = 0)

        self.plot_Mexico = Button(self.frame_menu,  
                                    command = lambda: getCountryData("Mexico", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: Mexico")
        self.plot_Mexico.grid(row = 6, column = 0)

        self.plot_Spain = Button(self.frame_menu,  
                                    command = lambda: getCountryData("Spain", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: Spain")
        self.plot_Spain.grid(row = 7, column = 0)

        self.plot_Italy = Button(self.frame_menu,  
                                    command = lambda: getCountryData("Italy", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: Italy")
        self.plot_Italy.grid(row = 4, column = 0)

        self.plot_India = Button(self.frame_menu,  
                                    command = lambda: getCountryData("India", self.frame_graph),
                                    height = 2,
                                    width = 20,
                                    text="Plot: India")
        self.plot_India.grid(row = 3, column = 0)

        self.clear_button = Button(self.frame_menu,  
                                    command = lambda: clear(),
                                    height = 2,
                                    width = 20,
                                    text="CLEAR")
        self.clear_button.grid(row = 10, column = 0)
        
        self.return_button = Button(self.frame_menu,  
                                    command = lambda: switch(self.frame_menu, self.frame_buttons),
                                    height = 2,
                                    width = 20,
                                    text="RETURN")
        self.return_button.grid(row = 11, column = 0)

        # This method removes widget1 from the window and replaces it with widget2
        def switch(widget1, widget2):
            widget1.grid_forget()
            widget2.grid(row = 0, column = 0)        

def getMasterCovidData() -> list:
    """ this function is called once to get the master data for 
        this application; 
        all data used in this application is derived from data 
        returned by this function
    """
    covid = Covid(source="worldometers") #instantiate
    data = covid.get_data()
    return data

def getCountryData(countryName: str, window):
    """ this function retrieves the number of comfirmed cases,
        active cases, deaths and recoveries for a country 
        specified by the user. The data is presented on a 
        bar graph
    """
    covid = Covid(source="worldometers") #instantiate
    data = covid.get_status_by_country_name(countryName)

    global plotted, canvas
    if plotted:
        return
    fig = Figure(figsize = (7, 4))
    plot1= fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = window) 
    
    # create the bar graph
    x = ['confirmed', 'active', 'deaths', 'recovered']
    y = [data['confirmed'], data['active'], data['deaths'], data['recovered']]
    plot1.bar(x, y)
    
    # set the title
    baseString = "COVID-19 Data for "
    title = baseString + countryName
    plot1.set_title(title)

    for tick in plot1.get_xticklabels(): #rotate the text slightly
        tick.set_rotation(15) 
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0)
    plotted = True

def getConfirmed(data1: list) -> list:
    """ this function uses the masterdata data1 and returns a 
        list of (country, confirmed) data
    """
    confirmed = []
    for i in data1:
        confirmed.append((i["country"], i["confirmed"]))
    #print("DEBUG: confirmed is ", confirmed)
    return confirmed

def getActive(data1: list) -> list:
    """ this function uses the masterdata data1 and returns a 
        list of (country, active) data
    """
    active = []
    for i in data1:
        active.append((i["country"], i["active"]))
    #print("DEBUG: active is ", active)
    return active

def getDeaths(data1: list) -> list:
    """ this function uses the masterdata data1 and returns a 
        list of (country, deaths) data
    """
    deaths = []
    for i in data1:
        deaths.append((i["country"], i["deaths"]))
    #print("DEBUG: deaths are ", deaths)
    return deaths

def getRecovered(data1: list) -> list:
    """ this function uses the masterdata data1 and returns a 
        list of (country, recovered) data
    """
    recovered = []
    for i in data1:
        recovered.append((i["country"], i["recovered"]))
    #print("DEBUG: recovered is ", recovered)
    return recovered

def plot(window, data: list, graphTitle: str):
    """ a callback function for the button;
        plots a histogram of the top 10 specified cases 
    """
    global plotted, canvas
    if plotted:
        return
    fig = Figure(figsize = (7, 4))
    plot1= fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = window) 

    # select only top 10 countries
    top10 = [data[i] for i in range(18)]
    
    # create the bar graph
    x = [top10[i][0] for i in range(8, 18)] # top 10 countries start at index 8 and end at index 17
    y = [top10[i][1] for i in range(8, 18)]
    plot1.bar(x, y)

    plot1.set_title(graphTitle)

    for tick in plot1.get_xticklabels(): #rotate the text slightly
        tick.set_rotation(15) 
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0)
    plotted = True

def clear():
    """ a callback for the Clear button """ 
    global plotted, canvas
    if plotted:
        canvas.get_tk_widget().destroy()
        plotted = False

root = Tk()
plotted = False
c = CovidDataGUI(root)
root.mainloop()

