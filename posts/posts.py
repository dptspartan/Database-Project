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

commentsdata = {
    "Just had the best cup of coffee ever! #coffeelover": [
        "Coffee goals! ",
        "Where's the coffee shop? Need recommendations!",
        "Coffee is life. Period.",
        "Coffee + Happiness = Perfect combo!",
        "I can almost smell it through the screen!",
        "Share the secret of that amazing coffee!",
        "Coffee envy right now!",
        "Sipping coffee while reading this. Cheers!",
        "Coffee is my love language.",
        "Need a cup after reading this!"],

    "Thinking about starting a new hobby. Any suggestions?": [
        "How about painting? ",
        "Coding is a cool hobby to explore!",
        "Hiking, photography, and nature walks are refreshing!",
        "Consider learning a musical instrument!",
        "Cooking or baking could be a tasty hobby!",
        "Gardening is therapeutic and rewarding!",
        "Book club! Join one and thank me later.",
        "DIY crafts for a creative outlet!",
        "Try your hand at writing. Start a blog!",
        "Learn a new language for a cognitive boost!"],

    "Lost my keys again. How does this keep happening?": [
        "Key-finding struggles are real!",
        "Time for a key holder by the door!",
        "Check the last place you found them—works wonders.",
        "Keys have a mind of their own, it seems.",
        "Consider a key tracker gadget!",
        "I feel you. Happens to the best of us.",
        "Maybe it's a sign to upgrade to a keyless entry!",
        "Try the classic retracing steps method.",
        "Lost keys = Life's little adventure.",
        "Keys and hide-and-seek, a classic combo."],

    "Movie night with friends was a blast! Recommend any good films?": [
        "What movie stole the show?",
        "Movie night is the best night!",
        "Give us your top movie recommendation!",
        "Did you go for a classic or something new?",
        "Movie buff here! Need genre specifics.",
        "Share the movie list! Need ideas.",
        "Any popcorn left? Asking for a friend.",
        "Movie nights make the best memories.",
        "Netflix and chill done right!",
        "Planning the next movie night already?"],

    "Feeling inspired to cook something new tonight. Any recipe ideas?": [
        "What cuisine are you feeling?",
        "Cooking adventure time! What's on the menu?",
        "Share the recipe if it turns out amazing!",
        "Homemade or exotic cuisine tonight?",
        "Cooking is an art. What's your masterpiece?",
        "Need quick or gourmet? I've got ideas!",
        "Let your taste buds guide you!",
        "Cooking playlist on? It's essential!",
        "Experimenting in the kitchen is the best!",
        "Share the culinary magic with us!"],

    "Can't believe it's already Friday. Time flies!": [
        "Friday feeling! Any weekend plans?",
        "The weekend is knocking on the door!",
        "Cheers to the weekend! ",
        "Time flies when you're having fun!",
        "Friday vibes in full swing!",
        "Weekend countdown starts now!",
        "Any special Friday traditions?",
        "Got that Friday energy! What's the plan?",
        "Friday is the gateway to the weekend!",
        "Make Friday amazing!"],

    "Just finished a great book. What should I read next?": [
        "Book recommendations, please!",
        "Tell us about the book you just finished!",
        "Bookworms unite! What's your genre?",
        "Any favorite authors or genres?",
        "Need a gripping novel or a light read?",
        "Book club vibes! What's the next pick?",
        "Share your literary adventures with us!",
        "Bookshelf envy is real right now!",
        "One book down, countless more to go!",
        "Bookworm problems: too many choices!"],

    "Spent the day at the beach. Perfect weather!": [
        "Beach day perfection! ",
        "Salty air and sandy toes—best combo!",
        "What's your beach day essential?",
        "Beach vibes all the way!",
        "Sunshine and ocean waves. Bliss!",
        "Favorite beach activity? Share it!",
        "A day at the beach is a day well spent.",
        "Wishing I were at the beach too!",
        "Sunscreen and beach reads—did you pack them?",
        "Beach day checklist: Sand, sea, and smiles!"],

    "Trying out a new workout routine. Wish me luck!": [
        "You got this! ",
        "Good luck on your fitness journey!",
        "What's your go-to workout music?",
        "Stay hydrated and enjoy the burn!",
        "New workout, new gains!",
        "Fitness goals in progress. Keep it up!",
        "Workout buddies make it even better!",
        "Share your favorite exercise so far!",
        "Sending all the positive vibes your way!",
        "Remember, progress, not perfection!"],

    "Got a promotion at work today. Hard work pays off!": [
        "Congratulations on the promotion!",
        "Hard work recognized and rewarded!",
        "Celebratory dinner in order! ",
        "What's the first thing you'll do in your new role?",
        "Boss moves only! Any advice for fellow professionals?",
        "Promotion party incoming!",
        "Well-deserved promotion! Any secrets to success?",
        "Cheers to climbing the career ladder!",
        "Next stop: corner office!",
        "Your success inspires us all!"],

    "Binge-watching my favorite TV show. No regrets.": [
        "What's the show? Need recommendations!",
        "Binge-watching is a lifestyle!",
        "No regrets, just great shows!",
        "Favorite TV show snacks? Share them!",
        "How many episodes deep are you?",
        "Show recommendations for the next binge?",
        "The art of productive binge-watching!",
        "Share your all-time favorite TV show!",
        "Binge-watch level: Expert!",
        "Savor every episode!"],

    "Found a hidden gem of a restaurant. Highly recommend!": [
        "Spill the details! What's the cuisine?",
        "Hidden gems are the best discoveries!",
        "New favorite dish found?",
        "Is it a cozy spot or a hidden hotspot?",
        "Restaurant recommendations are gold!",
        "Hidden gem alert! We trust your taste.",
        "What made it stand out? Ambiance or menu?",
        "Dining must-try: Check!",
        "Restaurant review time! Rate it!",
        "Planning my visit already!"],

    "Saw the most beautiful sunset. Nature is amazing.": [
        "Sunset magic! ",
        "Nature's canvas at its finest!",
        "Describe the colors! Sunset envy!",
        "Best spot to watch the sunset?",
        "Sunset photos or it didn't happen!",
        "Sunset meditation, anyone?",
        "Nature appreciation post!",
        "Sunset soundtrack: waves or birdsong?",
        "Chasing sunsets is a worthwhile hobby!",
        "Sunset vibes for a peaceful evening!"],

    "Planning a weekend getaway. Any travel tips?": [
        "Weekend getaway goals! Where to?",
        "Spontaneous or planned? Both are fun!",
        "Best travel tip you've ever received?",
        "Adventure awaits! Any travel buddies?",
        "Packing essentials: what are your must-haves?",
        "Road trip or flying? What's your style?",
        "Local recommendations or tourist attractions?",
        "Favorite travel destination so far?",
        "Travel playlist suggestions?",
        "Bon voyage! Have an amazing trip!"],

    "Learning a new language. ¡Hola, amigos!": [
        "¡Hola! ",
        "Language learning buddies unite!",
        "What inspired you to learn a new language?",
        "Favorite language learning app or resource?",
        "Language learning tips, por favor!",
        "How do you practice speaking the language?",
        "¡Buena suerte! (Good luck!)",
        "Next language on your list?",
        "Multilingual goals! What's the target?",
        "Language exchange anyone? ¡Vamos!"],

    "Attended a virtual conference today. So much to absorb!": [
        "Conference takeaways? Share them!",
        "Virtual conferences = Comfy learning!",
        "Best session you attended?",
        "Favorite virtual conference platform?",
        "Networking tips for virtual events?",
        "Did you ask any questions? How'd it go?",
        "Conference attire: Casual or business?",
        "Excited to implement what you learned!",
        "Virtual high-five for attending!",
        "Virtual or in-person conferences? Your preference?"],

    "Visited a museum and learned some fascinating history.": [
        "Museum vibes! Which one did you visit?",
        "Favorite exhibit or artifact?",
        "Museum recommendations for history buffs?",
        "History nerd alert! What fascinated you most?",
        "Did you take any museum selfies?",
        "Museum audio guide: worth it or not?",
        "Art or artifacts? What's your preference?",
        "Future history museum curator in the making!",
        "Museum memories are the best memories!",
        "Museum date or solo exploration? Your style?"],

    "Finally organized my closet. It's a small victory!": [
        "Closet organization goals achieved!",
        "Marie Kondo would be proud! Tidying up?",
        "Share your closet organization tips!",
        "Did you discover forgotten treasures?",
        "Small victories lead to big wins!",
        "Closet organization playlist: Yay or nay?",
        "What's the secret to maintaining it?",
        "Next on the organizing list?",
        "Closet envy incoming!",
        "Decluttering is therapeutic!"],

    "Trying to break a bad habit. Any advice?": [
        "Breaking habits is tough. You got this!",
        "Accountability buddies make a difference!",
        "What's the habit you're trying to break?",
        "Replace the bad habit with a good one!",
        "Small steps lead to big changes!",
        "Reward yourself for milestones!",
        "Seeking professional help is commendable!",
        "Share your progress updates with friends!",
        "Breaking habits = Personal growth journey.",
        "Habit-breaking tips welcomed!"],

    "Celebrating my pet's birthday today. They grow up so fast!": [
        "Happy birthday to your fur baby! ",
        "Pet birthday party details, please!",
        "Cake or treats for the birthday pet?",
        "How old is the birthday furball now?",
        "Pet birthday traditions in your household?",
        "Birthday outfit for the pet? Share pics!",
        "Any special pet-friendly treats?",
        "Birthday cuddles are a must!",
        "Pet birthdays are the best birthdays!",
        "Wishing your pet a year of belly rubs and joy!"],

    "New haircut, new me. What do you think?": [
        "Haircut transformation! Love it!",
        "New hair, who dis? Looking fabulous!",
        "Haircut details: What style did you go for?",
        "Did you go for a bold change or a trim?",
        "Hair salon recommendations needed!",
        "Haircut confidence level: 10/10!",
        "New haircut ritual: Mirror selfies?",
        "Haircare tips for the fresh cut?",
        "Haircut emoji:  or ?",
        "Confidence boost unlocked!"],

    "Reflecting on life and setting new goals. Excited for the future!": [
        "Life reflections lead to growth!",
        "Setting goals is the first step to success!",
        "Exciting times ahead! What goals?",
        "Reflect and project! What's in store?",
        "Goal-setting party! Share your aspirations!",
        "Big dreams require small steps. Go for it!",
        "Future plans: Travel, career, or personal?",
        "Visualizing success is a powerful motivator!",
        "What's the first goal on your list?",
        "The future is bright! Cheers to new beginnings!"],

    "Cooked a homemade meal from scratch. Feeling accomplished.": [
        "Homemade meals for the win! ",
        "Chef vibes! What did you cook?",
        "Cooking accomplishment level: Expert!",
        "Share the recipe if it's a secret!",
        "Did you experiment with flavors?",
        "Cooking playlist recommendations?",
        "Cooking from scratch = Love in every bite!",
        "How long did the cooking marathon last?",
        "Feeling accomplished and well-fed!",
        "Masterchef in the making!"],

    "Took a spontaneous road trip. Sometimes you just need to go!": [
        "Spontaneous road trips are the best!",
        "Destination unknown? Even more exciting!",
        "Share the highlight of the road trip!",
        "Favorite road trip snacks? Spill the details!",
        "Spontaneity adds spice to life!",
        "Road trip playlist: What's on it?",
        "Solo road trip or with company?",
        "Any quirky roadside attractions discovered?",
        "Road trip essentials: What are they?",
        "Spontaneous adventures = Lifelong memories!"],

    "Attended a live concert. Music is therapy for the soul.": [
        "Live music magic! ",
        "Concert vibes still lingering?",
        "Who performed at the concert?",
        "Best concert moment? Share it!",
        "Did you dance like no one was watching?",
        "Concert outfit details? Stylish, I'm sure!",
        "Favorite genre for live performances?",
        "Concert bucket list: Any artists in mind?",
        "Music connects souls! Agreed?",
        "Next concert on your radar?"],

    "Successfully planted a small garden. Green thumb achievement unlocked!": [
        "Green thumb goals! ",
        "What plants did you include in the garden?",
        "Gardening tips for beginners?",
        "Share garden photos! We'd love to see!",
        "Any unexpected challenges in gardening?",
        "Garden party in the future?",
        "Gardening achievement unlocked! Level up!",
        "Favorite part of having a garden?",
        "Garden vibes for a peaceful day!",
        "Next gardening project in mind?"],

    "Thinking about adopting a pet. Any pet parent advice?": [
        "Consider adopting from a local shelter.",
        "Research the specific needs of the pet you're interested in.",
        "Prepare your home for a new furry friend.",
        "Don't forget regular vet check-ups and vaccinations.",
        "Patience is key as your new pet adjusts to its new home.",
        "Invest in quality pet food and supplies.",
        "Training and socialization are important for a happy pet.",
        "Create a cozy space for your pet to feel safe.",
        "Remember to give lots of love and attention.",
        "Connect with other pet owners for support and advice."
    ],
    "Finished a DIY home project. Proud of the results!": [
        "Great job on completing the DIY project!",
        "Your hard work paid off—looks fantastic!",
        "DIY projects are so rewarding, aren't they?",
        "What was the most challenging part of the project?",
        "Impressive! What's your next DIY adventure?",
        "Your creativity shines through in your home.",
        "A proud moment indeed—celebrate your success!",
        "DIY skills level: Expert. Well done!",
        "The details make the difference—your attention shows!",
        "Share some before and after pictures, if you can!"
    ],
    "Tried a new fitness class. I can barely walk, but it was worth it!": [
        "Feeling the burn means it's working, right?",
        "Sore muscles today, strong muscles tomorrow!",
        "You're one workout closer to your fitness goals.",
        "What type of fitness class did you try?",
        "Pushing your limits is the key to progress.",
        "Celebrate the post-workout endorphin rush!",
        "Hydrate and stretch—it helps with the soreness.",
        "New fitness class conquered—go you!",
        "Variety in workouts keeps things interesting.",
        "Every step is a step towards a healthier you!"
    ],
    "Enjoying a lazy Sunday with a good book and hot cocoa.": [
        "Lazy Sundays and good books—perfect combo!",
        "Cozy vibes on point with hot cocoa in hand.",
        "What book are you currently immersed in?",
        "Lazy days are essential for recharging.",
        "Hot cocoa: the ultimate comfort drink.",
        "Any book recommendations for a relaxing day?",
        "Getting lost in a book is a great way to unwind.",
        "Cheers to a peaceful and relaxing Sunday!",
        "The best Sundays involve books and cocoa.",
        "Savor the moment—you deserve this tranquility."
    ],
    "Started a blog to share my passions. Excited for this new journey!": [
        "Congratulations on starting your blog!",
        "Excitement and passion—your blog will shine!",
        "What topics are you most excited to write about?",
        "Blogging is a fantastic way to express yourself.",
        "Looking forward to reading your future posts!",
        "Share the link—we'd love to check out your blog!",
        "Consistency is key in the blogging world. Keep it up!",
        "Every post is a step towards your blogging goals.",
        "Embrace the journey, and enjoy the writing process.",
        "Connecting with readers makes the blogging experience richer."
    ],
    "Solved a challenging puzzle. Feeling like a genius!": [
        "Puzzle master at work! Impressive!",
        "Genius level: Unlocked. Well done!",
        "Which type of puzzle was it? Jigsaw or brain teaser?",
        "The satisfaction of solving a challenging puzzle—priceless.",
        "Puzzles are like mental workouts—keep the brain fit!",
        "Share your puzzle-solving strategies with us!",
        "Next challenge: an even more complex puzzle!",
        "The world needs more puzzle-solving champions like you.",
        "A puzzle conquered is a victory well earned.",
        "Puzzle skills on display—applause for your achievement!"
    ],
    "Joined a book club. Can't wait to discuss the latest read.": [
        "Welcome to the book club community!",
        "Discussing books with others adds a new dimension to reading.",
        "Which book are you currently reading for the club?",
        "Book clubs make reading a social and enjoyable experience.",
        "Sharing diverse perspectives enhances the reading journey.",
        "Excitement builds for the upcoming book discussions.",
        "What drew you to join a book club?",
        "Book recommendations from fellow club members are golden.",
        "Discussion nights are the highlight of book club memberships.",
        "Happy reading, and enjoy the upcoming conversations!"
    ],
    "Attended a comedy show. Laughter is the best medicine.": [
        "Laughter therapy at its finest—comedy shows rock!",
        "Who was your favorite comedian from the show?",
        "Nothing beats the joy of a good belly laugh.",
        "Laughter is indeed the best medicine—prescription filled!",
        "Share your favorite jokes from the comedy night.",
        "Comedy shows: where stress goes to take a break.",
        "Glad you had a night filled with laughter and joy!",
        "Laughter is contagious—spread the good vibes!",
        "Comedy nights are like mini vacations for the soul.",
        "A good laugh can turn any day around. Cheers to comedy!"
    ],
    "Volunteered at a local charity event. Giving back feels great!": [
        "Kudos for volunteering! Your impact is significant.",
        "Giving back is a wonderful way to make a difference.",
        "Which charity event did you volunteer for?",
        "Volunteering brings a sense of community and purpose.",
        "The world needs more hearts like yours—thank you!",
        "Share your volunteer experience—it inspires others.",
        "What motivated you to get involved in charity work?",
        "The ripple effect of your kindness is far-reaching.",
        "Volunteering: where selflessness meets fulfillment.",
        "You're making the world a better place—one volunteer hour at a time."
    ],
    "Learning to play a musical instrument. Practice makes perfect!": [
        "Musical journey begins! What instrument are you learning?",
        "Practice sessions are stepping stones to musical mastery.",
        "Every note played is progress—keep at it!",
        "Learning an instrument is a rewarding and lifelong skill.",
        "Share a snippet of your musical practice with us!",
        "Music has the power to soothe the soul—enjoy the process.",
        "Striking the right chords: both in music and life.",
        "What inspired you to pick up a musical instrument?",
        "Practice may be challenging, but the results are worth it.",
        "Musical milestones await—keep playing and learning!"
    ],
    "Hosted a game night with friends. Board games are underrated.": [
        "Game nights are the best nights—great choice!",
        "Which board games were on the menu for game night?",
        "Board games bring friends closer together. Well done!",
        "The competition and camaraderie of game nights—priceless.",
        "Game nights: proving that laughter is the best game-winner.",
        "Share any epic moments or victories from game night!",
        "Hosting game nights is an art—you nailed it!",
        "Board games never go out of style—timeless fun.",
        "Who was the reigning champion of the night?",
        "Game nights are memory-makers—cherish those moments!"
    ],
    "Visited an art gallery. So much creativity in one place!": [
        "Art galleries are like treasure troves of creativity!",
        "Which artists' works captivated you the most?",
        "Discussing art: the beauty of diverse perspectives.",
        "Art has the power to evoke emotions and inspire.",
        "Any favorite pieces that left a lasting impression?",
        "Art appreciation is a journey that never ends—enjoy it!",
        "Visiting galleries is a feast for the eyes and the soul.",
        "What type of art resonates with you the most?",
        "Share your reflections on the art you encountered.",
        "Art galleries: where imagination meets expression."
    ],
    "Experimenting with new dessert recipes. Sugar rush incoming!": [
        "Dessert experiments—sweet tooth-approved!",
        "What's the latest dessert masterpiece from your kitchen?",
        "Sugar rush alert! Which recipe did you try?",
        "Dessert-making: turning the kitchen into a sweet haven.",
        "Share your go-to dessert recipe for fellow sweet tooths!",
        "Experimenting with flavors—any surprising discoveries?",
        "Homemade desserts: the ultimate form of self-care.",
        "Sweets made with love taste even better—true or true?",
        "Dessert enthusiasts unite! What's next on the baking agenda?",
        "Indulge in the sweetness of success—you deserve it!"
    ],
    "Attended a virtual workout class. Sweating at home is the new norm!": [
        "Virtual workouts: a convenient way to stay fit!",
        "Which virtual class did you attend? Share the details!",
        "Home workouts bring the gym experience to your doorstep.",
        "Sweating at home—embracing the new normal!",
        "Virtual high fives for completing the workout class!",
        "Props for adapting and prioritizing fitness at home.",
        "How do you stay motivated during virtual workouts?",
        "Share your favorite virtual workout tips with us!",
        "Virtual or not, fitness is all about dedication—keep it up!",
        "Cheers to breaking a sweat in the comfort of home!"
    ],
    "Finished a jigsaw puzzle with way too many pieces. Dedication level: expert.": [
        "Jigsaw puzzle champion in the house—well done!",
        "Way too many pieces? Challenge accepted and conquered!",
        "Your dedication to the puzzle is truly impressive.",
        "What was the theme or image of the jigsaw puzzle?",
        "Dedication level: Expert. Puzzle mastery achieved!",
        "Puzzles with many pieces are a true test of patience.",
        "Share a picture of the completed masterpiece!",
        "How long did it take you to finish the challenging puzzle?",
        "Puzzle enthusiasts salute your dedication and skill!",
        "Ready for the next puzzle challenge? Bring it on!"
    ],
    "Finally conquered my fear of public speaking. Facing fears head-on!": [
        "Congratulations on conquering your fear of public speaking!",
        "Facing fears head-on—true courage in action!",
        "Share some tips on overcoming public speaking anxiety.",
        "Your achievement inspires others to embrace challenges.",
        "Public speaking victories are milestones worth celebrating.",
        "What motivated you to tackle your fear of public speaking?",
        "Your journey from fear to triumph is truly commendable.",
        "Public speaking skills unlocked—confidence level up!",
        "How did you prepare for your public speaking debut?",
        "The stage is yours—keep shining and speaking with confidence!"
    ],
    "Trying meditation for the first time. Zen mode activated.": [
        "Welcome to the world of meditation—peace awaits!",
        "Zen mode activated: Breathe in, breathe out.",
        "What type of meditation did you try? Mindfulness or guided?",
        "Meditation: a journey inward for a calmer mind.",
        "Share any insights or experiences from your first session.",
        "Mindful moments are the foundation of a peaceful day.",
        "Meditation rookies unite! How did it feel?",
        "Consistency is key—make meditation a daily habit.",
        "Explore different meditation techniques to find your groove.",
        "May your journey into meditation bring tranquility and balance."
    ],
    "Started a journal to document daily gratitude. Positive vibes only!": [
        "Gratitude journaling is a beautiful practice—well begun!",
        "Positive vibes only—your journaling journey is off to a great start!",
        "What are you most grateful for today?",
        "Reflecting on gratitude: a recipe for a joyful life.",
        "Journaling is a powerful tool for self-reflection and growth.",
        "Share a snippet of your daily gratitude entry with us!",
        "Gratitude has the power to transform ordinary days into blessings.",
        "Gratitude is the best attitude—keep the positivity flowing!",
        "How has journaling impacted your mindset so far?",
        "May your journal be filled with countless reasons to be thankful."
    ],
    "Hosted a themed costume party. Best costumes won prizes!": [
        "Themed costume parties are the epitome of fun—great choice!",
        "Best costumes winning prizes—creative competition at its finest!",
        "What was the theme of the costume party? Share the highlights!",
        "Host of the year award goes to you! Bravo!",
        "Costume parties: where imagination knows no bounds.",
        "Who took home the coveted 'Best Costume' title?",
        "Share some pictures of the standout costumes from the party!",
        "The creativity and effort put into costumes make parties memorable.",
        "What inspired you to host a themed costume party?",
        "May your future parties be as lively and spirited as this one!"
    ],
    "Hiked to the top of a mountain. The view was breathtaking!": [
        "Hiking to the top of a mountain—nature's ultimate reward!",
        "The breathtaking view from the mountain top—worth every step.",
        "Which mountain did you conquer? Share the hiking details!",
        "Nature's beauty is the best motivator for a challenging hike.",
        "Hiking highs: the fresh air, the exercise, and that view!",
        "Share a snapshot of the majestic view from the mountain top!",
        "A sense of accomplishment and a view to remember—double win!",
        "Hiking adventures are the perfect blend of challenge and serenity.",
        "The mountains are calling, and you answered! Well done!",
        "What's your next hiking destination? The adventure continues!"
    ],
    "Attended a photography workshop. Capturing moments in pixels.": [
        "Photography workshops are a great investment in skill and artistry!",
        "Capturing moments in pixels—preserving memories in the best way.",
        "What photography tips did you learn at the workshop?",
        "Photography is a journey of constant learning and exploration.",
        "Share some of your favorite shots from the workshop!",
        "Photography is not just about the camera—it's about the eye behind it.",
        "Workshop takeaways: new skills, inspiration, and a fresh perspective.",
        "The world through a lens becomes a canvas of endless possibilities.",
        "Keep capturing those beautiful moments—your lens tells stories."
    ]


}
image_urls = [
    "https://source.unsplash.com/800x600/?bedroom",
    "https://source.unsplash.com/800x600/?jewelry",
    "https://source.unsplash.com/800x600/?computer",
    "https://source.unsplash.com/800x600/?beach",
    "https://source.unsplash.com/800x600/?birthday",
    "https://source.unsplash.com/500x500/?sunglasses",
    "https://source.unsplash.com/800x600/?technology",
    "https://unsplash.com/photos/long-coated-white-dog-pfNmcyaT_es",
    "https://unsplash.com/photos/a-landscape-with-trees-and-grass-68Ln0Cj84QE",
    "https://unsplash.com/photos/a-person-standing-in-the-middle-of-a-canyon-LHsmXVAnkyk",
    "https://unsplash.com/photos/a-view-of-a-mountain-range-with-clouds-in-the-sky-IX7VX9KWOl8",
    "https://unsplash.com/photos/a-large-building-with-a-lot-of-advertisements-on-it-N5NqaTQwbg8",
    "https://unsplash.com/photos/a-woman-walking-across-a-street-next-to-tall-buildings-haggiX6dnpY",
    "https://www.pexels.com/photo/monochrome-photo-of-people-crossing-a-bridge-5579045/",
    "https://www.pexels.com/photo/black-and-white-photo-of-a-footbridge-17340547/",
    "https://www.pexels.com/photo/brown-concrete-stairs-with-blue-metal-railings-13724295/",
    "https://www.pexels.com/photo/cable-car-in-old-town-19177885/",
    "https://www.pexels.com/photo/a-woman-in-white-long-sleeves-raising-hands-14465114/",
    "https://www.pexels.com/photo/tower-bridge-and-river-thames-in-london-18903386/",
    "https://www.pexels.com/photo/young-fashionable-woman-standing-on-the-sidewalk-with-a-cup-of-coffee-in-hand-19539371/",
    "https://www.pexels.com/photo/top-view-shot-of-sea-waves-crashing-the-sandy-shore-15012299/",
    "https://www.pexels.com/photo/people-on-a-street-with-umbrellas-19190086/",
    "https://www.pexels.com/photo/tasty-breakfast-with-beverages-19090942/",
    "https://www.pexels.com/photo/candle-stick-in-front-of-a-christmas-tree-19480569/",
    "https://unsplash.com/photos/a-person-pouring-syrup-onto-a-plate-of-chicken-and-waffles-s9lu2uNwb7A",
    "https://unsplash.com/photos/a-glass-of-wine-and-some-grapes-on-a-table-gtbkK8PHRtY",
    "https://unsplash.com/photos/a-table-topped-with-lots-of-plates-of-food-rUhdUhwBe8A",
    "https://www.pexels.com/photo/bouquet-of-wheat-on-a-grass-19520661/",
    "https://www.pexels.com/photo/a-woman-sitting-on-a-boat-with-her-phone-19564568/",
    "https://www.pexels.com/photo/motorboat-moored-near-ornamented-building-17077789/",
    "https://www.pexels.com/photo/photo-of-a-young-woman-keeping-up-scarf-14844570/",
    "https://www.pexels.com/photo/a-woman-wearing-a-brown-coat-and-brown-hat-14654512/",
    "https://www.pexels.com/photo/sun-shinning-through-tree-leaves-17988291/",
    "https://www.pexels.com/photo/aerial-view-of-an-abandoned-village-of-gamsutl-dagestan-russia-19561453/",
    "https://www.pexels.com/photo/town-by-river-ganges-in-india-19511794/",
    "https://www.pexels.com/photo/woman-holding-fabric-on-floor-10752108/",
    "https://unsplash.com/photos/a-group-of-people-holding-signs-in-front-of-a-building--vTnlOJec84",
    "https://unsplash.com/photos/brown-wooden-photo-frame-Ht76ryPF6lY",
    "https://unsplash.com/photos/person-holding-curology-spray-bottle-VItxz6u036U",
    "https://unsplash.com/photos/yellow-red-and-blue-fireworks-Dn7P1U26ZkE",
    "https://unsplash.com/photos/woman-standing-selecting-clothes-knKm7u_7Ihw",
    "https://unsplash.com/photos/a-person-laying-on-a-bed-with-a-laptop-j730eTMxDiw",
    "https://unsplash.com/photos/assorted-color-shirt-lot-hang-on-rack-xXJ6utyoSw0",
    "https://www.pexels.com/photo/blue-shade-painting-1762973/",
    "https://www.pexels.com/photo/pink-and-blue-watercolor-painting-587958/",
    "https://www.pexels.com/photo/photo-of-red-peonies-painting-1005711/",
    "https://www.pexels.com/photo/silhouette-photography-of-forest-795693/",
    "https://www.pexels.com/photo/photo-of-multicolored-illustration-2832382/",
    "https://www.pexels.com/photo/white-2-storey-house-near-trees-1115804/",
    "https://www.pexels.com/photo/high-rise-buildings-443383/",
    "https://www.pexels.com/photo/low-angle-photo-of-flatiron-building-1123982/",
    "https://www.pexels.com/photo/view-of-office-building-323772/",
    "https://www.pexels.com/photo/aerial-photography-of-cars-on-the-road-1123972/",
    "https://www.pexels.com/photo/blue-and-gray-high-rise-building-162031/",
    "https://www.pexels.com/photo/gray-high-rise-buildings-936722/",
    "https://www.pexels.com/photo/brown-wooden-house-on-edge-of-cliff-1028225/",
    "https://www.pexels.com/photo/photo-of-suspension-bridge-under-cloudy-sky-2570208/",
    "https://www.pexels.com/photo/sears-tower-usa-1722183/",
    "https://www.pexels.com/photo/gray-and-brown-boat-traveling-on-man-made-river-586687/",
    "https://www.pexels.com/photo/concrete-building-2628393/",
    "https://unsplash.com/photos/group-of-people-raising-there-hands-in-concert-aWXVxy8BSzc",
    "https://unsplash.com/photos/lighted-red-text-signage-1oKxSKSOowE",
    "https://unsplash.com/photos/people-gathering-on-green-grass-field-during-daytime-FUmDe-Bx1LA",
    "https://unsplash.com/photos/people-gathering-on-concert-during-daytime-SplXzxtv6AI"
]

