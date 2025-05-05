from sq_db import *
from pprint import pprint

# ----------------------------------------------------------------------------------------------
# Initializations Section:
# ----------------------------------------------------------------------------------------------

# Clear entire database:
clear_db()

# Create tables:
print("Creating tables...")
create_locations()
print("\t - Created Locations table")
create_location_details()
print("\t - Created Location Details table")
create_maps()
print("\t - Created Maps table")


# ----------------------------------------------------------------------------------------------
# Fill Locations Table:
# ----------------------------------------------------------------------------------------------

print("Inserting locations...")

# Taj Mahal:
insert_location(
    id=1, name="Taj Mahal",
    location="Agra, Uttar Pradesh",
    image="taj_mahal.jpg", image2="taj_mahal_2.jpg",
    image3="taj_mahal_3.jpg", image4="taj_mahal_4.jpg"
)
print('\t - Inserted Location 1 - Taj Mahal')

# Jaipur City Palace:
insert_location(
    id=2, name="Jaipur City Palace",
    location="Jaipur, Rajasthan",
    image="jaipur_palace.jpg", image2="jaipur_palace_2.jpg",
    image3="jaipur_palace_3.jpg", image4="jaipur_palace_4.jpg"
)
print('\t - Inserted Location 2 - Jaipur City Palace')

# Mysore Palace:
insert_location(
    id=3, name="Mysore Palace",
    location="Mysore, Karnataka",
    image="mysore_palace.jpg", image2="mysore_palace_2.jpg",
    image3="mysore_palace_3.jpg", image4="mysore_palace_4.jpg"
)
print('\t - Inserted Location 3 - Mysore Palace')

# Ellora Caves:
insert_location(
    id=4, name="Ellora Caves",
    location="Aurangabad, Maharashtra",
    image="ellora_caves_3.jpg", image2="ellora_caves_2.jpg",
    image3="ellora_caves.jpg", image4="ellora_caves_4.jpg"
)
print('\t - Inserted Location 4 - Ellora Caves')

# Gateway of India:
insert_location(
    id=5, name="Gateway of India",
    location="Mumbai, Maharashtra",
    image="gateway_of_india.jpg", image2="gateway_of_india_2.jpg",
    image3="gateway_of_india_3.jpg", image4="gateway_of_india_4.jpg"
)
print('\t - Inserted Location 5 - Gateway of India')

# Kaziranga National Park:
insert_location(
    id=6, name="Kaziranga National Park",
    location="Assam, Northeast India",
    image="kaziranga.jpg", image2="kaziranga_2.jpg",
    image3="kaziranga_3.jpg", image4="kaziranga_4.jpg"
)
print('\t - Inserted Location 6 - Kaziranga National Park')


# ----------------------------------------------------------------------------------------------
# Fill location details:
# ----------------------------------------------------------------------------------------------

print("Inserting location details...")

insert_location_details(
    location_id=1,
    description_intro="The Taj Mahal, located in Agra, India, is one of the most iconic monuments in the world and a symbol of love. Built in the 17th century by Mughal Emperor Shah Jahan, this stunning white marble mausoleum was dedicated to his beloved wife, Mumtaz Mahal. Its architectural beauty and intricate details draw millions of visitors each year, making it a UNESCO World Heritage site and one of the New Seven Wonders of the World.",

    description_history="The history of the Taj Mahal dates back to 1632 when Emperor Shah Jahan commissioned the construction in memory of his wife, Mumtaz Mahal, who passed away during childbirth. The mausoleum took about 22 years to complete, involving thousands of artisans, craftsmen, and architects. It is said that Shah Jahan spared no expense, importing the finest materials from across India and Asia, including white marble, precious stones, and intricate carvings. After Shah Jahan’s death, he was laid to rest beside Mumtaz Mahal in the tomb, fulfilling his vision of an eternal resting place for the two lovers.",

    description_highlights="Highlights of the Taj Mahal include the beautiful gardens with fountains leading up to the monument, the intricate marble inlay work featuring semi-precious stones, and the central dome that towers over the tomb. The building’s symmetry, combined with its reflection in the pool, is truly mesmerizing. The Taj Mahal also boasts four minarets and impressive calligraphy of Quranic verses along its walls. Visiting during sunrise or sunset can enhance the experience, as the monument's marble surface reflects different hues in varying lights.",

    description_tips="Visit early in the morning to avoid crowds and enjoy the best lighting. Be mindful of restricted areas, and avoid bringing large bags or food items, as these are not allowed inside. Hiring a local guide can enhance your visit by providing insight into the monument’s history and architecture."
)
print('\t - Added details for location 1 - Taj Mahal')


