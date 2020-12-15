# LCA Theatre using django/python back-end and mysql database
## A django web application which allows users to register, login, purchase, and view movies added by admin.
This project was completed by me as part of a self-initiated assignment.<br>
MySQL database is used rather than already available SQLite to gain more knowledge and to handle more data.

## Problem Statement:
### Admin Tasks:
<ol>
  <li>Admin can add or update movies and thumbnails to be listed in `All Movies` tab</li>
  <li>Admin can edit spare coins(which are transation medium for this website) for any user.</li>
  <li>Admin can assign movies to particular users using admin page.</li>
</ol>

### User Tasks:
<ol>
  <li>New user can register himself/herself on the website.</li>
  <li>Login using username and password.</li>
  <li>Buy and watch movies using spare coins.</li>
</ol>

### Additional Activities:
- After registration of new user, 20 spare coins are added to his/her account.
- There is no feature to buy more spare coins by user as of now(can be added later!).

## Technologies used:<br>
- Python
- Django
- Javascript
- Bootstrap
- CSS
- HTML
- MySQL Database

## Note:

<b>Only one video is uploaded in `media` folder.<br> 
One can add more videos using the custom django admin page by creating a super-user or using:<br>
`Username: admin`<br>
`Password: admin`</b>

## Usage:

    python manage.py makemigrations

    python manage.py migrate

    python manage.py runserver
    
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/

## Working:
Watch YouTube working video <a href="https://www.youtube.com/watch?v=Lsh8XKdAk3o">here</a> or click below:<br><br>
[![Watch the video](http://img.youtube.com/vi/Lsh8XKdAk3o/0.jpg)](https://www.youtube.com/watch?v=Lsh8XKdAk3o)

## Screenshots : 

