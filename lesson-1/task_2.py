print("\nПрограмма по преобразованию секунд в формат чч:мм:сек\n")
n = int ( input("Какое количество секунд нужно преобразовать? " ) )
print(n)
hours = n // 3600
n = n - hours * 3600
minutes = n // 60
seconds = n % 60
print(f"{hours}ч:{minutes}м:{seconds}сек")
