"""3. Создать (не программно) текстовый файл со следующим содержимым:


One — 1
Two — 2
Three — 3
Four — 4


Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.


Решение покрыть тестами."""


def main():
    numbers = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Чотири"}
    with open("cw_file.txt") as f:
        with open("new_hw_file.txt", "w", encoding="utf-8") as f_w:
            f_w.write(change_values(f, numbers))


def change_values(old_file, dict_values: dict):
    new_f = ""
    for line in old_file:
        new_line = line.split()
        for key, values in dict_values.items():
            while key in new_line:
                new_line[new_line.index(key)] = values
        new_f += " ".join(new_line) + "\n"
    return new_f


main()