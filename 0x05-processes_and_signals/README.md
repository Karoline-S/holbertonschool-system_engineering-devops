# 0x04. Loops, conditions and parsing
### HOLBERTON FOUNDATIONS

### Mandatory Tasks
0. Write a bash script that displays it's own PID
1. Write a bash script that displays a list of curretnly running processes. Requirements:
  - must show all processes, for all users, including those which might not have a TTY.
  - display in a user-oriented format
  - show process heirarchy
2. Using task 1 command, write a bash script that displays lines containing the **__bash__** word, thus allowing you to easily get the PID of your bash process. Requirements:
  - cannot use pgrep
  - third line of script must be **# shellcheck disable=SC2009**
3. Write a bash script that displays the PID, along with the process name, of processes whose name contain the word bash. You cannot use ps
4. Write a bash script that displays **To infinity and beyond** indefinitely. Between each iteration of the loop, add a sleep 2.
5. Write a bash script that stops the infinite loop in task 4 using kill.
6. Write a bash script that stops the infinite loop in task 4 without using kill, killall or Ctrl C.
7. Write a bash script that displays:
  - **__To infinity and beyond__** indefinitely
  - With a sleep 2 in between each iteration
  - **__I am invincible!!!__** when receiving a SIGTERM signal
8. Write a JBash scriopt that kills the process in task 7

### Advanced Tasks
9. Write a bash script that:
  - Creates the file /var/run/myscript.pid containing its PID
  - Displays To infinity and beyond indefinitely
  - Displays I hate the kill command when receiving a SIGTERM signal
  - Displays Y U no love me?! when receiving a SIGINT signal
  - Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
10. Write a manage_my_process Bash script that:
  - Indefinitely writes I am alive! to the file /tmp/my_process
  - In between every I am alive! message, the program should pause for 2 seconds  
   Write a bash (init) scripot that manages the above script. Requirements:
  - When passing the argument start:  
     - Starts manage_my_process
     - Creates a file containing its PID in /var/run/my_process.pid
     - Displays manage_my_process started
  - When passing the argument stop:
     - Stops manage_my_process
     - Deletes the file /var/run/my_process.pid
     - Displays manage_my_process stopped
  - When passing the argument restart
     - Stops manage_my_process
     - Deletes the file /var/run/my_process.pid
     - Starts manage_my_process
     - Creates a file containing its PID in /var/run/my_process.pid
     - Displays manage_my_process restarted
  - Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed