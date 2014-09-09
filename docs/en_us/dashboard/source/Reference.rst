.. _Reference:

#######################
Computation Reference
#######################

This chapter provides detailed information about how the values presented by edX Insights are computed. It contains sections for:

* :ref:`All Computations`

* :ref:`Enrollment Computations`

* :ref:`Engagement Computations`

.. _All Computations:

*********************************
All Computations
*********************************

* The data reported by EdX Insights is updated once a week, typically on
  Mondays.

* Computations are made each week through Sunday at 23:59:59 UTC (11:59 pm). 

* Changes over a one week period are computed from Monday at 00:00:00 UTC
  through Sunday at 23:59:59 UTC.

  For example, the one week change in enrollment reports the difference between
  the enrollment total at the beginning of the week on Monday to the total at
  the end of the week on Sunday.

* Computations for edX Insights and for the Instructor Dashboard take place at
  different times. As a result, they may not match exactly.

.. _Enrollment Computations:

*********************************
Enrollment Computations
*********************************

EdX changed the method used to track student enrollments on 3 December 2013. As
a result, enrollment activity data is not computed for courses created in
Studio before 4 December 2013. (Enrollment geography data is available for
those courses.)

**Current Enrollment count**

* Users are included as of the date and time they enroll in a course. 

* All users who are enrolled in the course are included. This means that in
  addition to students, all staff members and beta testers with privileged
  roles in the course are included.

* Users who do not activate their accounts at registration are included. 

* Users who unenroll are excluded from the count as of the date and time they
  unenroll.
    
* Course staff can enroll students from the **Membership** tab in the
  Instructor Dashboard by supplying a list of email addresses or usernames.
  Actual enrollments can occur on different dates, as follows.

 * When **Auto Enroll** is cleared, each student identified by email address or
   username must manually complete the enrollment process for the course. Users
   are included as of the date and time they enroll.

 * When **Auto Enroll** is selected, each student who already has a registered
   user account with one of the supplied email addresses or usernames is
   included as of the date and time the staff member clicks **Enroll**.

   Each student who registers a user account with one of the batch enrolled
   email addresses or usernames is included as of the date and time the user
   account is registered.

**Enrollment Activity graph** or is it Daily Student Enrollment?
  
* Each marker on the graph represents the number of users enrolled in the
  course each day.

* The x-axis shows the period from course creation through the end of the last
  computation period.

* The y-axis shows the total number of enrolled users.

**Geographic Distribution map**
&&&%%%%%%%%%%%ahhhhhha!!!!%%%%

* The IP address saved with the last event that a user o determine the location of each user, the 
  
  When users interact with course content, events User location is determined from the most recently emitted event IP address trawling through the activity logs for every event
for every user and geolocate the  -- last known location regardless
of course!!! 

Geolocation numbers and enrollment numbers are not going to match up as they are NOT computed in the same way.



Location is determined from user IP addresses. Each time a user interacts with a course, the IP address is logged (with other identifying information) in a log of tracking  each time a user interacts with any course. he most recently recorded tracking event 

an event is recorded in a tracking log. To determine location, the IP address  in the most recent event logged for each enrolled student is used. 

this is not over time

this is not 

expressed as a count and as a percentage of total enrollment.

Users with more than one activity on a given date, the IP address from the most recent one is used.

**Total Countries Represented**



**Most Prevalent Country** 

  
  The second and third most prevalent countries are determined in the same way.



.. _Engagement Computations:

*********************************
Engagement Computations
*********************************


Active Students Last Week

any event for the user in the course loading a page,show answer, reading dicussion forum, reading static pages, textbooks, 

attempted problem

clicking check on ANY capa problem ** 
(Alison - comment each one that Gabe determines to be a capa problem)
Create a subtask/story for Gabe in REview Documentation story

Watched a video: if they click the play on any video they are counted

**unique users across the date range per metric. Activity even once counts, and only counts once 









**Active Students Last Week count** 
  
  The total number of students who, at least once, visited a page in the
  course, played a video, contributed to a discussion topic, or clicked
  **Check** for a problem. 

  %%% what else? "other course activities" in B&R guide 

**Watched a Video Last Week count** 
  
  The total number of students who played at least one of the course videos.

**Tried a Problem Last Week count** 
  
* The total number of students who submitted an answer for at least one problem
  of these types:

Checkboxes (<choiceresponse>)
Dropdown (<optionresponse>)
Multiple choice (<multiplechoiceresponse>)
Numerical input (<numericalresponse>)
Text input (<stringresponse>)
Math expression input (<formularesponse>)



