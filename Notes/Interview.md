### Your questions

Who are the team members? How long have they been working here?

What type of technology and practices do you follow?

Why are you bringing on a software developer? replace or team grow?

How I can be successful at your team. I mean what problem you’re trying to solve hiring me, what I should be ready for?

Experience

#### Intern in Cerence

**Introduction**: 

develop , maintain and improve  test automation framework for vehicle voice recognition system using python.

Work in an agile environment with CICD, I working more on the continuous delivery side.

**Task**:  

Every beginning of the week we have new feature released, all test cases will run on Jenkins automated. After that I will collect and analysis all failing test cases,  find root cause and report defects in Jira. 

There are two main ways dealing with failing cases: either test case is out of date, which need modification or delete. I will fix it and update to code Collaborator for code review by team members. If the test case is correct, I need to find out why and where it fails, how many similar cases are affected by this error. Raise a new ticket on Jira assign it to right person. Meanwhile, i will double check with developer to make sure this where the problem is.

After the case analysis are done, I write the report of current status, how many cases are failing right now, how many new JIRA tickets are raised, and what's the reason of new tickets. 

All of these happens in 2 or 3 workdays, we have multiple projects running on the same time. So we work on different branches with slightly different in test cases, user behavior. 

**Contribution**:

At the 3rd month of my internship, I found that among 300 cases weekly, a large number of  them are the same error: cloud didn't response in time (time out error).  There are some repetitive work which can be automated. So I developed a tool that can read all log files and categories them roughly according to their failing reasons:  cloud error, ASR/NLU error, or domain error. This can filter out some simple classic error, so that team members can focus on more unique errors that never happens before. 



#### Software Developer INT

**Introduction**

developed a writing board software that can draw picture, write sentence with drawing tablet and import power point foliens content as elements in canvas.

**Task**

I was joined the team in the very beginning. I designed the Model-View-Controller model. I am responsible for user interface part: It looks like a writing board with a slide bar. in the top are buttons such as clear canvas, import new file, larger Font, smaller Font and so on. The slid bar store all elements including picture, formula. We also have 11 brush and canvas colors to choose.  

 As for the import, I don't know the details. But it uses python-pptx to read files and store the elements we need.

**contribution**

**Model**:  It is the application's dynamic data structure, independent of the user interface. It directly manages the data, logic and rules of the application. connect to DB.

**Controller**: Accepts input and converts it to commands for the model or view

**View**: Any representation of information 

![MVC diagram with routes](https://files.realpython.com/media/mvc_diagram_with_routes.e12c5b982ac8.png)

**Signals** and **slots** are used for communication between objects

A signal is emitted when a particular event occurs. 

A slot is a function that is called in response to a particular signal.



#### Big data Analysis

**Introduction**: We participated in the Data Mining Cup competition among universities all over the world. Finally we won the 11th place in among 193 groups. The task is: Given a store's past 6 months sale history, build a prediction model to predict sold out date of every single item in the next month.

**Task**

To have hand on experience of data science or machine learning pipeline. We went through data collection, data cleaning, feature engineering, model selection, hyper parameter tuning, model evaluation. We used linear regression, tree regression, and other methods like neural network. 

**contribution**

lead the 5 person team. set up topic for daily meeting. assign tasks for the team members and make final presentation. 



#### Master Thesis



我的开发要用到TDD，测试驱动开发。这是一种开发实践，首先是在编写任何代码之前编写测试代码。

测试的基本

单元测试

集成测试

性能测试

安全测试

### Behavior interview

Your strength / Weakness

fight with members? 

![image-20200610093902424](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20200610093902424.png)

### Spring vs Spring Boot

**Spring** is a web application framework based on Java. It provides tools and libraries to create a complete cutomized web application.

**Spring Boot** is a spring module which provides RAD (Rapid Application Development) feature to Spring framework

1. can just run
2.  needs very little spring configuration.

### Maven

Maven is a software project management and comprehension tool.

Based on the concept of a **project object model** (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

### Kafka

Apache Kafka is a distributed data store optimized for ingesting and processing streaming data in real-time.

Kafka is primarily used to build real-time streaming data pipelines and applications that adapt to the data streams. 

### Docker 

https://hijiangtao.github.io/2018/04/17/Docker-in-Action/

**Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口**

Docker vs VM



![img](https://hijiangtao.github.io/assets/in-post/2018-04-17-Docker-in-Action-1.png)

**![img](https://hijiangtao.github.io/assets/in-post/2018-04-17-Docker-in-Action-2.png)**

docker-compose: all configuration in one file

docker-machine: create VM with docker service

docker-swarm: cluster based on docker

### CI/CD

CI CD (Continuous Integration / Continuous Delivery / Continuous Deployment)

CI 持续集成，应用代码的新更改会定期构建、测试并合并到共享存储库中。

CD 持续交付，开发人员对应用的更改会自动进行错误测试并上传到存储库。

CD 持续部署，自动将开发人员的更改从存储库发布到生产环境。

![CI/CD 流程](https://www.redhat.com/cms/managed-files/ci-cd-flow-desktop_1.png)



REST API standards

**Representational state transfer** (**REST**) is a software architectural style that defines a set of constraints to be used for creating web services

Aim to have platform independence, not bind the API and client.

REST APIs are designed around *resources*, which are any kind of object, data, or service that can be accessed by the client.

A resource has an identifier,  no verbs in URI. 

common operations: GET, POST, PUT, PATCH, and DELETE.

state code: 200(OK) 4xx(error)

链接后端

### Microservices

A variant of the service-oriented architecture (SOA) structural style— that arranges an application as a collection of loosely coupled services





