<h1>Code Engine Resource Optimizer</h1>

This python code is designed to resever minimum number of instances upon execution
- it will set to 1 if minimum number of instances is set to 0 in order to have at least single pod running.
- it will set to 0 if minimum number of instances is set to 0 in order to scale down the application, especially after office hour.

```
IBM_API_KEY=
PROJECT_ID=
APPLICATION_NAME=standup
TIMEZONE_OFFSET=8
```
<li>PROJECT_ID - ID of Code Engine Project. This can be retrieved from IBM Cloud console URL, example: https://cloud.ibm.com/codeengine/project/jp-tok/PROJECT_ID/overview
<li>APPLICATION_NAME refers to the name of the application. If you have multiple applications you would like to schedule, just need to comma to separate, example: standup, standup-backend
<li>TIMEZONE_OFFSET refers to the timezone adjustment based on UTC/GMT, example Singapore +8