with open("posts\\users.txt", "r") as file:
    data = file.readlines()
usernames=[]
for i in data:
    usernames.append(i.split(",")[0])

with open("posts\\friendsList.txt", "r") as file:
    data = file.readlines()
friends={}
for i in data:
    i = i.split(",")
    if i[0] in friends:
        friends[i[0]].append(i[1])
    else:
        friends[i[0]] = [i[1]]
    if i[1] in friends:
        friends[i[1]].append(i[0])
    else:
        friends[i[1]] = [i[0]]


postline="INSERT INTO posts ( postId, userID, imageURL, caption)\nVALUES "

notifications = []
likes=[]
comments =[]


for i in range(len(captions)-1):
    userId= usernames[random.randint(1,len(usernames)-1)]
    postline += f"( {str(i)}, '{userId}', , '{captions[i]}'), \n"
    if userId in friends:
        for c in friends[userId]:
            likes.append([c, i])
            notifications.append([c, f"{userId} posted"])
            notifications.append([userId, f"{c} liked your post"])
        if captions[i] in commentsdata:
            for c in range(min(len(friends[userId]), len(commentsdata[captions[i]]))):
                comments.append([friends[userId][c], i ,commentsdata[captions[i]][c]])
                notifications.append([userId, f"{friends[userId][c]} commented on your post"])

