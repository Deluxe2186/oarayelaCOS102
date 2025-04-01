#listing out names of girls
g_names = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna',
           'Waje', 'Tola', 'Aisha', 'Latifa']

#listing out age of girls
g_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]

#listing out height of girls
g_heights = ["5'5", "6'0", "5'4", "5'9", "5'6",
            "5'5", "6'1", "6'0", "5'7", "5'5"]

#listing out scores of girls
g_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

#listing out names of boys
b_names = ['Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola',
            'Kunle', 'George', 'Thomas', 'Wesley']

#listing out ages of boys
b_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]

#listing out heights of boys
b_heights = ["5'7", "5'9", "5'8", "6'1", "5'9",
              "5'5", "6'1", "5'4", "5'8", "5'7"]

#listing out scores of boys
b_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

option = ['Boys', 'Girls', 'Both']
print('Which gender would you like to know the details of?')
print('1. Male')
print('2. Female')
print('3. Both')

choice = int(input('Enter your choice (1/2/3) '))

if choice == 1:
   for a in range(len(g_names)):
      print(f"\nName of boy: {b_names[a]} \n"
         f"Age: {b_ages[a]} \n"
         f"Height: {b_heights[a]} \n"
         f"Score: {b_scores[a]}\n")
      print('Number of boys: ', len(b_names))
elif choice == 2:
   for i in range(len(g_names)):
      print(f"\nName of girl: {g_names[i]} \n"
         f"Age: {g_ages[i]} \n"
         f"Height: {g_heights[i]} \n"
         f"Score: {g_scores[i]}\n")
      print('Number of girls: ', len(g_names))
elif choice ==3:
   for a in range(len(g_names)):
      print(f"\nName of boy: {b_names[a]} \n"
         f"Age: {b_ages[a]} \n"
         f"Height: {b_heights[a]} \n"
         f"Score: {b_scores[a]}\n")
   
   for i in range(len(g_names)):
      print(f"Name of girl: {g_names[i]} \n"
         f"Age: {g_ages[i]} \n"
         f"Height: {g_heights[i]} \n"
         f"Score: {g_scores[i]}\n")
   print('Number of boys: ', len(b_names))
   print('Number of girls: ', len(g_names))
   print('Total number of students: ', len(b_names) + len(g_names))