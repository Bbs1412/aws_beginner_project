// script.js

var S3_BASE_URL;
fetch('/get_s3_base_url')
    .then(response => response.json())
    .then(data => {
        // console.log(data);
        S3_BASE_URL = data;
    });


document.addEventListener('DOMContentLoaded', function () {
    const placesContainer = document.getElementById('placesContainer');
    placesContainer.innerHTML = '<div class="loading">Loading places...</div>';

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
    function createPlaceCard(loc) {
        const card = document.createElement('div');
        card.className = 'place-card';
        card.innerHTML = `
            <!-- Using flask 
            -->
            <img src="/get_img/${loc.image}" alt="${loc.name}" class="place-image">
            <img src="/get_img/${loc.image}" alt="${loc.name}"  class="place-bg-image">
            
            <!-- Using S3
            <img src="${S3_BASE_URL}/${loc.image}" alt="${loc.name}" class="place-image">
            <img src="${S3_BASE_URL}/${loc.image}" alt="${loc.name}"  class="place-bg-image">
            -->
            

            <div class="place-info">
                <h2>${loc.name}</h2>
                <p>${loc.location}</p>
            </div>
        `;

        // Add click event to navigate to detail page
        card.addEventListener('click', () => {
            window.location.href = `/place/${loc.id}`;
        });

        return card;
    }
});