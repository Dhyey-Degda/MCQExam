# Importing tkinter for GUI.
import tkinter as tk
# Importing everything for making GUI.
from tkinter import *
# Importing PIL for publishing Images.
# PIL--- It create image file for python.
from PIL import Image, ImageTk
# importing xlrd which has the capability to read excel files.
import xlrd
# importing random to generate random integers.
import random
# importing requests to upload files to the specified URL.
import requests
# importing cv2 in order to record videos.
import cv2
# importing sys in order to get the exception messages.
import sys
# importing threading to make a multi-threaded system.
import threading


# VideoRecorder ---> Video Recorder class is made with an objective to record video.
class VideoRecorder:
    # startVideoRecording ---> Starts video reocrding and stops till Question.exam does not become 1.
    def startVideoRecording(self):
        # Capture video from webcam
        vid_capture = cv2.VideoCapture(0)
        vid_cod = cv2.VideoWriter_fourcc(*'XVID')
        # Save the file to videos/cam_Video.mp4
        output = cv2.VideoWriter("cam_video.mp4", vid_cod, 20.0, (640, 480))

        while True:
            # Capture each frame of webcam video
            ret, frame = vid_capture.read()
            cv2.imshow("My cam video", frame)
            output.write(frame)
            # Close and break the loop if the exam variable of class Question is
            # set to 1 meaning that exam is completed.
            if Question.exam == 1:
                break
        # close the already opened camera
        vid_capture.release()
        # close the already opened file
        output.release()
        # close the window and de-allocate any associated memory usage
        cv2.destroyAllWindows()


# Authenticate ---> It is used for authenticating the user.
class Authenticate():
    # The variable is used for verifying the user.
    # If flag is set to 1 then it's verified.
    # Else, the user is not verified.
    flag = 0

    # verify ---> Primary job is to verify the user's authenticity.
    def verify(self):

        # Destroying all those variables which are not needed.
        self.e1.destroy()
        self.e2.destroy()
        self.Label1.destroy()
        self.Label2.destroy()
        self.button.destroy()
        

        # verifiying username and password.
        if self.name_get.get() == 'abc' and self.pass_get.get() == "Test@1":

            # Setting the flag to 1 over here.
            self.flag = 1
            # Re-directing the user to exam.
            lbl = tk.Label(self.window, text="Logged IN Succesfully.Re-directing", font=("Arial", 20), fg='green')
            lbl.place(x=375)

            # Displaying message to not cheat.
            lbl1 = tk.Label(self.window, text="You are our BAHUBALI.", font=("Arial", 25), fg='red')
            lbl1.place(x=375, y=50)
            lbl2 = tk.Label(self.window, text="BAHUBALI don't cheat.", font=("Arial", 30), fg='green')
            lbl2.place(x=375, y=100)

            # Adding an image of bahubali.
            # Create a photoimage object of the image in the path
            image1 = Image.open("bahu.jpg")
            resize_image = image1.resize((350, 450))
            test = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(image=test)
            label1.image = test
            # Position image of bahubali
            label1.place(x=0, y=0, anchor='nw')

            # Setting a time of 1 second after that the window will be automatically destroyed and questions would be
            # displayed. However, if user destroys before 1 second then also questions would be displayed.

            self.window.after(1000, self.window.destroy)

        # What if the username or password is wrong.
        else:
            # Informing the user about incorrect credentials.
            tk.Label(self.window, text="Please try Again. Re-run the program.", font=("Arial", 30), fg='red').pack()

            # Since, it is for project giving the project's actual credentials.
            tk.Label(self.window, text="Account name : abc", font=("Arial", 30), fg="red", bg="green").pack()
            tk.Label(self.window, text="Password : Test@1", font=("Arial", 30), fg="green", bg="red").pack()

            # setting a time of 1 second, after that if user doesn't close it, it would be close automatically.
            self.window.after(1000, self.window.destroy)

    # Constructor ---> Initializes the flag variable to zero.
    def __init__(self):
        self.flag = 0

    # initialise ---> Initialises the gui. The constructor was separated from it because we wanted to separate
    # the usual functionality from actual ones.
    def initialise(self):

        # Initailizing the tkinter window.
        self.window = tk.Tk()
        # Renaming it and setting it's geometry.
        self.window.title('ExamSense Authentication')
        self.window.geometry('850x550')

        # Asking for user name and password. They have been placed with fixed positiion.
        self.Label1 = tk.Label(self.window, text="Enter User name : ", font=("Times", 24))
        self.Label1.pack(padx=5, pady=15, side=TOP, anchor=NW)

        self.name_get = tk.StringVar()
        self.pass_get = tk.StringVar()
        self.e1 = tk.Entry(self.window, textvariable=self.name_get, font=("Times", 24))
        self.e1.pack(padx=5, pady=2, side=TOP, anchor=NW)

        self.Label2 = tk.Label(self.window, text="Enter password : ", font=("Times", 24))
        self.Label2.pack(padx=5, pady=10, side=TOP, anchor=NW)

        self.e2 = tk.Entry(self.window, show='*', textvariable=self.pass_get, font=("Times", 24))
        self.e2.pack(padx=5, pady=10, side=TOP, anchor=NW)

        self.button = tk.Button(self.window, text="Login", command=self.verify)
        self.button.pack(padx=5, pady=10, side=TOP, anchor=NW)

        # To boost the moral of student, this image is used.
        image1 = Image.open("best.png")
        resize_image = image1.resize((350, 450))
        test = ImageTk.PhotoImage(resize_image)
        self.label1 = tk.Label(image=test)
        self.label1.image = test
        # Positioning image.
        self.label1.place(x=800, anchor='ne')

        # Stopping the window from being resized. This is primarily because we don't want the user to change the look of window.
        self.window.resizable(0, 0)
        self.window.mainloop()


