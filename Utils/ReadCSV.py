import csv
from Utils.ReadConfig import ReadConfig

class ReadCSV:
    """Util class for reading data from a specified CSV file """

    def __init__(self) -> None:
        pass
    
    @staticmethod        
    def read_data_from_csv(filepath):
        """method returns rows from the csv file to feed in as pytest parameters"""
        with open(filepath ,"r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            data = [tuple(row) for row in reader]
        return data 
        