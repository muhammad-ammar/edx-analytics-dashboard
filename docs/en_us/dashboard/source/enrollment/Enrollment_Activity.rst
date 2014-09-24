.. _Enrollment_Activity:

#############################
Enrollment Activity
#############################

How many students are enrolled in my course? Enrollment activity data helps you
monitor how many people are enrolling in your course and how that number
changes over time. 

Enrollment activity data is updated every day to include changes in enrollment
through the end of the previous day (23:59 UTC).

.. note:: Enrollment activity data is not available for courses created in
 Studio before December 4, 2013.

********************************************
Gaining Insight into Course Enrollment
********************************************

EdX Insights delivers enrollment activity data in a chart, a set of metrics,
and a report that you can view or download. Descriptions follow; for detailed
information about the computations, see :ref:`Reference`.

======================================
Daily Student Enrollment Chart
======================================

Each marker on this chart represents the total number of enrolled learners on a
particular date. Moving your cursor over the chart shows a tool tip with the
enrollment count for each day.

The chart includes enrollment data for every day, beginning with the automated
enrollment of the course creator when the course was created in Studio. This
data is also available for review in tabular format and can be downloaded.

In this example, you see the enrollment climb fairly steadily over a period of
nearly six months. The markers begin with 2 "student" enrollments (almost
certainly the course creator and another staff member) on the day the course
was created in Studio. The course team might want to correlate the periods when
the enrollment rate increased with marketing efforts or automated enrollment
events to guage their effect. After the course start date, on September 1,
2014, enrollment increased to a high of 13,320, and then you can begin to see a
slight decline in the number of enrollees.

.. image:: ../images/enrollment_chart.png
 :alt: The Daily Student Enrollment chart for nearly six months. The periods
       when the rate of enrollment was greater are circled, and the tip for the
       course start date on September 1st is shown.

======================================
Enrollment Metric
======================================
  
This count reports the total number of students who enrolled in the course,
less any students who unenrolled.

======================================
Change in Last Week Metric
======================================
  
This metric reports the difference between the enrollment total at the
end of the day yesterday and at the end of the day seven days ago.

======================================
Enrollment Over Time Report 
======================================

The daily total enrollment count, through the date of the last update, is
available for review or download. Columns show each **Date** and its **Total
Enrollment**.

To download the Enrollment Over Time report in a comma-separated value file,
click **Download CSV**. The CSV file contains the following columns: 

* count
* course_id
* created (shows the date and time of the computation)
* date

See the :ref:`Reference` for a detailed description of how enrollment values
are determined.

.. info on why you might want to download, what to do with csv after

*******************************************************
Analytics in Action: Interpreting Changes in Enrollment
*******************************************************

===========================
The Colbert "Bump"
===========================

Enrollment for courses on the edX.org site opens several months before the
course start date. This strategy typically results in gradually increasing
enrollments over time, as site visitors find a course, sign up for it, and tell
their colleagues, friends, and family about it. This strategy also gives teams
the opportunity to watch for larger changes in enrollment, the temporary
"spikes" that can occur after particular events, such as marketing campaigns
for the course or for edX in general.

Such events can be expected or unexpected: teams for all edX courses saw
enrollments jump in the summer of 2013, after edX CEO Anant Agarwal was
interviewed on the July 24 edition of *The Colbert Report*, a satirical late-
night comedy show hosted by Stephen Colbert. 

.. what is the actionable insight for this story? It's so great, I'd like to use it, but is there a way to make it showcase a decision or change? Maybe use it to lead in to "the students you have aren't necessarily reflective of the students you *could* have"? (courtesy of John Hess)

===========================
Latecomers Welcome
===========================

After their course started, a team expected that enrollment would level off and
then begin a gradual decline. While they did see a decrease in the number of
enrollments each week, they also noticed that occasional small spikes in
enrollment continued to occur on certain days, even several weeks into the
course. To give these recently-enrolled students time to catch up, the team
chose to adjust the course to be more self-paced. They shifted due dates in
unreleased units later, and extended the end date to keep course content open
longer.
