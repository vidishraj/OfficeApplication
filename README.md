# Office Application
A reference application for topics such as OOPs, GUI programming, Session Management, Exception handling, Logging, and Code Organization.

The application mimics a mini office management application with four key components.

Offices</br>
</br>
Offices have the following properties: name, location, type, number of employees, and expenses. They can be of 2 types: international or local. An international office has an expense limit of $2000 and a local office has a limit of $100000 per month. 
A user should be allowed to add an office, list all the offices, and add an expense to a certain existing office. No office can exceed the limit set for its type.

Employees</br>
</br>
Employees have the following properties: name, age, salary, working hours, date of joining, manager, and type. There are five types of employees that the user should be allowed to create, which are: maid, software engineer, manager, architect, and IT staff. All have unique salaries and working hours(pre-configured). 
The user should be able to set the manager for an employee, change the salary and working hours, and have an option to list the employees as well.

Customers</br>
</br>
Customers have the following properties: name, age, Aadhar number, type, and account. Customers can be of 2 types: retail and non-retail. 
The user should be able to create a customer and list all the customers.

Accounts</br> 
</br>
Accounts have the following properties: Account Number, Deposit, Initial Deposit, and type. Accounts are classified into three types: checking, savings, and loan.Non-retail customers are allowed to open only loan accounts. The user should be allowed to open an account for an existing customer based on the type. There are different rates of interest which should be calculated on a weekly basis for the accounts. Savings accounts have an interest rate of 8%, checking 5% and Loan has an imposed interest of 9%. The user should be allowed to view all the accounts as well.


**GUI Programming**</br>
</br>
CustomTkinter has been used as the main library for the GUI in the project. It is an extension of Tkinter. There are a total of 11 unique pages that were created to implement all the features mentioned above. The goal was to familiarise myself with as many components that Tkinter can offer. The project uses various components like frames, icons, toplevels, labels, TKcalendar, buttons, drop-down menus, etc.

**Session Management**</br>
</br>
The application is a single-session application but it allows data persistence by registering new users and saving their data in a json file. The users' data is serialised internally and then saved in the json file. When the user logins again, the data is loaded back from the same file. This was done to simulate real-world applications by saving user data in large databases and then retrieving it similarly using REST APIs and message brokers./br>

**OOPs**</br>
</br>
The application should use all the aspects of OOPs. </br> 
i) Classes have been used to define all the components (abstraction). </br> 
ii) Inheritance is used for implementing various subtypes. </br> 
iii) Access modifiers have been used to mimic encapsulation. </br> 
iv) Overriding and overloading have been used in some places as well. </br>
</br>
**Exception Handling and Logging** </br>
</br> 
The goal of exception handling is to ensure that our application does not crash under any circumstances, to notify the user of errors, and to confirm the completion of processes.Pop-Ups were incorporated to inform the user of the errors and confirmations. Logging was done for every useful step to ensure easy debugging. </br> 
</br> 
**Code Organisation**</br>
</br> 
The project has been coded to minimise duplication, prettified and broken into packages for the GUI components, Services, Classes, PopUps and Logs. Even though it can be further divided, the current organisation is preferred. Other best practises have been followed as well.

**How to Begin**</br>
</br> 
i) Create a clone of the master branch. </br> 
ii) Run the main.py file. </br>
</br>
**Further Development**
</br>
Encorporate a configuration page for the user to change passwords, add new types of customers or employees, delete data, and so on. 
</br>
