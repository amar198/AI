## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* affirm
    - utter_goodbye
    - export

#-------------------------------------------------------------------------------------
#stories added by amar
#-------------------------------------------------------------------------------------
## Generated Story 01_29062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search{"budget": "around 400"}
    - slot{"budget": "medium"}
    - action_restaurant
    - utter_ask_email_id
* restaurant_search{"email": "abc.xyz@somemaildomain.com"}
    - slot{"email": "abc.xyz@somemaildomain.com"}
    - send_email
    - utter_goodbye

## Generated Story 02_29062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "300 and 700"}
    - slot{"budget": "medium"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "mrunmayee.deshpande28@gmail.com"}
    - slot{"email": "mrunmayee.deshpande28@gmail.com"}
    - email_check
    - slot{"email": "mrunmayee.deshpande28@gmail.com"}
    - send_email
    - slot{"email": "mrunmayee.deshpande28@gmail.com"}
    - utter_goodbye

## Generated Story - 03_29062019
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}
    - utter_goodbye

## Generated Story - 04_29062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_restaurant
    - slot{"location": "bengaluru"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}

## Generated Story 05_30062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_restaurant
    - slot{"location": "Hyderabad"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}
    - utter_goodbye

## Generated Story 06_30062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - city_check
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}
    - utter_goodbye

## Generated Story 07_30062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - city_check
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"email_response": "White Charcoal - The Empresa Hotel in The Empresa Hotel, Oberoi Complex, Off New Link Road, Andheri Lokhandwala, Andheri West has been rated 4.9\nKnotty Yard in 1st Floor, Above China Valley, Opposite Powai Hiranandani Bus Depot, Powai, Mumbai has been rated 4.9\nOn Toes in 1st Floor, New Chandra CHS, Above Skoda Showroom, Veera Desai Area, Mumbai has been rated 4.9\nTamasha in Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai has been rated 4.8\nHitchki in 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai has been rated 4.8\nHitchki in 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai has been rated 4.8\nHITCHKI in Ground Floor, Viviana Mall, Eastern Express Highway, Near Jupiter Hospital, Majiwada, Thane West has been rated 4.8\nPalladium Social in Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.8\nFebruary 30 in Shop 28, Ground Floor, Meera Co-Operative Housing Society Limited, Oshiwara Link Road, Oshiwara, Andheri West, Mumbai has been rated 4.8\nThe Studs Sports Bar & Grill in Shop 10 & 11, Sagar Pallazio, Near Sakinaka Junction, Andheri Kurla Road, Sakinaka, Mumbai has been rated 4.8\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}
    - utter_goodbye

## Generated Story 08_30062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - city_check
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Biergarten in 4th B Cross, Koramangala 5th Block, Bangalore has been rated 4.9\n\n2. Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore has been rated 4.9\n\n3. TBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore has been rated 4.9\n\n4. Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore has been rated 4.9\n\n5. Asia Kitchen By Mainland China in 136, Ground Floor, 1st Cross, 5th Block, Jyoti Niwas College Road, Koramangala 5th Block, Bangalore has been rated 4.9\n\n6. The Globe Grub in 2nd Floor, Soul Space Paradigm, Above Bata Showroom, Outer Ring Road, Marathahalli, Bangalore has been rated 4.9\n\n7. AB's - Absolute Barbecues in 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore has been rated 4.9\n\n8. Brew and Barbeque - A Microbrewery Pub in 36/4, Fourth Floor, Soul Space Arena, Outer Ring Road, Doddanekkundi Village, Marathahalli, Bangalore has been rated 4.8\n\n9. The Globe Grub in C K Emerald, Opposite Yes Bank, BTM Layout, Near Shoppers Stop Bannerghata Main Road, BTM, Bangalore has been rated 4.8\n\n10. Communiti in 67 & 68, Brigade Solitaire, Opposite To Advaith Hyundai, Residency Road, Bangalore has been rated 4.8\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}
    - utter_goodbye

