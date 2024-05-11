import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_code_engine_sdk.code_engine_v2 import *

from datetime import datetime, timedelta

IBM_API_KEY = os.getenv("IBM_API_KEY","")
PROJECT_ID = os.getenv("PROJECT_ID","")
APPLICATION_NAME = os.getenv("APPLICATION_NAME","").split(",")
TIMEZONE_OFFSET = int(os.getenv("TIMEZONE_OFFSET",0))

# Initialize correct current time base on UTC
current_time = datetime.now() + timedelta(hours=TIMEZONE_OFFSET)
print(f'Current Time: {current_time}')

# Initialize the IAM authenticator using an API key
authenticator = IAMAuthenticator(IBM_API_KEY)
service = CodeEngineV2(authenticator=authenticator)
service.set_service_url('https://api.jp-tok.codeengine.cloud.ibm.com/v2')

all_results = []
pager = AppsPager(
    client=service,
    project_id=PROJECT_ID,
    limit=100,
)
while pager.has_next():
    next_page = pager.get_next()
    assert next_page is not None
    all_results.extend(next_page)

for app in all_results:
    
    if(app["name"] in APPLICATION_NAME):
        
        print(f'Application {app["name"]} found in Project {PROJECT_ID}')
        current_scale_min_instances = int(app["scale_min_instances"])
        if (current_scale_min_instances >= 0 and current_scale_min_instances < 2):
            new_scale_min_instances = current_scale_min_instances^1
            app_patch_model = {
                "scale_min_instances": new_scale_min_instances,
            }
            print("Applying changes")
                
            # to extract last entity_tag from latest revision
            entity_tag = ""
        
            entity_tag = app["entity_tag"]
            print(f'entity_tag = {entity_tag}')
            response = service.update_app(
                project_id=PROJECT_ID,
                name=app["name"],
                if_match=entity_tag,
                app=app_patch_model,
            )
            app = response.get_result()
            print(f'Application is updated successfully')
        else:
            print("Detected scale mininum instance is more than 1. Automated reverse will not be applied.")