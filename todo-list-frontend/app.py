import streamlit as st
import requests

Base_URL = "http://127.0.0.1:8000" 

st.title("Welcome to TODO App")

operation = st.sidebar.radio("Select an Operation", ["GET", "POST", "PUT", "PATCH", "DELETE"])

#GET Logic
if operation == "GET":
    st.write("## Display all Tasks")

    if st.button("View All"):
        responce = requests.get(
            f"{Base_URL}/get-tasks"
        )
        st.json(responce.json())

#POST logic
if operation == "POST":
    st.write("## Add a Task to List")

    task_id = st.number_input("Task ID", min_value=1 , step=1)

    title = st.text_input("Title")
    desc = st.text_area("Description")

    if st.button("Add Task"):

        payload = {
            "title": title,
            "description": desc
        }

        responce = requests.post(
            f"{Base_URL}/post-task/{task_id}", json = payload
        )
        st.success("Task Added Successfully")

#PUT Logic

if operation == "PUT":
    st.write("## Edit all Sections of the Task.")

    task_id = st.number_input("Task ID:", min_value=1, step=1)

    title = st.text_input("Title:")
    desc = st.text_area("Description:")

    if st.button("Edit All Fileds"):

        payload = {
            "title":title,
            "description":desc
        }

        responce = requests.put(
            f"{Base_URL}/complete-change/{task_id}", json = payload 
        )
        st.success("Successfuly Updated the Task")

#PATCH Logic

if operation == "PATCH":
    st.write("Partially Edit a Task")

    task_id = st.number_input("Task ID", min_value=1, step = 1 )
    title = st.text_input("Title:")
    desc = st.text_area("Description")

    if st.button("Edit Task"):
      

        payload = {}
        
        if title:
            payload["title"] = title
        if desc:
            payload["description"] =desc   

        responce = requests.patch(
            f"{Base_URL}/edit-task/{task_id}", json = payload
        )
        st.success("Successfuly applied partial Edit")


#DELETE logic

if operation == "DELETE":
    st.write("Delete a Task from the List")

    task_id = st.number_input("Task ID",step=1, placeholder=0)
    
    if st.button("Delete Task?"):
        responce = requests.delete(
        f"{Base_URL}/del-task/{task_id}")
        st.error("Task Deleted Successfully")
