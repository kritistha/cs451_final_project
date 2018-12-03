# CS451 - Final Project

## Overview
For the final project you and a partner (triads are ok if necessary) will build a django web application. The direction of the project is completely up to you but must have the indicated components.

## Project Description
The Computer Science department would like a web application that allows students to search for a listing of jobs that are within 100 miles from NMHU.  For example, a user can see a listing of all jobs in the db within a 100 mile radius of NMHU. The application should show the listing of jobs and a marker on a map. A job is described as having a title, a salary, and location (latitude, longitude). The application should have a menu containing: a) access to all the jobs in the db as a list, b) acceess to a page containing a subset of jobs, c) the homepage. 


## Tasks Overview

1. Fork this project to one  member's github account. Add collaborators to the project.

2. Develop requirements and design pages.

3. Initialize the project tab to begin assigning tasks (issues) to the Kanban board

4. Begin implementation and update issues as needed.

5. Test (see [django unit testing](https://docs.djangoproject.com/en/2.1/topics/testing/overview/)) to test model

6. Deploy

## Project Components

* Must use Django v.2 web application framework, Bootstrap css framework, and javascript (for map display see [Leaflet](https://leafletjs.com/)

* Must use a github repository

* Github repo must include:

    - wiki page containing a) requirements listing using FURPS b) use cases, and c) class diagram 

    - identified tasks (issues) for each member of team

    - a Kanban board (github project tab) that organizes the tasks assigned to each member

* Source code must have:
    - source code (obvious)

    - pinned package requirements.txt file in root.



## Third party libraries

- geopy for calculating distances
