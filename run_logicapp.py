import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.logic import LogicManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.logic.models import Workflow
import requests
import json


def run_workflow(data):
    SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
    GROUP_NAME = "logictest"
    WORKFLOW_NAME = 'myworkflow'
    location="West US"
    url = "https://prod-151.westus.logic.azure.com:443/workflows/d092a0093a244788a688e20f284c86d7/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=SgCFaAx5h0hZ4uMNiL7Sgt18sr4KpGi8qT24wjZocmk"

    response = requests.post(url, data = data) 
    return response.json()