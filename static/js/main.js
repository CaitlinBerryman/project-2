// Creating map object
var myMap = L.map("map", {
    center: [40, 0],
    zoom: 3
});
  
  // Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/dark-v10",
    accessToken: API_KEY
}).addTo(myMap);

// json file paths
var countryLink = "static/data/countries.geojson";
var chartsLink = "static/data/charts.json";

// Promise is a new(ish) function that allows for multiple files to be json'd
Promise.all([
    d3.json(countryLink),
    d3.json(chartsLink)
]).then(function(data) {
    L.geoJson(data[0], {
        style: function(feature) {
            return {
                color:"#1ED65F",
                fillColor: "white",
                fillOpacity: 0.1,
                weight: 0.8
            };
        },
        onEachFeature: function(feature, layer) {
            layer.on({
                mouseover: function(event) {
                    layer = event.target;
                    layer.setStyle({
                        fillOpacity: 0.5
                    });
                },
                mouseout: function(event) {
                    layer = event.target;
                    layer.setStyle({
                        fillOpacity: 0.1
                    });
                }
            });
            var countryIndex = data[0].features.indexOf(feature);
            var chartPath = data[1].features[countryIndex].tracks.items;
            layer.bindPopup(
                "<h1>" + data[1].features[countryIndex].country_name + "</h1><hr>" +
                "<h3><strong>1. <a href='" + chartPath[0].track.external_urls.spotify + "'>" + chartPath[0].track.name + "</a></strong> by " + chartPath[0].track.artists[0].name + "</h3>" +
                "<h3><strong>2. <a href='" + chartPath[1].track.external_urls.spotify + "'>" + chartPath[1].track.name + "</a></strong> by " + chartPath[1].track.artists[0].name + "</h3>" +
                "<h3><strong>3. <a href='" + chartPath[2].track.external_urls.spotify + "'>" + chartPath[2].track.name + "</a></strong> by " + chartPath[2].track.artists[0].name + "</h3>" +
                "<h3><strong>4. <a href='" + chartPath[3].track.external_urls.spotify + "'>" + chartPath[3].track.name + "</a></strong> by " + chartPath[3].track.artists[0].name + "</h3>" +
                "<h3><strong>5. <a href='" + chartPath[4].track.external_urls.spotify + "'>" + chartPath[4].track.name + "</a></strong> by " + chartPath[4].track.artists[0].name + "</h3>" +
                "<h3><strong>6. <a href='" + chartPath[5].track.external_urls.spotify + "'>" + chartPath[5].track.name + "</a></strong> by " + chartPath[5].track.artists[0].name + "</h3>" +
                "<h3><strong>7. <a href='" + chartPath[6].track.external_urls.spotify + "'>" + chartPath[6].track.name + "</a></strong> by " + chartPath[6].track.artists[0].name + "</h3>" +
                "<h3><strong>8. <a href='" + chartPath[7].track.external_urls.spotify + "'>" + chartPath[7].track.name + "</a></strong> by " + chartPath[7].track.artists[0].name + "</h3>" +
                "<h3><strong>9. <a href='" + chartPath[8].track.external_urls.spotify + "'>" + chartPath[8].track.name + "</a></strong> by " + chartPath[8].track.artists[0].name + "</h3>" +
                "<h3><strong>10. <a href='" + chartPath[9].track.external_urls.spotify + "'>" + chartPath[9].track.name + "</a></strong> by " + chartPath[9].track.artists[0].name + "</h3><hr>" +
                "<h2><strong><a href='" + data[1].features[countryIndex].external_urls.spotify + "'>See Full Playlist</a></strong></h2>"
                );
        }
    }).addTo(myMap);
});
