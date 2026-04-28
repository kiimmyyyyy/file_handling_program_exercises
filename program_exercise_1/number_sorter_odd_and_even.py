try:
    with open ('numbers.txt', 'r') as source_file:
        numbers = [int(line.strip()) for line in source_file if line.strip()]

    with open ('even_numbers.txt', 'w') as even_source_file, open('odd_numbers.txt', 'w') as odd_source_file:
        for num in numbers:
            if num % 2 == 0:
                even_source_file.write(f'{num}\n')
            else:
                odd_source_file.write(f'{num}\n')

    print("Done!")

except FileNotFoundError:
        print("File not found!")