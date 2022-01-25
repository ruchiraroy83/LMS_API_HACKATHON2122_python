import requests as requests
import json
import pandas as pd
from behave import *
from utilFiles.JSON_schema_validation import validate_json
from utilFiles.fetch_data_from_property_file import readProperties
from utilFiles.CONSTANTS import *
use_step_matcher("re")
@given("Skills User is on Endpoint: url/Skills with valid username and password")
def step_impl(context):
    read_file = readProperties(CONFIG_PROPERTIES_FILE)
    context.base_url = read_file.get(URL).data
    context.username = read_file.get(Username).data
    context.password = read_file[Pwd].data

@when("skills User sends GET request")
def step_impl(context):
    context.response = requests.get(context.base_url+SKILLS_ENDPOINT, auth=(context.username, context.password))


@then("skills User validates StatusCode")
def step_impl(context):
    assert context.response.status_code == 200


@step("skills JSON schema is valid")
def step_impl(context):
    # Convert json to python object.
    jsonData = json.loads(context.response.text)
    Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.jsonFilePath=Newread_file.get(Skills_GET_Filepath).data
    # validate it
    is_valid, msg = validate_json(jsonData,context.jsonFilePath)
    print(msg)


@when('User sends GET request on skill id from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    print(context.ExcelFilePath )
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    print(data)
    context.df = data[CONST_SKILL_ID]
    print(context.df)
    print(RowNumber)

    context.newdf = data[CONST_SKILL_ID][RowNumber]
    print(context.newdf)




@then('skills User validates the StatusCode and StatusMessage from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    """
    :type context: behave.runner.Context
    :type SheetName: str
    :type RowNumber: str
    """
    raise NotImplementedError(
        u'STEP: Then skills User validates the StatusCode and StatusMessage from "<SheetName>" sheet and <RowNumber> row')


@step("skills check the Database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And skills check the Database')


@step('JSON schema is valid for "(?P<Method>.+)" in Skills')
def step_impl(context, Method):
    """
    :type context: behave.runner.Context
    :type Method: str
    """
    raise NotImplementedError(u'STEP: And JSON schema is valid for "<Method>" in Skills')