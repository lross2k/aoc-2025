def test(number, function, result):
    obtained_result = function(number)
    if (obtained_result == result):
        print("success", number)
    else:
        print("FAIL", number, result, "!=", obtained_result)

def turn_to_number_2(numbers: list[int]):
    number = 0
    for index in range(len(numbers)):
        base = 100**(index)
        number += base * numbers[len(numbers) - index - 1]
    return number

def turn_to_number(numbers: list[int]):
    number = 0
    for index in range(len(numbers)):
        base = 10**(index)
        number += base * numbers[len(numbers) - index - 1]
    return number

def process_battery_line(line: str, target=12):
    line_len = len(line)

    last_index = len(line)-1

    numbers = []
    skipped_numbers = []

    print(line)
    for index in range(line_len):
        remaining_chars = line_len - index
        current_len = len(numbers)
        if (len(numbers) > 0):
            previous_value = numbers[current_len-1]
        else:
            previous_value = 999
        current_value = int(line[index])
        if ((remaining_chars + current_len) > target and current_len < target):
            # append any number, if bigger than previous, replace
            if current_value > previous_value:
                skipped_numbers.append(previous_value)
                numbers[current_len-1] = current_value
            else:
                numbers.append(current_value)
        elif (remaining_chars >= target and current_len >= target):
            # overwrite any number if a bigger one is found
            print("hit0")
        else:
            # conservative mode, actually analyse best number
            #print("hit1", index, current_value)
            if current_len < target:
                numbers.append(current_value)
            elif current_value > previous_value:
                skipped_numbers.append(previous_value)
                numbers[current_len-1] = current_value
    print(numbers)
    return turn_to_number(numbers)

def divide_and_conquer_ahh(number):
    sub_numbers = []
    final = []
    previous = 0
    for i in range(16, len(number), 16):
        sub_numbers.append(number[previous:i])
        previous = i
    sub_numbers.append(number[previous:])

    for number_2 in sub_numbers:
        res = process_battery_line(number_2)
        for target in range(10,2,-2):
            #print('target', target, res)
            res = process_battery_line(str(res), target)
        final.append(res)

    new_final = [final[0]]

    # merge in groups of two from right to left
    for j in range(1, len(final), 2):
        new_final.append(str(final[j])+str(final[j+1]))

    the_final = []

    # process AGAIN
    for res in new_final:
        for target in range(7,3,-1):
            #print('target', target, res)
            res = process_battery_line(str(res), target)
        the_final.append(res)

    #print(new_final)
    #print(the_final)

    # process AGAIN AGAIN
    help_me = []
    final_help = []
    # merge in groups of two from right to left
    for j in range(0, len(the_final), 2):
        help_me.append(str(the_final[j])+str(the_final[j+1]))
    for res in help_me:
        for target in range(7,5,-1):
            #print('target', target, res)
            res = process_battery_line(str(res), target)
        final_help.append(res)

    #print('halp', help_me)
    #print('chapui', final_help)

    almost = str(final_help[0]) + str(final_help[1])
    #print('final', final, 'almost', almost, process_battery_line(almost))
    return process_battery_line(almost)

def split_contents(contents):
    content_list = []
    current = ""
    for character in contents:
        if character == "\n":
            content_list.append(current)
            current = ""
            continue
        current += character
    return content_list

def process_file(file_name: str):
    file_contents = open(file_name, 'r').read()
    file_contents = split_contents(file_contents)
    total_jolts = 0
    for line in file_contents:
        line_jolts = divide_and_conquer_ahh(line)
        total_jolts += line_jolts
        print(line, line_jolts)
    print(total_jolts)

def main():
    #test("987654321111111", process_battery_line, 987654321111)
    #test("6839153353242324143271184245154323237323424572457644344234734233332343344532643622213823683942455442", process_battery_line, 987654321111)
    #test("811111111111119", process_battery_line, 811111111119)
    #test("234234234234278", process_battery_line, 434234234278)
    #test("818181911112111", process_battery_line, 888911112111)
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
