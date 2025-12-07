def find_fresh_ingredients(ranges, ingredients):
    fresh = 0
    for ingredient in ingredients:
        ingredient_fresh = False
        for range_x in ranges:
            if not ingredient_fresh and ingredient >= range_x[0] and ingredient <= range_x[1]:
                fresh += 1
                ingredient_fresh = True
    return fresh

def prepare_environment(ranges, ingredients):
    improved_ranges = []
    for range_x in ranges:
        values = range_x.split('-')
        improved_ranges.append([int(values[0]), int(values[1])])
    return find_fresh_ingredients(improved_ranges, ingredients)

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

    done_with_ranges = False

    ranges = []
    ingredients = []

    for content in file_contents:
        if content == "":
            done_with_ranges = True
            continue

        if not done_with_ranges:
            ranges.append(content)
        else:
            ingredients.append(int(content))

    fresh = prepare_environment(ranges, ingredients)
    print(fresh)

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
