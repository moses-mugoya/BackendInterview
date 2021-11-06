if __name__ == '__main__':
    is_n_correct = False # variable to check if value n constraint is violated

    ''' Continously ask for user to enter the correct number of students '''
    while not is_n_correct:
        try:
            n = int(input()) # Input number of students

            if n < 2 or n > 10:
                print("Number of students should be between 2 and 10 inclusive")
            else:
                is_n_correct = True
        except:
            print("Please enter a positive number")
    

    student_marks = {}

    counter = 0 # variable to keep track of number of students whose scores are correct
    
    ''' Ask for score continously until corrrect score is entered '''
    while counter < n:
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        scores = set(scores) # convert map to set
        
        '''Validate the scores and the length of the array'''
        if len(scores) != 3:
            print("Please enter 3 scores")
        else:
            is_correct_counter = 0 # increment for every correct score
            for score in scores:
                if score < 100 and score > 0:
                    is_correct_counter += 1
            '''If is correct counter is equal to 3 -> all scores are correct '''        
            if is_correct_counter == 3:
                student_marks[name] = scores
                counter+=1
            else:
                print("Incorrect score")
    query_name = input() # Ask for query input

    total_score = 0 # initialize the total score variable

    for key, value in student_marks.items():
        if key == query_name:
            for v in value:
                total_score += v

    average = (total_score / 3)

    rounded_average = round(average,2) # round average to 2 decimal places

    print("\n")
    print(rounded_average)
