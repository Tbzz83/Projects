
class Med_school():
    def __init__(self, name, state, degree_type, average_GPA, average_MCAT, minimum_MCAT):
        self.name = name
        self.state = state
        self.degree_type = degree_type
        self.average_GPA = average_GPA
        self.average_MCAT = average_MCAT
        self.minimum_MCAT = minimum_MCAT


def read_database(filepath):
    with open (filepath, 'r') as f:
        return [l.strip() for l in f.readlines()]

database = read_database(r"C:\Users\Tobi\PycharmProjects\pythonProject\school_database.txt")

international_schools = read_database(r"C:\Users\Tobi\PycharmProjects\pythonProject\international_schools.txt")

def get_schools(upper_score = input("what is your upper score range? "), lower_score = input("what is your lower score range? ")):
    scores = []
    index = 0

    for i in range(int(lower_score),int(upper_score) + 1):
        scores.append(str(i))

    clean_schools = []
    clean_internationals = []
    for school in database:

        if "*" in school:
            school = school.replace("*", "")
            clean_schools.append(school)
        else:
            clean_schools.append(school)

    for school in international_schools:

        if "*" in school:
            school = school.replace("*", "")
            clean_internationals.append(school)
        else:
            clean_internationals.append(school)

    potentials = []
    for mcat in clean_schools:
        is_float = True
        try:
            float(mcat)
            if is_float == True:
                mcat = round(float(mcat))
                if str(mcat) in scores:
                    potentials.append(clean_schools[index - 4])
                    index += 1
                else:
                    index += 1
        except ValueError:
            is_float = False

            if str(mcat) in scores:
                potentials.append(clean_schools[index - 4])
                index += 1
            else:
                index += 1

    final_list = []
    for school in potentials:
        if school in clean_internationals:
            final_list.append(school)

    Get_Dict = {}
    j = 4
    for school in clean_schools:
        if school in final_list:
            Get_Dict[school] = clean_schools[j]
            j += 1
        else:
            j += 1

    counter = 0
    for i in final_list:
        counter += 1
    print(f'There are {counter} schools that you can apply to ')

    with open ("Med_schools_to_apply_to.txt", "w") as f:
        f.write("These are the " + str(counter) + " schools you are able to apply to within an MCAT range of " + str(lower_score) + " to " + str(upper_score) + "\n\n")
        for school, MCAT in Get_Dict.items():
            f.write('%s: %s\n' % (school, MCAT))


    return Get_Dict


print(f'These are the schools that you should apply to that accept internationals: {get_schools()}')









