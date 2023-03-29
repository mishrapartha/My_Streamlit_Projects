# ############################################### #
# ######### IMPORTING REQ PACKAGES ############## #
# ############################################### #
# Core Pkgs
import streamlit as st

# EDA Pkgs
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# DB Fxns
from my_app_8_TODO_DB_FXNS import *

def main():
    st.title('ToDo App in Streamlit')

    menu = ['Create Tasks', 'Read/View Tasks', 'Update Tasks', 'Delete Tasks', 'About']

    choice = st.sidebar.selectbox('Menu', menu)
    create_table()

    if choice == 'Create Tasks':
        st.subheader('Add Items')

        # Layout
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Task To Do")

        with col2:
            task_status = st.selectbox("Status", ['ToDo', 'Doing', 'Done'])
            task_due_date = st.date_input("Due Date")

        if st.button('Add Task'):
            add_data(task, task_status, task_due_date)
            st.success("Successfully added Task: {}".format(task))


    elif choice == 'Read/View Tasks':
        st.subheader('View Status of Tasks')
        result = view_all_data()
        clean_df = pd.DataFrame(result, columns=["Task", "Status", "Due Date"])
        with st.expander('View Status as Table'):
            st.dataframe(clean_df)

        with st.expander('View Task Status Plot'):
            task_df = clean_df['Status'].value_counts().to_frame()
            task_df = task_df.reset_index()
            task_df.columns = ['Status', 'Counts']
            st.dataframe(task_df)

            p1 = px.pie(task_df, names='Status', values='Counts', title='Distribution of Task Status')
            st.plotly_chart(p1, use_container_width=True)

    elif choice == 'Update Tasks':
        st.subheader('Edit/Update Items')

        result = view_all_data()
        clean_df = pd.DataFrame(result, columns=["Task", "Status", "Due Date"])
        with st.expander('View Current Status'):
            st.dataframe(clean_df)

        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Task to Edit", list_of_tasks)
        task_result = get_task(selected_task)

        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_due_date = task_result[0][2]

            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do", task)

            with col2:
                new_task_status = st.selectbox(task_status, ["ToDo", "Doing", "Done"])
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
                edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
                st.success("Updated ::{} ::To {}".format(task, new_task))

            with st.expander("View Updated Data"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
                st.dataframe(clean_df)

    elif choice == 'Delete Tasks':
        st.subheader('Delete Items')
        with st.expander("View All Tasks"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Select Task to Delete", unique_list)
        st.warning('Click on Delete button only if you are sure you want to Delete the selected task', icon='⚠')
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.success("Deleted: '{}'".format(delete_by_task_name))

        with st.expander("Remaining Tasks"):
            result = view_all_data()
            clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(clean_df)
    else:
        st.subheader('About')

        st.write('Amazon : ' + ' https://www.amazon.com/stores/author/B0BN2DYX1Q/about')
        st.write('Linkedin :' + ' https://www.linkedin.com/in/partha-m-02564616/')


if __name__ == '__main__':
    main()

