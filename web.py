import streamlit as st
import os as os
import functions as fc

todos = []

if not os.path.exists("todos.txt"):
    st.write("No todos just yet! :)")
else:
    todos = fc.read_data(os, "todos.txt")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(f"Entered todo item is: {todo}")
    todos.append(todo)
    st.write(todos)
    fc.write_data(os, "todos.txt", todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to increase your productivity.")

# st.checkbox("Buy groceries")
# st.checkbox("Throw trash")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(f"{todo}", key=todo)
    if checkbox:
        print(f"Item checked is: {todos[index]}")
        checked_item = todos.pop(index)
        fc.write_data(os, "todos.txt", todos)
        del st.session_state[todo] # Delete the pair that is selected from the list
        st.experimental_rerun() # Re-run the code for checkboxes

st.text_input(label="Enter your Todo item:",
              placeholder="ex: Pray",
              on_change=add_todo,
              key="new_todo")

st.session_state