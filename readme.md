# Atlantis Assement
![](https://lh6.googleusercontent.com/fIhKFM-JgUZhho7Q1Uv0K0Q8eRVt511ho1r6FEsW5a9-p6_PT0k9ykckm3mFwnLvFrz_Ag6uuKtG0-ypODi4bb5EgBIyAIzrwVNdXgA5JkwZxdzQZmtdMwlOrw-emObWd0zd3K77)


This is a solution repository for my Assement given by Atlantis. 
 
To run this project it is advisabe to make a python virtualenvironment.

Run this command to install the dependencies in the virtual env
```shell
pip3 install -r requirements.txt
```

Problems are

![](RackMultipart20211129-4-1syf0x3_html_1054476c8510db34.png)

**Backend/Python Coding round**

**Assignment 1:**
Write a python program to scrape the list of links available in this Github repository ([https://github.com/vinta/awesome-python](https://github.com/vinta/awesome-python)) and search them by exact name from the console. Search result should return the github url of the result repository.

Expected output:

```
$ python search\_repos.py
 > Query? graphene
 > Output: [https://github.com/graphql-python/graphene/](https://github.com/graphql-python/graphene/)

```
The list should be scraped and kept in a runtime variable as soon as the program is initialized.. Handle the error with a suitable error message in case the exact name is not matched from the list.

**Assignment 2:**

Write a python program to list all pronunciable substrings of a given string. A string is said to be pronunciable if it has at least one vowel (a, e, i, o, u) after at-most 2 consonants (letters except a, e, i, o, u). [Example - &quot;zay&quot; is pronunciable but &quot;zby&quot; is not).

Expected output:
```
$ python pronunciable.py
 > Word? \&lt;user inputs the word &quot;House&quot;>
 > Output: House: Ho, Hu, He, Hos, Hus Hose, Huse, (.. and so on).
```
**Assignment 3:**
Given the GPS coordinates of 4 arbitrary cities, A, B, C and D, find the shortest flight route between the 4 cities along the surface of the earth if your journey starts at A.

Expected output:
```
$ python city\_distance.py
 > City A: 51.5074 N, 0.1278 W
 > City B: 60.8566 N, 2.3522 E

> City C: 55.2311 N, 2.1222 E

> City D: 64.0010 N, 0.1002 W
 > Output: A to C to B to D
```
**Assignment 4:**
Write a python program to scrape a given wikipedia page and return the average of 3 letter, 4 letter and 5 letter words per paragraph.

**Expected output:**
```
$ python wikipedia.py
 > Enter wikipedia page?

> [https://en.wikipedia.org/wiki/Earth](https://en.wikipedia.org/wiki/Earth)

> Output: 3-letter words: 10/paragraph. 4-letter words: 20/paragraph. 5-letter words: 45/paragraph.
```
**Assignment 5:**
A building has 20 floors and 5 lifts. Each floor of the building has a lift lobby. A user can be on any of the 20 floors and can request a lift. The positions of the lifts are denoted by a 5-length array of random numbers representing the current floor position (and direction of) of each lift. If no direction is given, it means that the lift is sitting idle on that floor. Example:

lift\_position = [0, 1D, 12, 4U, 19D]

Write a python program to allot to most efficiently lift to a user who requests it from any floor with intention of going up or down. On running the program the lift position should be randomly initialized.

A user can request for a lift in the following format: \&lt;lift position> \&lt;going up or down>
 Such as 5U or 10D.

**Expected output:**
```
$ python lifts.py
 > Enter a request? 5U
 > Lift #4 will be coming up to receive you.
```
**Submission guidelines:**

1. Create a public GitHub repository and put your assignments there. Share the link of the assignment GitHub repos with us.
2. Please use the latest version of Python and include a requirements.txt for the packages used.
3. Place high emphasis on code quality, readability, employment of proper design patterns.
4. Please reach out in case of any difficulties or doubts.
5. Please include a README file in your repos with instructions on how to test your code.
6. The examples provided are illustrative of input and output format only and do not represent a real test case. Please do not test against them.