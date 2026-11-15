import datetime

import api_secrets


def pretty_output(input, type):
    pass #TODO: Implement a function to convert JSON files into graphs according to the "type" variable that the function gets
def ai_summary(unsummary, prompt="summarize this text/graph/json please", model="gemini-3.5-flash-lite"):
    pass #TODO: Implement a function to prompt the model according to the model variable to summarize the unsummary variable and return the summarized version.

def get_geotime_data(compatibility, longitude = False, latitude = False, time=False):
    #getting latitude and longtitude,
    #Data source: User input/Function input
    if latitude == False or longitude == False:
        latitude, longitude = '26.7652312' '81.1196719' #Defaults to Gosainganj Lucknow
    match compatibility:
        case 'meteomatics' : #Our meteomatics data pool is going to be deprecated after 22/11/2026 but may get support again in the near future!
            coordinates = str(f"{latitude},{longitude}")
            #getting time in meteomatics format
            #Data source: Function input / datetime.datetime.now
            if time == False:
                time = str(f'{str(datetime.datetime.now()).split(" ")[0]}T00:00:00Z')
            return {
                'coordinates' : coordinates,
                'time' : time,
                'passkey' : api_secrets.get_meteo()[0],
                'username' : api_secrets.get_meteo()[1],
            }
        case 'nasa_power' :
            pass
        case 'copernicus' :
            pass #This feature is coming soon, after hackathon finishes 
    
    