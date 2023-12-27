import random
captions=["Just had the best cup of coffee ever! #coffeelover",
"Thinking about starting a new hobby. Any suggestions?",
"Lost my keys again. How does this keep happening?",
"Movie night with friends was a blast! Recommend any good films?",
"Feeling inspired to cook something new tonight. Any recipe ideas?",
"Can't believe it's already Friday. Time flies!",
"Just finished a great book. What should I read next?",
"Spent the day at the beach. Perfect weather!",
"Trying out a new workout routine. Wish me luck!",
"Got a promotion at work today. Hard work pays off!",
"Binge-watching my favorite TV show. No regrets.",
"Found a hidden gem of a restaurant. Highly recommend!",
"Saw the most beautiful sunset. Nature is amazing.",
"Planning a weekend getaway. Any travel tips?",
"Learning a new language. ¡Hola, amigos!",
"Attended a virtual conference today. So much to absorb!",
"Visited a museum and learned some fascinating history.",
"Finally organized my closet. It's a small victory!",
"Trying to break a bad habit. Any advice?",
"Celebrating my pet's birthday today. They grow up so fast!",
"New haircut, new me. What do you think?",
"Reflecting on life and setting new goals. Excited for the future!",
"Cooked a homemade meal from scratch. Feeling accomplished.",
"Took a spontaneous road trip. Sometimes you just need to go!",
"Attended a live concert. Music is therapy for the soul.",
"Successfully planted a small garden. Green thumb achievement unlocked!",
"Thinking about adopting a pet. Any pet parent advice?",
"Finished a DIY home project. Proud of the results!",
"Tried a new fitness class. I can barely walk, but it was worth it!",
"Enjoying a lazy Sunday with a good book and hot cocoa.",
"Started a blog to share my passions. Excited for this new journey!",
"Solved a challenging puzzle. Feeling like a genius!",
"Joined a book club. Can't wait to discuss the latest read.",
"Attended a comedy show. Laughter is the best medicine.",
"Volunteered at a local charity event. Giving back feels great!",
"Learning to play a musical instrument. Practice makes perfect!",
"Hosted a game night with friends. Board games are underrated.",
"Visited an art gallery. So much creativity in one place!",
"Experimenting with new dessert recipes. Sugar rush incoming!",
"Attended a virtual workout class. Sweating at home is the new norm!",
"Finished a jigsaw puzzle with way too many pieces. Dedication level: expert.",
"Finally conquered my fear of public speaking. Facing fears head-on!",
"Trying meditation for the first time. Zen mode activated.",
"Started a journal to document daily gratitude. Positive vibes only!",
"Hosted a themed costume party. Best costumes won prizes!",
"Hiked to the top of a mountain. The view was breathtaking!",
"Attended a photography workshop. Capturing moments in pixels.",
"Saw a shooting star last night. Wishes do come true!",
"Embarked on a 30-day fitness challenge. Let the gains begin!",
"Reorganized my workspace for better productivity. Ready to conquer tasks!"]


with open("users.txt", "r") as file:
    data = file.readlines()
usernames=[]
for i in data:
    usernames.append(i.split(",")[0])


line="INSERT INTO posts ( postId, userID, imageURL, caption)\nVALUES "

for i in range(len(captions)-1):
    userId= usernames[random.randint(0,len(usernames)-1)]
    line += f"( {str(i)}, '{userId}', , '{captions[i]}''), \n"

with open("postsOut.txt", "w") as file:
    file.write(line)

