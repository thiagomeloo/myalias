import os
import re


def test_transform_file_into_list_of_tuples():
    filename = 'upload_file_test.txt'

    with open(filename, 'w') as file:
        file.write('###\n')
        file.write('"###" "###" "###" "###"\n')
        file.write('"myalias1" "description 1" "command 1"\n')
        file.write('"myalias2" "description 2" "command 2"\n')
        file.write('"myalias3" "description 3" "command 3"\n')
        file.write('"myalias4" "description 4" "command \'4\'"\n')

    tuples_list = []
    with open(filename, 'r') as file:
        for line in file:
            values = re.findall(r'"(.*?)"', line)

            if len(values) != 3:
                continue

            alias, description, command = values

            command = command.replace("'", '"')

            tuples_list.append((alias, description, command))

    assert len(tuples_list) == 4

    assert tuples_list[0] == ('myalias1', 'description 1', 'command 1')
    assert tuples_list[1] == ('myalias2', 'description 2', 'command 2')
    assert tuples_list[2] == ('myalias3', 'description 3', 'command 3')
    assert tuples_list[3] == ('myalias4', 'description 4', 'command "4"')

    os.remove(filename)


def test_transform_inexists_file_into_list_of_tuples():
    filename = 'upload_file_test.txt'

    assert os.path.exists(filename) == False
