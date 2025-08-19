# 📝 Simple To-Do List Application (C++)

This is a basic command-line to-do list manager written in C++. It's a great project for understanding fundamental C++ concepts like classes, objects, file I/O streams, and dynamic memory management. The application allows you to organize your tasks and saves your data for future use.

## **⚙️ Key Features**

* **Task Class:** Defines a `Task` as an object with a description and a completion status.
* **File Persistence:** Tasks are automatically loaded from and saved to a `tasks.txt` file using C++ file streams (`fstream`).
* **User-Friendly Interface:** A clear menu guides you through adding, viewing, and managing tasks.
* **Robust Input Handling:** The program handles various user inputs to prevent crashes and ensure a smooth experience.

## **🚀 How to Run**

### **Prerequisites**

* A C++ compiler (e.g., g++).

### **Compilation**

1.  Navigate to the `src` directory in your terminal.
2.  Compile the source code using your C++ compiler:
    ```sh
    g++ main.cpp -o todo_app
    ```

### **Execution**

1.  Run the compiled executable:
    ```sh
    ./todo_app
    ```
2.  Follow the prompts to interact with the application.

## **📋 Sample Output**

When you run the application for the first time, it will start with an empty list.
