# Manga Finder

## Project Overview

Manga Finder is a web application designed to simplify the process of finding manga titles based on user preferences. The idea stemmed from a personal need to easily discover and explore new manga series. Leveraging concepts learned from the CS50 course, I embarked on creating a user-friendly platform that would allow manga enthusiasts to search for titles by genre or specific keywords.

## Files and Functionality

1. *app.py*  
   - Serves as the main application file, responsible for handling routes and interactions between the front-end and back-end.
   - Implements Flask framework for web development.
   - Includes routes for search functionality, genre-based search, and managing user manga lists and displaying top mangas.

2. *templates/*  
   - Contains HTML templates rendered by Flask to create the user interface.
   - Utilizes Bootstrap for responsive design and components such as carousels, cards, and forms.
   - Includes pages like index.html for the main search functionality, genre.html for genre-based search later renamed to top.html, info.html for displaying manga details.

3. *static/*  
   - Holds static files such as CSS stylesheets, and images used in the front-end.
   - Enhances the visual appeal and interactivity of the web application.

4. *data/*  
   - Initially planned to hold CSV files or database-related files, decided to switch to web scrapping but stopped due to lack of a web site that met my needds. Ultimately not used due to the adoption of APIs for data retrieval.
 
## Design Choices and Challenges

### Database Selection
The initial challenge revolved around finding a suitable database to store manga information. After encountering difficulties with CSV to DB conversion and encountering incomplete datasets, I explored alternatives. Eventually, I settled on utilizing APIs for real-time data retrieval.

### API Integration
The decision to integrate APIs, specifically the Jikan API (an unofficial MyAnimeList API), proved to be a pivotal choice. It provided comprehensive manga data, including titles, synopses, genres, and cover images. This eliminated the need for manual data entry and ensured up-to-date information for users.

### Front-End Development
Bootstrap played a significant role in shaping the user interface of Manga Finder. Leveraging Bootstrap's components like carousels for manga showcases, cards for displaying manga details, and collapse elements for user manga lists, I created a visually appealing and intuitive user experience.

### Genre Search vs. Search
Initially, I planned separate pages for genre-based search and general search. However, upon implementation, I realized the similarities and opted to consolidate them into a single search interface. This decision simplified navigation and maintained consistency across the application.

### User Interaction
To enhance user interaction, I incorporated features such as hover effects on manga cards for scaling and a remove button on user-added manga cards. These additions improve usability and provide users with control over their manga lists.

## Challenges Faced

The development of Manga Finder was not without its challenges. One significant hurdle was the initial struggle to find a suitable database solution. CSV to DB conversion issues and incomplete datasets led to exploration of alternatives, ultimately resulting in API integration for real-time data retrieval.

Another challenge emerged during front-end development. While Bootstrap provided a robust framework for UI design, integrating complex components like carousels and interactive cards required a deeper understanding of the Bootstrap documentation and CSS customization.

The decision to consolidate genre-based search and general search into a single interface also posed challenges in terms of maintaining a streamlined user experience while accommodating diverse search criteria.

## Future Enhancements

Moving forward, several enhancements and features are planned for Manga Finder:
1. *User Accounts:* Implement user accounts and authentication to allow users to save preferences, bookmark manga titles, and receive personalized recommendations.
2. *Advanced Search Filters:* Introduce advanced search filters such as publication date, author, and popularity rankings to refine search results.
3. *Community Interaction:* Add features for users to rate and review manga titles, share recommendations, and participate in discussions.
4. *Mobile Optimization:* Optimize the web application for mobile devices to ensure a seamless user experience across different screen sizes.

## Conclusion

Manga Finder represents a journey of learning, problem-solving, and creativity in web application development. By addressing challenges, making strategic design choices, and incorporating user feedback, the project evolved into a functional and promising tool for manga enthusiasts. The README.md provides a comprehensive overview of the project's structure, functionalities, design decisions, challenges faced, and future plans, showcasing the dedication and effort put into creating a valuable resource for manga lovers.

##Acknowledgement

I would like to thank David J Malan and the staff at harvard for creating this course and meticulously explaining every little concept with such care. Moreover, I would like to thank the CS50 community for help anytime I needed. The most important figure I would like to thank is my brother for putting up with my relentless questions. 

THIS WAS CS50.
