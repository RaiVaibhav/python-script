
# Insert a Tittle for the script//TODO 

Hello! Command-line lover, who wants to use the web browser to know how long it will take between two locations when you have this great command-line script to do that? Nobody, right? 
Congratulations, you will no longer need to leave your beloved terminal for this.

## What does the script do?
The script calculates the time it will take you to go from location A to location B. You can choose between bicycling, driving or walking.

## Installing the dependencies
### `googlemaps` package
This script require the `googlemaps` package. To install this package, do:
```zsh
$> pip3 install googlemaps
```
If you have any issues with permission, consider using `sudo`.
### Getting your GoogleMaps API key
Visit the [google maps direction API website](https://developers.google.com/maps/documentation/directions/) and click on **get a key** on the top right corner. Then follow the instructions and copy your key into the script here:
```python
# (API key) : Google maps API key
GOOGLE_MAP_API_KEY = 'myawsomeapikey'
```

## How to use it
First, clone this repository:
```zsh
$> git clone https://github.com/RaiVaibhav/python-script.git
$> cd python-script/
```
Then:
```zsh
$> python3 Get_travel_time_between_two_location.py
```
