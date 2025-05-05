// script.js

document.addEventListener('DOMContentLoaded', function () {
    const placesContainer = document.getElementById('placesContainer');
    placesContainer.innerHTML = '<div class="loading">Loading places...</div>';

    // This is sample data - replaced with data from actual Flask backend
    // const places = [
    //     {
    //         id: 1,
    //         name: "Taj Mahal",
    //         location: "Agra, Uttar Pradesh",
    //         image: "taj_mahal.jpg"
    //     },
    //     {
    //         id: 2,
    //         name: "Jaipur City Palace",
    //         location: "Jaipur, Rajasthan",
    //         image: "jaipur_palace.jpg"
    //     },
    //     // ...
    // ];

    let places = [];

    fetch('/get_all_locations')
        .then(response => response.json())
        .then(data => {
            places = data;
            
            // Clear loading message
            placesContainer.innerHTML = '';
            
            // Render all places
            places.forEach(place => {
                placesContainer.appendChild(createPlaceCard(place));
            });
        })
        .catch(error => console.error('Error fetching places:', error));


    // Function to create place cards (based on the json data)
    function createPlaceCard(place) {
        const card = document.createElement('div');
        card.className = 'place-card';
        card.innerHTML = `
            <!-- <img src="/static/images/${place.image}" alt="${place.name}" class="place-image"> -->
            <!-- <img src="/static/images/${place.image}" alt="${place.name}"  class="place-bg-image"> -->

            <img src="/get_img/${place.image}" alt="${place.name}" class="place-image">
            <img src="/get_img/${place.image}" alt="${place.name}"  class="place-bg-image">
            

            <div class="place-info">
                <h2>${place.name}</h2>
                <p>${place.location}</p>
            </div>
        `;

        // Add click event to navigate to detail page
        card.addEventListener('click', () => {
            window.location.href = `/place/${place.id}`;
        });

        return card;
    }


});