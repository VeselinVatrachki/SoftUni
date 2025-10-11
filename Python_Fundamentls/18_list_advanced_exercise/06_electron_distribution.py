electrons = int(input())
shell_list = []
n = 0
while electrons > 0:
    n += 1
    shell = 2 * n ** 2
    if electrons >= shell:
        shell_list.append(shell)
        electrons -= shell
    else:
        shell_list.append(electrons)
        electrons = 0
print(shell_list)
