import folium
import numpy as np
import pandas as pd

save_map = True

# Create a map centered on Mexico
mexico_map = folium.Map(location=[23.6345, -102.5528], zoom_start=5)
mexico_map_new = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

# Add the states of Mexico with population information
states = {
    'Aguascalientes': {'coords': [21.8853, -102.2916], 'population': 1434635},
    'Baja California': {'coords': [30.8406, -115.2838], 'population': 3769020},
    'Baja California Sur': {'coords': [25.1614, -111.3705], 'population': 798447},
    'Campeche': {'coords': [19.8301, -90.5349], 'population': 928363},
    'Chiapas': {'coords': [16.7569, -93.1292], 'population': 5543828},
    'Chihuahua': {'coords': [28.6330, -106.0691], 'population': 3801487},
    'Coahuila': {'coords': [27.0587, -101.7068], 'population': 3218720},
    'Colima': {'coords': [19.2440, -103.7241], 'population': 731391},
    'Durango': {'coords': [24.8890, -104.8405], 'population': 1868996},
    'Guanajuato': {'coords': [21.1619, -101.6943], 'population': 6166934},
    'Guerrero': {'coords': [17.4392, -99.5451], 'population': 3544347},
    'Hidalgo': {'coords': [20.6595, -99.0806], 'population': 3080405},
    'Jalisco': {'coords': [20.6595, -103.3496], 'population': 8409693},
    'Mexico State': {'coords': [19.4969, -99.7233], 'population': 16992418},
    'Michoacán': {'coords': [19.5665, -101.7068], 'population': 4825401},
    'Morelos': {'coords': [18.6813, -99.1013], 'population': 2044058},
    'Nayarit': {'coords': [21.7514, -104.8455], 'population': 1288571},
    'Nuevo León': {'coords': [25.5922, -99.9962], 'population': 5784442},
    'Oaxaca': {'coords': [17.0732, -96.7266], 'population': 4143593},
    'Puebla': {'coords': [19.0414, -98.2063], 'population': 6604451},
    'Querétaro': {'coords': [20.5888, -100.3899], 'population': 2279637},
    'Quintana Roo': {'coords': [19.1817, -88.4798], 'population': 1857985},
    'San Luis Potosí': {'coords': [22.1565, -100.9855], 'population': 2832817},
    'Sinaloa': {'coords': [25.1721, -107.4795], 'population': 3156674},
    'Sonora': {'coords': [29.0892, -110.9617], 'population': 3150410},
    'Tabasco': {'coords': [17.8409, -92.6189], 'population': 2395272},
    'Tamaulipas': {'coords': [24.2669, -98.8363], 'population': 3650602},
    'Tlaxcala': {'coords': [19.4326, -98.2431], 'population': 1345842},
    'Veracruz': {'coords': [19.1738, -96.1342], 'population': 8112505},
    'Yucatán': {'coords': [20.7099, -89.0943], 'population': 2320898},
    'Zacatecas': {'coords': [22.7709, -102.5832], 'population': 1656608},
    'Mexico City': {'coords': [19.4326, -99.1332], 'population': 9187520}
}



#load data on internet and twitter users and update states dict
df = pd.read_csv('geodata1.csv')
for i,row in df.iterrows():
    states[row['Name']]['internet']=row['Internet Users']
    states[row['Name']]['twitter']=row['Twitter']
    states[row['Name']]['pop']=row['Population']




# Compute totals for each state
popTotal=0
internetTotal=0
twitterTotal=0

for state,info in states.items():
    p,i,t = info['population'],info['internet'],info['twitter']
    popTotal+=p
    internetTotal+=i
    twitterTotal+=t

# Add markers for each state with population information
for state, info in states.items():
    population,internet,twitter = info['population'],info['internet'],info['twitter']
    pop_percent = format(100*population/popTotal,".1f")
    internet_percent = format(100*internet/internetTotal,".1f")
    twitter_percent = format(100*twitter/twitterTotal,".1f")
    coords = info['coords']
    iFrame = f"{state}<br>Population: {population} ({pop_percent}%)<br>Internet users: {internet_percent}%<br>Twitter users: {twitter_percent}%"
    popup1 = folium.Popup(iFrame,
                    min_width=150,
                    max_width=150)
    folium.Marker(location=coords, popup=popup1).add_to(mexico_map)

# Display the map
mexico_map

if save_map:
    # Display the map
    mexico_map.save("mexico_map.html")


# --- Recreate map with Greater Mexico City --- #
states2 = states.copy()
GMC = ['Mexico City','Hidalgo','Mexico State']
#Add greater Mexico City to states dict
states2['Greater Mexico City'] = states['Mexico City'].copy()
vdict = states2['Greater Mexico City']
for s in ['Hidalgo','Mexico State']:
    vdict['population']+=states[s]['population']    
    vdict['internet']+=states[s]['internet']
    vdict['twitter']+=states[s]['twitter']
    vdict['pop']+=states[s]['pop']

del states2['Mexico City']
del states2['Mexico State']
del states2['Hidalgo']

for state, info in states2.items():
    population,internet,twitter = info['population'],info['internet'],info['twitter']
    pop_percent = format(100*population/popTotal,".1f")
    internet_percent = format(100*internet/internetTotal,".1f")
    twitter_percent = format(100*twitter/twitterTotal,".1f")
    coords = info['coords']
    iFrame = f"{state}<br>Population: {population} ({pop_percent}%)<br>Internet users: {internet_percent}%<br>Twitter users: {twitter_percent}%"
    popup1 = folium.Popup(iFrame,
                    min_width=150,
                    max_width=150)
    folium.Marker(location=coords, popup=popup1).add_to(mexico_map_new)

# Display the map
mexico_map_new

if save_map:
    # Display the map
    mexico_map_new.save("mexico_map_new.html")