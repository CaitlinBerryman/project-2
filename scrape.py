def scrape_info():
    from bs4 import BeautifulSoup
    import requests
    import json
    from pymongo import MongoClient
    from config import oauth

    client = MongoClient("mongodb://localhost:27017")
    db = client["spotify"]
    Collection = db["charts"]
    Collection.drop()

    countries = [
    ["AE","37i9dQZEVXbM4UZuIrvHvA","United Arab Emirates"],
    ["AR","37i9dQZEVXbMMy2roB9myp","Argentina"],
    ["AU","37i9dQZEVXbJPcfkRz0wJ0","Australia"],
    ["AT","37i9dQZEVXbKNHh6NIXu36","Austria"],
    ["BE","37i9dQZEVXbJNSeeHswcKB","Belgium"],
    ["BG","37i9dQZEVXbNfM2w2mq1B8","Bulgaria"],
    ["BO","37i9dQZEVXbJqfMFK4d691","Bolivia"],
    ["BR","37i9dQZEVXbMXbN3EUUhlg","Brazil"],
    ["CA","37i9dQZEVXbKj23U1GF4IR","Canada"],
    ["CH","37i9dQZEVXbJiyhoAPEfMK","Switzerland"],
    ["CL","37i9dQZEVXbL0GavIqMTeb","Chile"],
    ["CO","37i9dQZEVXbOa2lmxNORXQ","Colombia"],
    ["CR","37i9dQZEVXbMZAjGMynsQX","Costa Rica"],
    ["CZ","37i9dQZEVXbIP3c3fqVrJY","Czech Rep."],
    ["DE","37i9dQZEVXbJiZcmkrIHGU","Germany"],
    ["DK","37i9dQZEVXbL3J0k32lWnN","Denmark"],
    ["DO","37i9dQZEVXbKAbrMR8uuf7","Dominican Rep."],
    ["EC","37i9dQZEVXbJlM6nvL1nD1","Ecuador"],
    ["EG","37i9dQZEVXbLn7RQmT5Xv2","Egypt"],
    ["ES","37i9dQZEVXbNFJfN1Vw8d9","Spain"],
    ["EE","37i9dQZEVXbLesry2Qw2xS","Estonia"],
    ["FI","37i9dQZEVXbMxcczTSoGwZ","Finland"],
    ["FR","37i9dQZEVXbIPWwFssbupI","France"],
    ["GB","37i9dQZEVXbLnolsZ8PSNw","United Kingdom"],
    ["GR","37i9dQZEVXbJqdarpmTJDL","Greece"],
    ["GT","37i9dQZEVXbLy5tBFyQvd4","Guatemala"],
    ["HK","37i9dQZEVXbLwpL8TjsxOG","Hong Kong"],
    ["HN","37i9dQZEVXbJp9wcIM9Eo5","Honduras"],
    ["HU","37i9dQZEVXbNHwMxAkvmF8","Hungary"],
    ["ID","37i9dQZEVXbObFQZ3JLcXt","Indonesia"],
    ["IN","37i9dQZEVXbLZ52XmnySJg","India"],
    ["IE","37i9dQZEVXbKM896FDX8L1","Ireland"],
    ["IS","37i9dQZEVXbKMzVsSGQ49S","Iceland"],
    ["IL","37i9dQZEVXbJ6IpvItkve3","Israel"],
    ["IT","37i9dQZEVXbIQnj7RRhdSX","Italy"],
    ["JP","37i9dQZEVXbKXQ4mDTEBXq","Japan"],
    ["KR","37i9dQZEVXbNxXF4SkHj9F","Korea"],
    ["LT","37i9dQZEVXbMx56Rdq5lwc","Lithuania"],
    ["LU","37i9dQZEVXbKGcyg6TFGx6","Luxembourg"],
    ["LV","37i9dQZEVXbJWuzDrTxbKS","Latvia"],
    ["MA","37i9dQZEVXbJU9eQpX8gPT","Morocco"],
    ["MX","37i9dQZEVXbO3qyFxbkOE1","Mexico"],
    ["MY","37i9dQZEVXbJlfUljuZExa","Malaysia"],
    ["NI","37i9dQZEVXbISk8kxnzfCq","Nicaragua"],
    ["NL","37i9dQZEVXbKCF6dqVpDkS","Netherlands"],
    ["NO","37i9dQZEVXbJvfa0Yxg7E7","Norway"],
    ["NZ","37i9dQZEVXbM8SIrkERIYl","New Zealand"],
    ["PA","37i9dQZEVXbKypXHVwk1f0","Panama"],
    ["PE","37i9dQZEVXbJfdy5b0KP7W","Peru"],
    ["PH","37i9dQZEVXbNBz9cRCSFkY","Philippines"],
    ["PL","37i9dQZEVXbN6itCcaL3Tt","Poland"],
    ["PT","37i9dQZEVXbKyJS56d1pgi","Portugal"],
    ["PY","37i9dQZEVXbNOUPGj7tW6T","Paraguay"],
    ["RO","37i9dQZEVXbNZbJ6TZelCq","Romania"],
    ["RU","37i9dQZEVXbL8l7ra5vVdB","Russia"],
    ["SA","37i9dQZEVXbLrQBcXqUtaC","Saudi Arabia"],
    ["SG","37i9dQZEVXbK4gjvS1FjPY","Singapore"],
    ["SV","37i9dQZEVXbLxoIml4MYkT","El Salvador"],
    ["SK","37i9dQZEVXbKIVTPX9a2Sb","Slovakia"],
    ["SE","37i9dQZEVXbLoATJ81JYXz","Sweden"],
    ["TH","37i9dQZEVXbMnz8KIWsvf9","Thailand"],
    ["TR","37i9dQZEVXbIVYVBNw9D5K","Turkey"],
    ["TW","37i9dQZEVXbMnZEatlMSiu","Taiwan"],
    ["UA","37i9dQZEVXbKkidEfWYRuD","Ukraine"],
    ["UY","37i9dQZEVXbMJJi3wgRbAy","Uruguay"],
    ["US","37i9dQZEVXbLRQDuF5jeBp","United States"],
    ["VN","37i9dQZEVXbLdGSmz6xilI","Vietnam"],
    ["ZA","37i9dQZEVXbMH2jvi6jvjk","South Africa"]]

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {oauth}",
    }
    
    # website: https://developer.spotify.com/console/get-playlist/
    params = (
        ('fields', 'external_urls,tracks.items.track(artists.name,external_urls.spotify,name)'),
    )

    all_charts = []

    for country in countries:
        url = "https://api.spotify.com/v1/playlists/" + country[1]
        response = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        site_json = json.loads(soup.text)
        print("Success!")
        # Collection.insert_one(site_json)
        site_json["country_name"] = (country[2])
        all_charts.append(site_json)

    all_charts_dict = {"features": all_charts}
    
    with open("static/data/charts.json", "w") as file:
        json.dump(all_charts_dict, file)