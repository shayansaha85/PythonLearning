
def create_increment_sheet(details_path, salary_increment_path):

    details_file = open(details_path, "r")
    details_file_data = details_file.readlines()
    details_file.close()

    content = details_file_data[0].strip() + "," + "incremented_salary"

    raise_file = open(salary_increment_path, "r")
    raise_file_data = raise_file.readlines()
    raise_file.close()

    increments = {}

    for i in range(1, len(raise_file_data)):
        increments[raise_file_data[i].split(",")[0]] = raise_file_data[i].strip().split(",")[-1]

    new_sheet_content = ""
    new_sheet_content = new_sheet_content + content + "\n"

    for i in range(1, len(details_file_data)):
        new_sheet_content += details_file_data[i].strip() + "," + str(round((float(details_file_data[i].split(",")[4].strip()) + float(details_file_data[i].split(",")[4].strip()) * (float(increments[details_file_data[i].split(",")[0]])/100)), 2)) + "\n"


    new_file = open("updated_details.csv", "w")
    new_file.write(new_sheet_content)
    new_file.close()