insert_location_details(
    location_id=2,
    description_intro="The Jaipur City Palace is a grand complex of palaces, courtyards, and museums in Jaipur, Rajasthan. It showcases a unique blend of Mughal and Rajput architectural styles, offering visitors a glimpse into the royal heritage and cultural richness of the region. Constructed in the early 18th century, this palace still serves as a residence for Jaipur’s royal family and remains a must-visit attraction in the 'Pink City'.",

    description_history="Jaipur City Palace was established by Maharaja Sawai Jai Singh II, the founder of Jaipur, as a part of his vision for the new city in 1727. This elaborate complex was designed with a combination of Rajput, Mughal, and European architectural influences. The palace served as the royal residence and administrative center, hosting events, ceremonies, and royal gatherings. Successive rulers continued to add to its grandeur, creating an intricate network of courtyards, temples, and gardens, each showcasing unique artistic styles and historical significance.",

    description_highlights="Key highlights of the Jaipur City Palace include the Mubarak Mahal, with its collection of textiles and royal garments, and the Chandra Mahal, which houses royal artifacts and stunning frescoes. The Pritam Niwas Chowk courtyard is known for its intricately painted doorways, representing the four seasons. The museum within the complex offers insight into the rich cultural heritage of Jaipur, displaying royal artifacts, manuscripts, and artwork.",

    description_tips="Plan your visit in the morning to enjoy a quieter experience. Guided tours are available, providing historical insights. Be sure to dress respectfully, as some areas require traditional attire."
)
print('\t - Added details for location 2 - Jaipur City Palace')


insert_location_details(
    location_id=3,
    description_intro="Mysore Palace, located in Karnataka, India, is one of the most visited palaces in the country. Known for its Indo-Saracenic architecture and intricate interiors, this royal residence once belonged to the Wodeyar dynasty. With its impressive façade, grand halls, and vibrant festivals, Mysore Palace captures the essence of Karnataka's rich cultural heritage.",

    description_history="The original Mysore Palace was constructed in the 14th century but has been rebuilt several times due to damage from invasions and fires. The current palace was designed by British architect Henry Irwin in 1912, blending Hindu, Muslim, Rajput, and Gothic architectural elements to create a unique Indo-Saracenic style. The palace served as the seat of the Wodeyar Maharajas, who ruled Mysore for over five centuries, and was a focal point for cultural and political activities in the region.",

    description_highlights="Visitors to Mysore Palace can explore the Durbar Hall with its intricately carved pillars, the Kalyana Mantapa with beautiful stained glass ceilings, and the Ambavilasa hall, known for its impressive gold doors. During the annual Dussehra festival, the palace is illuminated with thousands of lights, creating a stunning spectacle. The palace grounds also host a museum displaying artifacts from the royal family.",

    description_tips="Plan to visit in the late afternoon to experience the palace’s illumination at night. Photography is allowed outside, but it is restricted within the interiors. Consider visiting during Dussehra for a special experience."
)
print('\t - Added details for location 3 - Mysore Palace')


insert_location_details(
    location_id=4,
    description_intro="The Ellora Caves in Maharashtra are a remarkable complex of rock-cut temples and monasteries, reflecting the harmonious coexistence of Hinduism, Buddhism, and Jainism in ancient India. Dating back to 600-1000 AD, Ellora is a UNESCO World Heritage site, known for its impressive architecture, artistry, and historical significance.",

    description_history="The Ellora Caves were carved over several centuries by skilled artisans and represent three major religious traditions of ancient India: Hinduism, Buddhism, and Jainism. The Kailasa Temple, one of the largest rock-cut temples in the world, is a masterpiece dedicated to Lord Shiva. Built in the 8th century under the patronage of the Rashtrakuta dynasty, it is known for its scale and architectural detail. The complex also includes Buddhist monasteries and Jain temples, each adorned with intricate carvings, statues, and pillars that showcase the spiritual and cultural synthesis of the time.",

    description_highlights="Highlights of the Ellora Caves include the Kailasa Temple, with its massive monolithic structure, the Buddhist viharas with their beautiful sculptures of Buddha, and the Jain caves showcasing intricate depictions of the Tirthankaras. The carvings in each cave are highly detailed, and exploring them offers a glimpse into ancient art and religious practices.",

    description_tips="Wear comfortable shoes, as the cave complex is extensive. A flashlight can be useful for viewing intricate details in dimly lit areas. Consider hiring a guide to fully appreciate the history and significance of each cave.",
)
print('\t - Added details for location 4 - Ellora Caves')


insert_location_details(
    location_id=5,
    description_intro="The Gateway of India, located in Mumbai, Maharashtra, is an iconic monument overlooking the Arabian Sea. Built to commemorate the visit of King George V and Queen Mary in 1911, this grand archway has become a symbol of Mumbai's rich history and resilience. It serves as a popular tourist attraction and a place for cultural gatherings.",

    description_history="Constructed in 1924, the Gateway of India was designed by architect George Wittet in the Indo-Saracenic style, combining Hindu, Muslim, and European architectural elements. It was originally intended as a ceremonial entrance for British Viceroys and other dignitaries arriving by sea. Over time, it became a symbol of India's colonial history, witnessing significant events, including the departure of the last British troops in 1948, marking India's independence.",

    description_highlights="The Gateway of India is known for its grand design, with an impressive central dome and intricate carvings on its basalt structure. It offers stunning views of the Arabian Sea and is situated near the iconic Taj Mahal Palace hotel. The site is especially beautiful in the evening when it is illuminated, and it provides a bustling atmosphere filled with street vendors and local artists.",

    description_tips="Visit early in the morning or late in the evening to avoid crowds. The area around the Gateway is bustling, so plan to spend some time exploring the nearby attractions, including ferry rides to Elephanta Caves."
)
print('\t - Added details for location 5 - Gateway of India')


