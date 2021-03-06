from planet_scrape import planet_scrape
from star_scrape import star_scrape
from galaxy_scrape import galaxy_scrape
from satellite_scrape import satellite_scrape
from satellite_img_urls_scrape import satellite_image_scrape
import json

stars = star_scrape()
planets = planet_scrape(stars)
galaxies = galaxy_scrape()
satellites = satellite_scrape()
satellite_image_scrape(satellites)

#stars = json.load(open("data/stars.json"), strict=False)
#galaxies = json.load(open("data/galaxies.json"), strict=False)
#planets = json.load(open("data/planets.json"), strict=False)
#satellites = json.load(open("data/satellites.json"), strict=False)

# hardcode elements

earth = {"pid":planets[len(planets)-1]["pid"] + 1,
         "name":"Earth",
         "diameter":float(12742),
         "ra":0.0,
         "dec":0.0,
         "gravity":9.81,
         "orbital_period":float(365),
         "mass":float(5.972 * (10 ** 24)),
         "temperature":287,
         "img_url":"https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
         "star_pid":stars[len(stars)-1]["pid"] + 1,
         "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1}

sun = {"pid":stars[len(stars)-1]["pid"] + 1,
       "name":"Sun",
       "diameter":1.3914 * (10 **6),
       "ra":0.49288194,
       "dec":3.1928926,
       "temperature":5778,
       "mass":1.0,
       "img_url": "http://nineplanets.org/images/thesun.jpg",
       "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1}

milky_way = {"pid":galaxies[len(galaxies)-1]["pid"] + 1,
             "name": "Milky Way",
             "ra":17.7533,
             "dec":-47.2833,
             "morph_type":"Spiral",
             "redshift":0.0,
             "size":360.0,
             "img_url": "https://apod.nasa.gov/apod/image/0801/16500feetmilkywaykc2_brunier.jpg"}

planets.append(earth)
stars.append(sun)
galaxies.append(milky_way)

for p in planets :
    p["galaxy_pid"] = milky_way["pid"]

for s in stars :
    s["galaxy_pid"] = milky_way["pid"]

for s in satellites :
    s["planet_pid"] = earth["pid"]
    s["star_pid"] = sun["pid"]
    s["galaxy_pid"] = milky_way["pid"]

planet_file = open("data/planets.json", "w")
star_file = open("data/stars.json", "w")
galaxy_file = open("data/galaxies.json", "w")
satellite_file = open("data/satellites.json", "w")

json.dump(planets, planet_file, indent="\t")
json.dump(stars, star_file, indent="\t")
json.dump(galaxies, galaxy_file, indent="\t")
json.dump(satellites, satellite_file, indent="\t")

print("Num of Planets:", len(planets))
print("Num of Stars:", len(stars))
print("Num of Galaxies:", len(galaxies))
print("Num of Satellites:", len(satellites))
print("Done")
