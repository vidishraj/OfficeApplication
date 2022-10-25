# OfficeApplication
Application made as a reference for topics like OOPs, GUI programming, Session Management, Exception handling, Logging and Code organisation,

**About**: The application mimics a mini office management application with 4 key components. 

Offices </br>
Offices have the following properties-: Name, Location, Type, Number of employee and Expenses. They can be of 2 types-: International/Local. An International Office has an expense limit of 200000 and a local offices has a limit of 100000. 
User should be allowed to add an office, list all the offices and add an expense to a certain existing office. No office can exceed the limit set for its type.

Employees</br>
Employees have the following properties-: Name, Age, Salary, Working Hours, Date of Joining, Manager and Type. There are 5 types of employees that the user should be allowed to create, which are Maid, Software Engineer, Manager, Architect and IT Staff. All have unique salaries and working hours(pre-configured). 
The user should be allowed to set the manager for an employee, change the salary and working hours and have an option for listing the employees as well.

Customers</br>
Customers have the following properties-: Name, Age, Aadhar number, Type and account. Customers can be of 2 types, retail and non-retail.
The user should be allowed to create a customer and list all the customers.

Accounts</br>
Accounts have the following properties-: Account Number, Deposit, Initial Deposit and type. Accounts can be of 3 types, Checkings, Savings and Loan. Non-retails customers are allowed to open only loan accounts. The user should be allowed to open an account for an existing customer based on the type. There are different rates of interests which should be calculated on a weekly basis for the accounts. Savings accounts have an interest rate of 8%, checking 5% and Loan has an imposed interest of 9%. The user should be allowed to view all the accounts as well. 


**GUI Programming**</br>
</br>
CustomTkinter has been used as the main library for the GUI in the project. It is an extension of Tkinter. There are in total 11 unique pages that were created to implement all the features mentioned above. The goal was to familiarize myself with as many components that tkinter can offer. The project uses various components like frames, icons, toplevels, labels, tkcalendar, buttons, drop-down menus, etc. 

**Session Management**</br>
</br>
The application is a single session application but it allowes data persistence by registering new users and the saving their data in a json file. The users data is serialized internally and then saved in the json file. When the user logins again, the data is loaded back from the same file. This has been done to mimic real world applications saving user data in large databases and then similarily fetching it using REST API's/ Message brokers. </br>

**OOPs**</br>
</br>
The application should uses all the for aspects of OOPs.</br>
i) Classes have been used to define all the components (abstraction).</br>
ii) Inheritence is used for implementing various subtypes.</br>
iii) Access modifiers have been used to mimic encapsulation.</br>
iv) Overriding and overloading has been used in some places as well.</br>
</br>
**Logging and Exception Handling**</br>
</br>
The goal of exception handling is to ensure that our application does not crash under any circumstances, give user messages informing him of the errors or give confirmation on completion of processes. Pop Ups were encorporated to inform the user of the errors and confirmations. Logging was done for every useful step to ensure easy debugging.</br>
</br>
**Code Organisation**</br>
</br>
The project has been coded to minimize duplication, prettified and broken into packages for the GUI components, Services, Classes, PopUps and Logs. Even though it can be further divided, the current organisation is preferred. Other best practices have been followed as well.

**How to start**</br>
</br>
i) Clone the master branch.</br>
ii) Run main.py file.</br>
</br>
**Further Development**
</br>
Encorporate a configuration page for the user to change passwords, add new types of customers/employees, delete data and so on.
</br>
