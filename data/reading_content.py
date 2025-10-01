"""Reading comprehension materials from tourism industry"""

READING_CONTENT = {
    "Hotel Description - Luxury Resort": {
        "type": "Hotel Description",
        "difficulty": "Intermediate",
        "text": """
Ma'yan Grand Hotel: Your Gateway to Comfort and Luxury

Nestled in the heart of Ma'yan's historic district, the Ma'yan Grand Hotel combines modern luxury with traditional charm. Our five-star property has been welcoming guests since 1995, earning a reputation for exceptional service and attention to detail.

Accommodation:
The hotel features 150 elegantly appointed rooms and suites, each designed with your comfort in mind. All rooms include complimentary high-speed Wi-Fi, flat-screen televisions, minibars, and luxurious bedding. Our deluxe rooms offer stunning views of either the city skyline or the surrounding mountains.

Dining Options:
Guests can enjoy diverse culinary experiences at our three on-site restaurants. The Olive Grove serves Mediterranean cuisine for breakfast, lunch, and dinner. For a more intimate dining experience, visit our rooftop restaurant, Sky Terrace, which offers panoramic views and an extensive wine list. Our casual café, Bean & Brew, serves light meals and specialty coffees throughout the day.

Facilities:
The hotel boasts a full-service spa, fitness center open 24/7, indoor heated pool, and outdoor sundeck. Business travelers will appreciate our state-of-the-art conference facilities and business center. Complimentary parking is available for all guests.

Location:
Situated just 2 kilometers from the ancient Ma'yan Fortress and within walking distance of the main shopping district, our hotel offers the perfect base for exploring the area. The airport is a convenient 20-minute drive away, and we offer shuttle services for our guests.

Our Commitment:
At Ma'yan Grand Hotel, we are committed to providing an unforgettable experience. Our multilingual staff is available 24 hours a day to assist with any request, from arranging tours to recommending local attractions. We look forward to welcoming you.
        """,
        "questions": [
            {
                "question": "When was the Ma'yan Grand Hotel established?",
                "options": ["1985", "1990", "1995", "2000"],
                "correct": 2
            },
            {
                "question": "How many restaurants does the hotel have?",
                "options": ["One", "Two", "Three", "Four"],
                "correct": 2
            },
            {
                "question": "What view options are available for deluxe rooms?",
                "options": [
                    "City or ocean views",
                    "City skyline or mountain views",
                    "Garden or pool views",
                    "Only mountain views"
                ],
                "correct": 1
            },
            {
                "question": "How far is the hotel from the Ma'yan Fortress?",
                "options": ["1 kilometer", "2 kilometers", "5 kilometers", "10 kilometers"],
                "correct": 1
            },
            {
                "question": "According to the text, what makes the hotel suitable for business travelers?",
                "options": [
                    "Free breakfast",
                    "Airport location",
                    "Conference facilities and business center",
                    "Spa services"
                ],
                "correct": 2
            }
        ],
        "vocabulary_focus": ["accommodation", "elegantly appointed", "culinary", "boasts", "state-of-the-art"]
    },
    
    "Booking Confirmation Email": {
        "type": "Business Correspondence",
        "difficulty": "Beginner",
        "text": """
Subject: Booking Confirmation - Reservation #MG789456

Dear Ms. Thompson,

Thank you for choosing Ma'yan Grand Hotel for your upcoming visit. We are delighted to confirm your reservation.

Reservation Details:
Guest Name: Sarah Thompson
Confirmation Number: MG789456
Check-in Date: December 5, 2025
Check-out Date: December 8, 2025
Room Type: Deluxe King Room with City View
Number of Guests: 2 Adults
Rate: $220 per night (3 nights = $660)

Your Rate Includes:
- Complimentary breakfast buffet for two guests
- Free high-speed Wi-Fi
- Access to fitness center and indoor pool
- Welcome drink upon arrival

Important Information:
Check-in time: 3:00 PM
Check-out time: 11:00 AM
Cancellation Policy: Free cancellation up to 48 hours before arrival
Parking: Complimentary self-parking available

A credit card was provided to guarantee your reservation. The card will only be charged in case of a no-show or late cancellation.

If you need to modify your reservation, please contact us at least 48 hours prior to arrival. You can reach us at reservations@mayangrand.com or call +123-456-7890.

We look forward to welcoming you to Ma'yan Grand Hotel and ensuring you have a memorable stay.

Warm regards,

Reservations Team
Ma'yan Grand Hotel
        """,
        "questions": [
            {
                "question": "What is Ms. Thompson's confirmation number?",
                "options": ["MG789456", "MG987654", "MT789456", "MG123456"],
                "correct": 0
            },
            {
                "question": "How many nights is the reservation for?",
                "options": ["2 nights", "3 nights", "4 nights", "5 nights"],
                "correct": 1
            },
            {
                "question": "What is the nightly rate for the room?",
                "options": ["$200", "$220", "$240", "$660"],
                "correct": 1
            },
            {
                "question": "How long before arrival can the reservation be cancelled for free?",
                "options": ["24 hours", "36 hours", "48 hours", "72 hours"],
                "correct": 2
            },
            {
                "question": "What is NOT included in the room rate?",
                "options": [
                    "Breakfast buffet",
                    "Wi-Fi",
                    "Parking",
                    "Airport shuttle"
                ],
                "correct": 3
            }
        ],
        "vocabulary_focus": ["confirmation", "complimentary", "guarantee", "modify", "prior to"]
    },
    
    "Customer Review - Positive": {
        "type": "Customer Feedback",
        "difficulty": "Intermediate",
        "text": """
Exceptional Stay at Ma'yan Grand Hotel
★★★★★ 5/5 stars
Reviewed by: Mark Williams, Business Traveler
Date of Stay: September 2025

I recently spent four nights at the Ma'yan Grand Hotel during a business trip, and I must say it exceeded all my expectations. From the moment I arrived, the staff demonstrated outstanding professionalism and hospitality.

The check-in process was seamless and efficient. Despite arriving earlier than the standard check-in time, my room was already prepared, which I greatly appreciated after a long flight. The front desk staff were courteous and provided helpful information about the hotel facilities and local attractions.

My deluxe room was spacious, impeccably clean, and well-appointed with modern amenities. The bed was extremely comfortable, ensuring I got good rest despite my busy schedule. The workspace was adequate for my needs, with reliable high-speed internet and convenient power outlets. I particularly enjoyed the city views from my window.

The hotel's location is ideal for both business and leisure travelers. It's within walking distance of several restaurants and shops, yet far enough from the main thoroughfare to ensure a peaceful environment. The business center and conference facilities were top-notch, and the staff was always available to assist with any technical requirements.

Breakfast at the Olive Grove restaurant was a highlight of my stay. The buffet offered an impressive variety of both local and international dishes, all fresh and delicious. The restaurant staff were attentive and kept everything well-stocked even during peak hours.

One evening, I dined at the Sky Terrace rooftop restaurant. The food was excellent, and the panoramic views of the city at sunset were breathtaking. I highly recommend making a reservation for dinner there.

The hotel's amenities, including the fitness center and pool, were well-maintained and never overcrowded. After long days of meetings, I found the gym particularly useful for staying active.

If I had to mention any area for improvement, it would be that the air conditioning in the room was slightly noisy at night. However, this is a minor issue and didn't significantly impact my overall experience.

I would definitely recommend the Ma'yan Grand Hotel to anyone visiting the area, whether for business or pleasure. The combination of excellent service, comfortable accommodations, and convenient location makes it an outstanding choice. I look forward to returning on my next visit to Ma'yan.
        """,
        "questions": [
            {
                "question": "What type of traveler is Mark Williams?",
                "options": ["Tourist", "Business traveler", "Family traveler", "Solo backpacker"],
                "correct": 1
            },
            {
                "question": "What positive aspect does the reviewer mention about check-in?",
                "options": [
                    "It was very cheap",
                    "The room was ready early",
                    "He got a free upgrade",
                    "There was no waiting"
                ],
                "correct": 1
            },
            {
                "question": "According to the review, what was a highlight of the stay?",
                "options": [
                    "The swimming pool",
                    "The breakfast buffet",
                    "The room service",
                    "The parking"
                ],
                "correct": 1
            },
            {
                "question": "What minor complaint did the reviewer mention?",
                "options": [
                    "Slow Wi-Fi",
                    "Small room",
                    "Noisy air conditioning",
                    "Unfriendly staff"
                ],
                "correct": 2
            },
            {
                "question": "What does the reviewer recommend?",
                "options": [
                    "Avoiding the rooftop restaurant",
                    "Requesting a different room",
                    "Making a reservation at Sky Terrace",
                    "Skipping breakfast"
                ],
                "correct": 2
            }
        ],
        "vocabulary_focus": ["exceeded expectations", "seamless", "impeccably", "well-appointed", "thoroughfare"]
    },
    
    "Tourism Guide - Historical Site": {
        "type": "Tourism Information",
        "difficulty": "Advanced",
        "text": """
The Ancient Ma'yan Fortress: A Journey Through Time

The Ma'yan Fortress stands as a testament to the region's rich historical heritage. Perched atop a strategic hilltop overlooking the valley, this magnificent structure has witnessed centuries of history, from ancient battles to peaceful times of prosperity.

Historical Background:
Construction of the fortress began in 1142 CE during the reign of Sultan Ahmad the Great. Built primarily as a defensive stronghold, the fortress played a crucial role in protecting trade routes that connected the region to neighboring territories. Over the centuries, it served various purposes: a military garrison, a royal residence, and eventually an administrative center.

The fortress complex covers approximately 45,000 square meters and originally consisted of three concentric defensive walls, watchtowers, barracks, a mosque, and residential quarters. Although parts of the outer walls have deteriorated over time, much of the original structure remains intact, offering visitors a glimpse into medieval architecture and military engineering.

Architectural Significance:
The fortress showcases remarkable architectural features characteristic of 12th-century fortifications. The main entrance, known as the Gate of Lions, features intricate stone carvings and a sophisticated defense mechanism including a drawbridge and murder holes. The inner courtyard contains a beautifully preserved mosque with ornate tilework and calligraphy that dates back to the fortress's original construction.

The watchtowers, standing at heights of up to 25 meters, provide breathtaking panoramic views of the surrounding valley. From these vantage points, guards could spot approaching threats from kilometers away. The ingenious water collection system, consisting of cisterns and channels, ensured the fortress could withstand prolonged sieges.

Cultural Impact:
In 1995, UNESCO designated the Ma'yan Fortress as a World Heritage Site, recognizing its outstanding universal value and historical significance. The designation has brought increased awareness and funding for preservation efforts, ensuring that future generations can appreciate this architectural marvel.

Today, the fortress serves as both a museum and a cultural center. Archaeological excavations continue to uncover artifacts that provide insights into daily life during various historical periods. The fortress hosts cultural festivals, educational programs, and traditional craft demonstrations, making history accessible and engaging for visitors of all ages.

Visiting Information:
The fortress is open year-round, though the most pleasant visiting conditions are during spring (March-May) and autumn (September-November). Summer temperatures can exceed 35°C, making exploration of the extensive grounds physically demanding. Early morning visits are recommended for optimal lighting and fewer crowds.

Guided tours in multiple languages are available and highly recommended, as knowledgeable guides bring the history to life through captivating narratives and little-known anecdotes. Audio guides in eight languages offer an alternative for independent explorers.

The site is partially accessible for visitors with mobility limitations. The main courtyard and ground-level exhibitions are wheelchair accessible, though the watchtowers and ramparts involve climbing stairs and may not be suitable for all visitors.

Conservation Challenges:
Despite ongoing preservation efforts, the fortress faces challenges from natural weathering, increased tourism, and urban development in surrounding areas. Conservation specialists work continuously to stabilize structures, protect delicate decorative elements, and implement sustainable tourism practices that balance accessibility with preservation.

The Ma'yan Fortress exemplifies the intersection of history, architecture, and culture. Whether you're a history enthusiast, an architecture admirer, or simply seeking to understand the region's heritage, a visit to this remarkable site promises an enriching and memorable experience.
        """,
        "questions": [
            {
                "question": "When did construction of the Ma'yan Fortress begin?",
                "options": ["1042 CE", "1142 CE", "1242 CE", "1342 CE"],
                "correct": 1
            },
            {
                "question": "When was the fortress designated as a UNESCO World Heritage Site?",
                "options": ["1985", "1990", "1995", "2000"],
                "correct": 2
            },
            {
                "question": "What is the main entrance of the fortress called?",
                "options": [
                    "The Grand Gate",
                    "The Gate of Lions",
                    "The Sultan's Gate",
                    "The Victory Gate"
                ],
                "correct": 1
            },
            {
                "question": "According to the text, what months are recommended for visiting?",
                "options": [
                    "June-August",
                    "December-February",
                    "March-May and September-November",
                    "January-March"
                ],
                "correct": 2
            },
            {
                "question": "What challenge to conservation is NOT mentioned in the text?",
                "options": [
                    "Natural weathering",
                    "Increased tourism",
                    "Urban development",
                    "Lack of funding"
                ],
                "correct": 3
            }
        ],
        "vocabulary_focus": ["testament", "perched", "stronghold", "garrison", "deteriorated", "intricate", "vantage points", "designation"]
    }
}

def get_all_content_types():
    """Return list of all content types"""
    types = set(content['type'] for content in READING_CONTENT.values())
    return list(types)

def get_content_by_type(content_type):
    """Return reading content filtered by type"""
    return {title: data for title, data in READING_CONTENT.items() 
            if data['type'] == content_type}

def get_content_by_difficulty(difficulty):
    """Return reading content filtered by difficulty"""
    return {title: data for title, data in READING_CONTENT.items() 
            if data['difficulty'] == difficulty}

def get_all_titles():
    """Return list of all reading content titles"""
    return list(READING_CONTENT.keys())

def get_content(title):
    """Return specific reading content"""
    return READING_CONTENT.get(title)
