class highest_gwa:
	def __init__(self, student_file, ranked_file):
		self.student_file = student_file
		self.ranked_file = ranked_file

	def rank_students(self):
		print(f"reading... {self.student_file}")

		with open(self.student_file, "r") as student_file:
			lines = student_file.readlines()

		header_row = lines[0]
		student_data = lines[1:]
		students = []

		print("done!")
		print("students' ranking...")

		for line in student_data:
			row = line.strip()
			if row != "":
				chopped_row = row.split(',')

			names = chopped_row[0]
			section = chopped_row[1]
			gwa = float(chopped_row[2])

			student = [gwa, names, section]
			students.append(student)

		print("Starting the process..")

		students.sort()

		print("Ranking process completed..")

		with open(self.ranked_file, "w") as ranked_file:
			ranked_file.write(header_row)

			for student in students:
				student_gwa = str(student[0])
				student_name = student[1]
				student_section = student[2]

				save_data = student_name + ',' + student_section + ',' + student_gwa + "\n"
				ranked_file.write(save_data)

		print("done! " + "File: " + self.ranked_file + " success!")
run_sorter = highest_gwa("student_record.csv", "student_rankings.csv")
run_sorter.rank_students()