# onSubmit ---> Is the function we'll call on clicking the submit button.
# This would make a file of questions and answers. It would upload it to the given HTTP via post method from requests.
def onSubmit(args, r):
    Question.exam = 1

    # The text file creation.
    f = open("test.txt", 'w', encoding='utf-8')
    # Text file writing.
    for i in args:
        for j in i.list_of_qa:
            f.write(str(j) + "\n")
        f.write(str(i.selection()) + "\n")
    # Closing the text file.
    f.close()

    # making a string object of the url, we're uploading the file on.
    myurl = 'http://admin.bayfoodmart.com/uploads/?new'
    # Getting the file ready for uploading.
    files = {'file': open('test.txt', 'rb')}
    # Uploading the file.
    getdata = requests.post(myurl, files=files)

    # Getting the video file ready for uploading.
    file1 = {'file': open('cam_video.mp4', 'rb')}
    # Uploading the file to the myurl.
    getdata = requests.post(myurl, files=file1)
    r.destroy()


# exception ---> Meant for handling exception in the code. We can't afford to make a try=except everywhere, because
# a) everything in this code is interdependent.Like an excel not opening can be handled by FileNotFound Error but
# in the next two lines we are using the same file object to access it's data.Hence, we can't afford to do it.
# However, in further updates,I'll try to make it a bit more robust. Hence, even though one part won't be working other parts would work fine.
# But, for the time being i have to use a centrallized try-except block.
# b) the other reason being python does stack-tracing itself. So, we can use a centrallized try-catch block.
# c) we're still on an experimental stage and hence I had to update it for better. Kind of a stage just before beta-state.
def exception(exceptionInProg):
    # Decribing the exception to the user.

    r1 = tk.Tk()
    r1.title("Exception")
    r1.geometry('750x550')
    if exceptionInProg is FileNotFoundError:
        exceptionInProg = "FileNotFound. Please re-download it."
    if exceptionInProg is TypeError:
        exceptionInProg = "Programming Error."
    if exceptionInProg is OSError:
        exceptionInProg = "We won't be able to run on your PC."

    # Descriptiong of the error.
    temp = tk.Label(r1, text=str(exceptionInProg), fg="red", bg="green", font=("Arial", 30))
    temp.pack(anchor=NW)

    # Self-destroying it after 10 seconds.
    r1.after(10000, r1.destroy)
    r1.mainloop()


