from pathlib import Path

import openeo

#Testing an API call to Copernicus Data Collection
#for an image of Antalya.. 
# Hey thats my house right there!
# Connect and log in using your Copernicus account.
connection = openeo.connect(
    "https://opene.o.dataspace.copernicus.eu"
)
connection.authenticate_oidc()

# Requesting Sentinel-2 red, green, and blue measurements.
data = connection.load_collection(
    "SENTINEL2_L2A",
    spatial_extent={
        "west": 30.700,
        "south": 36.880,
        "east": 30.710,
        "north": 36.890,
    },
    temporal_extent=["2025-09-01", "2025-09-15"],
    bands=["B04", "B03", "B02"],
)

# Combine the observations into one image using the median.
image = data.reduce_dimension(dimension="t", reducer="median")

# Process on Copernicus servers and download the result.
output = Path("outputs/antalya.tif")
output.parent.mkdir(exist_ok=True)

image.download(str(output), format="GTiff")
print(f"Downloaded to: {output.resolve()}")