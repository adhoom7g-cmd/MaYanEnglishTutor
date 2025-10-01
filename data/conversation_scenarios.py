"""Conversation scenarios for tourism and business contexts"""

CONVERSATION_SCENARIOS = {
    "Greeting Tourists at Hotel Reception": {
        "description": "Practice welcoming guests at hotel check-in",
        "difficulty": "Beginner",
        "dialogue": [
            {"speaker": "Receptionist", "text": "Good morning! Welcome to Ma'yan Grand Hotel. How may I assist you today?"},
            {"speaker": "Guest", "text": "Good morning. I have a reservation under the name Smith."},
            {"speaker": "Receptionist", "text": "Let me check that for you, Mr. Smith. Yes, I have your reservation here for a deluxe room for three nights. Is that correct?"},
            {"speaker": "Guest", "text": "Yes, that's correct."},
            {"speaker": "Receptionist", "text": "Wonderful. May I see your ID and credit card for incidentals, please?"},
            {"speaker": "Guest", "text": "Here you go."},
            {"speaker": "Receptionist", "text": "Thank you. Your room is on the fifth floor, room 507. Breakfast is served from 7 to 10 AM in the dining hall. Here's your key card. Enjoy your stay!"},
        ],
        "key_phrases": [
            "How may I assist you?",
            "I have a reservation under the name...",
            "May I see your ID?",
            "Your room is on the... floor",
            "Enjoy your stay!"
        ],
        "practice_points": [
            "Use polite greetings appropriate to time of day",
            "Confirm reservation details clearly",
            "Explain hotel amenities and important information",
            "Maintain professional and friendly tone"
        ]
    },
    "Handling Room Service Requests": {
        "description": "Respond to guest room service calls professionally",
        "difficulty": "Beginner",
        "dialogue": [
            {"speaker": "Staff", "text": "Good evening, Room Service. This is Maria speaking. How may I help you?"},
            {"speaker": "Guest", "text": "Hi, I'd like to order dinner to my room."},
            {"speaker": "Staff", "text": "Of course! May I have your room number, please?"},
            {"speaker": "Guest", "text": "Room 302."},
            {"speaker": "Staff", "text": "Thank you, Mr. Johnson. What would you like to order this evening?"},
            {"speaker": "Guest", "text": "I'll have the grilled salmon with vegetables and a Caesar salad."},
            {"speaker": "Staff", "text": "Excellent choice. Would you like any beverages with your meal?"},
            {"speaker": "Guest", "text": "Just a bottle of sparkling water, please."},
            {"speaker": "Staff", "text": "Perfect. Your order will be delivered within 30 minutes. Is there anything else I can help you with?"},
            {"speaker": "Guest", "text": "No, that's all. Thank you."},
            {"speaker": "Staff", "text": "You're welcome. Enjoy your meal!"},
        ],
        "key_phrases": [
            "How may I help you?",
            "May I have your room number?",
            "What would you like to order?",
            "Excellent choice",
            "Your order will be delivered within..."
        ],
        "practice_points": [
            "Identify yourself and department clearly",
            "Confirm room number for every order",
            "Provide time estimates for delivery",
            "Offer additional assistance"
        ]
    },
    "Handling Booking Inquiries by Phone": {
        "description": "Process reservation requests professionally over the phone",
        "difficulty": "Intermediate",
        "dialogue": [
            {"speaker": "Staff", "text": "Good afternoon, Ma'yan Grand Hotel Reservations. My name is Ahmad. How may I assist you?"},
            {"speaker": "Caller", "text": "Hi, I'd like to make a reservation for next month."},
            {"speaker": "Staff", "text": "I'd be happy to help you with that. What dates are you looking to book?"},
            {"speaker": "Caller", "text": "From October 15th to October 18th."},
            {"speaker": "Staff", "text": "Let me check our availability for those dates. How many guests will be staying?"},
            {"speaker": "Caller", "text": "Two adults."},
            {"speaker": "Staff", "text": "Perfect. We have availability for those dates. Would you prefer a standard room or a deluxe room?"},
            {"speaker": "Caller", "text": "What's the difference in price?"},
            {"speaker": "Staff", "text": "Our standard rooms are $150 per night, while deluxe rooms with a balcony and city view are $200 per night."},
            {"speaker": "Caller", "text": "I'll take the deluxe room."},
            {"speaker": "Staff", "text": "Excellent choice. That will be three nights at $200 per night, totaling $600 plus tax. May I have your name and contact information?"},
        ],
        "key_phrases": [
            "How may I assist you?",
            "Let me check our availability",
            "How many guests will be staying?",
            "Would you prefer...?",
            "May I have your name and contact information?"
        ],
        "practice_points": [
            "Speak clearly and at moderate pace on phone",
            "Ask clarifying questions to understand needs",
            "Provide pricing information clearly",
            "Confirm all details before finalizing"
        ]
    },
    "Handling Customer Complaints": {
        "description": "Address guest concerns with professionalism and empathy",
        "difficulty": "Intermediate",
        "dialogue": [
            {"speaker": "Guest", "text": "Excuse me, I need to speak to someone about my room."},
            {"speaker": "Staff", "text": "Of course, I'm here to help. What seems to be the problem?"},
            {"speaker": "Guest", "text": "The air conditioning isn't working, and it's very hot in my room."},
            {"speaker": "Staff", "text": "I sincerely apologize for the inconvenience. That must be very uncomfortable. Let me arrange for maintenance to check your room immediately."},
            {"speaker": "Guest", "text": "How long will it take?"},
            {"speaker": "Staff", "text": "Our maintenance team will be there within 15 minutes. In the meantime, would you like to wait in our lounge where it's cool and comfortable? I can offer you a complimentary beverage."},
            {"speaker": "Guest", "text": "Yes, that would be good."},
            {"speaker": "Staff", "text": "Perfect. I'll also make a note on your account and ensure this is resolved quickly. Again, I apologize for the inconvenience, and thank you for your patience."},
        ],
        "key_phrases": [
            "I sincerely apologize for the inconvenience",
            "That must be very uncomfortable",
            "Let me arrange for... immediately",
            "Would you like to...?",
            "Thank you for your patience"
        ],
        "practice_points": [
            "Acknowledge the problem immediately",
            "Show genuine empathy and apologize",
            "Offer immediate solutions",
            "Provide alternatives while problem is being fixed",
            "Follow up to ensure satisfaction"
        ]
    },
    "Explaining Hotel Amenities and Services": {
        "description": "Inform guests about available facilities and services",
        "difficulty": "Intermediate",
        "dialogue": [
            {"speaker": "Guest", "text": "Can you tell me about the hotel facilities?"},
            {"speaker": "Staff", "text": "Certainly! We have a wide range of amenities for our guests. We have a fitness center on the second floor, open 24 hours a day."},
            {"speaker": "Guest", "text": "That's great. What about dining options?"},
            {"speaker": "Staff", "text": "We have two restaurants: our main dining room serving breakfast, lunch, and dinner, and a rooftop restaurant with Mediterranean cuisine open for dinner. We also offer 24-hour room service."},
            {"speaker": "Guest", "text": "Do you have a pool?"},
            {"speaker": "Staff", "text": "Yes, we have both an indoor heated pool and an outdoor pool with a sundeck. The outdoor pool is open from 7 AM to 9 PM."},
            {"speaker": "Guest", "text": "Excellent. And business facilities?"},
            {"speaker": "Staff", "text": "We have a fully-equipped business center with computers, printers, and high-speed internet. We also have three conference rooms available for meetings and events."},
        ],
        "key_phrases": [
            "We have a wide range of amenities",
            "The facility is located on the... floor",
            "Open from... to...",
            "Available 24 hours",
            "Fully-equipped with..."
        ],
        "practice_points": [
            "Organize information clearly by category",
            "Provide specific details (hours, location)",
            "Highlight unique features",
            "Ask if guest needs additional information"
        ]
    },
    "Professional Email Response - Booking Confirmation": {
        "description": "Write and read aloud professional email confirmations",
        "difficulty": "Intermediate",
        "dialogue": [
            {"speaker": "Email", "text": "Dear Mr. Anderson,\n\nThank you for choosing Ma'yan Grand Hotel for your upcoming stay. This email confirms your reservation details:\n\nGuest Name: John Anderson\nCheck-in: November 10, 2025\nCheck-out: November 13, 2025\nRoom Type: Deluxe King Room\nNumber of Guests: 2 Adults\nTotal Cost: $600 (excluding taxes)\n\nYour reservation includes:\n- Complimentary breakfast for two\n- Free Wi-Fi throughout the hotel\n- Access to fitness center and pool\n\nCheck-in time begins at 3:00 PM and check-out is at 11:00 AM. Early check-in and late check-out are subject to availability.\n\nIf you need to modify your reservation or have any questions, please don't hesitate to contact us at reservations@mayangrand.com or call us at +123-456-7890.\n\nWe look forward to welcoming you to Ma'yan Grand Hotel.\n\nBest regards,\nReservations Team\nMa'yan Grand Hotel"}
        ],
        "key_phrases": [
            "Thank you for choosing...",
            "This email confirms...",
            "Your reservation includes...",
            "If you need to modify...",
            "We look forward to welcoming you"
        ],
        "practice_points": [
            "Use professional greeting and closing",
            "Present information in clear, organized format",
            "Include all relevant details",
            "Provide contact information",
            "Maintain warm but professional tone"
        ]
    },
    "Website Content Discussion with Client": {
        "description": "Discuss website updates and content strategy",
        "difficulty": "Advanced",
        "dialogue": [
            {"speaker": "Web Professional", "text": "Good morning, Ms. Chen. Thank you for meeting with me today to discuss your website updates."},
            {"speaker": "Client", "text": "Good morning. Yes, I'm eager to hear your recommendations."},
            {"speaker": "Web Professional", "text": "After analyzing your current site, I've identified several areas for improvement. First, I recommend updating the homepage layout to make it more responsive on mobile devices."},
            {"speaker": "Client", "text": "That makes sense. Many of our customers book on their phones."},
            {"speaker": "Web Professional", "text": "Exactly. We should also optimize your booking engine interface to reduce the number of steps required to complete a reservation. Currently, it takes six clicks, but we can reduce that to three."},
            {"speaker": "Client", "text": "That sounds excellent. What about our content?"},
            {"speaker": "Web Professional", "text": "I suggest enhancing your room descriptions with more detailed information and professional photography. We should also implement SEO optimization to improve your search engine rankings."},
            {"speaker": "Client", "text": "How long would these changes take to implement?"},
            {"speaker": "Web Professional", "text": "The complete overhaul would take approximately six weeks, but we can implement the changes in phases to minimize disruption to your booking system."},
        ],
        "key_phrases": [
            "After analyzing...",
            "I recommend...",
            "We should optimize...",
            "I suggest enhancing...",
            "We can implement the changes in phases"
        ],
        "practice_points": [
            "Present recommendations with supporting reasons",
            "Use technical terms appropriately",
            "Anticipate client concerns",
            "Provide clear timelines",
            "Offer phased implementation options"
        ]
    },
    "Describing Tourist Attractions to Visitors": {
        "description": "Provide information about local attractions enthusiastically",
        "difficulty": "Intermediate",
        "dialogue": [
            {"speaker": "Tourist", "text": "We have a free day tomorrow. What would you recommend we visit?"},
            {"speaker": "Guide", "text": "There are several wonderful attractions in the Ma'yan area! Are you interested in historical sites, nature, or cultural experiences?"},
            {"speaker": "Tourist", "text": "We'd love to see some historical sites."},
            {"speaker": "Guide", "text": "In that case, I highly recommend visiting the Ancient Ma'yan Fortress. It's a UNESCO World Heritage site dating back to the 12th century. The architecture is breathtaking, and from the top, you get panoramic views of the entire valley."},
            {"speaker": "Tourist", "text": "That sounds amazing! How do we get there?"},
            {"speaker": "Guide", "text": "It's about 20 minutes by car. I can arrange transportation for you, or there's a local bus that leaves from the main square every hour. I'd recommend going in the morning when it's cooler and less crowded."},
            {"speaker": "Tourist", "text": "Is there an entrance fee?"},
            {"speaker": "Guide", "text": "Yes, the entrance fee is 50 shekels per person, and guided tours are available for an additional 30 shekels. The guided tour is definitely worth it as you'll learn fascinating historical details."},
        ],
        "key_phrases": [
            "I highly recommend...",
            "It's a UNESCO World Heritage site",
            "The architecture is breathtaking",
            "I can arrange transportation",
            "I'd recommend going in the morning"
        ],
        "practice_points": [
            "Show enthusiasm about local attractions",
            "Provide practical information (cost, location, timing)",
            "Offer personal recommendations",
            "Give helpful tips for the best experience"
        ]
    }
}

def get_all_scenarios():
    """Return list of all scenario titles"""
    return list(CONVERSATION_SCENARIOS.keys())

def get_scenario(title):
    """Return specific scenario data"""
    return CONVERSATION_SCENARIOS.get(title)

def get_scenarios_by_difficulty(difficulty):
    """Return scenarios filtered by difficulty level"""
    return {title: data for title, data in CONVERSATION_SCENARIOS.items() 
            if data['difficulty'] == difficulty}
