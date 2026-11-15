import json  # noqa: I001

import functionz
import requests
from geopy.geocoders import Nominatim  


#functionz is a custom module that I made, you need to install it from here.
def main():
    loc = Nominatim(user_agent="GetLoc")
    global getLoc
    getLoc = loc.geocode({input('enter adress (Example: Antalya, Turkey) \n')})
    #Declaring parameters that measure the intensity on how much global warming affects given coordinates
    #Data Source: hard-coded
    #exrm paramters = Extreme heat
    climate_params = {
        '10_year_average' : 't_2m_10y_mean:C',
        'temp' : 't_2m:C',
        'exrm_hotDays' : 'hot_days:d',
        'exrm_summerDays' : 'summer_days:d',
        'exrm_heatIndex' : 'heat_index:C',
        'exrm_WBGT' : 't_wet_bulb_globe:C',
        #Wet-Bulb Globe Temperature (WBGT) is a measurement used to estimate how stressful hot weather is for the human body
        'demand_for_cooler' : 'cooling_degree_days:cdd',
    }
    with open('metomatic_output.json', 'w', encoding='utf-8') as file: 
        meteomatic_data = get_meteomatics_data(climate_params) 
        file.write(
            json.dumps(
                meteomatic_data,
                indent = 4
        ))


def get_meteomatics_data(params):
    #Data sources: parameters -> Function input, coordinates -> functionz custom module
    meteomatics_data = functionz.get_geotime_data('meteomatics', getLoc.longitude, getLoc.latitude)
    formatted_params = ','.join(list(params.values()))
    url = f"https://api.meteomatics.com/{meteomatics_data['time']}/{formatted_params}/{meteomatics_data['coordinates']}/json"
    response = requests.get(url, auth=(meteomatics_data['username'], meteomatics_data['passkey']))
    print("Status:", response.status_code)
    print("Response:", response.text[:3000])

    response.raise_for_status()
    data = response.json()
    print(data)
    return data
    #api.meteomatics.com/validdatetime/parameters/locations/format?optionals

main()