# Question ---> This is the class being called after authenticating the student.
# This is meant to display 3 questions from the excel file and display it. Alongwith a submit button.
class Question:
    # This int variable is initialized to zero because it's going to hold value of student's answer.
    # Zero indicating that student didn't attempted the question.
    v = 0
    exam = 0

    # Initializing the variable v.
    def __init__(self):
        self.v = IntVar()
        self.exam = 0

    # It returns the option that student selected.Here,
    # a) 0 means student didn't attempt the question.
    # b) 1 means first option of the MCQ was selected by the student.
    # c) 2 means second option of the MCQ was selected by the student.
    # d) 3 means third option of the MCQ was selected by the student.
    # e) 4 means fourth option of the MCQ was selected by the student.
    def selection(self):
        return self.v.get()

    # options ---> It is meant to display the questions and options to the user.
    # Here, r is the window where the questions would be appended.
    # sheet is the excel sheet where the questions and their options are saved.
    # i is the randomly generated question number. Here, ith row would be read and the questions would be dispalyed.
    def options(self, r, sheet, i):
        # It gets the list of values that are there on that particular row.
        li = sheet.row_values(i)

        # The first column in excel file is question, the remaining four are options.And like most of the programming
        # concepts would love it, here too, indexing starts from zero because we have stored it as a list.

        tk.Label(r, text=str(li[0]), width=0).pack()

        # The logic for respective values have been explained in explanation of selection function.
        tk.Radiobutton(r, text=str(li[1]), variable=self.v, value=1).pack(anchor=NW)
        tk.Radiobutton(r, text=str(li[2]), variable=self.v, value=2).pack(anchor=NW)
        tk.Radiobutton(r, text=str(li[3]), variable=self.v, value=3).pack(anchor=NW)
        tk.Radiobutton(r, text=str(li[4]), variable=self.v, value=4).pack(anchor=NW)

        # this list has been stored as in order to upload a file we need both question and answer. but the above list only has
        # lifetime till the current function returns None. after this line, li would be lost. Hence, we saved it to the object.
        self.list_of_qa = li


# startExam ---> starts the exam once user is verified.
def startExam():
    # Then, we try opening the excel file.
    loc = ("ExcelProg_python.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    # Trying to initialise the GUI for exam.
    r = tk.Tk()
    r.title('ExamSense')
    # This set is created for a reason. we are generating random numbers to read questions. It might happen that
    # two random numbers might be same. In that case, student would get same question twice. Hence, to avoid this
    # we use a set to save the numbers generated randomly. However, the complete prevention of duplicacy of questions
    # is written below.
    s = set()
    # Making the list of three questions,i.e., by appending three objects of Question class to the list.
    list_of_questions = [Question(), Question(), Question()]
    count = 0
    # SInce, the number of questions is three hence, this condition.
    while (len(s) < 3):
        # first we'll store the length of current set.
        temp = len(s)
        # We generate the random number.
        i = random.randint(1, 10)
        # We append the nbumber.Now, if the number was already there, length wouldn't change. else it will.
        s.add(i)
        # Getting the length after appending a random number.
        temp1 = len(s)
        # If both the lengths are different, meaning the random number generated is different. Hence, we might give
        # it access to print the question on GUI.
        if temp != temp1:
            list_of_questions[count].options(r, sheet, i)
            count += 1
    # the submit button
    button = tk.Button(r, text="Submit", command=lambda: onSubmit(list_of_questions, r))
    button.pack()
    # Not allowing the window to resize.
    r.resizable(0, 0)
    # giving the user 3 minutes for 3 questions.
    r.after(180000, lambda: onSubmit(list_of_questions, r))
    r.mainloop()


# StartVideo ---> It's a function where t2 named thread will call this function.
# This function is made with an objective to call VideoRecorder class. It's objective is to record video.
def StartVideo():
    # Making an objective of class VideoRecorder
    t = VideoRecorder()
    # startsVideoRecording
    t.startVideoRecording()


# Main fuction ---> Obviously here's where all the above functions are used.
if __name__ == '__main__':
    # as mentioned above, a universal try-except block.
    try:
        # Authentication the user.
        auth_user = Authenticate()
        # Calling the initialise function from class Authenticate.
        auth_user.initialise()
        # If the user is verified.The first thing we do is to delete the auth_user object.
        if auth_user.flag == 1:
            del auth_user
            # Making t1 and setting the target to startExam.
            # Meaning once the threading start then it would call startExam function.
            t1 = threading.Thread(target=startExam)
            # Making t2 and setting the target to StartVideo
            # Meaning once the threading start then it would call StartVideo function.
            t2 = threading.Thread(target=StartVideo)
            # starting thread 1
            t1.start()
            # starting thread 2
            t2.start()
    except:
        # Passing the system information for the exception information. It's stored on sys.exc_info()[0]
        # The function exc_info under the module sys is used to store exception information and it returns the list
        # The first member of list is exception if it occured.
        exception(sys.exc_info()[0])