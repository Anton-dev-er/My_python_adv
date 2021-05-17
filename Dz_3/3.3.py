"""3. Создать (не программно) текстовый файл со следующим содержимым:


One — 1
Two — 2
Three — 3
Four — 4


Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.


Решение покрыть тестами."""

with open("cw_file.txt") as f:
    new_f = ""
    for line in f:
        num_need_change = ""
        if "One" in line:
            num_need_change = "One"
            num_for_change = "Один"
        elif "Two" in line:
            num_need_change = "Two"
            num_for_change = "Два"
        elif "Three" in line:
            num_need_change = "Three"
            num_for_change = "Три"
        elif "Four" in line:
            num_need_change = "Four"
            num_for_change = "Чотири"

        if num_for_change != "":
            new_line = line.split(" ")
            new_line[new_line.index(num_need_change)] = num_for_change
            new_f += " ".join(new_line)
    with open("new_hw_file.txt", "w", encoding="utf-8") as f_w:
        f_w.write(new_f)