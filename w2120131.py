#Author:K.P.M.D.N.Buddhima Jothiwansa
#Date:2024.12.09
#Student ID:20240815

#importing CSV module
import csv
from datetime import datetime 

#initializing date variables
date=0
month=0
year=0

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    while True:
        try:
            date=int(input("Please enter the day of the survey in the format dd - "))
            if 1<=date<=31: 
                date=f"{date:02d}" #format the date in two digits
                break
            else:
                print("Out of range - values must be in the range 1 and 31. ")
        except ValueError:
            print("Integer required. ")
    
    while True:
        try:
            month=int(input("Please enter the month of the survey in the format MM - "))
            if 1<=month<=12:
                month=f"{month:02d}" #format the month in two digits
                break
            else:
                print("Out of range - values must be in the range 1 to 12.")
        except ValueError:
            print("Integer required. ")
            
    while True:
        try:
            year=int(input("Please enter the year of the survey in the format YYYY: "))
            if 2000<=year<=2024:
                break
            else:
                print("Out of range - values must range from 2000 and 2024. ")
        except ValueError:
            print("Integer required. ")
            
            
    return date, month, year #return the values
    

def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
    continue_input=input("Do you want to load another dataset ? (Y/N) - ").strip().upper() #strip - remove spaces 
    while True:
        if continue_input == 'Y' or 'N':
            return continue_input.upper()
        else:
            continue_input=input("Invalid input.Please enter Y/N - ")


# Task B: Processed Outcomes

def define_file_path(date):
    
    
    return filename #generate the filepath according to the given date


def process_csv_data(file_path):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    
    total_no_of_vehicles=0
    total_no_of_trucks=0
    total_no_of_electric_vehicles=0
    total_no_of_twowheeled_vehicles=0
    total_no_of_buses_ElmToNorth=0
    total_no_of_vehicles_without_turning=0
    total_no_of_bicycles=0
    total_no_of_vehicles_over_speed=0
    total_no_of_vehicles_through_only_Elm=0
    total_no_of_vehicles_through_only_Hanley=0
    total_no_of_scooters_through_Elm=0
    total_no_of_vehicles_in_peak_hours_Hanley=0
        
    peak_hours=[]
    peak_hour_on_hanley=[0]*24
    peak_hour_on_elm=[0]*24
    hour=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    rain_hours=[0]*24
    
    
    try:
        
        with open(file_path, mode='r') as csv_file: #open file path and read
            csv_reader=csv.DictReader(csv_file) #read the csv file as a dictionary
            
            for row in csv_reader:
                
                total_no_of_vehicles+=1 #adding one by one for each row
                
                #assign variables to each column in csv file
                junction=row.get('JunctionName')
                time_period=row.get('timeOfDay')
                travel_direction_in=row.get('travel_Direction_in')
                travel_direction_out=row.get('travel_Direction_out')
                weather_status=row.get('Weather_Conditions')
                speed_limit=row.get('JunctionSpeedLimit')
                vehicle_speed=row.get('VehicleSpeed')
                vehicle_type=row.get('VehicleType')
                electric_hybrid=row.get('elctricHybrid')
                
                
                #increment one by one based on condition 
                if vehicle_type=='Truck':
                    total_no_of_trucks+=1
                
                    
                if electric_hybrid=='True':
                    total_no_of_electric_vehicles+=1
                    
                if vehicle_type=='Buss': 
                    if travel_direction_out == 'N':
                        if junction == "Elm Avenue/Rabbit Road":
                            total_no_of_buses_ElmToNorth+=1
                        
                if travel_direction_in == travel_direction_out:
                    total_no_of_vehicles_without_turning+=1
                    
                if vehicle_speed > speed_limit:
                    total_no_of_vehicles_over_speed+=1
                    
                if 'Elm Avenue/Rabbit Road' in junction:
                    total_no_of_vehicles_through_only_Elm+=1
                    
                if 'Hanley Highway/Westway' in junction:
                    total_no_of_vehicles_through_only_Hanley+=1        
                    
                if 'Motorcycle' in vehicle_type:
                    total_no_of_twowheeled_vehicles+=1
                    
                if 'Bicycle' in vehicle_type:
                    total_no_of_twowheeled_vehicles+=1
                    total_no_of_bicycles+=1

                if 'Scooter' in vehicle_type:
                    total_no_of_twowheeled_vehicles+=1
                    
                hour=time_period.split(":")
                hour=int(hour[0])
                
                if 'Elm Avenue/Rabbit Road' in junction:
                    peak_hour_on_elm[hour]+=1
                if 'Hanley Highway/Westway' in junction:
                    peak_hour_on_hanley[hour]+=1
                    
                if weather_status in['Heavy Rain' ,'Light Rain' ]:
                    rain_hours[hour]+=1

                if vehicle_type=="Scooter":
                    if junction=="Elm Avenue/Rabbit Road":
                        total_no_of_scooters_through_Elm+=1
                
            #calculations       
            percentage_of_trucks=(total_no_of_trucks*100) // total_no_of_vehicles #performing floor division
            average_of_bikes=total_no_of_bicycles // 24 #performing floor division
            percentage_of_scooters_through_Elm=round((total_no_of_scooters_through_Elm / total_no_of_vehicles_through_only_Elm)*100) 
            peak_hour=peak_hour_on_hanley.index(max(peak_hour_on_hanley)) #get the maximum value
            peak_hour=f"{peak_hour:02d}:00 : {peak_hour+1:02d}:00"
            
            total_no_of_rain_hours=len(rain_hours)-rain_hours.count(0)

            peak_hour_traffic_count=max(peak_hour_on_hanley)
            peak_hours=[]
            
            for hour in range(24):
                if peak_hour_on_hanley[hour] == peak_hour_traffic_count:
                    peak_hours.append("{hour:02d}:00 and {hour+1:02d}:00")
                    
            #printing results in terminal
            outcomes=[
                file_path,
                total_no_of_vehicles,
                total_no_of_trucks,
                total_no_of_electric_vehicles,
                total_no_of_twowheeled_vehicles,
                total_no_of_buses_ElmToNorth,
                total_no_of_vehicles_without_turning,
                percentage_of_trucks,
                average_of_bikes,
                total_no_of_vehicles_over_speed,
                total_no_of_vehicles_through_only_Elm,
                total_no_of_vehicles_through_only_Hanley,
                percentage_of_scooters_through_Elm,
                peak_hour_traffic_count,
                total_no_of_rain_hours,
                peak_hour
            ]
            return outcomes,peak_hour_on_hanley,peak_hour_on_elm
                
    except FileNotFoundError:
        print("File not found. ")
        return True,None,None
   

