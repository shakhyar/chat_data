import pickle


def existing(counter):
	try:
		questions = pickle.load(open(f"questions{counter}.p", "rb"))
		answers = pickle.load(open(f"answers{counter}.p", "rb"))
		
		print("found previous data, new data will be appended to existing list..\n Type quit() to exit or read() to read data\n")

		taking_input = True
		
		while taking_input:
			q = input("question> ")
			a = input("answer> ")
			
			if q == "quit()" or a == "quit()":
				pickle.dump(questions, open(f'questions{counter}.p', 'wb'))
				pickle.dump(answers, open(f'answers{counter}.p', 'wb'))
				taking_input = False
			
			elif q == "read()" or a == "read()":
				print(questions, "\n", answers)

			elif q == "" or a == "":
				print("input cannot be empty\n")

			else:
				questions.append(q)
				answers.append(a)
	except Exception as e:
		print(e)


def new(counter):
	counter = counter + 1
	taking_input = True
	print("New questions and answers instance triggered. Type quit to exit(), read() to read new written data\n")
	questions = []
	answers = []
	
	while taking_input:
		q = input("question> ")
		a = input("answer> ")
		
		if q == "quit()" or a == "quit()":
			try:
				pickle.dump(questions, open(f'questions{counter}.p', 'wb'))
				pickle.dump(answers, open(f'answers{counter}.p', 'wb'))
				pickle.dump(counter, open('counter.p', 'wb'))
				taking_input = False
			except Exception as e:
				print(e)
		
		elif q == "read()" or a == "read()":
			try:
				print(questions, "\n", answers)
			except:
				print("question and answer data not created, please write some questions and answers and try again")

		else:
			questions.append(q)
			answers.append(a)



if __name__ == '__main__':	
	try:
		counter = pickle.load(open("counter.p", "rb"))
	except Exception as e:
		print(f"{e}\nNo existing counters found, counter set to 0")
		counter = 0
		pickle.dump(counter, open('counter.p', 'wb'))

	print("""

	If you want to create new q&a files, type --new\n
	If you want to add data to existing files, type --existing\n
	If you want to jump to individual files, type --custom counter\n

	""")
	head = input(">> ")

	if head == "--new":
		new(counter)

	elif head == "--existing":
		existing(counter)

	elif head == "--custom counter":
		counter = input("enter counter>> ")
		existing(counter)
	else:
		pass


