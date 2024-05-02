We submitted the files in the Moodle (by Yakov Schory). 
In addition, we created the project on GitHub, where all the submission files 
and the code are present. 

The link to GitHub:

https://github.com/ys1proj/advancedTopicsSoftwareEngineer

This is the Drive link to the detailed Report file with all necessary screenshots 
and diagrams, as well the detailed explaination of what was done:

https://docs.google.com/document/d/1F4IxUCQAJ4e5dGSHa8PQMIwsOcfTt1mzVAYAW7mhSKA/edit?usp=sharing

Additionally, here is the link to the Google Drive with all relevant files 
for this exercise:

https://drive.google.com/drive/folders/15akilEF5qHkLfEr7UL4i7L6_6bHUcZtw


//-------------------------------------------------------------------------------------//
Part 1. Roundtrip Engineering :
Question A.


We compiled and ran the code of the project, reviewed it and its outputs. The code 
performs a number of tests under "MainTest.java" on the two House objects - 
prints details on the state of the 2 houses by 2 methods.

* The first test (consists of two checks) - Iterates over the half of the existing 
"Customers" and tests the possibility of renting the first of the two "House" objects.
																					
For each "customer" the test performs a check whether the house is rented or not. 
If it is rented, a message is printed stating the house cannot be rented + the name 
of the current tenant-client ("customer"). Otherwise, the system rents the "house" to the first 
possible "customer" and prints a notice accordingly along with the tenant's name.
The same check is performed for the second "home" object, but for the other half of 
all existing "customers".


* The second test - for each customer we check if he currently rents either one or 
both of the "house" objects. If the "customer" indeed rents a house, the lease on 
the house is terminated and the house's status remains as "rented" (due to incorrect 
code) and a notice is printed regarding the termination of the lease + 
the "customer"'s name. Otherwise, prints a message that the "house" 
was not rented to the currently iterated "customer" + their name.

________________
Question B.

By using the Visual Paradigm tool we reverse engineered the project to Class Diagram. 
(q1_B.png file in the Drive )
 https://drive.google.com/file/d/1gulByhvqcbnM-0ismcfZpmMpmjSY5sK8/view?usp=drive_link

________________
Question C.

New classes with the relevant fields:

Room Class
	roomNumber : int
	size: double
	pricePerNight : double
	isAvailable : boolean
	houseID : int
	renter: Customer

For a different type of room (single, couple, family)
<Enum> RoomType:
	single
	duo
	family

Changes in the House Class:

- we added fields
  
	houseID: int
	rooms : Arraylist<Room>

- changed the field name:
rooms → numOfRooms: int

We added another enum of room type - freerooms (the house has free rooms) 
in HouseStatus:
<Enum> HouseStatus:
	free
	rented
	freerooms

We also added the relevant connections between the new and old classes, which you
can see on the diagram Model1.vpp .

(q1_C_afterChanges.jpg is a screenshot of Model1.vpp, the link to it is below)
https://drive.google.com/file/d/1U2_QZB7G4G-j6ssV7VINahveBfu53in1/view?usp=drive_link
________________  
Question D.

We created the new code from the class diagram, after the changes we have made in the 
previous section by using Visual Paradigm. The code is saved in the Code1.zip folder.

We checked this new code and made sure that all the classes are updated according 
to the changes we have performed early in the section C.
________________
Question E.

We used a reverse-engineering technique in Visual Paradigm, and received new Class 
Diagram Model2.vpp from the code which was generated in the section D (Code1.zip).

We checked the diagram,  all the new and updated classes, relationships appear as 
they should. This Class Diagram is the same as what we have got in section C as 
expected. The minor changes occured in the way the diagram was display, however, 
they don't matter logic wise (visual only) or change architecture in any way.

The screenshot of the Model2.vpp is located in the Drive and called 
q1_E_diagramFromGeneratedCode.jpg, the link is:
https://drive.google.com/file/d/1t5-lxiTZ-IQF3VnAT1QzZwLJqePbkDnR/view?usp=drive_link

//--------------------------------------------------------------------------//

Part 2.  Software Reuse:
Question A.

We decided to design a UI that allows the user to convert the price of the room 
to the currency he prefers (for example, weights to dollars). 

In addition we also used the CityLodgeUI interface which returns a rental date 
for houses and rooms.

________________
Question B.

At first, we ran a few queries and received multiple results that were not as 
we expected. Almost all of the results had some kind of problems and were not good 
enogh for our requirements and did not stand to the criteria( many of the GitHub 
projects do not have ReadMe files or any kind of explanation about the code and how 
it works). The commits, issues, forks, comments were lacking as many of projects 
were uploaded all at once. Also, often there was heavy use of external complicated 
libraries, API's and FrameWorks which we are not familiar with and require time 
and skill effort.

We ran two queries - a query for a currency exchange calculator interface 
- The query: "simple application convert currency java gui" and a query for a room 
rental interface 
- The query: "java room rental gui" as well as: "java simple swing gui".

We chose to display the result by "best match". The queries we ran on Github to get 
the desired products.
			

The results obtained by running the queries could be seen in the Report in the Drive
(the link is provided at the beginning and also below)
https://docs.google.com/document/d/1F4IxUCQAJ4e5dGSHa8PQMIwsOcfTt1mzVAYAW7mhSKA/edit?usp=sharing																						
  ________________
Question C. 

The products we chose:
1. Calculator - we chose this product from the three options we received.
We based our selection on two criteria:
Visibility criterion - this product is the only product for which there is a 
demonstration of what the component looks like so that we can get an impression 
of the visibility and decide whether the component is suitable for us.
The code criterion - in terms of our ability to understand the implementation of the 
code, this option was ideal.

2. General GUI - the second product we chose was the only one received. 
We tried other results, but they were not good enough (most were without visual 
interfaces and those that were were for unsuitable software)

3. Room rental interface - The third product we chose was for room rental in a more specific manner. 
We found a UI interface used for creating a simple phone book and converted it into an interface 
that allows room rentals. This interface was convenient and visually easy 
to understand for user and for our purposes. We looked for an interface that capable 
of displaying multiple screens simultaneously. From the results we received, we saw 
that it has:
4-star - meaning there are at least four people who found the code useful 
and saved it as a favorite.
8-fork - there are at least eight people who found interest in the code and 
decided to continue developing it in their own version.
2 participants (watch) - meaning at least two people chose to follow the code's 
progress.
Meaning it met our criteria requirements.
______________

Question D.

We will integrate the products into the improved project.

We were required to adapt the code to our project, add files to the package 
in our project, add lines of code to existing code, and also change the code of 
the product according to the needs of our project. 

We had to change the types of foreign currencies and their exchange rates. We changed 
the foreign currencies to CAD, AUD, USD Dollar, ILS. Also, we changed the rate for 
each of them according to what is correct today.

We continued to add screens in this style (reusing the same UI vehicles), which match 
the functionality of the existing code. 

For the Room Rental Screen we changed the components in a way to match
the phonebook's user interface we chose. The UI was built in order to make the interface accessible to the user.

All the screens (screenshots) can be seen in the Report in the Drive:
https://docs.google.com/document/d/1F4IxUCQAJ4e5dGSHa8PQMIwsOcfTt1mzVAYAW7mhSKA/edit?usp=sharing