def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    
    print(f'''
    data file selected is {outcomes[0]}        
    The total number of vehicles recorded for this data is {outcomes[1]}
    The total number of trucks recorded for this data is {outcomes[2]}
    The total number of electric vehicles recorded for this data is {outcomes[3]}
    The total number of two-wheeled vehicles recorded for this data is {outcomes[4]}
    The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes[5]}
    The total number of vehicles through both junctions not turning left or right is {outcomes[6]}
    The percentage of total vehicles recorded that are trucks for this date is {outcomes[7]}%
    The average number of Bikes per hour for this date is {outcomes[8]}
    The total number of vehicles recorded as over the speed limit for this data is {outcomes[9]}
    The total number of vehicles recorded through Elm Avenue/Rabbit road junction is {outcomes[10]}
    The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes[11]}
    {outcomes[12]}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.
    The highest number ofvehicles in an hour on Hanley Highway/Westway is {outcomes[13]}
    The most vehicles through Hanley Highway/Westway were recorded between {outcomes[15]}
    The number of hours of rain for this date is {outcomes[14]}
                
        ''')



# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    with open(file_name, 'a') as file:
        file.write(f'''
    data file selected is {outcomes[0]}        
    The total number of vehicles recorded for this data is {outcomes[1]}
    The total number of trucks recorded for this data is {outcomes[2]}
    The total number of electric vehicles recorded for this data is {outcomes[3]}
    The total number of two-wheeled vehicles recorded for this data is {outcomes[4]}
    The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes[5]}
    The total number of vehicles through both junctions not turning left or right is {outcomes[6]}
    The percentage of total vehicles recorded that are trucks for this date is {outcomes[7]}%
    The average number of Bikes per hour for this date is {outcomes[8]}
    The total number of vehicles recorded as over the speed limit for this data is {outcomes[9]}
    The total number of vehicles recorded through Elm Avenue/Rabbit road junction is {outcomes[10]}
    The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes[11]}
    {outcomes[12]}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.
    The most vehicles through Hanley Highway/Westway were recorded between {outcomes[13]}
    The number of hours of rain for this date is {outcomes[14]}
                        
    ''')


# Task D: Histogram Display
import tkinter as tk