insert_location_details(
    location_id=6,
    description_intro="Kaziranga National Park is a UNESCO World Heritage Site located in the state of Assam, India. It is home to the largest population of one-horned rhinoceroses in the world. Spanning over 1,000 square miles, the park is rich in biodiversity, including tigers, elephants, wild buffalo, and various species of birds. It is a crucial part of the Assam Valley's ecosystem and offers a unique glimpse into India's wildlife conservation efforts.",

    description_history="The park was established in 1905, initially as a forest reserve, and later declared a national park in 1974. Kaziranga has been a pioneer in rhino conservation, with the population of the one-horned rhino significantly increasing over the years. The park has faced many challenges, including poaching and floods, but continues to thrive due to its rigorous conservation practices.",

    description_highlights="Kaziranga is known for its vast grasslands, dense forests, and wetland areas. The park's most famous inhabitants are the one-horned rhinoceros, but it is also home to tigers, elephants, wild buffaloes, and hundreds of bird species. Visitors can enjoy jeep and elephant safaris to explore the diverse wildlife, and the park’s annual census of rhinos is a major event.",

    description_tips="When visiting Kaziranga, it's best to go between November and April, as the weather is more favorable for safaris. Be prepared for an early start for safaris, as the animals are most active in the morning. If you are traveling by road, ensure to check the conditions, as floods can sometimes affect the area. Also, carry binoculars for birdwatching and a good camera to capture the stunning landscapes and wildlife."
)
print('\t - Added details for location 6 - Kaziranga National Park')


# ----------------------------------------------------------------------------------------------
# Fill the maps:
# ----------------------------------------------------------------------------------------------

print("Inserting maps...")

insert_map(
    location_id=1,
    latitude=27.1751, longitude=78.0421,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3549.400402283387!2d78.0395672755463!3d27.17514954876302!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39747121d702ff6d%3A0xdd2ae4803f767dde!2sTaj%20Mahal!5e0!3m2!1sen!2sin!4v1731096906266!5m2!1sen!2sin')
)
print('\t - Added map for location 1 - Taj Mahal')


insert_map(
    location_id=2,
    latitude=26.9124, longitude=75.7873,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3557.2969486586367!2d75.82109647553895!3d26.925799059527854!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db40b8620b0c1%3A0x44801531017d7b60!2sThe%20City%20Palace!5e0!3m2!1sen!2sin!4v1731099652719!5m2!1sen!2sin')
)
print('\t - Added map for location 2 - Jaipur City Palace')


insert_map(
    location_id=3,
    latitude=12.3051, longitude=76.6551,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3898.157648891582!2d76.65259997524211!3d12.305168229138431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3baf701103f9a1f9%3A0xc37fbae2a124da0d!2sMysore%20Palace!5e0!3m2!1sen!2sin!4v1731099719717!5m2!1sen!2sin')
)
print('\t - Added map for location 3 - Mysore Palace')


insert_map(
    location_id=4,
    latitude=20.0264, longitude=75.1822,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14994.081656486365!2d75.15761048715821!3d20.02863330000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdb92609201a9eb%3A0xe0639ba6286a474!2sEllora%20Cave%20No.%2029%20The%20Dhumar%20Lena!5e0!3m2!1sen!2sin!4v1731098951522!5m2!1sen!2sin')
)
print('\t - Added map for location 4 - Ellora Caves')


insert_map(
    location_id=5,
    latitude=18.9220, longitude=72.8347,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3774.2124287744723!2d72.83207937534421!3d18.92198915678915!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7d1c73a0d5cad%3A0xc70a25a7209c733c!2sGateway%20Of%20India%20Mumbai!5e0!3m2!1sen!2sin!4v1731099772759!5m2!1sen!2sin')
)
print('\t - Added map for location 5 - Gateway of India')


insert_map(
    location_id=6,
    latitude=26.6574, longitude=93.1968,
    map_iframe=get_iframe_code('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14279.453420942631!2d92.98384525627273!3d26.524518829310978!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3744fbb424af3d57%3A0x4d16514f2d701362!2sKaziranga%20National%20Park%2C%20Assam!5e0!3m2!1sen!2sin!4v1731100048295!5m2!1sen!2sin')
)
print('\t - Added map for location 6 - Kaziranga National Park')

# ----------------------------------------------------------------------------------------------
# Testing Section:
# ----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Test the database operations:
    print("\n\n\n")
    pprint(get_location_data(2, output_format='dict'))
    print("\n\n\n")
    pprint(get_all_locations_data(output_format='dict'))

    print("Success!!")