storyline="INSERT INTO stories ( StoryId, userID, imageURL, status)\nVALUES "

for i in range(len(image_urls)-1):
    userId= usernames[random.randint(1,len(usernames)-1)]
    storyline += f"( {str(i)}, '{userId}', '{image_urls[i]}', 'availaible' ), \n"


likeline="INSERT INTO likes ( likeId, userID, postID)\nVALUES "
for i in range(len(likes)-1):
    likeline += f"( {str(i)}, '{likes[i][0]}', {str(likes[i][1])}), \n"

commentline="INSERT INTO comments ( commentId, userID, postID, comment)\nVALUES "
for i in range(len(comments)-1):
    commentline += f"( {str(i)}, '{comments[i][0]}', {str(comments[i][1])}, '{comments[i][2]}'), \n"

notifline="INSERT INTO notifications ( notifId, userID, NMessage, status)\nVALUES "
for i in range(len(notifications)-1):
    notifline += f"( {str(i)}, '{notifications[i][0]}', '{str(notifications[i][1])}',), \n"

with open("posts\\postsOut.txt", "w") as file:
    file.write(postline)
with open("posts\\likesOut.txt", "w") as file:
    file.write(likeline)
with open("posts\\commentsOut.txt", "w") as file:
    file.write(commentline)
with open("posts\\notifOut.txt", "w") as file:
    file.write(notifline)
with open("posts\\storyOut.txt", "w") as file:
    file.write(storyline)