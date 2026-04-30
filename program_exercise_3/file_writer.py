class LifeRecorder:
	def __init__(self, file_name):
		self.file_name = file_name

	def write_life(self):
		with open(self.file_name, "w") as life_file:
			while True:
				line_entry = input ("Enter line: ")
				life_file.write(line_entry + "\n")

				choose = input("Are there any additional lines? [y/n]: ").lower()

				if choose == "n":
					break

		print("Saving life entry...")
		print("Life Recorder successfully saved in: " + self.file_name)

write_now = LifeRecorder("my_life.txt")
write_now.write_life()