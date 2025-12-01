{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a9209a94-4102-4829-9250-55204ed72723",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to VIT'ian CGPA CALCULATOR\n",
      "\n",
      "Let's now calcuate the first semester's GPA\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 to calculate the Semester's GPA and CGPA, Enter 2 to exit :\n",
      " 1\n",
      "Enter the Total credits for the current semester : 4\n",
      "Enter the total number of course for the current semester : 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Now Enter the required details of the courses completed to calculate the GPA of the semester\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 if the course is a Theory course(LTP/LT) else if the course is a Laboratory/Projcet(PJ) based enter 2 :\n",
      " 1\n",
      "Enter the course credits : 4\n",
      "Enter your Mid-term marks of this course out of 50 : 40\n",
      "Enter your Term-end marks of this course out of 100 : 70\n",
      "Enter your internal marks out of 35: 25\n",
      "Enter your attendance percentage : 100\n",
      "Enter your class Average out of 100: 80\n",
      "Enter the standard devaition of the class : 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The course credits along with their Grade and Grade points are displayed below\n",
      "\n",
      "[4, 'C', 7]\n",
      "The GPA of the current semester is : 7.0 \n",
      "\n",
      "Your CGPA is : 7.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 to calculate the Semester's GPA and CGPA, Enter 2 to exit :\n",
      " 1\n",
      "Enter the Total credits for the current semester : 4\n",
      "Enter the total number of course for the current semester : 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Now Enter the required details of the courses completed to calculate the GPA of the semester\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 if the course is a Theory course(LTP/LT) else if the course is a Laboratory/Projcet(PJ) based enter 2 :\n",
      " 1\n",
      "Enter the course credits : 2\n",
      "Enter your Mid-term marks of this course out of 50 : 45\n",
      "Enter your Term-end marks of this course out of 100 : 60\n",
      "Enter your internal marks out of 35: 23\n",
      "Enter your attendance percentage : 100\n",
      "Enter your class Average out of 100: 80\n",
      "Enter the standard devaition of the class : 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 if the course is a Theory course(LTP/LT) else if the course is a Laboratory/Projcet(PJ) based enter 2 :\n",
      " 2\n",
      "Enter the course credits : 2\n",
      "Enter your Term-end marks of this course out of 100 : 70\n",
      "Enter your internal marks out of 10: 7\n",
      "Enter your Lab assignemnt marks out of 60 : 50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The course credits along with their Grade and Grade points are displayed below\n",
      "\n",
      "[2, 'C', 7, 2, 'F', 0]\n",
      "The GPA of the current semester is : 3.5 \n",
      "\n",
      "Your CGPA is : 5.25\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 to calculate the Semester's GPA and CGPA, Enter 2 to exit :\n",
      " 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using VIT'ian CGPA Calculator\n"
     ]
    }
   ],
   "source": [
    "## Creating a CGPA calulator for VIT'ans\n",
    "print(\"Welcome to VIT'ian CGPA CALCULATOR\\n\")\n",
    "print(\"Let's now calcuate the first semester's GPA\\n\")\n",
    "def GPA_Calculator():\n",
    "    Total_credits=int(input(\"Enter the Total credits for the current semester :\"))\n",
    "    Number_of_courses=int(input(\"Enter the total number of course for the current semester :\"))\n",
    "    print(\"Now Enter the required details of the courses completed to calculate the GPA of the semester\")\n",
    "    list_courses=[]\n",
    "    list_grades=[]\n",
    "    GPA=0\n",
    "    for i in range(0,Number_of_courses):\n",
    "        print()\n",
    "        Type_of_course=int(input(\"Enter 1 if the course is a Theory course(LTP/LT) else if the course is a Laboratory/Projcet(PJ) based enter 2 :\\n\"))\n",
    "        Course_credit=int(input(\"Enter the course credits :\"))\n",
    "        if(Type_of_course==1):\n",
    "            MTE=float(input(\"Enter your Mid-term marks of this course out of 50 :\"))\n",
    "            TEE=float(input(\"Enter your Term-end marks of this course out of 100 :\"))\n",
    "            Internals=float(input(\"Enter your internal marks out of 35:\"))\n",
    "            Attendance_percentage=float(input(\"Enter your attendance percentage :\"))\n",
    "            Class_avg=float(input(\"Enter your class Average out of 100:\"))\n",
    "            SD=float(input(\"Enter the standard devaition of the class :\"))\n",
    "            if(MTE <= 50 and TEE <= 100 and Internals <= 35 and Attendance_percentage <= 100 and Class_avg <= 100):\n",
    "                #Calculation TEE and MTE marks according to their weightage\n",
    "                MTE=(MTE/50)*30\n",
    "                TEE=(TEE/100)*30\n",
    "                #Caculation of Attendance marks\n",
    "                if(Attendance_percentage>=96):\n",
    "                    Attendance_marks=5\n",
    "                elif(Attendance_percentage>=91 and Attendance_percentage<=95):\n",
    "                    Attendance_marks=4\n",
    "                elif(Attendance_percentage>=86 and Attendance_percentage<=90):\n",
    "                    Attendance_marks=3\n",
    "                elif(Attendance_percentage>=81 and Attendance_percentage<=85):\n",
    "                    Attendance_marks=2\n",
    "                elif(Attendance_percentage>=75 and Attendance_percentage<=80):\n",
    "                    Attendance_marks=1\n",
    "                else:\n",
    "                    Attendance_marks=0\n",
    "                Total_marks=MTE+TEE+Internals+Attendance_marks\n",
    "                #Calculation of grade\n",
    "                if(Attendance_marks==0):\n",
    "                    Grade=\"F\"\n",
    "                    Grade_points=0\n",
    "                else:\n",
    "                    if(Total_marks>(Class_avg+(1.50*SD))):\n",
    "                        Grade=\"S\"\n",
    "                        Grade_points=10\n",
    "                    elif(Total_marks>(Class_avg+(0.50*SD)) and (Total_marks<=(Class_avg+(1.50*SD)))):\n",
    "                        Grade=\"A\"\n",
    "                        Grade_points=9\n",
    "                    elif(Total_marks>(Class_avg-(0.50*SD)) and (Total_marks<=(Class_avg+(0.50*SD)))):\n",
    "                        Grade=\"B\"\n",
    "                        Grade_points=8\n",
    "                    elif(Total_marks>(Class_avg-(1.0*SD)) and (Total_marks<=(Class_avg-(0.50*SD)))):\n",
    "                        Grade=\"C\"\n",
    "                        Grade_points=7\n",
    "                    elif(Total_marks>(Class_avg-(1.50*SD)) and (Total_marks<=(Class_avg-(1.0*SD)))):\n",
    "                        Grade=\"D\"\n",
    "                        Grade_points=6\n",
    "                    elif(Total_marks>(Class_avg-(2.0*SD)) and (Total_marks<=(Class_avg-(1.50*SD)))):\n",
    "                        Grade=\"E\"\n",
    "                        Grade_points=5\n",
    "                    else:\n",
    "                        Grade=\"F\"\n",
    "                        Grade_points=0\n",
    "                list_courses+=[Course_credit,Grade,Grade_points]\n",
    "            else:\n",
    "                print(\"Invalid Input, Enter the input with great care!\")\n",
    "                break\n",
    "        else:\n",
    "            TEE=float(input(\"Enter your Term-end marks of this course out of 100 :\"))\n",
    "            Internals=float(input(\"Enter your internal marks out of 10:\"))\n",
    "            Lab_assignment=float(input(\"Enter your Lab assignemnt marks out of 60 :\"))\n",
    "            TEE=(TEE/100)*30\n",
    "            Total_marks=TEE+Internals+Lab_assignment\n",
    "            if(TEE <= 100 and Internals<=10 and Lab_assignment<=60):\n",
    "                if(Total_marks>90):\n",
    "                    Grade=\"S\"\n",
    "                    Grade_points=10\n",
    "                if(Total_marks>80 and Total_marks<=90):\n",
    "                    Grade=\"A\"\n",
    "                    Grade_points=9\n",
    "                if(Total_marks>70 and Total_marks<=80):\n",
    "                    Grade=\"B\"\n",
    "                    Grade_points=8\n",
    "                if(Total_marks>60 and Total_marks<=70):\n",
    "                    Grade=\"C\"\n",
    "                    Grade_points=7\n",
    "                if(Total_marks>50 and Total_marks<=60):\n",
    "                    Grade=\"D\"\n",
    "                    Grade_points=6\n",
    "                if(Total_marks>40 and Total_marks<=50):\n",
    "                    Grade=\"E\"\n",
    "                    Grade_points=5\n",
    "                else:\n",
    "                    Grade=\"F\"\n",
    "                    Grade_points=0\n",
    "                list_courses+=[Course_credit,Grade,Grade_points]\n",
    "            else:\n",
    "                print(\"The inputs are invalid, please enter the inputs correctly again\")\n",
    "                break\n",
    "    print(\"The course credits along with their Grade and Grade points are displayed below\\n\")\n",
    "    print(list_courses)\n",
    "    \n",
    "    #Calculation of the semester's GPA\n",
    "    for i in range (0,len(list_courses),+3):\n",
    "        GPA=GPA+((list_courses[i]*list_courses[i+2])/Total_credits)\n",
    "        GPA=round(GPA, 2)\n",
    "    print(\"The GPA of the current semester is :\",GPA,\"\\n\")\n",
    "    return GPA,Total_credits\n",
    "list_GPA=[]\n",
    "list_Total_credits=[]\n",
    "Total_credits_completed=0\n",
    "for i in range(0,8):\n",
    "    Choice=int(input(\"Enter 1 to calculate the Semester's GPA and CGPA, Enter 2 to exit :\\n\"))\n",
    "    if(Choice==1):\n",
    "        CGPA_=0\n",
    "        CGPA=0\n",
    "        GPA_,Total_Credits=GPA_Calculator()\n",
    "        list_GPA.append(GPA_)\n",
    "        list_Total_credits.append(Total_Credits)\n",
    "        Total_credits_completed=Total_credits_completed+Total_Credits\n",
    "        for i in range(0,len(list_GPA)):\n",
    "            CGPA_=CGPA_+(list_GPA[i]*list_Total_credits[i])\n",
    "        CGPA=CGPA_/Total_credits_completed\n",
    "        CGPA=round(CGPA, 2)\n",
    "        if(CGPA>10.0):\n",
    "            print(\"You have made a mistake in entering the inputs please do enter the inputs with care!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Your CGPA is :\",CGPA)\n",
    "    else:\n",
    "        print(\"Thank you for using VIT'ian CGPA Calculator\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae5711bf-97ae-4fbb-aeed-e6c5fec97957",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
