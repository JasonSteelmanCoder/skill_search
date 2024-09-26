import re

skills = """
Etl
	1 		Hard Skill 	
Agile
	1 		Hard Skill 	
Queries
	3 	1 	Hard Skill 	
Code
	1 	1 	Hard Skill 	
Python
	1 	4 	Hard Skill 	
Latency
	1 		Hard Skill 	
Testing
	2 	1 	Hard Skill 	
Database
	1 	4 	Hard Skill 	
Analytics
	1 	1 	Hard Skill 	
Test Cases
	1 		Hard Skill 	
Exhibit
	1 		Hard Skill 	
Indexes
	1 		Hard Skill 	
Cloud Based
	1 	1 	Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Engineer
	4 	3 	Hard Skill 	
Architect
	1 		Hard Skill 	
Data Quality
	3 		Hard Skill 	
Data Services
	1 		Hard Skill 	
Etl Pipelines
	1 		Hard Skill 	
Business Rules
	1 		Hard Skill 	
Data Pipelines
	1 	1 	Hard Skill 	
Data Ingestion
	1 		Hard Skill 	
Enterprise Data
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Data Engineering
	1 		Hard Skill 	
Machine Learning
	1 		Hard Skill 	
Agile Methodology
	1 		Hard Skill 	
Business Analytics
	1 		Hard Skill 	
Materialized Views
	1 		Hard Skill 	
Performance Tuning
	1 		Hard Skill 	
Technology Solutions
	1 		Hard Skill 	
Business Requirements
	1 		Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Software Development Lifecycle
	1 	Node
	1 	1 	Hard Skill 	
Ruby
	1 		Hard Skill 	
Mysql
	1 		Hard Skill 	
Code
	2 	2 	Hard Skill 	
Kibana
	1 		Hard Skill 	
Angular
	1 		Hard Skill 	
Graphql
	1 		Hard Skill 	
Node.Js
	1 	1 	Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Marketing
	1 	1 	Hard Skill 	
Waterfalls
	1 		Hard Skill 	
Full Stack
	2 	4 	Hard Skill 	
Typescript
	1 		Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Engineer
	1 	2 	Hard Skill 	
Ruby On Rails
	1 		Hard Skill 	
Elasticsearch
	1 		Hard Skill 	
User Experiences
	1 	1 	Hard Skill 	
Customer Feedback
	1 	1 	Hard Skill 	
Production Environment
	C#
	2 		Hard Skill 	
Apis
	1 	3 	Hard Skill 	
Git
	1 	2 	Hard Skill 	
Sql
	1 	2 	Hard Skill 	
.Net
	2 		Hard Skill 	
Java
	2 		Hard Skill 	
Agile
	2 		Hard Skill 	
React
	1 	1 	Hard Skill 	
Scrums
	1 		Hard Skill 	
Code
	1 	1 	Hard Skill 	
Docker
	1 		Hard Skill 	
Novice
	1 		Hard Skill 	
Sprint
	1 		Hard Skill 	
Testing
	2 	1 	Hard Skill 	
Databases
	1 	2 	Hard Skill 	
Restful Apis
	1 	1 	Hard Skill 	
Selenium
	1 		Hard Skill 	
Teamwork
	1 	1 	Hard Skill 	
Scripting
	1 	1 	Hard Skill 	
Terraform
	1 		Hard Skill 	
Web Based
	1 		Hard Skill 	
Automotive
	1 		Hard Skill 	
Retrospectives
	1 		Hard Skill 	
Sql Server
	1 		Hard Skill 	
User Group
	1 		Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Engineer
	2 	2 	Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Construct
	1 		Hard Skill 	
Architecture
	1 		Hard Skill 	
Group Meetings
	1 		Hard Skill 	
Microservices
	1 		Hard Skill 	
Consumer Facing
	1 	1 	Hard Skill 	
Sprint Planning
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Domain Knowledge
	1 		Hard Skill 	
Agile Development
	1 		Hard Skill 	
Aws
	1 		Hard Skill 	
Technical Solutions
	1 		Hard Skill 	
Process Improvements
	1 		Hard Skill 	
Software EngineerDbt
	2 		Hard Skill 	
Etl
	2 		Hard Skill 	
.Net
	1 		Hard Skill 	
Azure
	2 		Hard Skill 	
Erwin
	1 		Hard Skill 	
Mysql
	1 		Hard Skill 	
Nosql
	1 		Hard Skill 	
Queries
	2 	1 	Hard Skill 	
Github
	1 	2 	Hard Skill 	
Oracle
	2 		Hard Skill 	
Python
	1 	4 	Hard Skill 	
Kinesis
	2 		Hard Skill 	
Databases
	3 	4 	Hard Skill 	
Etl Tools
	2 		Hard Skill 	
Redshift
	1 		Hard Skill 	
Analytics
	2 	1 	Hard Skill 	
Snowflake
	3 		Hard Skill 	
Automotive
	3 		Hard Skill 	
Postgresql
	1 	1 	Hard Skill 	
Cloud Based
	1 	1 	Hard Skill 	
Engineer
	3 	3 	Hard Skill 	
Informatica
	1 		Hard Skill 	
Kafka
	1 		Hard Skill 	
Architectures
	1 		Hard Skill 	
Data Analysis
	2 	1 	Hard Skill 	
Data Modeling
	3 		Hard Skill 	
Data Pipelines
	3 	1 	Hard Skill 	
Data Solutions
	3 	1 	Hard Skill 	
Data Warehouses
	3 		Hard Skill 	
Data Management
	1 		Hard Skill 	
Aws
	2 		Hard Skill 	
Product Management
	1 		Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Software Development Lifecycle
	Iis
	1 		Hard Skill 	
Ties
	1 		Hard Skill 	
Flask
	1 	1 	Hard Skill 	
Code
	3 	1 	Hard Skill 	
Python
	1 	4 	Hard Skill 	
Windows
	1 	1 	Hard Skill 	
Testing
	2 	1 	Hard Skill 	
Analytics
	1 	1 	Hard Skill 	
Debugging
	1 	1 	Hard Skill 	
Full Stack
	1 	4 	Hard Skill 	
Javascript
	1 	2 	Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Fingerprinting
	1 		Hard Skill 	
Public Safety
	5 	1 	Hard Skill 	
Test Plans
	1 		Hard Skill 	
Windows Servers
	1 		Hard Skill 	
Coding Standards
	2 		Hard Skill 	
Drivers License
	1 		Hard Skill 	
New Development
	1 		Hard Skill 	
Web Applications
	1 	1 	Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Development Work
	1 		Hard Skill 	
Issue Resolution
	1 		Hard Skill 	
Software Quality
	1 		Hard Skill 	
Software Solutions
	1 		Hard Skill 	
Information Systems
	1 	2 	Hard Skill 	
Project Managers
	1 		Hard Skill 	
User Documentation
	1 		Hard Skill 	
Development Projects
	1 		Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Information Technology
	2 	1 	Hard Skill 	
Software Development Life CycleC#
	1 		Hard Skill 	
Sql
	4 	4 	Hard Skill 	
.Net
	5 	1 	Hard Skill 	
T Sql
	2 		Hard Skill 	
Temp
	1 		Hard Skill 	
Code
	3 	1 	Hard Skill 	
Hiring
	1 		Hard Skill 	
Asp.Net
	1 		Hard Skill 	
Audits
	1 		Hard Skill 	
Indexes
	1 		Hard Skill 	
Sql Server
	1 		Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Engineer
	2 	1 	Hard Skill 	
Programming
	2 	1 	Hard Skill 	
Anticipation
	1 		Hard Skill 	
Normalization
	1 		Hard Skill 	
Full Life Cycle
	1 		Hard Skill 	
Web Application
	1 	1 	Hard Skill 	
Development Work
	1 		Hard Skill 	
Software Engineer
	2 		Hard Skill 	
Technical Requirements
	1 	1 	Hard Skill 	
Development Background
	1 		Hard Skill 	
Transaction Processing
	1 		Hard Skill 	
Application Development
	1 		Hard Skill 	
Full Life Cycle Development
	1 		Hard Skill 	
Web Application Development
	C#
	1 		Hard Skill 	
Git
	1 	2 	Hard Skill 	
Java
	1 		Hard Skill 	
Node
	1 	1 	Hard Skill 	
Redis
	1 		Hard Skill 	
Mysql
	1 		Hard Skill 	
React
	1 	1 	Hard Skill 	
Swift
	1 		Hard Skill 	
Code
	1 	1 	Hard Skill 	
Docker
	1 		Hard Skill 	
Hire
	1 		Hard Skill 	
Python
	1 	3 	Hard Skill 	
Angular
	1 		Hard Skill 	
Node.Js
	1 	1 	Hard Skill 	
Databases
	2 	2 	Hard Skill 	
Teamwork
	1 	1 	Hard Skill 	
Full Stack
	2 	4 	Hard Skill 	
Kubernetes
	1 		Hard Skill 	
Version
	1 	1 	Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Engineer
	3 	2 	Hard Skill 	
Architecture
	1 		Hard Skill 	
Cloud Services
	1 	2 	Hard Skill 	
Elasticsearch
	1 		Hard Skill 	
Microservices
	1 		Hard Skill 	
Orchestration
	1 		Hard Skill 	
Version Control
	1 	1 	Hard Skill 	
Containerization
	1 		Hard Skill 	
Aws
	1 		Hard Skill 	
Mobile Development
	1 		Hard Skill 	
Relational Databases
	2 	1 	Hard Skill 	
Software EngineerNlp
	1 		Hard Skill 	
Sql
	1 	2 	Hard Skill 	
Hive
	1 		Hard Skill 	
Hadoop
	1 		Hard Skill 	
Python
	1 	3 	Hard Skill 	
Databases
	1 	2 	Hard Skill 	
Analytics
	2 		Hard Skill 	
Automotive
	3 		Hard Skill 	
Mathematics
	1 		Hard Skill 	
Data Science
	2 	1 	Hard Skill 	
Data Analysis
	1 	1 	Hard Skill 	
Decision Trees
	1 	1 	Hard Skill 	
It Development
	1 		Hard Skill 	
Business Processes
	1 		Hard Skill 	
Machine Learning
	2 	1 	Hard Skill 	
Project Plans
	1 		Hard Skill 	
Model Development
	1 		Hard Skill 	
Operational Systems
	1 		Hard Skill 	
Business Requirements
	1 		Hard Skill 	
Relational Databases
	1 	1 	Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Solution Development
	1 		Hard Skill 	
Time Series Analysis
	1 		Hard Skill 	
Business Intelligence
	1 		Hard Skill 	
Technical Requirements
	1 	1 	Hard Skill 	
Large Scale Data Analysis
	Ui
	2 	1 	Hard Skill 	
Apis
	1 	3 	Hard Skill 	
Hvac
	1 		Hard Skill 	
React
	2 	1 	Hard Skill 	
Python
	2 	3 	Hard Skill 	
Angular
	2 		Hard Skill 	
Frontend
	4 	2 	Hard Skill 	
Ux Designs
	1 	1 	Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Engineer
	2 	1 	Hard Skill 	
Web Applications
	1 	1 	Hard Skill 	
Aws
	1 		Hard Skill 	
Cross Browser Compatibility
	C#
	2 		Hard Skill 	
Ui
	1 	1 	Hard Skill 	
Sql
	1 	2 	Hard Skill 	
Soa
	1 		Hard Skill 	
.Net
	1 		Hard Skill 	
Code
	1 	1 	Hard Skill 	
Oracle
	1 		Hard Skill 	
Draw
	1 		Hard Skill 	
Budget
	1 		Hard Skill 	
Mathematics
	1 		Hard Skill 	
Sql Server
	1 		Hard Skill 	
Data Access
	1 		Hard Skill 	
Engineer
	2 	2 	Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Architects
	1 		Hard Skill 	
Process Flows
	2 		Hard Skill 	
Quantitative
	1 		Hard Skill 	
Architectural
	1 		Hard Skill 	
Business Logic
	1 	1 	Hard Skill 	
Data Migration
	1 		Hard Skill 	
Design Documents
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Project Plans
	1 		Hard Skill 	
Technical Design
	1 		Hard Skill 	
Software Solutions
	1 		Hard Skill 	
Application Designs
	1 		Hard Skill 	
Enterprise Software
	1 		Hard Skill 	
Management Practices
	1 		Hard Skill 	
Security Management
	1 		Hard Skill 	
Business Requirements
	1 		Hard Skill 	
Development Languages
	1 		Hard Skill 	
Programming Languages
	1 	1 	Hard Skill 	
Software Requirements
	1 		Hard Skill 	
Application DevelopmentFdm
	1 		Hard Skill 	
Sql
	3 	3 	Hard Skill 	
Code
	1 	1 	Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Healthcare
	1 		Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Data Network
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Training Program
	1 		Hard Skill 	
Business Solutions
	1 	1 	Hard Skill 	
Technical Training
	1 		Hard Skill 	
Business Knowledge
	1 		Hard Skill 	
Solution Development
	1 		Hard Skill 	
Requirement Gathering
	C#
	1 		Hard Skill 	
Api
	1 	3 	Hard Skill 	
Sql
	1 	2 	Hard Skill 	
.Net
	2 	1 	Hard Skill 	
Azure
	1 		Hard Skill 	
T Sql
	1 		Hard Skill 	
Teach
	1 		Hard Skill 	
Polymorphism
	1 	1 	Hard Skill 	
Api Development
	1 	1 	Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Dependency Injection
	1 	1 	Hard Skill 	
Cutting Edge Technologies
	1 		Hard Skill 	
Collaborative Environment
	Apis
	6 	2 	Hard Skill 	
Dba
	2 		Hard Skill 	
Etl
	1 		Hard Skill 	
Erp
	1 		Hard Skill 	
F&O
	2 		Hard Skill 	
Sql
	6 	2 	Hard Skill 	
Qlik
	4 		Hard Skill 	
Agile
	2 		Hard Skill 	
Azure
	4 		Hard Skill 	
Queries
	1 	1 	Hard Skill 	
Rdbms
	2 		Hard Skill 	
T Sql
	2 		Hard Skill 	
Devops
	2 		Hard Skill 	
Python
	2 	3 	Hard Skill 	
Tableau
	2 		Hard Skill 	
Trade
	1 		Hard Skill 	
Database
	12 	3 	Hard Skill 	
Power Bi
	2 		Hard Skill 	
Data Flow
	1 	1 	Hard Skill 	
Fabric
	2 		Hard Skill 	
Sql Queries
	2 	1 	Hard Skill 	
Scripting
	2 		Hard Skill 	
Automation
	3 		Hard Skill 	
Indexing
	1 		Hard Skill 	
Powershell
	2 		Hard Skill 	
Sql Server
	3 		Hard Skill 	
Data Driven
	2 		Hard Skill 	
Engineer
	1 	2 	Hard Skill 	
Sql Database
	2 		Hard Skill 	
Data Exchange
	1 		Hard Skill 	
Data Integrity
	1 		Hard Skill 	
Api Development
	2 		Hard Skill 	
Api Integration
	1 		Hard Skill 	
Database Designs
	1 		Hard Skill 	
Software Systems
	1 		Hard Skill 	
Business Processes
	1 		Hard Skill 	
Computer Science
	2 	1 	Hard Skill 	
Custom Reports
	1 		Hard Skill 	
Stored Procedures
	1 		Hard Skill 	
Microsoft Power Bi
	2 		Hard Skill 	
Performance Tuning
	2 		Hard Skill 	
Process Automation
	1 		Hard Skill 	
Scripting Languages
	2 		Hard Skill 	
Technical Solutions
	2 		Hard Skill 	
Backup And Recovery
	1 		Hard Skill 	
Bi
	7 		Hard Skill 	
Information Technology
	2 		Hard Skill 	
Database AdministrationNode
	2 	2 	Hard Skill 	
React
	1 	2 	Hard Skill 	
Code
	4 	1 	Hard Skill 	
Uptime
	1 	1 	Hard Skill 	
Node.Js
	2 	2 	Hard Skill 	
Testing
	1 	1 	Hard Skill 	
React.Js
	1 		Hard Skill 	
Typescript
	2 	1 	Hard Skill 	
Code Reviews
	1 		Hard Skill 	
Engineer
	2 	2 	Hard Skill 	
Programming
	1 	1 	Hard Skill 	
System Testing
	1 		Hard Skill 	
Cloud Computing
	1 	1 	Hard Skill 	
Coding Standards
	2 		Hard Skill 	
Issue Resolution
	1 	1 	Hard Skill 	
Software Products
	1 		Hard Skill 	
Knowledge Sharing
	1 		Hard Skill 	
Software Solutions
	1 		Hard Skill 	
Programming Languages
	1 	1 	Hard Skill 	
Software Engineer
	2 	1 	Hard Skill 	
Software Performance
	1 		Hard Skill 	
Information Technology
	1 	1 	Hard Skill 	
Application Development
	1 	1 	Hard Skill 	
Technical Specifications
	Dcs
	2 		Hard Skill 	
Qlik
	1 		Hard Skill 	
Excel
	1 	1 	Hard Skill 	
Windows
	1 	1 	Hard Skill 	
Tableau
	1 		Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Power Bi
	1 		Hard Skill 	
Analytics
	2 	1 	Hard Skill 	
Assortment
	6 		Hard Skill 	
Automotive
	1 		Hard Skill 	
Field Sales
	1 		Hard Skill 	
Powerpoint
	1 	2 	Hard Skill 	
Merchandising
	1 		Hard Skill 	
Product Mix
	1 		Hard Skill 	
Market Trends
	1 		Hard Skill 	
Product Lines
	1 		Hard Skill 	
Supply Chain
	3 		Hard Skill 	
Project Based
	1 		Hard Skill 	
Customer Service
	1 		Hard Skill 	
Training Sessions
	1 		Hard Skill 	
Internet Explorer
	1 		Hard Skill 	
Inventory Management
	1 		Hard Skill 	
Microsoft Powerpoint
	1 	1 	Hard Skill 	
Bi
	1 		Hard Skill 	
Technical ProficienciesC#
	1 		Hard Skill 	
Sql
	1 	2 	Hard Skill 	
Wms
	1 		Hard Skill 	
.Net
	2 		Hard Skill 	
Wmos
	1 		Hard Skill 	
Coding
	1 	1 	Hard Skill 	
Oracle
	1 		Hard Skill 	
Windows
	1 	1 	Hard Skill 	
Database
	1 	3 	Hard Skill 	
Engineer
	1 	2 	Hard Skill 	
Correct
	1 		Hard Skill 	
Supply Chain
	1 	1 	Hard Skill 	
Windows Services
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Information Systems
	1 	2 	Hard Skill 	
Software Development
	2 	1 	Hard Skill 	
Software EngineerUi
	1 	1 	Hard Skill 	
C++
	2 		Hard Skill 	
Qml
	1 		Hard Skill 	
Wms
	1 		Hard Skill 	
Linux
	1 		Hard Skill 	
React
	1 	1 	Hard Skill 	
Webgl
	1 		Hard Skill 	
Add On
	1 		Hard Skill 	
Code
	1 	1 	Hard Skill 	
Python
	1 	3 	Hard Skill 	
Algebra
	1 		Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Frontend
	1 	1 	Hard Skill 	
Full Stack
	2 	4 	Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Typescript
	1 		Hard Skill 	
Engineer
	2 	2 	Hard Skill 	
Interfacing
	1 		Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Translation
	2 		Hard Skill 	
Asynchronous
	1 		Hard Skill 	
Architecture
	1 		Hard Skill 	
Linear Algebra
	1 		Hard Skill 	
Product Design
	1 		Hard Skill 	
User Interface
	2 	1 	Hard Skill 	
Management Tools
	1 	1 	Hard Skill 	
User Experience
	2 	1 	Hard Skill 	
Computer Graphics
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Product Development
	1 		Hard Skill 	
System Architecture
	1 		Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Software Engineer
	1 	1 	Hard Skill 	
Technical SpecificationErp
	1 	1 	Hard Skill 	
Sql
	2 	2 	Hard Skill 	
Agile
	1 		Hard Skill 	
Azure
	1 		Hard Skill 	
Scrum
	1 		Hard Skill 	
Devops
	1 		Hard Skill 	
Oracle
	1 		Hard Skill 	
Pl/Sql
	1 		Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Database
	1 	4 	Hard Skill 	
Power Bi
	1 		Hard Skill 	
Scripting
	1 		Hard Skill 	
Estimating
	1 		Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Engineering
	1 	1 	Hard Skill 	
Erp Software
	1 	1 	Hard Skill 	
Agile Software
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Pl/Sql Developer
	1 		Hard Skill 	
Software Quality
	1 		Hard Skill 	
Database Analysis
	1 	1 	Hard Skill 	
Development Languages
	1 		Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Bi
	1 		Hard Skill 	
Information Technology
	2 	1 	Hard Skill 	
Agile Software Development
	1 		Hard Skill 	
Software Development Methodologies
	Ant
	1 		Hard Skill 	
Git
	1 	2 	Hard Skill 	
Sql
	1 	2 	Hard Skill 	
Java
	1 		Hard Skill 	
Rest
	1 	1 	Hard Skill 	
Unix
	1 		Hard Skill 	
Grails
	1 		Hard Skill 	
Html5
	1 	1 	Hard Skill 	
Banner
	4 	1 	Hard Skill 	
Groovy
	1 		Hard Skill 	
Oracle
	1 		Hard Skill 	
Pl/Sql
	1 		Hard Skill 	
Eclipse
	1 		Hard Skill 	
Database
	1 	3 	Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Version
	1 	1 	Hard Skill 	
Web Services
	1 	1 	Hard Skill 	
Version Control
	1 	1 	Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Higher Education
	1 	1 	Hard Skill 	
Design Consulting
	1 		Hard Skill 	
Software Development
	1 	1 	Hard Skill 	
Version Control Tools
	1 	1 	Hard Skill 	
Object Oriented DesignApi
	3 	2 	Hard Skill 	
Farm
	2 		Hard Skill 	
Node
	2 	1 	Hard Skill 	
Soil
	2 		Hard Skill 	
Turf
	1 		Hard Skill 	
Azure
	2 		Hard Skill 	
Fiber
	1 		Hard Skill 	
Linux
	1 		Hard Skill 	
React
	1 	1 	Hard Skill 	
Urban
	1 		Hard Skill 	
Github
	2 	1 	Hard Skill 	
Python
	2 	3 	Hard Skill 	
Ecology
	1 		Hard Skill 	
Edit
	1 		Hard Skill 	
Jenkins
	2 		Hard Skill 	
Mongodb
	1 		Hard Skill 	
Node.Js
	2 	1 	Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Biofuels
	1 		Hard Skill 	
Database
	6 	3 	Hard Skill 	
Overhauling
	1 		Hard Skill 	
Teaching
	1 		Hard Skill 	
Postgresql
	1 	1 	Hard Skill 	
Agriculture
	1 		Hard Skill 	
Soil Sciences
	1 		Hard Skill 	
Soil Management
	1 		Hard Skill 	
Virtual Machines
	1 		Hard Skill 	
User Interactions
	1 		Hard Skill 	
Production Systems
	1 		Hard Skill 	
Environmental Sciences
	2 		Hard Skill 	
Sustainable AgricultureApi
	3 	2 	Hard Skill 	
Sql
	1 	2 	Hard Skill 	
Html
	1 	3 	Hard Skill 	
Rest
	1 	1 	Hard Skill 	
Admin
	1 		Hard Skill 	
Hobby
	1 		Hard Skill 	
Mysql
	1 		Hard Skill 	
React
	5 	1 	Hard Skill 	
Redux
	2 	1 	Hard Skill 	
Nodejs
	1 	1 	Hard Skill 	
Mongodb
	1 		Hard Skill 	
Web Apps
	1 	1 	Hard Skill 	
Database
	1 	3 	Hard Skill 	
Layers
	1 		Hard Skill 	
Start Up
	1 		Hard Skill 	
Data Flow
	1 	1 	Hard Skill 	
Ecommerce
	2 	1 	Hard Skill 	
Front End
	4 	2 	Hard Skill 	
Full Stack
	6 	4 	Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Engineer
	4 	2 	Hard Skill 	
Programming
	1 	2 	Hard Skill 	
Dashboard
	1 		Hard Skill 	
User Friendly
	1 	1 	Hard Skill 	
Business Logic
	1 		Hard Skill 	
Customer Facing
	1 	1 	Hard Skill 	
Database Design
	1 		Hard Skill 	
Remote Development
	1 		Hard Skill 	
Product Requirements
	1 	1 	Hard Skill 	
Back End Programming
	1 	1 	Hard Skill 	
Start Up Environment
	1 		Hard Skill 	
    Apis
	1 	2 	Hard Skill 	
Coding
	1 	1 	Hard Skill 	
Draw
	1 		Hard Skill 	
Financial
	1 		Hard Skill 	
Test
	2 	1 	Hard Skill 	
Databases
	1 	2 	Hard Skill 	
Teaching
	1 		Hard Skill 	
Script
	1 		Hard Skill 	
Data Systems
	1 		Hard Skill 	
Duplication
	1 		Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Programmer
	1 	1 	Hard Skill 	
System Design
	1 		Hard Skill 	
Data Reporting
	1 		Hard Skill 	
Human Resources
	1 		Hard Skill 	
Industry Trends
	1 		Hard Skill 	
Managing Projects
	1 		Hard Skill 	
Business Systems
	1 		Hard Skill 	
Coding Standards
	1 		Hard Skill 	
School District
	2 	1 	Hard Skill 	
Office Equipment
	1 		Hard Skill 	
Personnel Policies
	1 		Hard Skill 	
Setting Priorities
	1 		Hard Skill 	
Child Development
	1 		Hard Skill 	
Management Systems
	1 		Hard Skill 	
Quality Assurance
	1 		Hard Skill 	
Collaborative Working
	1 		Hard Skill 	
Information System
	2 	2 	Hard Skill 	
Knowledge Transfer
	1 		Hard Skill 	
Administrative Tools
	1 		Hard Skill 	
Innovative Solutions
	1 		Hard Skill 	
Learning Management
	1 		Hard Skill 	
Programming Languages
	1 	1 	Hard Skill 	
Technical Information
	1 		Hard Skill 	
Educational Programs
	1 		Hard Skill 	
Learning Management Systems
	1 		Hard Skill 	
Student Information System
	2 	1 	Hard Skill 	
    C#
	1 		Hard Skill 	
Api
	1 	2 	Hard Skill 	
Mvc
	1 	1 	Hard Skill 	
.Net
	1 		Hard Skill 	
Html
	1 	3 	Hard Skill 	
Arrays
	1 		Hard Skill 	
Karma
	1 		Hard Skill 	
Xunit
	1 		Hard Skill 	
Mstest
	1 		Hard Skill 	
Angular
	1 		Hard Skill 	
Asp.Net
	2 		Hard Skill 	
Jasmine
	1 		Hard Skill 	
Testing
	1 	2 	Hard Skill 	
Databases
	1 	3 	Hard Skill 	
Angularjs
	1 		Hard Skill 	
Bootstrap
	1 		Hard Skill 	
Front End
	1 	1 	Hard Skill 	
Javascript
	2 	3 	Hard Skill 	
Version
	1 	1 	Hard Skill 	
Client Side
	1 	1 	Hard Skill 	
Programming
	1 	2 	Hard Skill 	
Server Side
	1 	1 	Hard Skill 	
Unit Testing
	1 	1 	Hard Skill 	
Data Structures
	1 	1 	Hard Skill 	
Design Patterns
	1 	1 	Hard Skill 	
Web Technologies
	1 	1 	Hard Skill 	
Version Control
	1 	1 	Hard Skill 	
Relational Databases
	1 	1 	Hard Skill 	
Object Oriented Programming
	1 	1 	Hard Skill 	
    Dcs
	1 		Hard Skill 	
Lans
	1 		Hard Skill 	
Windows
	1 	1 	Hard Skill 	
Trace
	1 		Hard Skill 	
Courtesy
	1 		Hard Skill 	
Treat
	1 		Hard Skill 	
Helpdesk
	1 		Hard Skill 	
Health Systems
	1 		Hard Skill 	
Security Tools
	1 		Hard Skill 	
Access Control
	1 		Hard Skill 	
Network Devices
	1 		Hard Skill 	
Windows Desktop
	1 		Hard Skill 	
Active Directory
	2 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Behavioral Health
	1 		Hard Skill 	
Computer Hardware
	1 	1 	Hard Skill 	
Domain Controllers
	1 		Hard Skill 	
Technical Assistance
	1 		Hard Skill 	
Server Administration
	1 		Hard Skill 	
Network Access Control
	1 		Hard Skill 	
Network Administrator
	2 	1 	Hard Skill 	
    Ui
	8 		Hard Skill 	
Nlp
	1 		Hard Skill 	
Sas
	1 		Hard Skill 	
Ios
	1 	1 	Hard Skill 	
Atomic
	5 		Hard Skill 	
Css3
	1 		Hard Skill 	
Adobe
	2 		Hard Skill 	
Agile
	1 		Hard Skill 	
Figma
	1 		Hard Skill 	
Html5
	1 		Hard Skill 	
Sketch
	1 		Hard Skill 	
Front End
	2 	1 	Hard Skill 	
Storybook
	2 		Hard Skill 	
User Flows
	2 		Hard Skill 	
Data Entry
	2 		Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Data Driven
	1 	1 	Hard Skill 	
Design Tools
	1 		Hard Skill 	
Engineers
	3 	2 	Hard Skill 	
Form Design
	3 		Hard Skill 	
Style Guides
	1 		Hard Skill 	
Typography
	1 		Hard Skill 	
Tokens
	1 		Hard Skill 	
Design Systems
	1 		Hard Skill 	
Questionnaires
	1 		Hard Skill 	
User Research
	2 		Hard Skill 	
User Interface
	2 	1 	Hard Skill 	
Web Products
	1 		Hard Skill 	
Design Solutions
	1 		Hard Skill 	
Interactive Web
	1 		Hard Skill 	
Mobile Platforms
	1 		Hard Skill 	
User Experience
	2 		Hard Skill 	
Web Applications
	2 	1 	Hard Skill 	
Complex Data Sets
	1 		Hard Skill 	
Design Principles
	3 		Hard Skill 	
User Interactions
	1 		Hard Skill 	
Responsive Design
	1 		Hard Skill 	
Data Visualization
	1 		Hard Skill 	
Product Managers
	1 		Hard Skill 	
Customer Experience
	1 		Hard Skill 	
Front End Developers
	2 		Hard Skill 	
Innovative Solutions
	1 		Hard Skill 	
Language Processing
	1 		Hard Skill 	
User Interface Design
	1 		Hard Skill 	
Natural Language Processing
	1 		Hard Skill 	
    Qa
	1 	1 	Hard Skill 	
Mvc
	1 		Hard Skill 	
Ios
	1 		Hard Skill 	
Java
	1 		Hard Skill 	
Mvvm
	1 		Hard Skill 	
Agile
	1 		Hard Skill 	
Swift
	1 		Hard Skill 	
Code
	5 	1 	Hard Skill 	
Kotlin
	1 		Hard Skill 	
Prowess
	1 		Hard Skill 	
Test
	1 	1 	Hard Skill 	
Xamarin
	1 		Hard Skill 	
Debugging
	1 		Hard Skill 	
Ecosystem
	1 		Hard Skill 	
Native Ios
	1 		Hard Skill 	
Publisher
	1 		Hard Skill 	
Automation
	1 		Hard Skill 	
Full Stack
	1 	3 	Hard Skill 	
Engineering
	1 	2 	Hard Skill 	
Objective C
	1 		Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Architectures
	3 		Hard Skill 	
Development Work
	1 		Hard Skill 	
Technical Design
	1 		Hard Skill 	
Agile Development
	1 		Hard Skill 	
Consumer Messaging
	1 		Hard Skill 	
Mobile Architecture
	1 		Hard Skill 	
Business Requirements
	1 		Hard Skill 	
Platform Development
	1 		Hard Skill 	
Software Development
	1 		Hard Skill 	
Technical Competence
	1 		Hard Skill 	
Messaging Architecture
	1 		Hard Skill 	
Application Development
	1 		Hard Skill 	
Development Environment
	1 		Hard Skill 	
Enterprise Architecture
	1 		Hard Skill 	
Implementation Plans
	1 		Hard Skill 	
Cross Platform Development
	1 		Hard Skill 	
Software Development Life Cycle
	1 		Hard Skill 	
    C#
	1 		Hard Skill 	
Apis
	2 	2 	Hard Skill 	
C++
	1 		Hard Skill 	
Gcp
	2 		Hard Skill 	
Git
	1 	1 	Hard Skill 	
Sql
	1 	1 	Hard Skill 	
Gift
	1 		Hard Skill 	
Java
	5 		Hard Skill 	
Unix
	1 		Hard Skill 	
Agile
	1 		Hard Skill 	
Linux
	1 		Hard Skill 	
Mysql
	1 		Hard Skill 	
Queries
	1 		Hard Skill 	
Scrum
	1 		Hard Skill 	
Code
	3 	1 	Hard Skill 	
Github
	1 	1 	Hard Skill 	
Groovy
	1 		Hard Skill 	
Kanban
	1 		Hard Skill 	
Windows
	2 	1 	Hard Skill 	
Angular
	1 		Hard Skill 	
Jenkins
	1 		Hard Skill 	
Ceremonies
	1 		Hard Skill 	
Databases
	3 	1 	Hard Skill 	
Analytics
	1 		Hard Skill 	
Bitbucket
	1 		Hard Skill 	
Debugging
	1 		Hard Skill 	
Gift Cards
	1 		Hard Skill 	
Scripting
	1 		Hard Skill 	
Kubernetes
	1 		Hard Skill 	
Retrospectives
	1 		Hard Skill 	
User Story
	1 		Hard Skill 	
Cloud Based
	1 		Hard Skill 	
Diagrams
	1 		Hard Skill 	
Engineer
	1 	2 	Hard Skill 	
Google Cloud
	1 		Hard Skill 	
Stored Value
	1 		Hard Skill 	
Architecture
	3 		Hard Skill 	
Microservices
	1 		Hard Skill 	
Cloud Platform
	1 		Hard Skill 	
Design Patterns
	1 		Hard Skill 	
Design Documents
	1 		Hard Skill 	
Hosted Solution
	1 		Hard Skill 	
Loyalty Programs
	1 		Hard Skill 	
Shell Scripting
	1 		Hard Skill 	
Business Processes
	1 		Hard Skill 	
Computer Science
	1 	1 	Hard Skill 	
Distributed Team
	1 		Hard Skill 	
Software Products
	1 		Hard Skill 	
Data Architectures
	1 		Hard Skill 	
High Availability
	1 		Hard Skill 	
Acceptance Criteria
	1 		Hard Skill 	
Customer Engagement
	2 		Hard Skill 	
Software Technologies
	1 		Hard Skill 	
Application Security
	1 		Hard Skill 	
Software Development
	1 		Hard Skill 	
Software Engineer
	2 		Hard Skill 	
Technical Leadership
	1 		Hard Skill 	
Architectural Patterns
	1 		Hard Skill 	
Google Cloud Platform
	1 		Hard Skill 	
Product Demonstration
	1 		Hard Skill 	
Saas
	1 		Hard Skill 	
Enterprise Design Patterns
	1 		Hard Skill 	
Service Oriented Architecture
	2 		Hard Skill 	
    R
	1 	1 	Hard Skill 	
Apis
	1 	2 	Hard Skill 	
Cics
	1 		Hard Skill 	
Ddl
	1 		Hard Skill 	
Dml
	1 		Hard Skill 	
Ims
	1 		Hard Skill 	
Pci
	1 		Hard Skill 	
Sql
	1 	1 	Hard Skill 	
Ios
	1 	1 	Hard Skill 	
.Net
	1 		Hard Skill 	
Html
	1 	3 	Hard Skill 	
Java
	1 		Hard Skill 	
Node
	1 	2 	Hard Skill 	
Rhel
	1 		Hard Skill 	
Ruby
	1 		Hard Skill 	
Z/Os
	1 		Hard Skill 	
Cobol
	1 		Hard Skill 	
Linux
	1 		Hard Skill 	
Mysql
	1 		Hard Skill 	
Nosql
	1 		Hard Skill 	
React
	1 	2 	Hard Skill 	
Redux
	1 	2 	Hard Skill 	
Code
	8 	1 	Hard Skill 	
Hadoop
	1 		Hard Skill 	
Matlab
	1 		Hard Skill 	
Oracle
	1 		Hard Skill 	
Python
	2 	2 	Hard Skill 	
Tandem
	1 		Hard Skill 	
Ubuntu
	1 		Hard Skill 	
Windows
	1 	1 	Hard Skill 	
Jquery
	1 		Hard Skill 	
Angular
	1 		Hard Skill 	
Eclipse
	1 		Hard Skill 	
Node.Js
	1 	2 	Hard Skill 	
Test
	3 	1 	Hard Skill 	
Webpack
	1 		Hard Skill 	
Database
	4 	1 	Hard Skill 	
React.Js
	1 	1 	Hard Skill 	
Debugging
	1 		Hard Skill 	
Front End
	1 	1 	Hard Skill 	
Mainframe
	2 		Hard Skill 	
Hp Nonstop
	1 		Hard Skill 	
Javascript
	1 	3 	Hard Skill 	
Sql Server
	1 		Hard Skill 	
Tensorflow
	1 		Hard Skill 	
Engineer
	1 	2 	Hard Skill 	
Programming
	1 	1 	Hard Skill 	
Architectures
	1 		Hard Skill 	
Ms Sql Server
	1 		Hard Skill 	
Visual Studio
	1 		Hard Skill 	
Web Frameworks
	1 		Hard Skill 	
Web Technologies
	1 		Hard Skill 	
External Client
	1 		Hard Skill 	
Computer Science
	2 	1 	Hard Skill 	
Development Tools
	1 		Hard Skill 	
Machine Learning
	1 		Hard Skill 	
Software Solutions
	1 		Hard Skill 	
Information Systems
	2 	1 	Hard Skill 	
Linux Distributions
	1 		Hard Skill 	
Mobile Development
	1 		Hard Skill 	
Security Compliance
	1 		Hard Skill 	
Back End Programming
	1 		Hard Skill 	
Programming Languages
	2 		Hard Skill 	
Software Development
	1 		Hard Skill 	
Software Engineer
	1 	1 	Hard Skill 	
Information Technology
	2 		Hard Skill 	
Development Environment
	1 		Hard Skill 	
Implementation Plans
	1 		Hard Skill 	
Management Information Systems
	2 		Hard Skill 	
Software Development Life Cycle
	1 		Hard Skill 	
    Grammar
	1 	1 	Hard Skill 	
Database
	1 	1 	Hard Skill 	
Diagnoses
	1 		Hard Skill 	
Electronic
	1 		Hard Skill 	
Firmware
	1 		Hard Skill 	
Catalogs
	1 		Hard Skill 	
Formats
	1 		Hard Skill 	
Public Schools
	1 		Hard Skill 	
School Safety
	1 		Hard Skill 	
Learning Styles
	1 		Hard Skill 	
Record Keeping
	1 		Hard Skill 	
Safety Practices
	1 		Hard Skill 	
Software Update
	1 		Hard Skill 	
Digital Learning
	1 		Hard Skill 	
Office Equipment
	1 		Hard Skill 	
Setting Priorities
	1 		Hard Skill 	
Child Development
	1 		Hard Skill 	
Learning Environments
	1 		Hard Skill 	
    Crew
	1 		Hard Skill 	
Epics
	2 		Hard Skill 	
Agile
	4 		Hard Skill 	
Delta
	1 		Hard Skill 	
Scrum
	1 		Hard Skill 	
Devops
	1 		Hard Skill 	
Mockups
	1 		Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Airlines
	1 		Hard Skill 	
Drill
	1 		Hard Skill 	
User Stories
	1 		Hard Skill 	
Diagrams
	2 		Hard Skill 	
Elicit
	2 		Hard Skill 	
Engineer
	2 	2 	Hard Skill 	
Bug Tracking
	1 		Hard Skill 	
Construct
	1 	1 	Hard Skill 	
Process Flows
	1 		Hard Skill 	
User Scenarios
	1 		Hard Skill 	
Business Logic
	1 		Hard Skill 	
Re Engineering
	1 		Hard Skill 	
Business Process
	1 		Hard Skill 	
Decision Support
	1 		Hard Skill 	
Project Planning
	1 		Hard Skill 	
Agile Methodology
	1 		Hard Skill 	
Effort Estimation
	1 		Hard Skill 	
Internal Customer
	1 		Hard Skill 	
Business Value
	1 		Hard Skill 	
Product Manager
	1 		Hard Skill 	
Project Manager
	1 		Hard Skill 	
Acceptance Criteria
	1 		Hard Skill 	
Development Project
	1 		Hard Skill 	
Business Requirements
	1 		Hard Skill 	
Software Development
	2 		Hard Skill 	
Customer Relationships
	1 		Hard Skill 	
Functional Requirements
	1 		Hard Skill 	
Production Environments
	1 		Hard Skill 	
Non Functional Requirements
	1 		Hard Skill 	
Business Process Re Engineering
	1 		Hard Skill 	
Sdlc
	1 		Hard Skill 	
    Lpr
	1 		Hard Skill 	
Rta
	1 		Hard Skill 	
Dumps
	1 		Hard Skill 	
Trax
	1 		Hard Skill 	
Angel
	1 		Hard Skill 	
Logix
	1 		Hard Skill 	
Finance
	1 		Hard Skill 	
Parking
	16 		Hard Skill 	
Testing
	1 	1 	Hard Skill 	
Database
	1 	1 	Hard Skill 	
Tailor
	1 		Hard Skill 	
Construction
	2 	1 	Hard Skill 	
Architecture
	1 		Hard Skill 	
Change Control
	1 		Hard Skill 	
Customer Service
	1 		Hard Skill 	
Corrective Action
	1 		Hard Skill 	
Disaster Recovery
	1 		Hard Skill 	
It Infrastructure
	1 		Hard Skill 	
System Evaluations
	1 		Hard Skill 	
Associate Director
	1 		Hard Skill 	
Process Improvements
	1 		Hard Skill 	
Technical Knowledge
	1 		Hard Skill 	
System Administration
	2 		Hard Skill 	
    Iis
	1 		Hard Skill 	
Php
	1 		Hard Skill 	
Linux
	1 		Hard Skill 	
Apache
	1 		Hard Skill 	
Nodejs
	1 		Hard Skill 	
Windows
	1 	1 	Hard Skill 	
Database
	1 	1 	Hard Skill 	
Ecosystem
	2 		Hard Skill 	
Coldfusion
	1 		Hard Skill 	
Prevent
	2 		Hard Skill 	
Smartphone
	1 		Hard Skill 	
Reduce Costs
	1 		Hard Skill 	
Server Side
	1 		Hard Skill 	
Web Services
	1 		Hard Skill 	
Programmers
	1 		Hard Skill 	
Windows Server
	1 		Hard Skill 	
Invasive Species
	2 		Hard Skill 	
Incident Response
	1 		Hard Skill 	
Workable Solutions
	2 		Hard Skill 	
Amazon Web Services
	1 		Hard Skill 	
System Performance
	1 		Hard Skill 	
Digital Applications
	1 		Hard Skill 	
Root Cause Analysis
	1 		Hard Skill 	
Database Applications
	1 		Hard Skill 	
Continuous Deployment
	2 		Hard Skill 	
Continuous Integration
	1 		Hard Skill
"""

raw_list = re.split(r'[\n\t]', skills)

filtered_list = []

for string in raw_list:
    if string.strip() not in ['Hard Skill' , '', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        filtered_list.append(string.strip())

counts = {}

for skill in filtered_list:
    if skill not in counts:
        counts[skill] = 1
    else:
        counts[skill] += 1

sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

for count in sorted_counts:
    if count[1] > 1:
        print(count)