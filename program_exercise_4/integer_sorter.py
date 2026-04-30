class IntegerSorter:
    def __init__(self, input_file="integers.txt"):
        self.input_file = input_file

    def process_data(self):
        try:
            with open(self.input_file, "r") as file:
                numbers = [int(line.strip()) for line in file if line.strip()]
            with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
                for number in numbers:
                    if number % 2 == 0:
                        squared = number ** 2
                        double_file.write(f"{squared}\n")
                    else:
                        cubed = number ** 3
                        triple_file.write(f"{cubed}\n")

            print("Number Sorter Completed. You may check double.txt and tripl.txt")

        except FileNotFoundError:
            print(f" Error: {self.input_file} does not exist")
        except ValueError:
            print(f" Error: {self.input_file} does not contain integers")


if __name__ == "__main__":
    processor = IntegerSorter()
    processor.process_data()