## Generated Story 09_30062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - city_check
    - slot{"location": "chennai"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Coal Barbecues in Shop 17-18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai has been rated 4.9\n\n2. Coal Barbecues in 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai has been rated 4.9\n\n3. AB's - Absolute Barbecues in 45, GN Chetty Road, T. Nagar, Chennai has been rated 4.9\n\n4. AB's - Absolute Barbecues in 5th Floor, Vivira Mall, Navallur, Chennai has been rated 4.9\n\n5. Barbeque Nation in 39, 1st Floor, Bazullah Road, Star City Serviced Apartments, T. Nagar, Chennai has been rated 4.9\n\n6. Chili's American Grill & Bar in S-29, 2nd Floor, Phoneix Market City, 142, Velachery Main Road, Chennai has been rated 4.8\n\n7. Chili's American Grill & Bar in 49 & 50 L, Express Avenue Mall, White's Road, Royapettah, Chennai has been rated 4.8\n\n8. Barbeque Nation in 11, Ground Floor, Ramaniyam Isha, Block 1, Thuraipakkam, Chennai has been rated 4.8\n\n9. The Black Pearl in Plot 155, 292/132, Ground Floor, Rajiv Gandhi Salai, Old Mahabalipuram Road, Sholinganallur, Chennai has been rated 4.7\n\n10. Mainland China in 1st Floor, 142, Phoenix Market City, Velachery, Chennai has been rated 4.7\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - slot{"email": "amar198@gmail.com"}
    - utter_goodbye

## Generated Story 10_30062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - city_check
    - slot{"location": "jodhpur"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"email_response": "1. Punjabi Chic Inn in 130, Medical College Road, Sindhi Colony, Opposite Dr S N Medical College, Shastri Nagar, Bhagat Ki Kothi, Jodhpur has been rated 4.6\n\n2. Janta Sweet Home in 3, Nai Sarak, Kabir Nagar, Jodhpur has been rated 4.6\n\n3. Gypsy in Ground Floor, 689, 9th C Road, Sardarpura, Jodhpur has been rated 4.5\n\n4. Gypsy Dining Hall in First Floor, 689, 9th C Road, Sardarpura, Bhagat Ki Kothi, Jodhpur has been rated 4.5\n\n5. Mauryan in Below Talwarkar Gym, 11 B Road, Sardarpura, Bhagat Ki Kothi, Jodhpur has been rated 4.5\n\n6. New Raja Chicken Corner in H61, Near Anand Cinema, Railway Station Road, Station Road, Jodhpur has been rated 4.3\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "samipshah.89@gmail.com"}
    - slot{"email": "samipshah.89@gmail.com"}
    - email_check
    - slot{"email": "samipshah.89@gmail.com"}
    - send_email
    - slot{"email": "samipshah.89@gmail.com"}
    - utter_goodbye

## Generated Story 11_30062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "pune"}
    - slot{"cuisine": "American"}
    - slot{"location": "pune"}
    - city_check
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search
    - utter_ask_budget
* restaurant_search
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Level 5 Bistro and Bar in Survey 1365, 5th Floor, House of Nosh, Above Kalinga Veg Gourmet Kitchen, Opposite Mehendale Garage, Gulawani Maharaj Path, Erandwane, Pune has been rated 4.9\n\n2. Agent Jack's in West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune has been rated 4.9\n\n3. AB's - Absolute Barbecues in Shop 206, 2nd Floor, White Square Building, Opposite Atlanta Complex, Hinjawadi, Pune has been rated 4.8\n\n4. Le Plaisir in Survey 759/125, Rajkamal, Opposite Kelkar Eye Hospital, Prabhat Road, Deccan Gymkhana, Pune has been rated 4.8\n\n5. Sentosa MultiCuisine Restaurant in Pune-Mumbai Expressway, Ravet, Pune has been rated 4.8\n\n6. Chili's American Grill & Bar in UG 49, Phoenix Market City, Nagar Road, Viman Nagar, Pune has been rated 4.8\n\n7. The Sassy Spoon in Lane 7, Sanskriti Lifestyle Complex, Koregaon Park, Pune has been rated 4.7\n\n8. The Urban Foundry in Shop 1, Balewadi High Street, Cummins India Office Campus, Baner-Balewadi Link Road, Baner, Pune has been rated 4.7\n\n9. BarBerry in 121/122, Rambaug Colony, Paud Road, Next Lane Of MIT Collage, Kothrud, Pune has been rated 4.7\n\n10. Pop Tate's in Shop T08, 3rd floor, Phoenix Market City Mall, Viman Nagar, Pune has been rated 4.7\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "yadav86mangesh@gmail.com"}
    - slot{"email": "yadav86mangesh@gmail.com"}
    - email_check
    - slot{"email": "yadav86mangesh@gmail.com"}
    - send_email
    - slot{"email": "yadav86mangesh@gmail.com"}
    - utter_goodbye

## Generated Story 12_30062019
* affirm
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "joghpur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "joghpur"}
    - city_check
    - slot{"location": ""}
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - city_check
    - slot{"location": ""}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - city_check
    - slot{"location": "kolkata"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Barbeque Nation in Second Floor, City Center Mall 2, Block C, Rajarhat, New Town, Kolkata has been rated 4.9\n\n2. Momo I Am in 36/F, Offbeat CCU, Topsia Road, Topsia, Kolkata has been rated 4.9\n\n3. Barbeque Nation in 1st Floor, 24, Park Center Building, Park Street Area, Kolkata has been rated 4.8\n\n4. Spice Kraft in 54/1/2A, Hazra Road, Ballygunge Phari, Near Hazra Law College, Ballygunge, Kolkata has been rated 4.8\n\n5. Momo I Am in RBD Cinema, 1st Floor, Sector 5, Salt Lake, Kolkata has been rated 4.7\n\n6. The Saffron Tree in 100, Raja Basanta Roy Road, Southern Avenue, Kolkata has been rated 4.7\n\n7. Barbeque Nation in K1, RDB Boulevard, Block EP & GP, Sector 5, Salt Lake has been rated 4.7\n\n8. Chili's Grill & Bar in 4th Floor, Quest Mall, 33, Syed Ali Amir Avenue, Ballygunge, Kolkata has been rated 4.7\n\n9. Kouzina Mining Co. in AD - 79, Sector 1, Salt Lake City, Kolkata has been rated 4.7\n\n10. Chili's Grill & Bar in Acropolis Mall, 1858, Rajdanga Main Road, Kasba, Kolkata has been rated 4.7\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "sumeetpanchal.21@gmail.com"}
    - slot{"email": "sumeetpanchal.21@gmail.com"}
    - email_check
    - slot{"email": "sumeetpanchal.21@gmail.com"}
    - send_email
    - slot{"email": "sumeetpanchal.21@gmail.com"}
    - utter_goodbye

## Generated Story 13_30062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - city_check
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "pritampatil.143@gmail.com"}
    - slot{"email": "pritampatil.143@gmail.com"}
    - email_check
    - slot{"email": "pritampatil.143@gmail.com"}
    - send_email
    - utter_goodbye

