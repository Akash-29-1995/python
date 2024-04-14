Objective:

● Set up a GitHub repository for your sample application.

● Create a GitHub Actions workflow to build and test the application on every push.

● Implement a deployment workflow for automatically deploying to a staging environment.

Step1: I have chosen one simple Python code and created a test file for the same separately.
Step2: Create Dockerfile for the same.
Step3: Go to actions and then create a new workflow ( you can also choose a template from the given option to get an idea of yaml file structure) 

Step4: To execute the job we need to have runner there are two options for the same one are you can use GitHub runner and second you can use self hosted runner its like your cicd job will be using the environment of that server(runner) and also the resources. To configure that runner go to settings>actions> runner> add new self hosted runner. then it will show some commands that you have to run on server which you want to use as runner.

![Screenshot from 2024-04-13 14-10-38](https://github.com/Akash-29-1995/python/assets/45091399/b829a465-2b8e-4e2a-bc39-9296d3eaec80)


step4. make the changes and the commit which will automatically trigger the job.

![Screenshot from 2024-04-13 14-37-52](https://github.com/Akash-29-1995/python/assets/45091399/50f32bb3-2cc2-4ca8-b767-a021c3ddc635)

