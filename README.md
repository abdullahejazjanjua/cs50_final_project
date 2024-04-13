# Manga Finder

<div style="text-align:center;">
  <a href="https://www.youtube.com/watch?v=1FKR5jviN2E">
    <img src="https://img.youtube.com/vi/1FKR5jviN2E/0.jpg" alt="Video Thumbnail">
  </a>
</div>

## Project Overview

Manga Finder is a web application designed to simplify the process of finding manga titles based on user preferences. The idea stemmed from a personal need to easily discover and explore new manga series. Leveraging concepts learned from the CS50 course, I embarked on creating a user-friendly platform that would allow manga enthusiasts to search for mangas by either specific names or if not sure what to read they can visit the top mangas section. This project utilizes flask for backend and bootstrap to create an imersive user interface.

## Files and Functionality

1. *app.py*
   - Serves as the main application file, responsible for handling routes and interactions between the front-end and back-end.
   - Implements Flask framework for web development.
   - Includes routes for search functionality, genre-based search, and managing user manga lists and displaying top mangas.

2. *templates/*
   - Contains HTML templates rendered by Flask to create the user interface.
   - Utilizes Bootstrap for responsive design and components such as carousels, cards, and forms.
   - Includes pages like layout.html, which serves as a template for the rest of the pages, index.html, for the main search functionality, genre.html for genre-based search later renamed to top.html for displaying current top mangas, info.html for displaying manga details and finally, apology.html for display an error code.

3. *static/*
   - Holds static files such as CSS stylesheets, and log.jpg, which I designed for the web app.
   - This enhances the visual appeal and interactivity of the web application.

4. *data/*
   - Initially planned to hold CSV files or database-related files, decided to switch to web scrapping but stopped due to lack of a web site that met my needs. Ultimately, I decided to adopt the use of APIs for data retrieval.

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
To enhance user interaction, I incorporated features such as hover effects on manga cards for scaling and a remove/add button on user-added manga cards. These additions improve usability and provide users with control over their manga lists.

## Challenges Faced

The development of Manga Finder was not without its challenges. One significant hurdle was the initial struggle to find a suitable database solution. CSV to DB conversion issues and incomplete datasets led to exploration of alternatives, ultimately resulting in API integration for real-time data retrieval.

Another challenge emerged during front-end development. While Bootstrap provided a robust framework for UI design, integrating complex components like carousels and interactive cards required a deeper understanding of the Bootstrap documentation and CSS customization. After perseverance and I developed my understanding of bootstrap by reading the official bootstrap document and watching videos on youtube.

The decision to consolidate genre-based search and general search into a single interface also posed challenges in terms of maintaining a streamlined user experience while accommodating diverse search criteria. At the end, I decided to just implement a top mangas page due to lack of a genre keyword in the database.

## Conclusion

Manga Finder represents a journey of learning, problem-solving, and creativity in web application development. By addressing challenges, making strategic design choices, and incorporating user feedback, the project evolved into a functional and promising tool for manga enthusiasts. The README.md provides a comprehensive overview of the project's structure, functionalities, design decisions, challenges faced, showcasing the dedication and effort put into creating a valuable resource for manga lovers.

## Acknowledgement

I would like to thank David J Malan and the staff at harvard for creating this course and meticulously explaining every little concept with such care. Moreover, I would like to thank the CS50 community for help anytime I needed. The most important figure I would like to thank is my brother for putting up with my relentless questions.

THIS WAS CS50.
