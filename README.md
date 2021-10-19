# Project 2 - What's the World Listening to today?

An interactive map showcasing the Top 10 tracks by region, sourced from Spotify.

Files missing from repo: config.py in the root folder containing the Spotify authorisation key, and config.js in static/js containing the MapBox API key.

## The Process

Using the Spotify Developer Console (https://developer.spotify.com/), I could use my regular Spotify account to acquire data at certain levels of access. The tool can access personal playlists and other information with permission; the playlists I require are all public, so no special permissions are needed. The "key" I'm given is only temporary, with options to refresh (not set up in this instance).

Of the multiples tools available to me, I use the one to gather data from playlists (https://developer.spotify.com/console/get-playlist/). This requires knowing the unique ID of each playlist, which is included in its link. Once the ID, selective parameters, and OAuth token are provided, a link is returned in cURL format - along with the data itself being returned in the console. This forms the basis of the scrape.py file, which loops through scraping playlist data from the Daily Top 50 charts for all available countries. It then sends all the data to a json file to be accessed through JavaScript. This script is activated from the command line.

The Charts json is complemented by a geojson file containing geographical parameters for all countries with a chart on Spotify. They are indexed identically for easy reference.

Newer versions of d3 allow for multiple files to be called at once, using the Promise.all function. This is employed to combine each country's geography with a popup listing its current top 10 hits, with links to each single and the playlist as a whole.

## Issues / Further Development

Initially, the plan was to use Spotify's own Charts website, which lists the top 200 songs daily/weekly by region - with historical data. Unfortunately, Spotify blocked this website from being scraped around 6 months ago.

The script can easily be modified to send data to mongoDB, but no amount of frustration with Node.js got me anywhere, and the json method was substituted instead.

Currently I'm manually refreshing the OAuth token, but I want to have it constant for the purpose of widespread deployment.