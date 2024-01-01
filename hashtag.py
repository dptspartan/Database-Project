import random

# Sample data for hashtags
hashtags = [
    "FitnessJourney",
    "PromotionCelebration",
    "BingeWatching",
    "HiddenGems",
    "BeautifulSunset",
    "WeekendGetaway",
    "LanguageLearning",
    "VirtualConference",
    "ArtGalleryVisit",
    "ClosetOrganization",
    "BreakingBadHabits",
    "PetBirthday",
    "NewHaircut",
    "ReflectAndSetGoals",
    "HomemadeMeal",
    "SpontaneousRoadTrip",
    "LiveConcertExperience",
    "GardeningAchievement",
    "PetAdoption",
    "DIYHomeProject",
    "NewFitnessClass",
    "LazySunday",
    "StartingABlog",
    "PuzzleSolving",
    "BookClubDiscussion",
    "ComedyShowNight",
    "VolunteeringExperience",
    "LearningMusicalInstrument",
    "GameNightFun",
    "ArtGalleryExploration",
    "DessertExperiments",
    "PhotographyWorkshop"
]

# Function to generate random hashtags for each post
def generate_post_hashtags():
    return random.sample(hashtags, random.randint(1, 5))

# SQL code for Hashtag table
hashtag_table_line = "INSERT INTO hashtag (hashtagID, hashtagName)\nVALUES "
for i, hashtag in enumerate(hashtags, start=1):
    hashtag_table_line += f"({i}, '{hashtag}'), \n"

# SQL code for HashtagRelationship table
hashtag_rel_line = "INSERT INTO hashtag_relationship (hashtagRelID, hashtagID, postID)\nVALUES "
post_count = 48
ind = 0
for i in range(post_count):
    post_hashtags = generate_post_hashtags()
    for hashtag in post_hashtags:
        hashtag_id = hashtags.index(hashtag) + 1
        hashtag_rel_line += f"({ind}, {hashtag_id}, {i}), \n"
        ind += 1

# Write SQL code to files
with open("posts\\hashtagTableOut.txt", "w") as file:
    file.write(hashtag_table_line)

with open("posts\\hashtagRelTableOut.txt", "w") as file:
    file.write(hashtag_rel_line)
