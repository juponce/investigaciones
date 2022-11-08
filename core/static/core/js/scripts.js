// var osm_map = L.tileLayer(
//     'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
//     {
//         attribution:
//             '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
//     }
// );

// var map = L.map('map', {
//     layers: [osm_map],
// }).setView([8.7832, 34.5085], 3);


const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

let myMap = L.map('map').setView([-33.516452, -70.599746], 18)

L.tileLayer(tilesProvider, {
    maxZoom: 18,
}).addTo(myMap)

L.Marker.prototype.options.icon = L.icon({
    iconUrl: "/static/core/img/marker-icon-2x.png"
});

var greenIcon = L.icon({
    iconUrl: '/static/core/img/marker-icon-2x.png',

    iconSize:     [38, 95], // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

let marker = L.marker([-33.516452, -70.599746], {icon: greenIcon}).addTo(myMap)

L.Control.geocoder().addTo(myMap)