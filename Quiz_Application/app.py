import requests
import os
from choices_dict import category, difficulty, option_list
import random
num_ques = int(input('How many questions do you want: '))
difficulty_level = input('Enter the difficulty level (easy, medium, hard): ').lower()

print(f'Difficulty level: {difficulty_level}')

print('Enter the category you want to take the quiz:')
for i, cat in enumerate(category.keys()):
    print(f'{i + 1} {cat}')

print("*" * 50)
selected_cat = int(input('Select a category (by number): '))

category_value = category.get(option_list.get(selected_cat, None), None)
os.system('cls')
print(f'Selected category: {option_list.get(selected_cat,None)}')

api_url = f'https://opentdb.com/api.php?amount={num_ques}&category={category_value}&difficulty={difficulty_level}&type=multiple'

# Make the API request
response = requests.get(api_url)
score = 0
i = 0

if response.status_code == 200:
    data = response.json()
    results = data.get('results', [])

    if results:
        while i < num_ques:
            question = results[i].get('question', '')
            correct_ans = results[i].get('correct_answer', '')
            incorrect_ans = results[i].get('incorrect_answers', [])
            incorrect_ans.append(correct_ans)
            random.shuffle(incorrect_ans)
            print(f'Question {i + 1}: {question}')
            print("OPTIONS:")
            for j, option in enumerate(incorrect_ans):
                print(f'{j + 1} {option}')

            selected_opt = input('Enter the option number: ')

            if selected_opt.isdigit() and 1 <= int(selected_opt) <= len(incorrect_ans):
                if incorrect_ans[int(selected_opt) - 1].lower() == correct_ans.lower():
                    print('✓ Correct answer')
                    score += 1
                else:
                    print('× Wrong Answer')

                if i < num_ques - 1:
                    option = input('Would you like to continue? Type "yes" or "no": ').lower().strip()

                    if option != 'yes' and option != 'y':
                        break
                else:
                    break
            else:
                print('Invalid option. Please select a valid option number.')

            i += 1
    else:
        print('ERROR IN FETCHING THE DATA FROM API')
else:
    print(f'Failed to fetch data. Status code: {response.status_code}')
print("*"*50)
print(f'TOTAL SCORE: {score}/{num_ques}')
print("\n THANKS FOR PLAYING")
