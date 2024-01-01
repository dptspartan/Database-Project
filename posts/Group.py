import random

# Sample data for users
user_data = [
    ("gjewkes0", "Gherardo", "Jewkes", "pG0~0D'odpe", "M"),
    ("tguice1", "Tann", "Guice", 'nU6+\'HxJ)V""', "M"),
    ("dcleal2", "Dorthea", "Cleal", "cW5#$HD!)20oA", "F"),
    ("mmcduffie3", "Montgomery", "McDuffie", "fR5+_KXY9Y", "M"),
    ("kimlacke4", "Kenna", "Imlacke", "tR2_AXzfS0+u", "F"),
    ("nyanshin5", "Natka", "Yanshin", "yC6<xKgOrDl7gh", "F"),
    ("cmaccostye6", "Clair", "MacCostye", "nM9)'_|VcLl'7`Yc", "F"),
    ("pfouracres7", "Pauletta", "Fouracres", "bT0_0\\?p(Ri", "F"),
    ("smcguffie8", "Stacee", "McGuffie", '"jB2!l&,v1"', "F"),
    ("btindle9", "Beale", "Tindle", '"iK7!s0ZtA|z,"', "M"),
    ("akhidra", "Alfreda", "Khidr", "gU4~+{(HC", "F"),
    ("swenningtonb", "Sig", "Wennington", "hE3+2T>\\$~0L", "M"),
    ("zfargiec", "Zena", "Fargie", "dZ7`gbnPS", "F"),
    ("slubertid", "Stephana", "Luberti", '"vI0~y6\\+%"', "F"),
    ("lmcaughtrye", "Lynette", "McAughtry", '"fZ8,2_""NT8Bs""zAx"', "F"),
    ("slockyerf", "Simone", "Lockyer", "gS6_Xob$5", "M"),
    ("jmuffeng", "Jeanelle", "Muffen", '"wE1{0,9fw"', "F"),
    ("rovillh", "Rosamond", "Ovill", "tM8)zRX2vLa*=", "F"),
    ("bbedoi", "Belinda", "Bedo", "fS5!G1o(Ej3f0o52", "F"),
    ("sgillanj", "Sheffy", "Gillan", '"uH0,bx?&,4"', "M"),
]

# Function to generate random user ID
def generate_random_user_id():
    return random.choice(user_data)[0]

# SQL code for Group table
group_table_line = "INSERT INTO group_table (groupID, groupName, adminID)\nVALUES "
for i in range(1, 6):  # Assuming there are 5 groups
    group_admin = generate_random_user_id()
    group_table_line += f"({i}, 'Group-{i}', '{group_admin}'), \n"

# SQL code for GroupMembers table
group_members_line = "INSERT INTO group_members (gMembershipID, groupID, username)\nVALUES "
for i in range(1, 21):  # Assuming 20 members in total
    group_id = random.randint(1, 5)
    username = generate_random_user_id()
    group_members_line += f"({i}, {group_id}, '{username}'), \n"

# Write SQL code to files
with open("group_table_out.txt", "w") as file:
    file.write(group_table_line)

with open("group_members_out.txt", "w") as file:
    file.write(group_members_line)
