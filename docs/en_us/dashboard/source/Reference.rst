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
  
* :ref:`Error Conditions`

.. _All Computations:

*********************************
All Computations
*********************************

* Computations for the different metrics reported by edX Insights take place at
  different times. In addition, computations for reports and metrics that are
  available from the Instructor Dashboard of a course, take place on a
  different schedule. As a result, differences can occur.

.. Jennifer asks for an x-ref to more information. Pending some work with Victor to figure out the update schedule for Insights.

* All users who are enrolled in a course are included in the computations.
  This means that in addition to students, all staff members and beta testers
  with privileged roles in the course are included.

* A user who registers an account and enrolls in a course, but does not
  activate the user accounts, is included in all computations as of the date
  and time of enrollment.

.. _Enrollment Computations:

*********************************
Enrollment Computations
*********************************

The number of enrolled students is computed every day, and the values reported
on the Enrollment Activity page in edX Insights are updated every day.

.. important:: EdX changed the method used to track student enrollments on 
 3 December 2013. As a result, enrollment activity data is not computed for
 courses created in Studio prior to 4 December 2013. However, geographic data
 relating to enrollment is available for those courses.

For information about viewing enrollment activity data in edX Insights, see
:ref:`Enrollment_Activity`.

**Enrollment count**

* Users are included in the count as of the date and time they enroll in a
  course.

* Users who unenroll are excluded from the count as of the date and time they
  unenroll.

* Course staff can enroll students from the **Membership** page in the
  Instructor Dashboard by supplying a list of email addresses or usernames.
  Actual resulting enrollments can occur on different dates, as follows.

 * When the **Auto Enroll** option is cleared, each student identified by email
   address or username must manually complete the enrollment process for the
   course. Users are included as of the date and time they enroll.

 * When **Auto Enroll** is selected, each student with a user account
   corresponding to one of the supplied email addresses or usernames is
   enrolled in the course and included in the count as of the date and time the
   initiating staff member clicks **Enroll**.

   Students who are autoenrolled in a course but have not yet registered a user
   account are included as of the date and time that they do register their
   user accounts.

**Enrollment Activity graph**
  
* The markers on the graph represent the number of users enrolled in the
  course each day.

* The x-axis shows the last 60 days. 

* The y-axis shows the total number of enrolled users.

.. _Location Computations:

*********************************
Location Computations
*********************************

* The geographic locations of students are updated every day.

* User location is determined from the IP address used during interactions with
  course content. An ISO 3166 country code is associated with each IP address. 

* The last known location of each user, as of the end of the update period, is
  used.

* User location is determined without regard to a specific course. Users who
  are enrolled in more than one course are identified as being in the same
  location for all of their courses.

For information about viewing geographic data in edX Insights, see
:ref:`Enrollment_Geography`.

**Geographic Distribution map**

* The number of users and the percentage of the total is provided for each
  country.

* Users with IP addresses that cannot be geolocated, or that result in a "non-
  country" code such as A1 (Anonymous Proxy), A2 (Satellite Provider), or O1
  (Other Country), are reported in the "Unknown" category.

* The computational approaches and frequency used in determining user
  location and user enrollment status are different. As a result, discrepancies
  can be noted when a direct comparison of enrollment activity to enrollment
  geography is made.

**Total Countries Represented**

* The sum of the unique country codes identified from user IP addresses. 

* This total does not include "non-country" ISO codes such as A1, A2, or O1.

**Top Country** 

The country in which the largest number of users is located. The countries in
which the second and third largest numbers of users are located are identified
as well.

.. _Engagement Computations:

*********************************
Engagement Computations
*********************************

* The computations for student engagement are updated once a week, typically on
  Mondays.

* Computations are made on data collected through Sunday at 23:59 UTC (11:59
  pm).

* Changes over a one week period are computed for the period Monday at 00:00:00
  UTC through Sunday at 23:59:59 UTC.

* Measures of student engagement with course content identify the number of
  unique users who completed an activity during a week.

* Each unique user who engages in one of the categories of activity increases
  the count for that category by 1. A student who completes 10 problems
  increases the count of students who tried a problem by 1. The same student
  also increases the overall count of active students by 1.

For information about viewing engagement metrics in edX Insights, see
:ref:`Engagement_Content`.

**Active Students Last Week count** 
  
* The number of unique users who visited any page in the course (a URL) at
  least once during the last update period.

  Some examples of the activities that a student can complete on a page, and
  that are included in this count, include contributing to a discussion topic,
  reading a textbook, submitting an answer to any type of problem, playing a
  video, and reviewing the course updates.

* This metric includes all course activities, excluding enrollment and
  unenrollment.  

**Watched a Video Last Week count** 
  
* The number of unique users who clicked play for at least one of the course
  videos. 

* Only videos played on the edX platform video player are included.

**Tried a Problem Last Week count** 
  
* The number of unique users who submitted an answer for at least one problem
  of these types:

  * Checkboxes (<choiceresponse>)
  * Dropdown (<optionresponse>)
  * Multiple choice (<multiplechoiceresponse>)
  * Numerical input (<numericalresponse>)
  * Text input (<stringresponse>)
  * Math expression input (<formularesponse>)

.. Gabe believes that there may actually be a few more. Subtask created.
.. TODO: when comlete list received, comment in doc for each problem type that Gabe determines to be a capa problem for future reference

.. **Enrollment Activity graph**
  
.. * The markers on the graph represent the number of users who interacted with different aspects of the course each week.

.. * The x-axis includes computations made from course creation through the end of the last update period.

.. * The y-axis shows the total number of unique users.

.. _Error Conditions:

*****************
Error Conditions
*****************

The data that edX collects from student interactions has expanded over time to
capture increasingly specific information, and continues to expand as we add
new features to the platform. As a result, data for every value reported by edX
Insights is not available for every course.

EdX changed the method used to track student enrollments on 3 December 2013. As
a result, enrollment activity data is not computed for courses created in
Studio prior to 4 December 2013. Other data is available for those courses.