## Generated Story 14_30062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - city_check
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "above Rs 700"}
    - slot{"budget": "above Rs 700"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_restaurant
    - slot{"email_response": "1. AB's - Absolute Barbecues in Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad has been rated 4.9\n\n2. Con\u00e7u in Plot 738, Road 37, Jubilee Hills, Hyderabad has been rated 4.9\n\n3. Chili's American Grill & Bar in Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad has been rated 4.9\n\n4. The Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad has been rated 4.8\n\n5. Chili's American Grill & Bar in F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad has been rated 4.8\n\n6. AB's - Absolute Barbecues in 8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad has been rated 4.8\n\n7. B-Dubs in Plot 806, Axis Tower, Road Number 36, Jubilee Hills, Hyderabad has been rated 4.8\n\n8. Churrolto in Film Nagar Main Road, In Front Of Indian Oil, Film Nagar, Hyderabad has been rated 4.8\n\n9. AB's - Absolute Barbecues in Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad has been rated 4.7\n\n10. Zero40 Brewing in 271-A, Road 10, Jubilee Hills, Hyderabad has been rated 4.7\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar.mehta@bobfinancial.com"}
    - slot{"email": "amar.mehta@bobfinancial.com"}
    - email_check
    - slot{"email": "amar.mehta@bobfinancial.com"}
    - send_email
    - slot{"email": "amar.mehta@bobfinancial.com"}
    - utter_goodbye

## Generated Story 15_30062019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - city_check
    - slot{"location": "bhopal"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"email_response": "1. Kebabsville - Sayaji Hotel in A-3,Van Vihar Road, Prempura, TT Nagar, Bhopal has been rated 4.9\n\n2. The Public House Caf\u00e9 n Restaurant in Mahadev Complex, Lower Ground Floor, Shivaji Nagar Opposite Board Office, Maharana Pratap Nagar, Bhopal has been rated 4.7\n\n3. Under The Mango Tree - Jehan Numa Palace in Hotel Jehan Numa Palace, 157, Shymala Hills, TT Nagar, Bhopal has been rated 4.5\n\n4. Tilak's Chocolady Bakery & Restaurant in Plot 2, Trilochand Nagar, Near Bank Of Baroda, Gulmohar Colony, Bhopal has been rated 4.4\n\n5. Shahnama - Jehan Numa Palace in Hotel Jehan Numa Palace, 157, Shymala Hills, TT Nagar, Bhopal has been rated 4.4\n\n6. Sanchi - Sayaji Hotel in A-3,Van Vihar Road, Prempura, TT Nagar, Bhopal has been rated 4.4\n\n7. Under The Jamun Tree in Jehan Numa Retreat, Dr. Sallem Ali Road, Near Van Vihar, Maharana Pratap Nagar, Bhopal has been rated 4.4\n\n8. Bhopal Express in Opposite Doordarshan Premises, Lake View, Shamla Hills, TT Nagar, Bhopal has been rated 4.3\n\n9. Marbal Arch - Noor Us Sabah Palace in Hotel Noor Us Sabah Palace, VIP Road, Kohefiza, Bhopal has been rated 4.3\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search
    - email_check
    - slot{"email": ""}
    - utter_ask_email_id
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - utter_goodbye

## Generated Story 15_30062019
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - city_check
    - slot{"location": "nagpur"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "amar198@gmail.com"}
    - slot{"email": "amar198@gmail.com"}
    - email_check
    - slot{"email": "amar198@gmail.com"}
    - send_email
    - utter_goodbye

## Generated Story 16_30062019
* greet
    - utter_greet
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - city_check
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Plum By Bent Chair in The Walk, Worldmark 2, Aerocity, New Delhi has been rated 4.9\n\n2. Out Of The Box in 5, Khan Market, New Delhi has been rated 4.9\n\n3. Inferno Brewpub in Plot 6 & 7, Sector 29, Gurgaon has been rated 4.9\n\n4. Doodle's Garden in Plot 1, 2nd Floor, NWA Club Road, Punjabi Bagh, New Delhi\nNext to Nik Bakers has been rated 4.9\n\n5. Drunken Detective in 1st Floor, C Block, Indirapuram Habitat Center, Ahinsa Khand 1, Indirapuram, Ghaziabad has been rated 4.9\n\n6. Feel Alive in SCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon has been rated 4.8\n\n7. Friction The Drinkery in SCO 29, Sector 29, Gurgaon has been rated 4.8\n\n8. Lazeez Affaire in 6/48, Malcha Marg Market, Chanakyapuri, New Delhi has been rated 4.8\n\n9. CIA Call it Asiian in 13/14/15/16, Narmada Shopping Complex, Opposite Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi has been rated 4.8\n\n10. Fat Cat Bistro in C116, Ground Floor, Panchsheel Vihar, Khirki Main Road, Malviya Nagar, New Delhi has been rated 4.8\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "femi404@gmail.com"}
    - slot{"email": "femi404@gmail.com"}
    - email_check
    - slot{"email": "femi404@gmail.com"}
    - send_email
    - slot{"email": "femi404@gmail.com"}
    - utter_goodbye

## Generated Story 17_01072019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Asia Kitchen By Mainland China in City Point, Ground Floor, Dhole Patil Road, Pune has been rated 4.9\n\n2. Agent Jack's in West Block, Amanora Town Centre, Hadapsar Kharadi Bypass, Hadapsar, Pune has been rated 4.9\n\n3. Sentosa MultiCuisine Restaurant in Pune-Mumbai Expressway, Ravet, Pune has been rated 4.8\n\n4. Gong in Shop 22/23, Balewadi High Street, Cummins India Office Campus, Baner- Balewadi Link Road, Baner, Pune has been rated 4.8\n\n5. AB's - Absolute Barbecues in Shop 206, 2nd Floor, White Square Building, Opposite Atlanta Complex, Hinjawadi, Pune has been rated 4.8\n\n6. The Urban Foundry in Shop 1, Balewadi High Street, Cummins India Office Campus, Baner-Balewadi Link Road, Baner, Pune has been rated 4.7\n\n7. BarBerry in 121/122, Rambaug Colony, Paud Road, Next Lane Of MIT Collage, Kothrud, Pune has been rated 4.7\n\n8. Pop Tate's in Shop T08, 3rd floor, Phoenix Market City Mall, Viman Nagar, Pune has been rated 4.7\n\n9. AB's - Absolute Barbecues in Shop 10, 11 & 12, Mariplex Mall, Kalyani Nagar, Pune has been rated 4.7\n\n10. Royal China in Business Plaza Westin Hotel, KP Annexe, Mundhwa, Pune has been rated 4.7\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_goodbye

## Generated Story 18_01072019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - city_check
    - slot{"location": "indore"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Kebabsville - Sayaji Hotel in Sayaji Hotel, H-1, Scheme 54, Vijay Nagar, Indore has been rated 4.9\n\n2. Hobnob Gourmet Caf\u00e9bar in Infiniti Hotel, 1C/CA, Scheme 94, Vijay Nagar, Indore has been rated 4.7\n\n3. Tic Tac Toe in Plot 64-65, Floor 1, Girirag Grande, Scheme 54, Vijay Nagar, Indore has been rated 4.5\n\n4. Little Italy in 78/2nd, Brilliant Convention Centre, Near Lifecare Hospital, Vijay Nagar, Indore has been rated 4.5\n\n5. Taberna - The Cafe Bar in Scheme 94C, 18A, 1st Floor, Velocity Multiplex, Ring Road, Vijay Nagar, Indore has been rated 4.4\n\n6. Bollywood Theka in IC/CA Scheme 94, Infiniti Hotel, Vijay Nagar, Indore has been rated 4.4\n\n7. Opium Bar By The Roof in Infiniti Hotel, IC/CA Scheme 94, Vijay Nagar, Indore has been rated 4.4\n\n8. One Asia - Indore Marriott Hotel in H-2, Scheme 54, Meghdoot Garden, Vijay Nagar, Indore has been rated 4.4\n\n9. Patissez in Flat 2, Plot - 306A, Scheme 54, PU-4, AB Road, Vijay Nagar, Indore has been rated 4.3\n\n10. Mr. Beans in 100, Saket, Old Palasia, Indore has been rated 4.3\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_goodbye

## Generated Story 19_01072019
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - city_check
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"location": "italian"}
    - slot{"location": "italian"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - city_check
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"email_response": "1. Bayroute in 1, Ground Floor, Transocean House, Lake Blve Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9\n\n2. Loco Loca in The Empresa Hotel, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai has been rated 4.9\n\n3. Knotty Yard in 1st Floor, Above China Valley, Opposite Powai Hiranandani Bus Depot, Powai, Mumbai has been rated 4.9\n\n4. White Charcoal - The Empresa Hotel in The Empresa Hotel, Oberoi Complex, Off New Link Road, Andheri Lokhandwala, Andheri West has been rated 4.9\n\n5. Rocky Star Cocktail Bar in Third Floor, Trade View Building, Kamala Mills Compound, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.9\n\n6. On Toes in 1st Floor, New Chandra CHS, Above Skoda Showroom, Veera Desai Area, Mumbai has been rated 4.9\n\n7. Tamasha in Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai has been rated 4.8\n\n8. Hitchki in 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai has been rated 4.8\n\n9. Hitchki in 5, Transocean, Hiranandani Business Park, Lake Boulevard Road, Powai, Mumbai has been rated 4.8\n\n10. HITCHKI in Ground Floor, Viviana Mall, Eastern Express Highway, Near Jupiter Hospital, Majiwada, Thane West has been rated 4.8\n\n"}
    - utter_if_details_required_in_email
* affirm
    - utter_goodbye

