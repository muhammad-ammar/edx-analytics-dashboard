.. _Reference:

#######################
Computation Reference
#######################

This chapter provides detailed information about how values presented by
edX Insights are computed. It contains sections for:

* :ref:`All Computations`

* :ref:`Enrollment Computations`

* :ref:`Location Computations`

* :ref:`Engagement Computations`

.. _All Computations:

*********************************
All Computations
*********************************

* The data reported by EdX Insights is updated once a week, typically on
  Mondays.

* Computations are made on data collected through Sunday at 23:59:59 UTC (11:59
  pm).

* Changes over a one week period are computed for "an ISO week", from the
  period Monday at 00:00:00 UTC through Sunday at 23:59:59 UTC.

  Each complete week, from the beginning of the week on Monday to the end of
  the week on Sunday, is an update period for edX Insights.

* Computations for edX Insights and for the Instructor Dashboard take place at
  different times. As a result, differences can occur.

.. _Enrollment Computations:

*********************************
Enrollment Computations
*********************************

EdX changed the method used to track student enrollments on 3 December 2013. As
a result, enrollment activity data is not computed for courses created in
Studio prior to 4 December 2013. However, geographic data relating to
enrollment is available for those courses.

**Current Enrollment count**

* All users who are enrolled in the course are included. This means that in
  addition to students, all staff members and beta testers with privileged
  roles in the course are included.

* Users are included as of the date and time they enroll in a course. 

* Users who do not activate their accounts at registration are included. 

* Users who unenroll are excluded from the count as of the date and time they
  unenroll.
    
* Course staff can enroll students from the **Membership** page in the
  Instructor Dashboard by supplying a list of email addresses or usernames.
  Actual resulting enrollments can occur on different dates, as follows.

 * When **Auto Enroll** is cleared, each student identified by email address or
   username must manually complete the enrollment process for the course. Users
   are included as of the date and time they enroll.

 * When **Auto Enroll** is selected, each student with a user account
   corresponding to a supplied email address or username is enrolled in the
   course and included in the count as of the date and time the initiating
   staff member clicks **Enroll**.

   Students who register a user account with one of the batch enrolled email
   addresses or usernames after batch enrollment is initiated are  included as
   of the date and time that they register their user accounts.

**Enrollment Activity graph**
  
* Each marker on the graph represents the number of users enrolled in the
  course each day.

* The x-axis shows the period from course creation through the end of the last
  computation period.

* The y-axis shows the total number of enrolled users.

.. _Location Computations:

*********************************
Location Computations
*********************************

**Geographic Distribution map**

* User location is determined from the IP address used during interactions with
  course content.

* The last known location of each user, as of the end of the update period
  (Sunday at 23:59:59 UTC), is used.

* User location is determined without regard to a specific course. Users who
  are enrolled in more than one course are identified as being in the same
  location for all of their courses.

* User location is reported by country. Users with IP addresses that are identifed as bein in non-country A country cannot be determined for every IP address. Users who are 

* The number of users from each country is expressed as a count and as a
  percentage of the total number of users from all countries.

* The approaches used for determining user location and user enrollment status
  are different. As a result, discrepancies can be noted when a direct
  comparison of enrollment activity to enrollment geography is made.

**Total Countries Represented**

The sum of the unique country codes identified from user IP addresses. 

**Most Prevalent Country** 

The country in which the largest number of users is located. The countries in
which the second and third largest number of users are located are identified
as well.

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
  
The number of students who visited a course URL in the
  course at least once during the last complete update period.

  , played a video, contributed to a discussion topic, or clicked
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

.. Gabe believes that there may actually be a few more. 

