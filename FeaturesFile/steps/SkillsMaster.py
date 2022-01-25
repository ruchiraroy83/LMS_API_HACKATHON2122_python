import requests as requests
import json
import pandas as pd
from behave import *

from utilFiles.Fetch_data_from_sql import get_data_from_DB
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
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    context.Skill_ID = data[CONST_SKILL_ID][int(RowNumber)]
    context.StatusCode = data[CONST_STATUS_CODE][int(RowNumber)]
    context.StatusMsg = data[CONST_STATUS_MESSAGE][int(RowNumber)]
    context.response = requests.get(context.base_url + SKILLS_ENDPOINT+"/"+str(context.Skill_ID), auth=(context.username, context.password))
    print(context.response.text)

@then('skills User validates the StatusCode and StatusMessage from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    assert context.response.status_code == context.StatusCode
    json_object = json.loads(context.response.text)

    if not (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (
            context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        assert context.StatusMsg == json_object["message"]


@step('JSON schema is valid for GET with id in Skills')
def step_impl(context):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        jsonData = json.loads(context.response.text)
        Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
        context.jsonFilePath = Newread_file.get(Skills_GET_id_Filepath).data

        # validate it
        is_valid, msg = validate_json(jsonData, context.jsonFilePath)
        print(msg)


@step('skills check the Database with Skill id from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    context.Skill_ID = data[CONST_SKILL_ID][int(RowNumber)]

    context.StatusCode = data[CONST_STATUS_CODE][int(RowNumber)]
    print(context.StatusCode)
    context.StatusMsg = data[CONST_STATUS_MESSAGE][int(RowNumber)]
    context.response = requests.get(context.base_url + SKILLS_ENDPOINT + "/" + str(context.Skill_ID),
                                    auth=(context.username, context.password))
    print(context.response.text)


@then('skills User validates the StatusCode and StatusMessage from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    assert context.response.status_code == context.StatusCode
    json_object = json.loads(context.response.text)

    if not (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (
            context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        assert context.StatusMsg == json_object["message"]


@step('JSON schema is valid for GET with id in Skills')
def step_impl(context):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        jsonData = json.loads(context.response.text)
        Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
        context.jsonFilePath = Newread_file.get(Skills_GET_id_Filepath).data

        # validate it
        is_valid, msg = validate_json(jsonData, context.jsonFilePath)
        print(msg)


@step('skills check the Database with Skill id from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        read_file = readProperties(CONFIG_PROPERTIES_FILE)
        context.dbHostname = read_file.get(dbHostname).data
        context.dbName = read_file.get(dbName).data
        context.dbUsername = read_file.get(dbUsername).data
        context.dbPassword = read_file.get(dbPassword).data
        context.Query = "select skill_id,skill_name from tbl_lms_skill_master where skill_id='" + str(
            context.Skill_ID) + "'"
        dbdf = get_data_from_DB(context.dbHostname, context.dbName, context.dbUsername, context.dbPassword,
                                context.Query)
        json_dic = json.loads(context.response.text)

        for key in dbdf:

            new_dict = key
            new_dict1 = dict((k.lower(), v) for k, v in new_dict.items())
            json_dic1 = dict((k.lower(), v) for k, v in json_dic.items())

            for key in new_dict1.keys() & json_dic1.keys():
                if key in json_dic1 and new_dict1:
                    assert json_dic1[key] == new_dict1[key]



