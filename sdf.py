import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)

offline_engine = pyttsx3.init()
offline_engine.setProperty('rate', 150)
offline_engine.setProperty('volume', 1.0)

def speak(text, use_online=True):
    if use_online:
        engine.say(text)
        engine.runAndWait()
    else:
        offline_engine.say(text)
        offline_engine.runAndWait()

def listen(recognizer, use_online=True):
    with sr.Microphone(device_index=None, sample_rate=48000, chunk_size=512) as source:
        speak("next, ask...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=10)
            print("Recognizing...")
            if use_online:
                query = recognizer.recognize_google(audio, key=None)
            else:
                query = recognizer.recognize_sphinx(audio)
            speak(f"received request: {query}", use_online)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry,?", use_online)
            return ""
        except sr.RequestError as e:
            if use_online:
                speak(f"Could not request results from Google Speech Recognition service; {e}")
            else:
                speak("Speech recognition offline mode is not available. Please check your installation.")
            return ""

def virtual_assistant():
    speak("HAI, MY NAME IS ELIZA, HOW CAN I HELP YOU ")

    recognizer = sr.Recognizer()

    try:
        while True:
            command = listen(recognizer)
            if "hello" in command  or 'hey' in command or 'can i talk with you' in command: 
                speak("hey hii, my  name is eliza, iam a voice bot, how can i help you")
            elif "hai" in command:
                speak("hii how can i help you ,feel free to ask ")
            elif "what is csm" in command or "csm means" in command or "importance of csm" in command or "about csm bracnh" in command or 'tell me about csm branch' in command:
                speak('Computer Science and Engineering (CSE) with a specialization in Artificial Intelligence  and Machine Learning  is a popular and rapidly evolving branch in the field of engineering and technology, Here are some key aspects of CSE with AI and ML specialization, Core Computer Science Knowledge,:Artificial Intelligence,Machine Learning ,and Data Science,Deep Learning:')
            elif "hey hi" in command or "can you hear me" in command:
                speak("hey hii, how can i assist you any queries")
            elif "how are you" in command:
                speak("I'm just a computer program, so I don't have feelings, but I'm here to help you!")
            elif "good morning" in command:
                speak("good morning, have a nice day ")
            elif "college" in command and "name" in command:
                speak("this is sree venkateswara college of engineering which is located in balaji nagar,kadapa")
            elif all(keyword in command for keyword in ["what", "hod", "csm", "name"]):
                speak("P A ramesh sir is the h o d of c s m.")
            elif "what is your name" in command :
                speak("my name is voice bot and iam created by csm 2nd year student name mahendra,by using speech recognisation and text to speech modules in python")
            elif "who is" in command and "head of department of" in command and  "artificial intelligence and machine learning branch" in command or 'who is head of  csm department' in command or 'who is csm hod' in command :
                speak("P A ramesh sir is the H O D of CSM")
            elif "who is" in command and "ramesh sir" in command or "ramesh sir belongs to which branch" in command:
                speak("ramesh sir belongs to artificial intelligence & machine learning branch,and he is the H O D of C S M")
            elif "CSE" in command or "what is CSE" in command or "what is csc" in command or "about csc" in command or "about cse" in command or "tell me about cse" in command or "tell me about csc" in command:
                speak("Computer Science and Engineering (CSE) is a field that focuses on the study of computation, algorithms, programming languages, software development, computer hardware, and related areas. It encompasses a wide range of topics including artificial intelligence, machine learning, data science, cybersecurity, computer networks, and more")
            elif "where are you going" in command:
                speak("i can't go anywhere because iam a chatbot i dont have any legs")
            elif "who is mahendra" in command:
                speak("mahendra belongs to artificial intelligence branch and he is studying 2nd year in sree venkateswara college of engineering")
            elif "bye bye" in command or "bye" in command:
                speak("okay bye, bye, have a good day and feel free to ask anything!")
                break
            elif "where is" in command and 'ramesh' in command and 'room ' in command or "where is ramesh sir room" in command:
                speak("ramesh sir room is in 3rd block 3rd floor beside the stairs")
            elif "where is" in command and "ramesh sir" in command:
                speak("ramesh sir is at csm department and he is available in between 9AM TO 5 PM")
            elif "can i meet" in command or "i want meet" in command and "ramesh sir" in command:
                speak("yeah, sure, u can meet him at department room which is at 3rd block 3rd floor")
            elif "how can i meet" in command and "ramesh sir" in command:
                speak("you can meet, ramesh sir if ramesh sir is available at department ,if available u can meet him directly")
            elif "did ramesh sir" in command and "comes to college" in command :
                speak("yes ramesh sir will come to college regularly")
            elif "how will" in command and "ramesh sir" in command and "come to collge" in command or "comes colllege" in command:
                speak("ramesh sir will come to college via bike")
            elif "what are the qualifications" in command and "ramesh sir" in command or 'qualifications of ramesh sir' in command:
                speak("as per my 2024 knowledge ramesh sir completed his degree alomg with masters")
            elif "at what time" in command and "ramesh sir is available" in command :
                speak("in the college ramesh sir will be available from morning 9am to 5 pm")
            elif "ramesh sir" in command and "went to class" in command or "takes any classes" in command:
                speak("yes, ramesh sir takes classes to all years of  C S M and ramesh sir teaches the core subjects of artificial intelligence and machine learning")
            elif "what is the role of ramesh sir" in command or "ramesh sir role in svck" in command or "ramesh sir role in this college" in command:
                speak("The role of ramesh sir in svck college is he is the hod of csm branch and teaches the core computer subjects to all csm students")
            elif "ramesh sir belongs to which branch" in command or "is ramesh sir" in command and "belongs to" in command and 'AI & ML branch' in command or "artificial intelligence and machine learning" in command or "C S M" in command:
                speak("ramesh sir belongs to artificial intelligence and machine learning (AI&ML) branch in sv college of engineering")
            elif "is ramesh sir worked in any college" in command or "ramesh sir experience" in command or "is ramesH sir worked in any college" in command or "rameswar experience" in command:
                speak("ramesh sir previously worked at sree venkateshwara engineering college,, thirupathi ,and ramesh sir having more than 12 years of experience ")
            elif "tell me about csm in this college" in command or "tell me about csm department" in command or "csm department details" in command or "can u tell me about csm branch in this college" in command:
                speak("""csm refers to artificial intelligence and machine learning, in this college csm department consist of 4 faculty members
                1)H O D of csm (ramesh sir),
                2)teaching faculty  (pradeep sir),
                3)teaching faculty (varsha madam),
                4)teaching faculty (chandraobul reddy sir)
                """)
            elif "tell me a joke" in command :
                speak("you are looking so handsome and beautiful, hahahhahhaha, iam laughing, beacuse you are not laughing")
            elif "who are you" in command or "tell me about yourself" in command or "what are the technologies that are used in this" in command:
                speak("I am a voice bot created by a human. I am here to assist you with your queries and provide helpful information. Feel free to ask me anything you need assistance with! The speech recognition and speech conversion libraries used in this voice bot are SpeechRecognition and py ttsx3.")
            elif  "location of this college" in command or "s v college location" in command or "s v c k college location" in command or 'where is' in command and 'this college' in command or 'svck college' in command or 'sv college' in command  and 'located' in  command:
                speak("the sree venkateswara college of engineering is located in middle of the kadapa city The exact location of the svck college is""balaji nagar"" opposite to svdc degree college balaji nagar")
            elif "what is your favourite food" in command:
                speak("My favourite food is biryani. And what about you? Do you like biriyani?")
            elif "who is pradeep sir" in command:
                speak("pradeep sir belongs to artificial intelligence and machine learning branch (C S M). and pradeep sir teaches the C S M branch subjects")
            elif ("which" in command or "what" in command) and ("subject" in command or "favourite subject" in command) and ("ramesh sir" in command or "hod sir" in command or "csm hod" in command):
                speak("For CSM H O  D Ramesh sir, Java programming is the favorite subject. Other than Java, as per my knowledge, Ramesh sir shows much more interest in web development and database management system (DBMS).")
            elif "who is varsha madam" in command or "is varsha madam belongs to" in command and 'csm' in command or 'ai ml' in command or 'artificial intelligence and machine learning' in command:
                speak("varsha madam belongs to artificial intelligence and machine learning branch (C S M). as per my knowledge of this year 2024, varsha madam is now taking the subject, advance data structures to 1st year students")
            elif "varsha madam belongs to which branch" in command or "is varsha madam belongs to csm branch" in command:
                speak("varsha madam belongs to artificial intelligence and machine learning branch (C S M)")
            elif "what is the second year csm room number" in command  or "room number of second year csm" in command or "csm second year room number" in command or "second year csm room number" in command:
                speak("the second year csm room number is, 3 4 0 1, it is at 3rd block 3rd floor , sometimes it may vary also")
            elif "what is the name of principal" in command or "what is the name of your principal" in command or "who is your principal" in command or "who is r v sudarshana reddy sir" in command or "principal name" in command:
                speak("doctor R V sudharshana reddy sir is the principal of sree venkateswara college of engineering,kadapa")
            elif "what is the third year csm room number" in command or "third year csm room number" in command or "csm third year room number" in command:
                speak("the third year csm room number is, 3 4 0 2, it is at 3rd block, 3rd floor")
            elif "what is the final year csm room number" in command or "final year csm room number" in command or "csm final year room number" in command or "what is the fourth year csm room number" in command or "csm fourth yer room number" in command or "fourth year cs, roo number" in command:
                speak("the fourth year csm room number is, 3 4 0 4, it is at 3rd block, 3rd floor")
            elif "what is the csm department room number" in command or "csm department room number" in command or "room number of csm department" in command:
                speak("the csm department room number is, 3 4 0 3, and it is loacted at 3rd block , 3rd floor")
            elif "3401" in command or "three four zero one" in command:
                speak("3 4 0 1, is the second year csm room number, which is located at 3rd block 3rd floor")
            elif "3402" in command or "three four zero two" in command:
                speak("3 4 0 2 is the 3rd year csm room number, which is located at 3rd block 3rd floor")
            elif "3403" in command or "three four zero three" in command:
                speak("3 4 0 3 is the csm department room number, which is located at 3rd block 3rd floor")
            elif "3404" in command or "three four zero four" in command:
                speak("3 4 0 4 is the final year or fourth year csm room number, which is located at 3rd block 3rd floor")
            elif "haritha" in command.lower() or "who is 2 2 K H 1 A 3 3 0 1" in command:
                speak("Haritha belongs to artificial intelligence and machine learning branch,(AI&ML), with roll number 22kh1a3306n, SHE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif "prudhvi" in command or "prudhvi nath reddy" in command or "who is prudhvinath reddy" in command:
                speak("prudhvi nath reddy , he belongs to artificial intelligence and machine learning branch,(ai&ml), and prudhvi nath reddy roll number is, 2 2 K H 1 A 3 3 0 2, HE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'meghana' in command or 'who is meghana' in command:
                speak('meghana , she belongs to artificial intelligence and machine learning branch,(ai&ml), and meghana roll number is, double two k h one a double three zero three, SHE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE')
            elif 'vasantha' in command :
                speak("vasantha , she belongs to artificial intelligence and machine learning branch,(ai&ml), and vasantha roll number is, double two, k, h, one, a, double three, zero four, SHE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'harsha' in command:
                speak("harsha , he belongs to artificial intelligence and machine learning branch,(ai&ml), and harsha roll number is, double two k h one a double three zero five, HE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'mahendra' in command:
                speak("mahendra , he belongs to artificial intelligence and machine learning branch,(ai&ml), and mahendra roll number is, double two k h one a double three zero six, HE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'nagaraj' in command or 'nagaraju' in command:
                speak("nagaraju , he belongs to artificial intelligence and machine learning branch,(ai&ml), and nagaraju roll number is, double two k h one a double three zero seven, HE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'lekhya' in command or 'lekhya reddy' in command or 'lekya' in command:
                speak("lekhya , she belongs to artificial intelligence and machine learning branch,(ai&ml), and lekhya roll number is, double two k h one a double three zero eight, SHE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'guru' in command or 'gurunath' in command or 'gurunadh' in command:
                speak("gurunath , he belongs to artificial intelligence and machine learning branch,(ai&ml), and gurunath roll number is, double two k h one a double three zero nine, HE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'harinath' in command:
                speak("harinath , he belongs to artificial intelligence and machine learning branch,(ai&ml), and harinath roll number is, double two k h one a double three one zero, HE IS STUDYING SECOND YEAR, SECOND SEMESTAR IN THIS COLLEGE")
            elif 'full form of csm' in command:
                speak("csm refers to artificial intelligence and machine learning branch")
            elif 'about artificial intelligence' in command or 'tell me about artificial intelligence' in command or 'what is ai' in command or 'tell me about ai' in command:
                speak("Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans, This field of computer science encompasses various approaches, techniques, and methodologies aimed at creating systems that can perform tasks that typically require human intelligence.")
            elif 'explain ai' in command or 'explain artificial intelligence' in command or 'advantages of csm' in command or 'advantages of artificial intelligence' in command or 'expalin about ai' in command or 'explain about artificial intelligence' in command or 'what is machine learning' in command or 'about machine learning' in command or 'reasons to join ai and ml' in command or 'why we have take ai and ml in this college' in command or 'specialities of csm branch' in command:
                speak('''                   
                        Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. This field of computer science encompasses various approaches, techniques, and methodologies aimed at creating systems that can perform tasks that typically require human intelligence. These tasks include but are not limited to:
                        Reasoning: Drawing logical conclusions from available information.
                        Problem-solving: Finding solutions to complex problems.
                        Learning: Acquiring knowledge and improving performance based on experience.
                        Perception: Interpreting and understanding sensory inputs such as images, sounds, and text.
                        Natural Language Processing (NLP): Understanding, interpreting, and generating human language.
                        Planning and Decision Making: Formulating strategies and making decisions to achieve goals.
                        Robotics: Controlling robots to perform tasks in the physical world.''')
            elif 'csm, ai and ml are same' in command or 'difference between ai ml and csm' in command:
                speak('csm,ai and ml are same,csm means, computer science and engineering with specialization of artificial intelligence and machine learning ')
            elif ('ai and ml' in command or 'ai and ml branch' in command or 'csm' in command or 
                ('artificial intelligence and machine learning' in command and ('introduced year' in command or 
                'intoduced in this year' in command or 'year of establishment' in command or 'was introduced' in command or 
                'introduced' in command))):
                speak('in the sv college of engineering, the artificial intelligence and machine learnning was introduced in 2016')
            elif 'why so many people dont know ai and ml branch' in command or 'why people dont know about csm' in command or 'why' in command or 'what' in command and 'dont know about csm' in command or 'reasons for not joining in csm branch' in command or 'not joining in ai and ml branch' in command or 'ai ml branch' in command:
                speak('There could be several reasons why students might choose not to pursue a branch of study in Artificial Intelligence (AI) and Machine Learning (ML), :Perceived Difficulty:, AI and ML are often seen as challenging fields, requiring strong mathematical and programming skills, Some students might feel intimidated by the complexity of the subject matter, Lack of Interest:,  Not all students find AI and ML topics intriguing or relevant to their career goals. They might have different passions or interests that lead them to pursue other fields of study, Limited Resources: Some educational institutions may not offer comprehensive courses or resources in AI and ML, making it difficult for students to access quality education in these areas.')
            elif 'ARE THERE ANY LABS PRESENT IN CSM DEPARTMENT FLOOR' in command or 'labs' in command and 'present' in command and 'csm floor' in command or 'csm department' in command:
                speak('there are no laborateries are present in the csm department floor,csm department floor contains 3 classrooms and one big hall only')   
            elif 'job opportunities for csm' in command or 'csm' in command and 'jobs' in command or 'jobs available for csm' in command or 'opportunities for csm' in command or 'ai ml branch jobs' in command or 'ai ml jobs' in command or 'jobs for artificial intelligence' in command or 'jobs for machine learning' in command or 'future of ai and ml' in command or 'future of artificial intelligence' in command:
                speak("""There is a wide range of job opportunities available for individuals with skills and expertise in Artificial Intelligence (AI) and Machine Learning (ML). Some of the prominent job roles in this field include:,
                1. Machine Learning Engineer,
                2. Data Scientist,
                3. AI Research Scientist,
                4. AI/ML Software Develope,r
                5. AI Ethicist,
                6. AI Product Manager,
                7. AI Consultant,
                8. AI/ML Research Engineer,
                9. Computer Vision Engineer,
                10. Natural Language Processing (NLP) Engineer """) 
            elif 'room number' in command and 'ramesh sir' in command or  'csm block' in command:
                speak('3 4 0 3 is the room n number of ramesh sir , as well as csm department')   
            elif 'where is' in command and 'ramesh sir' in command:
                speak('ramesh sir is at csm department,the csm department is located at 3rd block,3rd floor ,3 4 0 3 is the roo number,you can meet ramesh sir')
            elif 'timings of csm hod' in command or 'timings of ramesh sir' in command:
                speak('ramesh sir available in college from morning 9 am to evening 5pm ')   
            elif 'work experience' in command and 'ramesh sir' in command or 'experience of ramesh sir' in command or 'teaching experience' in command and 'ramesh sir' in command:
                speak('ramesh sir previously worked at thirupathi sv engineering college,  and ramesh sir is having more than 12 years of experience')
            elif 'aim of' in command and 'ramesh sir' in command or 'main aim of' in command and 'ramesh sir' in command or 'aim of csm hod' in command:
                speak('the main aim of the ramesh sir, (HOD OF CSM) is to get a software job more than 6 lakhs package, and placed in an good comapny with good package')
            elif 'lift available' in command:
                speak('no, there is lift facility available in this college for moving from one floor to another floor')
            elif  'first year' in command and 'H O D' in command or 'hod of first year students' in command:
                speak('praveen babu sir is the hod of all first year students')
            elif 'sections in first year' in command or 'number of sections in first year' in command or 'how many sections are there in first year' in command or 'sections' in command and 'first year' in command:
                speak("""there are 5 sections are avilable in the first year, they are,  1)1)CSM
                2)ECE
                3)CSE(A, B AND C)
                CSM AND ECE CONTAIN ONLY 1 SECTION EACH AND CSE CONTAINS 3 SECTIONS,this information regarding to acedamic year 2023-2024
                """ )
            elif 'sections in second year' in command or 'number of sections in second year' in command or 'sections' in command and 'second year' in clommand or 'how many sections are there in second year' in command:
                speak('there are 4 sections are present in the second year, they are, 1)CSE, 2)ECE, 3), CSM, ece and csm contains 1 section each and cse contains 2 sections ,this information regarding to acedamic year 2023-2024,the data may be vary from year to year')
            elif 'sections in third year' in command or 'number of sections in second year' in command or 'sections' in command and 'third year' in clommand or 'how many sections are there in third year' in command:
                speak('there are 4 sections are present in the third year, they are, 1)CSE, 2)ECE, 3), CSM, ece and csm contains 1 section each and cse contains 2 sections ,this information regarding to acedamic year 2023-2024,the data may be vary from year to year')
            elif 'sections in fourth year' in command or 'number of sections in second year' in command or 'sections' in command and 'second year year' in command or 'how many sections are there in fourth year' in command or 'final year' in command and 'sections' in command:
                speak('there are 4 sections are present in the final year, they are, 1)CSE, 2)ECE, 3), CSM, ece and csm contains 1 section each and cse contains 2 sections ,this information regarding to acedamic year 2023-2024,the data may be vary from year to year')
            elif 'projectors in csm' in command or 'is there any projectors are available in csm' in command or 'projectors' in command and 'csm' in command:
                speak("yes,csm class rooms contains projectors for digital classes")
            elif 'wash room' in command and 'csm' in command or 'csm floor' in command or 'csm floor' in command or 'washrooms in csm department' in command:
                speak('yeah,there is a gents toilet is avialable in the csm deaprtment')
            else:
                speak("i cant understood that can you repeat  one more time,")
    except KeyboardInterrupt:
        speak("Program terminated. Goodbye!")

if __name__ == "__main__":
    virtual_assistant()
