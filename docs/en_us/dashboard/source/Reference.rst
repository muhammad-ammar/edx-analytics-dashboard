.. _Reference:

#######################
Computation Reference
#######################



* The data that is reported by EdX Insights is updated once a week. 

* Computations are made through %%day of week, 23:59 UTC (11:59 pm). 

* Changes over time are computed from %%day of week, 00:00 UTC thorugh %%day of
  week, 23:59 UTC. For example, the change in enrollment for a one week period
  reports the difference between the enrollment total on %% day to the total on
  %%day.

* Computations for data reported by edX Insights and on the Instructor
  Dashboard for a live course take place at different times, and as a result
  may not match exactly.

*********************************
Enrollment Computations
*********************************

**Current Enrollment count**

* Users are included as of the date and time they enroll in a course. 

* All users who are enrolled in the course are included. This means that in
    addition to students, all staff members and beta testers with privileged
    roles in the course are included.
    
* Users who do not activate their accounts at registration are included. 

* Users who unenroll from the course are not included in the count. (%%not clear
  enough yet -- counted as enrolled until thaty unenroll, not retroactively
  unenrolled)
    
* Students who are bulk / automatically enrolled on the Instructor Dashboard are enrolled based on the check box --> immediately or after reacting to email

* before 12/3/2013, enrollment was not tracked rigorously and was garbage
     for a course that had enrollments that traverse 12/3/2013, so we don't show a graph at all for such courses (we will at some poin tin the future back track to figure out how many were enrolled as of 12/3, but not for MVP)
     geolocation data will be there, rest will not


**Enrollment Activity graph** or Daily Student Enrollment?
  
  * Each marker on the graph represents the number of registered users enrolled
    in the course as of 23:59 UTC each day.

  * The x-axis shows the time period from the course creation date until the
    date of the last computation update.

  * The y-axis shows the number of enrollees.
  
**Enrollment Breakdown report**
  
  * Columns for Date and Total Enrollment

  downloadable report should have the data that is graphed (daily)

**Enrollments This Week delta**

  * Compares the enrollment at the start of the last complete 7 day period to
    the end of that period.

**Geographic Distribution map**

  , expressed as a percentage of total enrollment. 

  Student geographic location is determined by the IP address used when they registered a user account on the site. 



Geolocation is computed by trawling through the activity logs for every event
for every user and geolocate the IP address -- last known location regardless
of course!!! 

Geolocation numbers and enrollment numbers are not going to match up as they are NOT computed in the same way.


**Total Countries Represented**



**Most Prevalent Country** 

  
  The second and third most prevalent countries are determined in the same way.





*********************************
Engagement Computations
*********************************



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