class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date  # date for histogram
        self.root = tk.Tk()  # to create the main window
        self.canvas = None  # Will hold the canvas for drawing
        self.width = 1400 #width of canvas
        self.height = 620 #height of canvas
        self.margin = 50 #margin for labels
        self.bar_width = 15 #width of each bar in histogram
        self.spacing = 20 #space between bars
        self.bar_gap = 2  #gap between two bars
        self.elm_data = self.traffic_data[0] #traffic data for elm avenue
        self.hanley_data = self.traffic_data[1] #traffic data for hanley avenue

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.root.title(f"Histogram for {self.date}") #set the title of window
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack() #add the canvas to the window

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        max_value = max(max(self.elm_data), max(self.hanley_data))
        self.scale = (self.height - 2 * self.margin) / max_value

        # Draw x-axis
        self.canvas.create_line( self.margin, self.height - self.margin, self.width - self.margin, self.height - self.margin, width=2,)

        for i in range(24):  # 24 hours
            # Calculate positions for each bar
            x0 = self.margin + i * (self.bar_width * 2 + self.spacing + self.bar_gap)
            x1 = x0 + self.bar_width
            y0_elm = self.height - self.margin - self.elm_data[i] * self.scale
            y0_hanley = self.height - self.margin - self.hanley_data[i] * self.scale

            # Elm Highway bar
            self.canvas.create_rectangle(x0, y0_elm, x1, self.height - self.margin, fill="lightgreen")
            self.canvas.create_text( x0 + self.bar_width // 2, y0_elm - 10, text=str(self.elm_data[i]), fill="green", font=("Arial", 10))

            # Hanley Highway bar
            x0_hanley = x1 + self.bar_gap
            x1_hanley = x0_hanley + self.bar_width
            self.canvas.create_rectangle(x0_hanley, y0_hanley, x1_hanley, self.height - self.margin, fill="lightpink")
            self.canvas.create_text( x0_hanley + self.bar_width // 2, y0_hanley - 10, text=str(self.hanley_data[i]), fill="red", font=("Arial", 10) )

            # Hour labels
            hour_label = f"{i:02d}"
            label_x = x0 + self.bar_width + self.bar_gap // 2
            self.canvas.create_text(label_x, self.height - self.margin + 20, text=hour_label, font=("Arial", 10))

        # Add title and x-axis label
        self.canvas.create_text(self.margin, self.margin // 2, text=f"Histogram of Vehicle Frequency per Hour {self.date}", font=("Arial", 16),anchor="w" )

        self.canvas.create_text(540, 615, text="Hours (00:00 to 24:00)", font=("Arial", 14, "bold"))
       

    def add_legend(self):
        """
        Adds a legend to the histogram.
        """
        self.canvas.create_rectangle(50, 50, 70, 70, fill="lightgreen") #legend for elm avenue
        self.canvas.create_text(80, 60, text="Elm Avenue/Rabbit Road", anchor="w")
        self.canvas.create_rectangle(50, 80, 70, 100, fill="lightcoral") #legend for hanley avenue
        self.canvas.create_text(80, 90, text="Hanley Highway/Westway", anchor="w")

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_window() #set up the main window and canvas
        self.add_legend() #add the legend
        self.draw_histogram() #draw the histogram
        self.root.mainloop()


class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None #holding current data

    def load_csv_file(self, file_path):
        """
        Loads a CSV file and processes its data.
        """
        outcomes, peak_hour_on_hanley, peak_hour_on_elm = process_csv_data(file_path) #loading data from csv files
        self.outcomes = outcomes #file processing outcomes
        self.traffic_data = [peak_hour_on_hanley, peak_hour_on_elm] 

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        date, month, year = validate_date_input()
        date = int(date)
        month = int(month)
        self.file_path = f"traffic_data{date:02d}{month:02d}{year}.csv"
        self.file_date = f"{date}/{month}/{year}"

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            try:
                self.handle_user_interaction() #handle user input
                self.load_csv_file(self.file_path) #load and process csv files
                if self.outcomes == "True":
                    raise FileNotFoundError("")
                display_outcomes(self.outcomes)
                save_results_to_file(self.outcomes)
                graph = HistogramApp(self.traffic_data, self.file_date) #creating histogram
                graph.run() #display histogram
                continue_input = validate_continue_input()
                if continue_input == "Y":
                    continue
                else:
                    print("End of run")
                    break
            except FileNotFoundError:
                print("File not found. Please try again.")
                continue_input = validate_continue_input()
                if continue_input == "Y":
                    continue
                else:
                    print("End of run")
                    break


if __name__ == "__main__":
    traffic_program = MultiCSVProcessor() #initialize the csv processor
    traffic_program.process_files() #start processing files

