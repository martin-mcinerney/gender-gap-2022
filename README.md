# PandoraTech


![cover image]()
Developers: Andrew, Arron, Dee, Jamie, Martin

[Deployed Site]()  
(Note: Ctrl + click to open in a new tab)    


## Table of Content
1. [Project Goals](#project-goals)
   1. [User Goals](#user-goals)
   2. [Site owner Goals](#site-owner-goals)
2. [User Experience](#User-Experience)
   1. [Target Audience](#target-audience)
   2. [User Requirements and Expectations](#user-requirments-and-expectations)
   3. [Manual](#manual)
   4. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
   1. [Flowcharts](#flowcharts)
   2. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
   1. [Languages](#Languages)
   2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
7. [PEP8 Validation](#pep8-validation)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#ackowledgements)

## Project Goals

### User Goals
- 
- 
- 
- 

### Site Owner Goals
- 
- 
- 
- 

[Back to Top](<#table-of-content>)
## User Experience

### Target Audience
- The target audience for is women interested in a career in the tech industry.

### User Requirments and Expectations
- 
- 
- 
- 
- 

[Back to Top](<#table-of-content>)  
## User Stories

### User
1. As a User, I would like
2. As a User, I would like
3. As a User, I would like
4. As a User, I would like
5. As a User, I would like
6. As a User , I would like
7. As a User , I would like
 
### Site Owner
8. As the site owner, I would like
9. As the site owner, I would like
10. As the site owner, I would like
11. As the site owner, I would like
12. As the site owner, I would like
13. As the site owner, i would like
 
[Back to Top](<#table-of-content>)
## Technical Design


### Flow Charts

<details><summary>Feature</summary>
<img src="">
</details>

<details><summary>Feature</summary>
<img src="">
</details>

<details><summary>Feature</summary>
<img src="">
</details>

### Wireframes

<details><summary>Wireframes</summary>
<img src="">
</details>

   
[Back to Top](<#table-of-content>)
## Technologies Used

### Languages
- [Python](https://www.python.org/)


### Frameworks and Tools
- [Balsamiq](https://balsamiq.com/)

- [GitPod](https://gitpod.io/)

- [GitHub](https://github.com/)

[Back to Top](<#Table-of-Content>)

### Libraries

#### Python Libraries
- [OS](https://docs.python.org/3/library/os.html)
- [Date time](https://docs.python.org/3/library/datetime.html)
- [Unittest](https://docs.python.org/3/library/unittest.html)

#### Third Party Libraries
- 
- 

## Features

### Blog
- A fun and challengibng quiz for all fans of The Simpsons.
- Contains a variety of questions related to The Simpsons.
- User stories covered:
<details><summary>Quiz image</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/features/feature_quiz.PNG">
</details>  


### Info Section
- 
- 
- User stories covered:
<details><summary>Image</summary>
<img src="">
</details>  


### Careers Section
- 
- User stories covered:
<details><summary>Image
</summary>
<img src="">
</details>  


### Courses Section
- 
- User stories covered:
<details><summary>Image</summary>
<img src="">
</details>  
 
### Logo
-
- User stories covered:
<details><summary>Image</summary>
<img src="">
</details>  


[Back to Top](<#table-of-content>)
## Validation

### PEP8 Validation
<details><summary>page</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP3_The_Simpsons_Quiz/main/docs/validation/validation_pep8_run.PNG">
</details>

<details><summary>Page</summary>
<img src="">
</details>

<details><summary>Page</summary>
<img src="">
</details>  


## Testing

### Manual Testing

<details><summary>View manual testing</summary>

### Testing User Stories

 User:
1. As a User, I would like to...

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |   |  |  |
|  |  |  |  |
<details><summary>Images</summary>
<img src="">
<img src="">
</details>



Site Owner
8. As the site owner, I would like...

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  |  |

<details><summary>Images</summary>
<img src="">
<img src="">
</details>

### Automated Testing
 
 <details><summary>View automated testing</summary>

- Automated testing was done using the unittest and coverage librararies for Python.


### Unit Tests
- Test...

<img src="">

- Test ran and passed with the correct email format submitted for the test.

<img src="">

### Coverage 

- Coverage was installed via the terminal, pip install coverage
<img src="">


- Coverage was then used to test using the following...
<img src="">


- The results of the test were the following:
<img src="">

- A HTML report was also generated using the command, coverage html
<img src="">

</details>






[Back to Top](<#table-of-content>)
## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| Bug I had | I fixed it by...|
| Bug I had | I fixed it by... |


[Back to Top](<#table-of-content>)
## Deployment
### Heroku / Firebase

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)
1. Log in to your account at heroku.com.
2. Create a new app, add a unique app name and choose your region.
3. Click on create app.
4. Go to "Settings".
5. Under Config Vars store any sensitive data in .json file. Name 'Key' field, copy the .json file paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to buid your app from.
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

[Back to Top](<#table-of-content>)
## Credits


### Media
- [Flaticon](https://www.flaticon.com/free-icon/physics_4270905?term=nuclear&page=1&position=16&page=1&position=16&related_id=4270905&origin=search): Nuclear icons created by Freepik - Flaticon</a>
- [Background image](https://www.freepik.com/vectors/fluffy-clouds) 
created by pch.vector - www.freepik.com</a>

### Code
- [Site](https://www.google.com)


## Acknowledgements

### Special thanks to the following:
- Deloitte
- Trust in Soda
- Code Institute

[Back to Top](<#table-of-content>)